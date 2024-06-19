import openpyxl
import fitz  # PyMuPDF

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
                # Parsează textul pentru a extrage datele necesare
                lines = text.split('\n')
                for line in lines:
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
    # Exemplu simplificat pentru extragerea valorii
    parts = line.split()
    for part in parts:
        try:
            return float(part.replace(',', ''))
        except ValueError:
            continue
    return 0.0

def update_excel_with_data(excel_file, data):
    """
    Actualizează fișierul Excel cu datele extrase
    
    Args:
    excel_file (UploadedFile): Fișierul Excel încărcat
    data (dict): Datele extrase din PDF
    """
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook["1A-Bilant"]
    
    # Adaugă datele extrase în celulele corespunzătoare
    sheet["D8"] = data.get('Cheltuieli de constituire', 0.00)
    sheet["D9"] = data.get('Cheltuieli de dezvoltare', 0.00)
    sheet["D10"] = data.get('Concesiuni, brevete, licențe', 0.00)
    sheet["D11"] = data.get('Fond comercial', 0.00)
    sheet["D12"] = data.get('Active necorporale de explorare', 0.00)
    sheet["D13"] = data.get('Avansuri', 0.00)
    
    # Salvează workbook-ul actualizat
    workbook.save("/mnt/data/Macheta_Actualizata.xlsx")


