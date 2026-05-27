from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="dataset/data.yaml",
    epochs=25,
    imgsz=640,
    batch=8
)

model.predict(
    source="your_video.mp4",
    save=True,
    save_format="mp4"
)