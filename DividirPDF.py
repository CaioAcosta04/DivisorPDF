import os
from PyPDF2 import PdfReader, PdfWriter
import shutil
from pathlib import Path
from time import sleep

#Digite o caminho completo do PDF
pdf_file_path = 'C:/PDF/Holerite.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')
output_folder_path = os.path.join(os.getcwd(), 'Output')

pdf = PdfReader(pdf_file_path)

#Criando variável para armazenar os nomes dos funcionarios
nomes = []
#Variavel para quantos nomes serão adicionados
quantNomes = int(input('Quantos nomes serão adicionados?: '))
#Criando variavel para append na lista
nome = ''
#Armazenando meses do ano:
mes = ''
print('1- Janeiro', end='   ')
print('2- Fevereiro')
print('3- Março', end='     ')
print('4- Abril')
print('5- Maio', end='      ')
print('6- Junho')
print('7- Julho', end='     ')
print('8- Agosto')
print('9- Setembro', end='  ')
print('10- Outubro')
print('11- Novembro', end='  ')
print('12- Dezembro')
nummes = int(input('Digite o numero correspondente ao mês corrente: '))

if nummes == 1:
    mes = 'Janeiro'
elif nummes == 2:
    mes = 'Fevereiro'
elif nummes == 3:
    mes = 'Marco'
elif nummes == 4:
    mes = 'Abril'
elif nummes == 5:
    mes = 'Maio'
elif nummes == 6:
    mes = 'Junho'
elif nummes == 7:
    mes = 'Julho'
elif nummes == 8:
    mes = 'Agosto'
elif nummes == 9:
    mes = 'Setembro'
elif nummes == 10:
    mes = 'Outubro'
elif nummes == 11:
    mes = 'Novembro'
elif nummes == 12:
    mes = 'Dezembro'

for i in range(0,quantNomes):
    nome = input('Digite o nome: ')
    nomes.append(nome)

for page_num in range(len(pdf.pages)):
    pdfWriter = PdfWriter()
    pdfWriter.add_page(pdf.pages[page_num])

    with open(os.path.join(output_folder_path, '{0}_{1}_{2}.pdf'.format(file_base_name, mes, nomes[page_num])), 'wb') as f:
        pdfWriter.write(f)
        f.close()

print('PDF Cortado com sucesso!')
print()

