# Resume parsing logic
import PyPDF2
import docx2txt
import os

def extract_text_from_pdf(file):
    """Extracts text from a PDF file."""
    text = ""
    try:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    except Exception as e:
        text = f"[Error reading PDF: {e}]"
    return text.strip()

def extract_text_from_docx(file):
    """Extracts text from a DOCX file."""
    try:
        return docx2txt.process(file).strip()
    except Exception as e:
        return f"[Error reading DOCX: {e}]"

def extract_text_from_txt(file):
    """Extracts text from a TXT file."""
    try:
        return file.read().decode("utf-8").strip()
    except Exception as e:
        return f"[Error reading TXT: {e}]"

def parse_resume(file):
    """
    Detects file type and extracts text accordingly.
    Returns extracted text as a string.
    """
    ext = os.path.splitext(file.name)[1].lower()
    
    if ext == ".pdf":
        return extract_text_from_pdf(file)
    elif ext == ".docx":
        return extract_text_from_docx(file)
    elif ext == ".txt":
        return extract_text_from_txt(file)
    else:
        return "[Unsupported file type]"
