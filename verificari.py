import fitz  # PyMuPDF
import streamlit as st

def extract_data_from_pdf(pdf_file):
    """
    Extrage datele din PDF
    
    Args:
    pdf_file (UploadedFile): Fișierul PDF încărcat
    
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
    
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf:
        # Găsește pagina cu titlul "SITUATIA ACTIVELOR IMOBILIZATE"
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text("text")
            if "SITUATIA ACTIVELOR IMOBILIZATE" in text:
                st.write(f"Pagina {page_num}: {text}")  # Log textul paginii pentru verificare
                # Parsează textul pentru a extrage datele necesare
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    st.write(f"Linie {i + 1}: {line}")  # Log fiecare linie pentru verificare cu număr de linie
                    if "1.Cheltuieli de constituire" in line:
                        data['Cheltuieli de constituire'] = extract_value_from_lines(lines, i)
                    elif "2.Cheltuieli de dezvoltare" in line:
                        data['Cheltuieli de dezvoltare'] = extract_value_from_lines(lines, i)
                    elif "3.Concesiuni,brevete, licente" in line:
                        data['Concesiuni, brevete, licențe'] = extract_value_from_lines(lines, i)
                    elif "4.Fond comercial" in line:
                        data['Fond comercial'] = extract_value_from_lines(lines, i)
                    elif "5Active necorporale de explorare" in line:
                        data['Active necorporale de explorare'] = extract_value_from_lines(lines, i)
                    elif "6.Avansuri acordate pentru imobilizari necorporale" in line:
                        data['Avansuri'] = extract_value_from_lines(lines, i)
    return data

def extract_value_from_lines(lines, start_index):
    """
    Extrage valoarea numerică din liniile consecutive de text
    
    Args:
    lines (list): Liniile de text
    start_index (int): Indexul de început
    
    Returns:
    float: Valoarea numerică extrasă
    """
    for i in range(start_index, len(lines)):
        line = lines[i]
        st.write(f"Extracting value from line {i + 1}: {line}")  # Log linia pentru verificare
        # Adaptează această parte pentru a extrage corect valoarea
        parts = line.split()
        for part in parts:
            try:
                # Eliminăm virgulele și convertim în float
                value = float(part.replace(',', '').replace('-', ''))
                st.write(f"Extracted value: {value}")
                return value
            except ValueError:
                continue
    return 0.0






