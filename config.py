from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
MODEL_DIR = BASE_DIR / "models"

INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

CONFIG = {
    "model_name": "yolov8n.pt",
    "device": "cuda",
    "confidence_threshold": 0.25,
    "iou_threshold": 0.45,
    "tracker": "bytetrack.yaml",
    "input_video": INPUT_DIR / "input_video.mp4",
    "output_video": OUTPUT_DIR / "tracked_output.mp4"
}
