# 🐱🐶 Cat vs Dog Image Classification using CNN

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A complete end-to-end deep learning project that classifies images of cats and dogs using a Custom Convolutional Neural Network (CNN) built with TensorFlow/Keras. The trained model is deployed via a lightweight Flask web application, allowing users to upload an image and receive real-time predictions.

---

## 📌 Project Overview

This repository demonstrates a complete machine learning lifecycle, from raw data to a deployed web application. 

**Key Features:**
* Robust dataset preprocessing (corrupted image detection and removal)
* Automated Train/Test/Validation splits
* Data augmentation to prevent overfitting
* Custom deep CNN architecture
* Comprehensive model evaluation and metrics tracking
* User-friendly Flask web interface for model inference

---

## 📂 Project Structure

```text
cat-dog-classifier/
├── app/
│   ├── app.py                 # Flask application entry point
│   ├── templates/
│   │   └── index.html         # Web UI frontend
│   └── static/
│       └── uploads/           # Temporary storage for uploaded images
├── model/
│   └── model.h5               # Saved, trained CNN model
├── notebook/
│   └── training.ipynb         # Jupyter notebook containing the ML pipeline
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignored files and directories

📊 Dataset
Source: Microsoft Cats vs Dogs Dataset

Size: Approximately 25,000 images

Classes: Cat (0), Dog (1)

Preprocessing Pipeline:

Scanning for and deleting corrupted image files.

Splitting the data into Training, Validation, and Testing sets.

Organizing data into the directory structure required by TensorFlow's image_dataset_from_directory.

## 🛠 Technologies & Libraries

| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.x |
| **Deep Learning** | TensorFlow, Keras |
| **Computer Vision** | OpenCV, Pillow (PIL) |
| **Data Manipulation** | NumPy, Scikit-learn |
| **Visualization** | Matplotlib |
| **Backend/Web** | Flask |

🧠 Model Architecture
The custom CNN architecture is designed for optimal feature extraction and consists of progressively expanding convolutional blocks:

Input Image (128x128x3)
│
├── Conv2D (32) + BatchNorm + MaxPooling + Dropout
├── Conv2D (64) + BatchNorm + MaxPooling + Dropout
├── Conv2D (128) + BatchNorm + MaxPooling + Dropout
├── Conv2D (256) + BatchNorm + MaxPooling + Dropout
│
├── Flatten
├── Dense (512 neurons)
│
└── Output Layer (Sigmoid Activation for Binary Classification)

## ⚙️ Training Configuration

| Parameter | Value |
| :--- | :--- |
| **Image Size** | `128 x 128` |
| **Batch Size** | `32` |
| **Optimizer** | `Adam` |
| **Loss Function**| `Binary Crossentropy` |
| **Epochs** | `30` |

Data Augmentation Strategy:
Training images are augmented using Rotation, Zoom, Shear, Horizontal Flip, and Rescaling to improve model generalization.

Callbacks Implemented:

EarlyStopping: Halts training when validation loss stops improving.

ReduceLROnPlateau: Drops learning rate if learning stagnates.

ModelCheckpoint: Saves the best-performing weights.

CSVLogger: Logs epoch-level metrics to a file.

🚀 Running the Project Locally
1. Clone the repository

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/cat-dog-classifier.git](https://github.com/your-username/cat-dog-classifier.git)
cd cat-dog-classifier

2. Install dependencies
It is recommended to use a virtual environment.

pip install -r requirements.txt

3. Run the Flask application

cd app
python app.py

4. Open your browser
Navigate to http://127.0.0.1:5000. Upload an image of a cat or dog to see the model in action!

📌 Future Improvements
[ ] Implement Transfer Learning (ResNet50, EfficientNet, MobileNetV2) for higher accuracy.

[ ] Add confidence score percentages to the UI.

[ ] Implement Grad-CAM visualization to show what the model is "looking at".

[ ] Support multiple simultaneous image predictions.

[ ] Containerize the application using Docker.

[ ] Deploy to cloud platforms (Render, Railway, AWS, or Azure).

[ ] Build an alternative frontend using Streamlit.

👩‍💻 Author
Mahi Yadav
B.Tech (Industrial Internet of Things)

Deep Learning • Computer Vision • Machine Learning

If you found this repository helpful, please consider giving it a ⭐!
