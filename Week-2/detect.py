from ultralytics import YOLO

model=YOLO('yolov8n.pt')
results=model("https://ultralytics.com/images/bus.jpg", show=True)

results[0].save(filename="bus_detected.jpg")