# DermAI Business Pro v2.0 🩺✨

**Intelligent Skin Disease Detection & Personalized Care Management System**

---

## 🚀 Overview
DermAI is a professional-grade, AI-powered computer vision solution designed to provide preliminary skin condition analysis and personalized treatment recommendations. By combining **Deep Learning (MobileNetV2)** with a robust **Recommendation Engine**, DermAI bridges the gap between early symptoms and professional dermatological guidance.

> **Business Edition Features**: Now includes a full Business Intelligence Dashboard and Automated Clinical PDF Reporting.

---

## ✨ Key Features
- **🎯 Precision Detection**: Classifies skin lesions into 7 distinct categories (HAM10000 standard) using Transfer Learning.
- **📊 BI Dashboard**: A central command center to monitor system performance, detection accuracy, and patient analysis stats.
- **🌿 Hybrid Recommendations**: Provides a dual-path care plan featuring both **Medicated Clinical Treatments** and **Herbal/Natural Remedies**.
- **🧬 Skin Type Personalization**: Tailors advice specifically for Oily, Dry, Sensitive, or Combination skin types.
- **📄 Professional PDF Reports**: Generates instant, download-ready clinical reports for users to take to their healthcare providers.
- **🌸 Premium Aesthetic**: A high-fidelity, pink-and-purple "Glassmorphism" interface designed for a modern user experience.

---

## 🛠️ Technology Stack
- **AI Framework**: TensorFlow 2.19 / Keras
- **Computer Vision**: OpenCV (Open Source Computer Vision Library)
- **Backend**: Flask (Python Web Framework)
- **Reporting**: FPDF2 (Professional PDF Generation)
- **Frontend**: Vanilla JS, CSS3 (Custom Design System), HTML5
- **Data Handling**: NumPy, Pandas, Scikit-learn

---

## 📂 Project Structure
```text
OpenCV_Project/
├── app/
│   ├── static/             # CSS, JS, and UI Assets
│   ├── templates/          # Dashboard and Analyzer HTML
│   └── app.py              # Flask Server Backend
├── data/
│   ├── processed/          # Visual analysis outputs
│   └── sample_images/      # Test datasets
├── models/                 # Pre-trained model weights (.h5)
├── notebooks/              # R&D and Training experiments
├── src/
│   ├── model.py            # CNN Architecture definition
│   ├── preprocessing.py    # Image optimization pipeline
│   ├── recommendation.py   # Hybrid care logic
│   └── reports.py          # PDF Generation engine
├── main.py                 # CLI Inference Entry point
├── requirements.txt        # Production dependencies
└── README.md               # Documentation
```

---

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd OpenCV_Project
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the System**:
   ```bash
   python app/app.py
   ```
   Open your browser at `http://127.0.0.1:5000`

---

## 🎯 Usage

### Web Interface (Recommended)
1. Navigate to the **DermAI Pro Dashboard**.
2. Click **"Launch Analyzer"**.
3. Drag & Drop a clear image of the skin lesion.
4. Select your **Skin Type**.
5. View analysis and click **"Download Report"** for your PDF copy.

### CLI Mode (Advanced)
For batch processing or server-side analysis:
```bash
python main.py --image data/sample_images/test_skin.png --skin_type dry
```

---

## 📊 Class Mapping
DermAI is trained on the ISIC / HAM10000 benchmark:
- **AKIEC**: Actinic keratoses
- **BCC**: Basal cell carcinoma
- **BKL**: Benign keratosis-like lesions
- **DF**: Dermatofibroma
- **MEL**: Melanoma
- **NV**: Melanocytic nevi
- **VASC**: Vascular lesions

---

## ⚖️ Medical Disclaimer
**IMPORTANT**: DermAI is an artificial intelligence system designed for **educational and awareness purposes only**. It is not a replacement for professional medical diagnosis, advice, or treatment. Always seek the advice of a board-certified dermatologist or other qualified health providers with any questions you may have regarding a medical condition.

---
**Developed with ❤️ by the DermAI Engineering Team**
