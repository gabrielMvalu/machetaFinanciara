import fitz  # PyMuPDF
import streamlit as st

def find_page_with_phrase(pdf_content, phrase):
    """
    Find the page number in the PDF that contains the specified phrase.
    
    Args:
    pdf_content (bytes): The content of the uploaded PDF file
    phrase (str): The phrase to search for
    
    Returns:
    list: List of page numbers containing the phrase
    """
    found_pages = []
    
    with fitz.open(stream=pdf_content, filetype="pdf") as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text("text")
            if phrase in text:
                found_pages.append(page_num + 1)  # Adding 1 to match human-readable page numbers
                st.write(f"Found phrase on page {page_num + 1}")
    
    return found_pages

def extract_data_from_pdf(pdf_content):
    """
    Extrage datele din PDF
    
    Args:
    pdf_content (bytes): The content of the uploaded PDF file
    
    Returns:
    dict: Datele extrase organizate într-un dicționar
    """
    data = {
        "Cheltuieli de constituire": 0.0,
        "Cheltuieli de dezvoltare": 0.0,
        "Concesiuni, brevete, licențe": 0.0,
        "Fond comercial": 0.0,
        "Active necorporale de explorare": 0.0,
        "Avansuri": 0.0
    }
    
    pages_with_phrase = find_page_with_phrase(pdf_content, "SITUATIA ACTIVELOR IMOBILIZATE")
    
    if not pages_with_phrase:
        st.write("Phrase 'SITUATIA ACTIVELOR IMOBILIZATE' not found in any page.")
        return data
    
    with fitz.open(stream=pdf_content, filetype="pdf") as pdf:
        for page_num in pages_with_phrase:
            page = pdf.load_page(page_num - 1)  # Subtracting 1 to get the correct index
            text = page.get_text("text")
            lines = text.split('\n')
            for line in lines:
                st.write(f"Line: {line}")  # Log fiecare linie pentru verificare
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
    Extrage valoarea numerică dintr-o linie de text
    
    Args:
    line (str): Linia de text
    
    Returns:
    float: Valoarea numerică extrasă
    """
    st.write(f"Extracting value from line: {line}")  # Log linia pentru verificare
    # Adaptează această parte pentru a extrage corect valoarea
    parts = line.split()
    for part in parts:
        try:
            value = float(part.replace(',', '').replace('-', ''))
            st.write(f"Extracted value: {value}")
            return value
        except ValueError:
            continue
    return 0.0




