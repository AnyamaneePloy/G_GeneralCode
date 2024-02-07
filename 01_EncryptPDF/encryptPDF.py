# Version2- AP
'''
Encrypt for PDF file
Deverlop By: Anyamanee P.
Version: 2.0 : 
How to running code on CMD => python encryptPDF.py "xPassword" "xPathfile"
'''
from pypdf import PdfReader, PdfWriter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('xPassword', help='Password for the PDF encryption')
parser.add_argument('xPathfile', help='Path to the PDF file to be encrypted')
args = parser.parse_args()

reader = PdfReader(args.xPathfile)
input_pwd = args.xPassword

writer = PdfWriter()
writer.append_pages_from_reader(reader)
writer.encrypt(input_pwd)

with open("output1.pdf", "wb") as out_file:
    writer.write(out_file)