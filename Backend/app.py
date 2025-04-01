from flask import Flask, request
import cv2
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

NAIL_COLOR_MAP = {
    "fair": ["Pastel Pink", "Nude", "Light Blue"],
    "medium": ["Deep Red", "Burgundy", "Rose Gold"],
    "dark": ["Metalic Gold", "Dark Green", "Vibrant Purple"]
}

def detect_hand(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        return True, image_rgb
    return False, None

def analze_nail():
    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read()))
    image = np.array(image)

if __name__ = "__main__":
    app.run(debug=True)