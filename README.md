# Resume Tailoring App

A Streamlit-based web application that helps you tailor your resume to match specific job descriptions.

## Overview

This application allows users to upload their resume and a job description, then generates a tailored resume based on the inputs. Users can also optionally provide a sample resume for style reference.

## Features

- **Resume Upload**: Upload your existing resume in TXT, DOCX, or PDF format
- **Job Description Upload**: Upload the job description you're applying for
- **Sample Resume (Optional)**: Upload a sample resume to use as a style reference
- **Generate Tailored Resume**: Create a customized resume based on your inputs
- **Download**: Download the tailored resume as a TXT file

## Requirements

- Python 3.7+
- Streamlit
- python-docx
- PyPDF2

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Resume_optimization
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Upload your resume and job description using the file uploaders

4. Optionally, upload a sample resume for style reference

5. Click "Generate Tailored Resume" to create your customized resume

6. Copy the result or use the download button to save it as a TXT file

## Supported File Formats

- `.txt` - Text files with text extraction
- `.docx` - Microsoft Word documents (using python-docx)
- `.pdf` - PDF documents (using PyPDF2)

All three formats are fully supported for text extraction.

## Future Enhancements

- LLM/OpenAI integration for intelligent resume tailoring
- Additional output formats

## License

This project is open source and available for use.
