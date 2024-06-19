import streamlit as st
from verificari import find_page_with_phrase

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
        # Extrage datele din PDF
        data_from_pdf = extract_data_from_pdf(pdf_file)
        st.write("Date extrase din Bilanțul Contabil:")
        st.write(data_from_pdf)

with col2:
    # Incarcă fișierul Excel al machetei financiare
    excel_file = st.file_uploader("Încarcă Macheta Financiară (Excel)", type=["xlsx"])
    # Afișează mesaj de confirmare a încărcării fișierului Excel
    if excel_file is not None:
        st.toast("Macheta Financiară a fost încărcată cu succes.", icon='🎉')

        if pdf_file is not None:
            # Actualizează workbook-ul Excel cu datele extrase din PDF
            update_excel_with_data(excel_file, data_from_pdf)
            st.toast("Datele au fost adăugate în macheta financiară.", icon='✅')
            st.write("Descărcați macheta financiară completată:")
            st.download_button(
                label="Descărcați Macheta Financiară",
                data=open("/mnt/data/Macheta_Actualizata.xlsx", "rb"),
                file_name="Macheta_Actualizata.xlsx"
            )


