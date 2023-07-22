from flask import Flask, jsonify, request
from kahve import Kahvefali
import torch

app = Flask(__name__)
falci = Kahvefali(23, "dataset/outputs/model100.pth", 0.5, ["cup", "cake"])

@app.route('/fal', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        try:
            anno = falci.fortune(img_bytes)
        except ValueError as e:
            return jsonify(error_msg=e)
        return jsonify(anno)

if __name__ == '__main__':
    app.run()
