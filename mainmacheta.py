import streamlit as st

# Titlul aplicației
st.title("Automatizare Machetă Financiară")

# Creăm două coloane
col1, col2 = st.columns(2)

with col1:
    # Incarcă PDF-ul bilanțului contabil
    pdf_file = st.file_uploader("Încarcă Bilanțul Contabil (PDF)", type=["pdf"])
    # Afișează mesaj de confirmare a încărcării fișierului PDF
    if pdf_file is not None:
        st.toast("Bilanțul Contabil a fost încărcat cu succes.", icon='🎉')

with col2:
    # Incarcă fișierul Excel al machetei financiare
    excel_file = st.file_uploader("Încarcă Macheta Financiară (Excel)", type=["xlsx"])
    # Afișează mesaj de confirmare a încărcării fișierului Excel
    if excel_file is not None:
        st.toast("Macheta Financiară a fost încărcată cu succes.", icon='🎉')

