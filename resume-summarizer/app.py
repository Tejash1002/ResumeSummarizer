# ===================================================================
# 1. IMPORTS
# ===================================================================
import streamlit as st
import PyPDF2
from transformers import pipeline  

# Load Hugging Face summarization pipeline
@st.cache_resource  
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# ===================================================================
# 2. THE SUMMARIZATION FUNCTION
# ===================================================================
def summarize_with_hf(resume_text):
    if not resume_text:
        return "Error: No text provided for summarization."
    try:
        num_words = len(resume_text.split())

        max_len = min(150, int(num_words * 0.75))
        min_len = min(100, int(max_len * 0.75))

        summary = summarizer(
            resume_text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )[0]['summary_text']

        sentences = summary.split('. ')
        bullet_points = "\n".join(f"- {s.strip()}" for s in sentences if s)
        return bullet_points

    except Exception as e:
        return f"An error occurred: {e}"

# ===================================================================
# 3. PDF TEXT EXTRACTION
# ===================================================================
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:  
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

# ===================================================================
# 4. STREAMLIT UI
# ===================================================================
st.set_page_config(page_title="Resume Summarizer", layout="wide")
st.title("📄 AI-Powered Resume Summarizer (Hugging Face)")
st.write("Upload a resume in PDF format or paste text to get a concise bullet-point summary.")

input_method = st.radio("Select Input Method", ('Upload a PDF', 'Paste Text'))
resume_text = ""

if input_method == 'Upload a PDF':
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
else:
    resume_text = st.text_area("Paste your resume text here", height=300)

if st.button("✨ Summarize"):
    if resume_text:
        with st.spinner("Generating summary..."):
            summary = summarize_with_hf(resume_text)
            st.subheader("Generated Summary")
            st.text(summary)
    else:
        st.warning("Please upload a PDF or paste text.")