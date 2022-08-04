import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import docx2txt
# import textract 
from PIL import Image 
#from PyPDF2 import PdfFileReader
#import pdfplumber

st.title (" Keamanan Jaringan")
docx_file = st.file_uploader("Network Security")

st.text("1. Pengertian network security")
st.text("2. Penggunaan network Security ")
st.text("3. Jenis-jenis network security")
st.text("4. Cara kerja network Security")

if docx_file is not None :
    raw_text = docx2txt.process(docx_file)
    st.write(raw_text)





##insert gambar
link1 = "https://nagitec.com/jenis-dan-kegunaan-network-security/"
link2 = "https://www.goldenfast.net/blog/network-security/"
st.write("Source : ")
st.write( " (%s)" %link1)
st.write(" (%s)" %link2)






