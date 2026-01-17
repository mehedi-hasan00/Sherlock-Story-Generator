# 🕵️ Sherlock Holmes Story Generator

A Deep Learning based **Next Word Prediction** project trained on Sherlock Holmes stories. This model uses **Long Short-Term Memory (LSTM)** networks to generate creative text that mimics the writing style, vocabulary, and character interactions of Sir Arthur Conan Doyle.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

🌐 **Live App:** [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)

---

## 🚀 Live Demo

🔗 **Streamlit App:** [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)

Run the Streamlit app to generate your own mystery-style text.

**Input**
`Sherlock Holmes said to me`

**AI Output (Example)**
`...upon the lawn that morning and he would never be on the scene of the next room`

---

## 🧠 Project Overview

The goal of this project is to build a language model capable of predicting the **next word** in a sentence.

By training on a large corpus of Sherlock Holmes stories, the model learns:

* **Grammar & Sentence Structure** – forms coherent English sentences
* **Context Awareness** – remembers characters like *Oakshott* or *The Lascar*
* **Writing Style** – captures the classic Victorian-era mystery tone

---

## 🛠️ Model Architecture

Built using **Keras / TensorFlow**:

1. **Embedding Layer** – converts words into dense vectors
2. **LSTM Layer 1** – 150 units (captures sequence patterns)
3. **LSTM Layer 2** – 150 units (captures deeper context)
4. **Dropout Layer** – 0.1 (reduces overfitting)
5. **Dense Output Layer** – Softmax activation

**Training Configuration**

* Loss Function: `sparse_categorical_crossentropy`
* Optimizer: `Adam`
* Training Accuracy: ~73% (balanced for creativity)

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mehedi-hasan00/sherlock-story-generator.git
cd sherlock-story-generator
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
conda create -n sherlock python=3.10
conda activate sherlock
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
├── next_word_prediction.ipynb   # Model training notebook
├── app.py                       # Streamlit web app
├── sherlock_model.keras         # Trained LSTM model
├── tokenizer.pickle             # Tokenizer for word decoding
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
```

---

## 📝 requirements.txt

Keep this file in the repository to ensure smooth setup and avoid **Protobuf-related errors**.

```txt
tensorflow
numpy
streamlit
pickle-mixin
protobuf==5.29.0
```

---

## 📊 Performance

* Epochs: 100
* Training Accuracy: ~73%
* Loss: ~0.99

The model avoids strict memorization and produces creative outputs consistent with the mystery genre.

---

## 🤝 Future Improvements

* Train on the complete Sherlock Holmes collection
* Implement **Beam Search** for better sentence flow
* Deploy to **Streamlit Cloud**

---

## 👤 Author

**Mehedi Hasan**

* 🔗 Kaggle: [https://www.kaggle.com/mehedi71](https://www.kaggle.com/mehedi71)
* 🔗 LinkedIn: [https://www.linkedin.com/in/mehedi-hasan-094855388/](https://www.linkedin.com/in/mehedi-hasan-094855388/)

