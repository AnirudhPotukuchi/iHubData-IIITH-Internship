# YOLO Dataset Folder Structure

Below is the structured representation of the `datasets` folder (specifically for the `coco8` dataset) required by YOLO object detection models:

```markdown
    datasets/
    └── coco8/
        ├── images/
        │   ├── train/        # Contains training images (.jpg, .png, etc.)
        │   └── val/          # Contains validation images (.jpg, .png, etc.)
        ├── labels/
        │   ├── train/        # Contains training annotation files (.txt)
        │   ├── val/          # Contains validation annotation files (.txt)
        │   └── val.cache     # YOLO generated cache file for faster data loading
        ├── LICENSE           # Dataset license information
        └── README.md         # Dataset documentation and overview
```

### Key Requirements for this Structure:
- **Image and Label Matching**: The `images` and `labels` directories must mirror each other exactly. An image at `images/train/image_01.jpg` must have its corresponding bounding box annotations located at `labels/train/image_01.txt`.
- **Data Splits**: The dataset is explicitly split into `train` (data the model learns from) and `val` (data the model is evaluated against during training).
