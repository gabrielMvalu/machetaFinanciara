import fitz  # PyMuPDF
import streamlit as st

def find_page_with_phrase(pdf_content, phrase):
    """
    Find the page number in the PDF that contains the specified phrase.
    
    Args:
    pdf_content (bytes): The content of the uploaded PDF file
    phrase (str): The phrase to search for
    
    Returns:
    int: The page number containing the phrase (1-based index), or -1 if not found
    """
    with fitz.open(stream=pdf_content, filetype="pdf") as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text("text")
            if phrase in text:
                return page_num + 1  # Returning 1-based page number
    return -1

def extract_data_from_pdf(pdf_content):
    """
    Extract data from PDF
    
    Args:
    pdf_content (bytes): The content of the uploaded PDF file
    
    Returns:
    dict: Extracted data organized in a dictionary
    """
    data = {
        "Cheltuieli de constituire": 0.0,
        "Cheltuieli de dezvoltare": 0.0,
        "Concesiuni, brevete, licențe": 0.0,
        "Fond comercial": 0.0,
        "Active necorporale de explorare": 0.0,
        "Avansuri": 0.0
    }
    
    page_num = find_page_with_phrase(pdf_content, "SITUATIA ACTIVELOR IMOBILIZATE")
    
    if page_num == -1:
        st.write("Fraza 'SITUATIA ACTIVELOR IMOBILIZATE' nu a fost găsită în PDF.")
        return data
    else:
        st.write(f"Fraza 'SITUATIA ACTIVELOR IMOBILIZATE' a fost găsită la pagina {page_num}.")
    
    with fitz.open(stream=pdf_content, filetype="pdf") as pdf:
        page = pdf.load_page(page_num - 1)  # Subtracting 1 to get the correct index
        text = page.get_text("text")
        lines = text.split('\n')
        for line in lines:
            st.write(f"Linie: {line}")  # Log fiecare linie pentru verificare
            if "1.Cheltuieli de constituire" in line:
                data['Cheltuieli de constituire'] = extract_value_from_line(line)
            elif "2.Cheltuieli de dezvoltare" in line:
                data['Cheltuieli de dezvoltare'] = extract_value_from_line(line)
            elif "3.Concesiuni,brevete, licente" in line:
                data['Concesiuni, brevete, licențe'] = extract_value_from_line(line)
            elif "4.Fond comercial" in line:
                data['Fond comercial'] = extract_value_from_line(line)
            elif "5Active necorporale de explorare" in line:
                data['Active necorporale de explorare'] = extract_value_from_line(line)
            elif "6.Avansuri acordate pentru imobilizari necorporale" in line:
                data['Avansuri'] = extract_value_from_line(line)
    
    return data

def extract_value_from_line(line):
    """
    Extract numeric value from a line of text
    
    Args:
    line (str): The line of text
    
    Returns:
    float: Extracted numeric value
    """
    st.write(f"Extracting value from line: {line}")  # Log the line for verification
    parts = line.split()
    for part in parts:
        try:
            value = float(part.replace(',', '').replace('-', ''))
            st.write(f"Extracted value: {value}")
            return value
        except ValueError:
            continue
    return 0.0




