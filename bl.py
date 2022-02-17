import os
import shutil

from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

result_dir = os.path.join(os.getcwd(),"result")
raw_dir = os.path.join(os.getcwd(),"raw")


def read_pdf(file_name):
    pdf_file_path = os.path.join(raw_dir, file_name)
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return str(output_string.getvalue())

def find_name(text):
   a = text.find("2022")
   name = text[a-7:a+4]
   return name
for file in os.listdir(raw_dir):
    text = read_pdf(file)
    new_name = find_name(text)+ "_" + file
    shutil.move(os.path.join(raw_dir, file), os.path.join(result_dir, new_name))
