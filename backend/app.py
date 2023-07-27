from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from kahve import Kahvefali
import meaning


app = Flask(__name__)

limiter = Limiter(
  get_remote_address,
  app=app,
  default_limits=["20 per day", "5 per hour"],
  storage_uri="redis://localhost:6379",
  storage_options={"socket_connect_timeout": 30},
  strategy="fixed-window",
)

falci = Kahvefali(23, "dataset/outputs/model50.pth", 0.07, ["cup", "cake"])


@app.route('/fal/en', methods=['POST'])
def predict_en():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        try:
            anno = falci.fortune(img_bytes)
        except ValueError as e:
            return jsonify(error_msg=str(e))

        definitions = meaning.get_en_meaning(anno)
        return jsonify(anno | {'defs': definitions})


@app.route('/fal/tr', methods=['POST'])
def predict_tr():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        try:
            anno = falci.fortune(img_bytes)
        except ValueError as e:
            return jsonify(error_msg=str(e))

        definitions = meaning.get_tr_meaning(anno)
        return definitions


if __name__ == '__main__':
    app.run()
