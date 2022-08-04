import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import docx2txt
# import textract 
from PyPDF2 import PdfFileReader
import pdfplumber
import docx2txt
from PIL import Image 

st.title (" Keamanan Siber")

st.text("1. Manfaat security Pada Bidang Bisnis")
st.text("2. Jenis Ancaman Cybersecurity")
st.text("3. Konsep Cyber security")
st.text("4. Standard Cyber Security")
st.text("5. 5 Cara Mengatasi Cyber Crime")


def read_pdf(file) :
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_text = ''
    for i in range(count):
        page = pdfReader.getPage(i)
        all_text += page.extractText()
    return all_text


st.title (" Keamanaan Siber")
docx_file = st.file_uploader("Cyber Security")
if docx_file is not None :
    raw_text = read_pdf(docx_file)
    st.write(raw_text)


link1 = "https://glints.com/id/lowongan/cybersecurity-adalah/#.YudOmXZBzIU"
link2 = "https://runsystem.id/id/blog/cyber-security/"
link3 = "https://www.niagahoster.co.id/blog/cyber-security-adalah/#4_Serangan_Man-in-the-Middle"
link4 = "https://www.dewaweb.com/blog/apa-itu-cyber-security/"
link5 = "https://runsystem.id/id/blog/cyber-security/"
link6 = "https://infokomputer.grid.id/read/122710604/apa-itu-cyber-security-mengapa-cyber-security-kini-makin-penting?page=all"


st.write("Source : ")
st.write( " (%s)" %link1)
st.write(" (%s)" %link2)
st.write(" (%s)" %link3)
st.write(" (%s)" %link4)
st.write(" (%s)" %link5)
st.write(" (%s)" %link6)