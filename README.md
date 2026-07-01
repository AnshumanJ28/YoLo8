# YOLOv8 + ByteTrack Multi-Object Tracking

A computer vision project that performs real-time object detection and multi-object tracking using **YOLOv8** and **ByteTrack**. The pipeline detects objects in each video frame, assigns persistent tracking IDs, and exports an annotated video with bounding boxes, labels, confidence scores, and track IDs.

---

## Features

- Real-time object detection with YOLOv8
- Multi-object tracking using ByteTrack
- Persistent tracking IDs across frames
- Bounding boxes with confidence scores
- Class labels for detected objects
- Annotated output video generation
- Gradio interface for interactive testing
- MLflow integration for experiment tracking

---

## Project Structure

```
YoLo8/
│
├── yolov8 bytetrack tracking.ipynb
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Ultralytics YOLOv8
- ByteTrack
- OpenCV
- Supervision
- Gradio
- MLflow

---

## Installation

Clone the repository

```bash
git clone https://github.com/AnshumanJ28/YoLo8.git
cd YoLo8
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Open the notebook using Jupyter Notebook or Google Colab.

```
yolov8 bytetrack tracking.ipynb
```

Run the cells sequentially to:

1. Install dependencies
2. Load the YOLOv8 model
3. Process the input video
4. Perform ByteTrack tracking
5. Generate the annotated output

---

## Pipeline

```
Input Video
      │
      ▼
YOLOv8 Detection
      │
      ▼
ByteTrack Tracking
      │
      ▼
Bounding Boxes
+ Class Labels
+ Confidence
+ Track IDs
      │
      ▼
Annotated Output Video
```

---

## Applications

- Traffic monitoring
- Smart surveillance
- Sports analytics
- Crowd monitoring
- Retail analytics
- Autonomous driving research

---

## Future Improvements

- Custom-trained YOLO models
- Vehicle counting
- Speed estimation
- Multi-camera tracking
- DeepSORT comparison
- Person re-identification

---

## Author

**Anshuman Pandey**

AI/ML Student | Computer Vision | Deep Learning | MLOps

GitHub: https://github.com/AnshumanJ28
