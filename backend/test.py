import sys
from io import BytesIO
from PIL import Image
from kahve import Kahvefali

falci = Kahvefali(23, "dataset/outputs/model100.pth", 0.0005, ["cup", "cake"])

fd = open(sys.argv[1], "rb")

img = fd.read()
fd.close()

anno = falci.fortune(img)
print(anno)
