import os
from PyPDF2 import PdfReader, PdfWriter
import shutil
from pathlib import Path
from time import sleep
import subprocess, sys

#declarando variaveispara abrir diretorio
path_dir = 'C:/PDF'

#Digite o caminho completo do PDF
pdf_file_path = 'C:/PDF/arquivo.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')
output_folder_path = os.path.join(os.getcwd(), 'Output')

pdf = PdfReader(pdf_file_path)

for page_num in range(len(pdf.pages)):
    pdfWriter = PdfWriter()
    pdfWriter.add_page(pdf.pages[page_num])

    with open(os.path.join(output_folder_path, '{0}_{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
        pdfWriter.write(f)
        f.close()
print('Procurando PDF...')
sleep(2)
print('PDF Encontrado! Cortando PDF....')
sleep(4)
print('PDF Cortado com sucesso!')
sleep(2)
print('Abrindo Pasta...')
sleep(2)
os.startfile(path_dir)
print()
