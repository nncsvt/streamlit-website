import streamlit as st
import streamlit.components.v1 as stc
from PyPDF2 import PdfFileReader
import pdfplumber
import docx2txt
# import textract 
from PIL import Image 
#from PyPDF2 import PdfFileReader
#import pdfplumber

##read pdf file 
st.title (" Ancaman Keamanaan Siber")


def read_pdf(file) :
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_text = ''
    for i in range(count):
        page = pdfReader.getPage(i)
        all_text += page.extractText()
    return all_text



docx_file = st.file_uploader("Ancaman")
if docx_file is not None :
    raw_text = read_pdf(docx_file)
    st.write(raw_text)
