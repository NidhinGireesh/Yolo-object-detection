# YOLOv8 Object Detection

## Overview

This project demonstrates object detection using the YOLOv8 (You Only Look Once) model from the Ultralytics library. The script loads a pre-trained YOLOv8 model, performs object detection on an image, and saves the output image with detected objects highlighted using bounding boxes.

## Features

* Uses the lightweight YOLOv8 Nano model (`yolov8n.pt`)
* Performs object detection on an image
* Automatically downloads the model if not available
* Saves the output image with bounding boxes and labels
* Simple and easy-to-understand implementation

## Project Structure

```text
yolo-object-detection/
│
├── detect.py
├── requirements.txt
├── results.jpg
├── .gitignore
└── README.md
```

## Prerequisites

* Python 3.11 or later
* pip package manager

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd yolo-object-detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the detection script:

```bash
python detect.py
```

The script will:

1. Load the YOLOv8 Nano model.
2. Perform object detection on the sample image.
3. Save the detected image as `results.jpg`.

## Sample Code

```python
from ultralytics import YOLO

# Load pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")

# Perform inference
results = model("https://ultralytics.com/images/bus.jpg")

# Save output image
for r in results:
    r.save(filename="results.jpg")

print("Detection completed!")
```

## Output

The generated `results.jpg` contains:

* Bounding boxes around detected objects
* Object class labels
* Confidence scores

Example detected objects may include:

* Person
* Bus
* Car
* Traffic Light

## Requirements

The project dependencies are listed in `requirements.txt`.

Example:

```text
ultralytics
opencv-python
torch
torchvision
```

## Technologies Used

* Python
* YOLOv8
* Ultralytics
* PyTorch
* OpenCV

## Author

**Nidhin Gireesh**
B.Tech Computer Science and Engineering
Government Engineering College, Idukki

## License

This project is created for educational and learning purposes.
