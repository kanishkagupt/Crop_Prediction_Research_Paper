# 🌱 AgriVision - Crop Prediction & Fertilizer Recommendation System

🚀 Smart agriculture solution using Machine Learning to predict the best crops and recommend fertilizers based on soil and environmental conditions.

---

## 📌 Overview

AgriVision is a machine learning-based decision support system designed to help farmers choose the most suitable crop and fertilizer for their land. It uses soil nutrients and environmental parameters to provide accurate, real-time recommendations.

The system aims to reduce crop failure and improve agricultural productivity through data-driven insights.

---

## 🎯 Key Features

* 🌾 **Crop Prediction**

  * Predicts the best crop among **22 crop types**
* 🧪 **Fertilizer Recommendation**

  * Suggests fertilizers based on soil nutrient deficiencies (N, P, K)
* ⚡ **High Accuracy**

  * Achieves **98.18% accuracy** using Support Vector Classifier (SVC)
* 🌐 **Web-Based Interface**

  * Built using Flask with a simple and user-friendly UI
* 📊 **Real-Time Results**

  * Instant prediction based on user input

---

## 🧠 Machine Learning Models Used

* Logistic Regression
* Support Vector Classifier (SVC with RBF Kernel)

📈 **Model Performance:**

* SVC Accuracy: **98.18%**
* Logistic Regression Accuracy: **97.05%**

---

## 📥 Input Parameters

The system takes the following 7 inputs:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

---

## 🛠️ Tech Stack

| Component     | Technology            |
| ------------- | --------------------- |
| Programming   | Python 3.8+           |
| Backend       | Flask                 |
| ML Library    | Scikit-learn          |
| Frontend      | HTML, CSS, JavaScript |
| Data Handling | Pandas, NumPy         |
| Visualization | Matplotlib, Seaborn   |

---

## 📁 Project Structure

```
.
├── CropPrediction_G-19/        # Main project code
├── docs/                      # Project documents
│   ├── research-paper.pdf
│   ├── ai-report.pdf
│   └── plagiarism-report.pdf
├── README.md
```

---

## 📄 Documents

* 📘 Research Paper → [View](docs/research-paper.pdf)
* 🤖 AI Report → [View](docs/ai-report.pdf)
* 📊 Plagiarism Report → [View](docs/plagiarism-report.pdf)

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Crop_Prediction_Research_Paper.git
cd Crop_Prediction_Research_Paper
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Example Prediction

Input:

```
N = 90, P = 42, K = 43  
Temperature = 20°C  
Humidity = 82%  
pH = 6.5  
Rainfall = 202 mm
```

Output:

```
Recommended Crop: Rice
```

---

## 🚧 Limitations

* Requires manual input of soil parameters
* Limited to dataset of 22 crops
* Does not consider regional variations
* English-only interface

---

## 🔮 Future Improvements

* 🌦️ Integration with real-time weather APIs
* 🌍 Region-specific crop models
* 📱 Mobile application (React Native)
* 🌐 Multilingual support
* 🔌 IoT-based automatic data collection
* 📊 Explainable AI using SHAP

---

## 🙏 Acknowledgment

This project was developed as part of an academic research initiative at **Chitkara University, Punjab**. Special thanks to the Kaggle community for providing the dataset.

---

## 👨‍💻 Authors

* Kanishka Gupta
* Vansh Pant
* Dr. Shikha Tuteja

---

## 📜 License

This project is for academic and educational purposes.

---

⭐ If you like this project, don’t forget to star the repo!

