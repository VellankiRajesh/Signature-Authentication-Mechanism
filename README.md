# ✍️ Signature Authentication Mechanism

A Flask-based machine learning project that verifies whether a signature is **real or forged** using OpenCV, scikit-learn, and a trained model.

---

## 🚀 Project Overview

This system uses computer vision and machine learning to compare uploaded signature images with trained data and determine authenticity. It's designed with simplicity, modularity, and extendability in mind.

---

## 🧠 How It Works

1. Signature image is uploaded via a Flask web app
2. OpenCV extracts visual features from the image
3. A pre-trained model (stored as `model.pkl`) makes the prediction
4. The result ("Real" or "Forged") is displayed on the web interface

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

git clone (https://github.com/VellankiRajesh/Signature-Authentication-Mechanism.git)
cd Signature-Authentication-Mechanism


### 2️⃣ Create & Activate Virtual Environment

python3 -m venv myenv

# For Linux/macOS:
source myenv/bin/activate

# For Windows:
myenv\Scripts\activate


### 3️⃣ Install Requirements

pip install -r requirements.txt

### 4️⃣ Run the Flask App

python app.py


Go to your browser and open:
http://127.0.0.1:5000




