# YOLO Dataset Structure and Format Report

This report provides a detailed breakdown of the standard dataset structure required by YOLO object detection models, based on an exploration of the `datasets/coco8` directory.

## 1. Dataset Folder Structure

The YOLO standard requires a specific and organized directory structure to separate image data from annotation (label) data, and further splits them into subsets for training, validation, and testing.

In the explored `coco8` dataset, the structure is as follows:

```text
datasets/
└── coco8/
    ├── images/
    │   ├── train/  # Contains training images (.jpg, .png, etc.)
    │   └── val/    # Contains validation images
    ├── labels/
    │   ├── train/  # Contains training labels (.txt)
    │   └── val/    # Contains validation labels (.txt)
    ├── LICENSE
    └── README.md
```

### Key Rules:
- **Mirroring:** The `images` and `labels` directories must mirror each other exactly. For example, if there is an image located at `images/train/000000000009.jpg`, its corresponding annotation file must be at `labels/train/000000000009.txt`.
- **Modularity:** This structure allows you to swap out image datasets easily and guarantees that data loaders can parse subsets (train vs. val) efficiently without mixing training data into validation evaluation.

---

## 2. YAML Configuration

YOLO uses a `.yaml` configuration file to tie the folder structure together and inform the model about the dataset's specific properties. While not always manually stored in the dataset directory (often pre-configured in libraries like Ultralytics for known datasets like COCO8), a custom dataset would require a file typically named `data.yaml` or `dataset.yaml`.

A typical YAML configuration looks like this:

```yaml
# Dataset Root Path
path: ../datasets/coco8

# Train/Val/Test Splits (relative to 'path')
train: images/train
val: images/val
test:  # (Optional)

# Classes
nc: 80  # Number of classes
names:
  0: person
  1: bicycle
  2: car
  ...
  # Maps integer class IDs to string names
```

### Role of the YAML File:
It acts as the **single source of truth** for the model during training. The data loader reads the `train` and `val` paths, calculates the number of expected classes (`nc`), and maps the class outputs to human-readable `names` during inference plotting.

---

## 3. Label File Format

YOLO models expect annotation data in a specific normalized text format. Each image in the dataset has a corresponding `.txt` file containing the bounding box annotations for all objects in that image. 

Upon viewing `labels/train/000000000009.txt`, the format is confirmed as follows:

```text
45 0.479492 0.688771 0.955609 0.5955
49 0.646836 0.132552 0.118047 0.0969375
...
```

### Structure:
Each line represents one bounding box and follows this syntax:
`<class-id> <x_center> <y_center> <width> <height>`

- **`class-id`**: An integer representing the object class (0-indexed).
- **`x_center` & `y_center`**: The coordinates of the center of the bounding box. These are **normalized** (from 0.0 to 1.0) relative to the image's total width and height.
- **`width` & `height`**: The dimensions of the bounding box, also **normalized** relative to the image dimensions.

*Why normalize?* Normalization ensures that annotations remain accurate even if the images are resized by the data loader before being fed into the neural network.

---

## 4. Metadata Used by YOLO

During training and inference, YOLO generates and utilizes several forms of metadata:

1. **`.cache` Files (e.g., `labels/val.cache`)**
   - As observed in the `coco8/labels/` directory, YOLO creates a `.cache` file when a dataset is loaded for the first time.
   - **Purpose:** Scanning directories for thousands of images and parsing `.txt` files is slow. The cache file stores metadata such as image paths, image dimensions, parsed bounding box arrays, and flags for any corrupted or empty files. This significantly accelerates subsequent training runs.

2. **Dataset Configuration Metadata**
   - Derived from the YAML file, the model caches the number of classes (`nc`) and the class mapping (`names`) directly into the final trained model weights (`.pt` file). This allows the model to predict string labels without needing the YAML file again during deployment.

3. **Hyperparameter and Distribution Metadata**
   - Before training begins, YOLO analyzes the dataset's bounding boxes to calculate metadata like **class distributions** (to adjust focal loss or class weights) and **AutoAnchor** parameters (calculating optimal starting anchor box sizes based on the dataset's specific object sizes).

> [!TIP]
> Deleting the `.cache` files in the `labels/` directory forces YOLO to re-scan the dataset. This is highly recommended if you manually add, remove, or modify any images or `.txt` label files to ensure the model trains on the most up-to-date data.
