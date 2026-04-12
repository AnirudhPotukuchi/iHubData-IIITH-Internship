from ultralytics import YOLO

model=YOLO('yolov8n.pt')
result=model(
    source=r"C:\Users\Anirudh Potukuchi\Documents\Internship-Works\iHubData-IIITH-Internship\Week-2\Objects-Motion-Video-Cropped-1min-audio.mp4",
    save=True,
    show=True,
)
