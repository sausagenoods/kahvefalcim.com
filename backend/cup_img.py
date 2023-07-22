import cv2
import numpy as np
import imutils
from PIL import Image

# Attempt to remove the background to isolate the cup
def isolate_cup(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, blockSize=51, C=0)

    nlabel,labels,stats,centroids = cv2.connectedComponentsWithStats(thresh_gray, connectivity=8)

    # Find second largest cluster (the cluster is the background):
    max_size = np.max(stats[1:, cv2.CC_STAT_AREA])
    max_size_idx = np.where(stats[:, cv2.CC_STAT_AREA] == max_size)[0][0]

    mask = np.zeros_like(thresh_gray)

    # Draw the cluster on mask
    mask[labels == max_size_idx] = 255

    # Use "open" morphological operation for removing some artifacts
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)))

    # Fill the plate with white pixels
    cv2.floodFill(mask, None, tuple(centroids[max_size_idx].astype(int)), newVal=255, loDiff=1, upDiff=1)

    # Find contours, and get the contour with maximum area
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = imutils.grab_contours(cnts)

    c = max(cnts, key=cv2.contourArea)

    # Draw contours with maximum size on new mask
    mask2 = np.zeros_like(mask)
    cv2.drawContours(mask2, [c], -1, 255, -1)
    image[(mask2==0)] = 255
    cv2.imwrite("processed.jpg", image)
    return image

def get_cup_insides(img, bounds):
    cup = img[bounds[0][1]:bounds[0][3], bounds[0][0]:bounds[0][2]]

    # Match the colors of coffee grains
    mask = cv2.inRange(cup, (0, 0, 0), (200, 200, 150))
    bk = np.full(cup.shape, 255, dtype=np.uint8)  # white bk

    # get masked foreground
    fg_masked = cv2.bitwise_and(cup, cup, mask=mask)

    # get masked background, mask must be inverted
    mask = cv2.bitwise_not(mask)
    bk_masked = cv2.bitwise_and(bk, bk, mask=mask)

    # combine masked foreground and masked background
    final = cv2.bitwise_or(fg_masked, bk_masked)
    mask = cv2.bitwise_not(mask)  # revert mask to original

    cv2.imwrite("otsu.jpg", final)

    ret  = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)
    pil = Image.fromarray(ret)
    return ret
