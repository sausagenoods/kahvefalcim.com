from flask import Flask, jsonify, has_request_context, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask.logging import default_handler
import logging

from kahve import Kahvefali, NotCupError, NothingPredictedError
import meaning


app = Flask(__name__)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.headers.get('X-Forwarded-For')
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


logger = logging.getLogger("kahve")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("/var/log/kahve.log")
fh.setFormatter(RequestFormatter('[%(asctime)s] %(remote_addr)s %(url)s - %(message)s'))
logger.addHandler(fh)

limiter = Limiter(
  get_remote_address,
  app=app,
  default_limits=["200 per day", "20 per hour"],
  storage_uri="redis://localhost:6379",
  storage_options={"socket_connect_timeout": 30},
  strategy="fixed-window",
)

falci = Kahvefali(23, "/root/dataset/outputs/model50.pth", 0.2, ["cup", "cake"])


@app.route('/fal/en', methods=['POST'])
def predict_en():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        try:
            anno = falci.fortune(img_bytes)
        except NotCupError:
            logger.error("Not a cup")
            return jsonify(error_msg="No cup/mug was detected in your image.")
        except NothingPredictedError:
            logger.error("nothing predicted")
            return jsonify(error_msg="No pattern was detected in your coffee. Try taking a picture at a different angle.")

        definitions = meaning.get_en_meaning(anno)
        logger.info("Serving response:" + str(anno))
        return jsonify(anno | {'defs': definitions})


@app.route('/fal/tr', methods=['POST'])
def predict_tr():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        try:
            anno = falci.fortune(img_bytes)
        except NotCupError:
            logger.error("Not a cup")
            return jsonify(error_msg="Yüklenen fotoğrafta fincan veya kupa bulunamadı.")
        except NothingPredictedError:
            logger.error("Nothing predicted")
            return jsonify(error_msg="Farklı açıdan bir fotoğraf ile tekrar deneyiniz.")

        definitions = meaning.get_tr_meaning(anno)
        logger.info("Serving response:" + str(anno))
        return definitions


if __name__ == '__main__':
    app.run()
