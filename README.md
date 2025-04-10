# Webstract
AI-Powered UI Element Detection in Website Screenshots using YOLOv8

---

## 🚀 Features

- Detects UI elements in website screenshots
- Trained using a custom YOLOv8 model
- Outputs visual bounding boxes with labels
- Easily extendable to more components or screen types

---

## 🧠 Tech Stack

- **Python** 🐍
- **YOLOv8 (Ultralytics)** for object detection
- **OpenCV** for image processing
- **Roboflow** for dataset management & annotation

---

## Dataset: [Dataset Used - Roboflow link](https://universe.roboflow.com/augmented-startups/website-elements-nmmi7/dataset/3)

---

## 🛠️ How to Run Locally

**Clone the repo**

```bash
git clone https://github.com/AtharvKasar04/Webstractor.git
cd Webstract
```
```bash
pip install -r requirements.txt
```

**Download your trained YOLOv8 weights**

You can export your model weights from Roboflow or wherever you've trained them (e.g., best.pt). Place the weights file inside a new folder:

```bash
Webstract/models/best.pt
```

## ▶️ Run Inference

To run object detection on a new screenshot:

```bash
python scripts/infer.py
```

This will:

- Load the trained YOLOv8 model from models/best.pt

- Read test image(s) from test_images/

- Show/save images with bounding boxes and labels

### Make sure to place test images inside the test_images/ folder.

---

To evaluate the trained model on your test set:

```bash
python scripts/evaluate.py
```

This script:

- Loads models/best.pt

- Evaluates it on datasets/dataset/test/

- Prints detailed metrics like mAP@50, mAP@50-95, Precision, Recall

---

## Folder Structure
![image](https://github.com/user-attachments/assets/33c45b6d-208d-444d-a3a0-4f47848b9271)

---

## 📄 License
This project is licensed under the MIT License.
