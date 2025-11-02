import os

from Modulos import extract_text_from_pdf
from config import FATURAS_FOLDER

file = fr"{FATURAS_FOLDER}\fatura_1762020700430.pdf"
extract_text_from_pdf(file)
