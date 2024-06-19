import fitz  # PyMuPDF
import streamlit as st

def find_page_with_phrase(pdf_file, phrase):
    """
    Find the page number in the PDF that contains the specified phrase.
    
    Args:
    pdf_file (UploadedFile): The uploaded PDF file
    phrase (str): The phrase to search for
    
    Returns:
    list: List of page numbers containing the phrase
    """
    found_pages = []
    
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text("text")
            if phrase in text:
                found_pages.append(page_num)
    
    return found_pages

# Streamlit interface
st.title("Find Phrase in PDF")

# Upload PDF file
pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])

# Define the phrase to search for
phrase = "SITUATIA ACTIVELOR IMOBILIZATE"

if pdf_file is not None:
    # Find the pages containing the phrase
    pages_with_phrase = find_page_with_phrase(pdf_file, phrase)
    
    # Show the result in Streamlit
    if pages_with_phrase:
        st.write(f"Phrase '{phrase}' found on pages: {pages_with_phrase}")
    else:
        st.write(f"Phrase '{phrase}' not found in the PDF.")







