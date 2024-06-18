import streamlit as st

# Titlul aplicației
st.title("Automatizare Machetă Financiară")

# Incarcă PDF-ul bilanțului contabil
pdf_file = st.file_uploader("Încarcă Bilanțul Contabil (PDF)", type=["pdf"])

# Incarcă fișierul Excel al machetei financiare
excel_file = st.file_uploader("Încarcă Macheta Financiară (Excel)", type=["xlsx"])

# Afișează mesaj de confirmare a încărcării fișierelor
if pdf_file is not None:
    st.toast("Bilanțul Contabil a fost încărcat cu succes.")
if excel_file is not None:
    st.toast("Macheta Financiară a fost încărcată cu succes.")
