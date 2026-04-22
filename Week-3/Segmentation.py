from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

results = model(
    source=r"C:\Users\Anirudh Potukuchi\Documents\Internship-Works\iHubData-IIITH-Internship\Week-3\Objects-Motion-Video-Cropped-1min-audio.mp4",
    save=True,
    show=True
)