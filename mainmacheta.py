import streamlit as st
from verificari import check_excel_template

# Titlul aplicației
st.title("Automatizare Machetă Financiară")

# Incarcă PDF-ul bilanțului contabil
pdf_file = st.file_uploader("Încarcă Bilanțul Contabil (PDF)", type=["pdf"])

# Incarcă fișierul Excel al machetei financiare
excel_file = st.file_uploader("Încarcă Macheta Financiară (Excel)", type=["xlsx"])

# Afișează mesaj de confirmare a încărcării fișierelor
if pdf_file is not None:
    st.success("Bilanțul Contabil a fost încărcat cu succes.")

if excel_file is not None:
    st.write("Verificarea machetei financiare...")
    is_valid, message = check_excel_template(excel_file)
    if is_valid:
        st.success(f"Macheta Financiară a fost încărcată cu succes și conține foaia '1A-Bilant'. {message}")
    else:
        st.error(message)
