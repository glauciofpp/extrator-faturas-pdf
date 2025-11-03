from Modulos import extract_text_from_pdf
from Modulos import logger

from config import FATURAS_FOLDER

logger.info("Iniciando o processamento de faturas.")

file = fr"{FATURAS_FOLDER}\fatura_1762020700430.pdf"
logger.debug(f"Processando o arquivo: {file}")

extract_text_from_pdf(file)
