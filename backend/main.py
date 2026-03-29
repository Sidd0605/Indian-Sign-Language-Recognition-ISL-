from __future__ import annotations

from io import BytesIO
import json
import os
from pathlib import Path
from typing import Optional
from urllib.parse import quote, urlsplit

from PIL import Image, ImageDraw
import werkzeug.urls
import werkzeug

if not hasattr(werkzeug.urls, "url_quote"):
    werkzeug.urls.url_quote = quote
if not hasattr(werkzeug.urls, "url_parse"):
    werkzeug.urls.url_parse = urlsplit
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "3"

from flask import Flask, jsonify, make_response, request, send_file
from flask_cors import CORS
from werkzeug.exceptions import HTTPException


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "pretrained_models" / "best.pt"
OUTPUT_IMAGE_PATH = BASE_DIR / "images" / "result.jpg"
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}

os.environ.setdefault("YOLO_CONFIG_DIR", "/tmp/Ultralytics")

app = Flask(__name__)
CORS(app)

_model = None
_model_error: Optional[str] = None


class NotFoundError(HTTPException):
    def __init__(self, status_code: int):
        self.response = make_response("", status_code)


class PostValidationError(HTTPException):
    def __init__(self, status_code: int, error_code: str, error_message: str):
        message = {"error_code": error_code, "error_message": error_message}
        self.response = make_response(json.dumps(message), status_code)


def get_model():
    global _model, _model_error

    if _model is not None:
        return _model

    if _model_error is not None:
        raise RuntimeError(_model_error)

    if not MODEL_PATH.exists():
        _model_error = f"Model file not found at {MODEL_PATH}"
        raise RuntimeError(_model_error)

    try:
        from ultralytics import YOLO
    except Exception as exc:
        _model_error = f"Unable to import ultralytics: {exc}"
        raise RuntimeError(_model_error) from exc

    try:
        _model = YOLO(str(MODEL_PATH))
    except Exception as exc:
        _model_error = f"Unable to load model: {exc}"
        raise RuntimeError(_model_error) from exc

    return _model


def create_annotated_img(res, img: Image.Image, save_path: Path) -> Path:
    save_path.parent.mkdir(parents=True, exist_ok=True)

    annotated = img.copy()
    draw = ImageDraw.Draw(annotated)
    boxes = res[0].boxes

    xyxy = boxes.xyxy.cpu().numpy()
    conf = boxes.conf.cpu().numpy()
    cls = boxes.cls.cpu().numpy().astype(int)

    for i in range(len(xyxy)):
        x, y, x_max, y_max = xyxy[i]
        box_width = x_max - x
        box_height = y_max - y
        confidence = conf[i]
        class_label = cls[i]

        draw.rectangle((x, y, x + box_width, y + box_height), outline="red", width=3)
        draw.text((x, max(0, y - 16)), f"{res[0].names[class_label]}, {confidence:.2f}", fill="white")

    annotated.save(save_path, format="JPEG")
    return save_path


@app.route("/", methods=["GET"])
def home():
    model_ready = False
    model_status = "not loaded"

    try:
        get_model()
        model_ready = True
        model_status = "ready"
    except RuntimeError as exc:
        model_status = str(exc)

    return jsonify(
        {
            "message": "Indian Sign Language Recognition backend is running",
            "model_ready": model_ready,
            "model_status": model_status,
        }
    )


@app.route("/health", methods=["GET"])
def health():
    return home()


@app.route("/upload", methods=["POST"])
def upload_crop_image():
    if "file" not in request.files:
        raise PostValidationError(
            status_code=400,
            error_code="BE1003",
            error_message="Image file is not uploaded",
        )

    file = request.files["file"]

    if not file.filename:
        raise PostValidationError(
            status_code=400,
            error_code="BE1005",
            error_message="No file selected",
        )

    extension = Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise PostValidationError(
            status_code=400,
            error_code="BE1004",
            error_message="Invalid file type",
        )

    try:
        model = get_model()
    except RuntimeError as exc:
        return (
            jsonify(
                {
                    "error_code": "BE2001",
                    "error_message": str(exc),
                }
            ),
            503,
        )

    try:
        img = Image.open(BytesIO(file.read())).convert("RGB")
    except Exception as exc:
        raise PostValidationError(
            status_code=400,
            error_code="BE1006",
            error_message=f"Unable to read image: {exc}",
        ) from exc

    res = model.predict(source=img, verbose=False)
    create_annotated_img(res, img, OUTPUT_IMAGE_PATH)

    if len(res[0].boxes) == 0:
        return jsonify(
            {
                "class_label": "",
                "confidence": 0.0,
                "total_spots": 0,
                "annotated_image": "/result",
                "message": "No detection found",
            }
        )

    class_index = int(res[0].boxes.cls.cpu().numpy()[0])
    confidence = float(res[0].boxes.conf.cpu().numpy()[0])

    return jsonify(
        {
            "class_label": res[0].names[class_index],
            "confidence": confidence,
            "total_spots": len(res[0].boxes),
            "annotated_image": "/result",
        }
    )


@app.route("/result", methods=["GET"])
def get_result():
    if OUTPUT_IMAGE_PATH.exists():
        return send_file(OUTPUT_IMAGE_PATH, mimetype="image/jpeg")
    raise NotFoundError(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
