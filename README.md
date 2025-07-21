# 🌿 Fasal Doctor: AI-Powered Plant Disease Diagnosis

**An intelligent assistant for Indian farmers, providing instant crop disease diagnosis and actionable remedy plans using the power of Computer Vision and Large Language Models.**

---

## 🎯 The Mission

In India, small-scale farmers form the backbone of our agriculture, yet they often face significant crop losses due to diseases they can't identify or treat quickly. Access to expert agronomists is limited and often too slow.

**Fasal Doctor** aims to bridge this gap by putting an AI-powered agronomist in every farmer's pocket. By simply taking a photo of a plant leaf, farmers can get an instant, accurate diagnosis and a clear, easy-to-understand action plan in seconds.

---

## ✨ Key Features

-   **Instant AI Diagnosis:** Uses a deep learning model trained on over 70,000 images to identify 38 different plant diseases.
-   **High Accuracy:** The computer vision model achieves high precision in identifying diseases across various crops like Tomato, Potato, Apple, and more.
-   **Detailed Remedy Plans:** Leverages a powerful Large Language Model (Groq Llama-3) to generate practical, step-by-step remedy plans.
-   **Actionable Advice:** Provides both organic and chemical solutions, along with crucial prevention tips for future seasons.
-   **Simple & Intuitive UI:** Built with Streamlit for a clean, user-friendly interface that requires no technical skills to operate.

---

## 🛠️ How It Works: The Tech Stack

Fasal Doctor employs a sophisticated two-stage AI pipeline:

1.  **Stage 1: Vision AI (The "Eyes")**
    -   A user uploads an image of a plant leaf.
    -   A **TensorFlow/Keras-based Convolutional Neural Network (CNN)** analyzes the image.
    -   The model predicts the most likely disease and provides a confidence score.
    -   **Technology:** `TensorFlow`, `Keras`, `Pillow`

2.  **Stage 2: Language AI (The "Brain")**
    -   The predicted disease name is passed to a Large Language Model.
    -   Using a carefully crafted prompt and the **Groq API**, the **Llama-3 LLM** generates a detailed, structured, and easy-to-understand remedy plan.
    -   **Technology:** `LangChain`, `langchain-groq`, 

The entire application is served through a user-friendly web interface built with **Streamlit**.

---

## 📂 Project Structure

The project is organized with a modular and scalable structure to ensure maintainability and robustness.

```
fasal_doctor/
├── app.py              # Main Streamlit UI file
├── main.py             # Script for command-line testing
├── requirements.txt    # Project dependencies
├── setup.py            # Project setup script
├── .env                # Environment variables (API keys)
├── src/
│   ├── agent/
│   │   └── workflow.py   # Main analysis pipeline orchestrator
│   ├── components/
│   │   ├── model_predictor.py
│   │   └── remedy_generator.py
│   ├── config/
│   │   └── config.yaml   # Configuration for model paths and class names
│   ├── exception/      # Custom exception handling
│   ├── logger/         # Logging setup
│   ├── prompts/
│   │   └── sys_prompt.py
│   └── utils/
│       └── common.py     # Utility functions
├── models/
│   └── plant_disease_model_v1.h5 # The trained deep learning model
└── notebooks/
    └── 1_model_training.ipynb    # Jupyter notebook for model training
```

---

## 🚀 Getting Started: Setup and Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.9 or higher
-   An API key from [Groq](https://console.groq.com/keys)

### Installation Guide

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Tushar7012/FASAL_AI.git
    cd FASAL_AI
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    -   Create a new file named `.env` in the root directory.
    -   Add your Groq API key to this file:
        ```
        GROQ_API_KEY="your_actual_api_key_here"
        ```

5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
    Your web browser will automatically open with the Fasal Doctor application running!

---

## 📖 How to Use

1.  **Launch the App:** Run the `streamlit run app.py` command.
2.  **Upload Image:** Click the "Choose an image..." button and select a clear photo of a plant leaf.
3.  **Analyze:** Click the "Analyze Image" button.
4.  **View Results:** The AI will display the diagnosed disease, its confidence level, and a complete, detailed action plan.

---

## 🔮 Future Scope

-   **Multi-Language Support:** Translate the UI and remedy plans into major Indian languages.
-   **Mobile Application:** Develop a native Android/iOS app for easier access in the field.
-   **Offline Mode:** Allow the vision model to work offline, with remedy plans synced when a connection is available.
-   **Community Forum:** A place for farmers to share results, ask questions, and help each other.

---

## 🙏 Acknowledgements

This project would not be possible without the comprehensive **New Plant Diseases Dataset** available on Kaggle.
-   **Dataset:** [New Plant Diseases Dataset (Augmented)](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

---

