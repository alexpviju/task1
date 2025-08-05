# 🧠 Image Classification with Lightweight Models

This project demonstrates image classification on a small **Cats vs Dogs** dataset using three efficient and lightweight deep learning models:
- **MobileNetV2**
- **MobileNetV3-Small**
- **YOLOv8n-cls (Ultralytics)**

All models are optimized for low inference time (preferably under 20ms/image) while maintaining reasonable accuracy.

---

## 📁 Project Structure

```
img-classification/
├── cifar2/                # Dataset directory (train/valid)
├── myenv/                 # Python virtual environment
├── runs/classify/         # YOLOv8 classification logs
├── arrange.py             # Script to prepare dataset
├── img_classi.ipynb       # Main Jupyter notebook
├── mobilenetv2.pth        # Saved MobileNetV2 model
├── mobilenetv3small.pth   # Saved MobileNetV3-Small model
└── yolov8n-cls.pt         # Saved YOLOv8n classification model
```

---

## 📝 Steps to Reproduce

### 1. 🔧 Environment Setup

```bash
python -m venv myenv
myenv\Scripts\activate   # On Windows
pip install torch torchvision ultralytics scikit-learn matplotlib
```

---

### 2. 📦 Dataset Preparation

- Download a small Cats vs Dogs dataset (100 cat + 100 dog images).
- Organize as follows:

```
cifar2/
├── train/
│   ├── cat/  
│   └── dog/  
└── valid/
    ├── cat/ 
    └── dog/  
```

- If your dataset contains all images mixed (e.g., `cat.0.jpg`, `dog.0.jpg`), use the `arrange.py` script to split into folders.

---

### 3. 🚀 Train Models (in `img_classi.ipynb`)

Each of the following models is trained and evaluated in the notebook:

#### ✅ MobileNetV2
- Fine-tuned on `cifar2/train`
- Saved as `mobilenetv2.pth`

#### ✅ MobileNetV3-Small
- Smaller version of MobileNet
- Saved as `mobilenetv3small.pth`

#### ✅ YOLOv8n-cls
- Ultralytics classification model
- Trained via `ultralytics` library
- Saved as `yolov8n-cls.pt`

---

### 📊 Model Evaluation

Each model is evaluated using:
- **Accuracy**
- **Average inference time per image**

---

## 📊 Comparison Table

| Model              | Accuracy (%) | Inference Time (ms/image) |
|-------------------|--------------|----------------------------|
| MobileNetV2        | 86.00        | 19.21                      |
| MobileNetV3-Small  | 76.00        | 11.13                      |
| YOLOv8n-cls        | 73.00        | 8.60                     |

> 📌 You can update accuracy/inference time with your actual evaluation results.

---

## 💾 Saving and Loading Models

Each model is saved using `torch.save(model.state_dict(), 'filename.pth')` and loaded with the same architecture + `load_state_dict()`.

---

## 🧪 Inference

Inference results and timing are recorded using `time.time()` and `accuracy_score()` from `sklearn`.

---

## 👨‍💻 Author

**Name:** Alex P V  
**Task:** Task 1 - Lightweight Image Classification  
**Tools:** PyTorch, Torchvision, Ultralytics, Scikit-learn, Matplotlib

---

## 📌 Notes

- Models are selected to ensure **< 20ms** inference where possible.
- Trained on CPU/GPU depending on availability.

---
