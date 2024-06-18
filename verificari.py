import openpyxl
from openpyxl import load_workbook

def check_excel_template(excel_file):
    """
    Verifică dacă fișierul Excel conține foaia '1A-Bilant'
    
    Args:
    excel_file (UploadedFile): Fișierul Excel încărcat
    
    Returns:
    bool: True dacă foaia '1A-Bilant' este prezentă, altfel False
    """
    try:
        workbook = load_workbook(excel_file, data_only=True)
        sheet_names = workbook.sheetnames
        if "1A-Bilant" in sheet_names:
            return True
        else:
            return False
    except Exception as e:
        return False
