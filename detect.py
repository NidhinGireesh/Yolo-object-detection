import sys

try:
    from ultralytics import YOLO
except Exception:
    sys.exit("Missing dependency: 'ultralytics' is not installed. Install it with: pip install ultralytics")


# Load pre-trained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Run detection on an image
results = model("https://ultralytics.com/images/bus.jpg")

# Save the result image
for r in results:
    r.save(filename="results.jpg")

print("Detection completed!")
print("Output saved as results.jpg")