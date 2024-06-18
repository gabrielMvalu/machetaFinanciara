import openpyxl
from openpyxl import load_workbook
import time

def check_excel_template(excel_file):
    """
    Verifică dacă fișierul Excel conține foaia '1A-Bilant'
    
    Args:
    excel_file (UploadedFile): Fișierul Excel încărcat
    
    Returns:
    tuple: (bool, str) True dacă foaia '1A-Bilant' este prezentă și un mesaj de succes, altfel False și un mesaj de eroare
    """
    start_time = time.time()
    try:
        workbook = load_workbook(excel_file, data_only=True)
        sheet_names = workbook.sheetnames
        duration = time.time() - start_time
        if "1A-Bilant" in sheet_names:
            return True, f"Sheet check completed in {duration} seconds"
        else:
            return False, f"Sheet check completed in {duration} seconds, but '1A-Bilant' not found."
    except Exception as e:
        return False, f"Eroare la încărcarea fișierului Excel: {e}"
