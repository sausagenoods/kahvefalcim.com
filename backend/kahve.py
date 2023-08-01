import torch
import cv2
import numpy as np
from PIL import Image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_V2_Weights, faster_rcnn
from torchvision.transforms.functional import to_pil_image, pil_to_tensor, crop

import cup_img as ci
from classes import num_classes, CLASSES

class Kahvefali:
    def __init__(self, n_classes, model_path, detection_threshold, label_whitelist):
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        
        # Specialized model for tasseography.
        self.tas_model = fasterrcnn_resnet50_fpn(pretrained=True)

        # get the number of input features
        in_features = self.tas_model.roi_heads.box_predictor.cls_score.in_features
        # define a new head for the detector with required number of classes
        self.tas_model.roi_heads.box_predictor = faster_rcnn.FastRCNNPredictor(in_features, n_classes)

        self.tas_model.to(self.device).load_state_dict(torch.load(
            model_path, map_location=self.device
        ))
        self.tas_model.eval()
        self.tas_model.share_memory()

        # Generic model for object detection. Used to locate the cup.
        self.rcnn_weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
        self.gen_model = fasterrcnn_resnet50_fpn_v2(
                weights=self.rcnn_weights,
                score_thresh=detection_threshold
        )
        self.gen_model.eval()
        self.gen_model.share_memory()
        self.rcnn_preprocess = self.rcnn_weights.transforms()
        self.label_whitelist = label_whitelist
        self.detection_threshold = detection_threshold
        print("Initialized detection models")


    def get_cup(self, img):
        batch = [self.rcnn_preprocess(img)]
        prediction = self.gen_model(batch)[0]

        cup_boundary_box = None
        for idx, label_idx in enumerate(prediction["labels"]):
            label = self.rcnn_weights.meta["categories"][label_idx]
            if label in self.label_whitelist:
                cup_boundary_box = prediction["boxes"][idx]
                cup_boundary_box = cup_boundary_box.clone().detach().type(torch.int)
                cup_boundary_box = cup_boundary_box.unsqueeze(0)
                return cup_boundary_box

        raise NotCupError


    def detect_obj_inside_cup(self, image, orig):
        # make the pixel range between 0 and 1
        image /= 255.0
        image = np.transpose(image, (2, 0, 1)).astype(float)
        image = torch.tensor(image, dtype=torch.float)
        image = torch.unsqueeze(image, 0)
        with torch.no_grad():
            outputs = self.tas_model(image)

        # load all detection to device for further operations
        outputs = [{k: v.to(self.device) for k, v in t.items()} for t in outputs]
        
        boxes = outputs[0]['boxes'].data.numpy()
        scores = outputs[0]['scores'].data.numpy()
        # filter out boxes according to `detection_threshold`
        boxes = boxes[scores >= self.detection_threshold].astype(np.int32)
        if len(boxes) == 0:
            raise NothingPredictedError
        draw_boxes = boxes.copy()
        # get all the predicited class names
        pred_classes = [CLASSES[i] for i in outputs[0]['labels'].cpu().numpy()]
        
        res = []
        for j, box in enumerate(draw_boxes):
            cv2.rectangle(orig,
                        (int(box[0]), int(box[1])),
                        (int(box[2]), int(box[3])),
                        (0, 0, 255), 2)
            cv2.putText(orig, pred_classes[j],
                        (int(box[0]), int(box[1]-5)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                        2, lineType=cv2.LINE_AA)
            res.append({'pos': [int(box[0]), int(box[1]), int(box[2]), int(box[3])], 'obj': pred_classes[j]})
        return res


    def fortune(self, img):
        image = np.asarray(bytearray(img), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(image)

        bounds = self.get_cup(pil_img)
        just_cup = ci.isolate_cup(image)
        insides = ci.get_cup_insides(just_cup, bounds)
        orig_cropped = image[bounds[0][1]:bounds[0][3], bounds[0][0]:bounds[0][2]]
        annotations = self.detect_obj_inside_cup(insides.astype(float), orig_cropped)
        return {"cup_boundaries": [int(bounds[0][0]), int(bounds[0][1]), int(bounds[0][2]), int(bounds[0][3])], "annotations": annotations}


class NotCupError(Exception):
    pass


class NothingPredictedError(Exception):
    pass
