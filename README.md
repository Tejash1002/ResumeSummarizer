# 📄 AI-Powered Resume Summarizer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.com) This project uses a **Hugging Face Transformer model** to generate concise, bullet-point summaries from resume text or PDF files, all wrapped in a simple and interactive web app built with **Streamlit**.

---

## 📘 Project Overview

The goal of this project is to:

* Build a user-friendly tool for quick resume analysis and summarization.
* Process resumes from both raw text input and uploaded PDF files.
* Leverage a powerful pre-trained AI model for high-quality, abstractive summarization.
* Deploy the tool as a live, interactive web application.

---

## 🧠 Tech Stack

* **Python 3.9+**
* **Streamlit** — For building and serving the interactive web interface.
* **Hugging Face Transformers** — For the core AI summarization pipeline (`facebook/bart-large-cnn`).
* **PyPDF2** — For reliably extracting text from PDF documents.

---

## 📁 Folder Structure

```
ResumeSummarizer/
│
├── app.py              # The main Streamlit application script
├── requirements.txt    # Required Python packages for setup
├── .gitignore          # Specifies files for Git to ignore
├── Sample Resumes/     # (Optional) Folder for sample PDFs
└── README.md           # This documentation file
```

---

## ⚙️ Setup and Instructions

### 1️⃣ Clone this Repository

```bash
git clone [https://github.com/Tejash1002/ResumeSummarizer.git](https://github.com/Tejash1002/ResumeSummarizer.git)
cd ResumeSummarizer
```

### 2️⃣ Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to keep project dependencies isolated.

- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3️⃣ Install Required Packages

Install all the necessary libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
pip install streamlit PyPDF2 transformers torch
```

### 4️⃣ Run the Streamlit App

Start the Streamlit server to launch the web application.

```bash
streamlit run app.py
```
Your web browser should open with the application running.

---

## 🚀 How to Use the App

1.  Once the app is running, choose your preferred input method: **'Upload a PDF'** or **'Paste Text'**.
2.  If uploading, click **'Browse files'** and select a resume in PDF format from your computer.
3.  If pasting text, copy the full content of the resume into the text area provided.
4.  Click the **"✨ Summarize"** button to start the AI generation.
5.  Within seconds, a concise, bullet-pointed summary will appear on the screen.

---

## 👤 Author

**Tejash**

* [**GitHub Profile**](https://github.com/Tejash1002)

⭐ *If you found this project helpful, don’t forget to star the repository!*
