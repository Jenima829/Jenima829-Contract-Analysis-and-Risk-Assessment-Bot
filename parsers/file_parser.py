# parsers/file_parser.py

import PyPDF2
import docx
import io


def parse_pdf(file):
    """Extract text from PDF"""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"

    return text


def parse_docx(file):
    """Extract text from DOCX"""
    doc = docx.Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def parse_txt(file):
    """Extract text from TXT"""
    stringio = io.StringIO(file.getvalue().decode("utf-8"))
    text = stringio.read()
    return text


def parse_contract(uploaded_file):
    """Main parser router"""

    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        return parse_pdf(uploaded_file)

    elif file_type == "docx":
        return parse_docx(uploaded_file)

    elif file_type == "txt":
        return parse_txt(uploaded_file)

    else:
        return "Unsupported file format"
