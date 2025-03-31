from flask import Flask, request
import cv2
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

def analze_nail():
    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read()))
    image = np.array(image)

if __name__ = "__main__":
    app.run(debug=True)