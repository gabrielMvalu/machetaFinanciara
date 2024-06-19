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
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text("text")
            if "SITUATIA ACTIVELOR IMOBILIZATE" in text:
                st.write(f"Pagina {page_num}: {text}")  # Log textul paginii pentru verificare
                # Parsează textul pentru a extrage datele necesare
                lines = text.split('\n')
                for line in lines:
                    st.write(f"Linie: {line}")  # Log fiecare linie pentru verificare
                    if "1. Cheltuieli de constituire" in line:
                        data['Cheltuieli de constituire'] = extract_value_from_line(line)
                    elif "2. Cheltuieli de dezvoltare" in line:
                        data['Cheltuieli de dezvoltare'] = extract_value_from_line(line)
                    elif "3. Concesiuni, brevete, licențe" in line:
                        data['Concesiuni, brevete, licențe'] = extract_value_from_line(line)
                    elif "4. Fond comercial" in line:
                        data['Fond comercial'] = extract_value_from_line(line)
                    elif "5. Active necorporale de explorare" in line:
                        data['Active necorporale de explorare'] = extract_value_from_line(line)
                    elif "6. Avansuri" in line:
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
    parts = line.split()
    for part in parts:
        try:
            # Extrage prima valoare numerică întâlnită în linie
            value = float(part.replace(',', '').replace('-', ''))
            st.write(f"Extracted value: {value}")
            return value
        except ValueError:
            continue
    return 0.0



