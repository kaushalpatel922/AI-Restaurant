from flask import Flask, request
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image
import io

app = Flask(__name__)

MODEL_PATH = "skin_tone_model.h5"
model = load_model(MODEL_PATH)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.7)

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

@app.route("/analyze", methods=["POST"])
def analze_nail():
    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read()))
    image = np.array(image)

    hand_detected, processed_image = detect_hand(image)
    if not hand_detected:
        return jsonify({"error": "No hand detected"})

if __name__ = "__main__":
    app.run(debug=True)