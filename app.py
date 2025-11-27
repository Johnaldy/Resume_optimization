import streamlit as st
from docx import Document
from PyPDF2 import PdfReader
import io

st.title("Resume Tailoring App")

st.write("Upload your resume and a job description, and get a tailored resume back!")

# Upload widgets
resume_file = st.file_uploader("Upload your resume", type=['txt', 'docx', 'pdf'])
job_file = st.file_uploader("Upload the job description", type=['txt', 'docx', 'pdf'])
sample_file = st.file_uploader("Optional: Upload a sample resume for style (txt/docx/pdf)", type=['txt', 'docx', 'pdf'])

def extract_text(uploaded_file):
    if uploaded_file is None:
        return ""
    
    file_name = uploaded_file.name.lower()
    
    # Handle TXT files
    if file_name.endswith(".txt"):
        return uploaded_file.getvalue().decode("utf-8")
    
    # Handle DOCX files using python-docx
    if file_name.endswith(".docx"):
        try:
            doc = Document(io.BytesIO(uploaded_file.getvalue()))
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        except Exception:
            return "Error reading DOCX file. Please ensure the file is a valid DOCX document."
    
    # Handle PDF files using PyPDF2
    if file_name.endswith(".pdf"):
        try:
            reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
            text_parts = []
            for page in reader.pages:
                text_parts.append(page.extract_text() or "")
            return "".join(text_parts)
        except Exception:
            return "Error reading PDF file. Please ensure the file is a valid PDF document."
    
    # Unsupported file type
    return f"Unsupported file type: {file_name}. Please upload a TXT, DOCX, or PDF file."

if st.button("Generate Tailored Resume"):
    resume_text = extract_text(resume_file)
    job_text = extract_text(job_file)
    sample_text = extract_text(sample_file)

    # For now, use a simple dummy result (replace this block with LLM/OpenAI logic as needed)
    tailored_resume = (
        "Tailored Resume based on your input:\n\n"
        f"Original Resume:\n{resume_text}\n\n"
        f"Job Description:\n{job_text}\n\n"
        f"Sample Resume (if any):\n{sample_text}\n"
        "\nEdit this with your favorite edits or use LLM integration!"
    )

    st.subheader("Your tailored resume below (copy or download):")
    st.text_area("Result", value=tailored_resume, height=300)
    st.download_button("Download tailored resume as TXT", tailored_resume, file_name="tailored_resume.txt")
