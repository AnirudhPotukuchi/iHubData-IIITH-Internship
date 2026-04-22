from ultralytics import YOLO

import time
start = time.time()

model = YOLO("yolov8n.pt")

results = model(
    source=r"C:\Users\Anirudh Potukuchi\Documents\Internship-Works\iHubData-IIITH-Internship\Week-3\Objects-Motion-Video-Cropped-1min-audio.mp4",
    save=True,
    show=True,
    conf=0.25
)

end = time.time()

print("Total Execution Time:", round(end - start, 2), "seconds")
print("Detection Completed")

metrics = model.val(data="coco8.yaml")
print(metrics)