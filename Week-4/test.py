from ultralytics import YOLO

model = YOLO("runs/detect/train2/weights/best.pt")

model.predict(
    source="Regular-Indian-Traffic.mp4",
    save=True,
    show=True
)