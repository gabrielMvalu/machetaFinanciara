import openpyxl
from openpyxl import load_workbook
import time

def check_excel_template(excel_file):
    """
    Verifică dacă fișierul Excel conține foaia '1A-Bilant'
    
    Args:
    excel_file (UploadedFile): Fișierul Excel încărcat
    
    Returns:
    bool: True dacă foaia '1A-Bilant' este prezentă, altfel False
    """
    start_time = time.time()
    try:
        workbook = load_workbook(excel_file, data_only=True)
        sheet_names = workbook.sheetnames
        if "1A-Bilant" in sheet_names:
            st.write(f"Sheet check completed in {time.time() - start_time} seconds")
            return True
        else:
            st.write(f"Sheet check completed in {time.time() - start_time} seconds")
            return False
    except Exception as e:
        st.error(f"Eroare la încărcarea fișierului Excel: {e}")
        return False

