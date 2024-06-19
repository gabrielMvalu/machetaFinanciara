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
                        data['Cheltuieli de constituire'] = extract_value_from_line(line, 'Cheltuieli de constituire')
                    elif "2.Cheltuieli de dezvoltare" in line:
                        data['Cheltuieli de dezvoltare'] = extract_value_from_line(line, 'Cheltuieli de dezvoltare')
                    elif "3.Concesiuni,brevete, licente" in line:
                        data['Concesiuni, brevete, licențe'] = extract_value_from_line(line, 'Concesiuni, brevete, licențe')
                    elif "4.Fond comercial" in line:
                        data['Fond comercial'] = extract_value_from_line(line, 'Fond comercial')
                    elif "5Active necorporale de explorare" in line:
                        data['Active necorporale de explorare'] = extract_value_from_line(line, 'Active necorporale de explorare')
                    elif "6.Avansuri acordate pentru imobilizari necorporale" in line:
                        data['Avansuri'] = extract_value_from_line(line, 'Avansuri')
    return data

def extract_value_from_line(line, category):
    """
    Extrage valoarea numerică dintr-o linie de text
    
    Args:
    line (str): Linia de text
    category (str): Categoria pentru log-uri
    
    Returns:
    float: Valoarea numerică extrasă
    """
    st.write(f"Extracting value for {category} from line: {line}")  # Log linia pentru verificare
    # Adaptează această parte pentru a extrage corect valoarea
    parts = line.split()
    value = 0.0
    for part in parts:
        try:
            if part.replace(',', '').replace('-', '').isdigit():
                value = float(part.replace(',', '').replace('-', ''))
                st.write(f"Extracted value for {category}: {value}")
                break
        except ValueError:
            continue
    return value





