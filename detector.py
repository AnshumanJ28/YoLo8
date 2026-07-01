from ultralytics import YOLO
from config import CONFIG


class ObjectDetector:
    def __init__(self):
        self.model = YOLO(CONFIG["model_name"])

    def detect(self, frame):
        return self.model.predict(
            frame,
            conf=CONFIG["confidence_threshold"],
            iou=CONFIG["iou_threshold"],
            device=CONFIG["device"],
            verbose=False
        )
