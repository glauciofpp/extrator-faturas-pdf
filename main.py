import os
from Modulos import extract_text_from_pdf
from Modulos import logger

from config import FATURAS_FOLDER

logger.info("Iniciando o processamento de faturas.")

def get_faturas_from_folder(folder_path: str):
    try:
        faturas = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
        logger.info(f"Encontradas {len(faturas)} faturas na pasta: {folder_path}")
        return faturas
    except Exception as e:
        logger.error(f"Erro ao listar faturas na pasta {folder_path}: {e}")
        return []
    
def start_processing():
    faturas = get_faturas_from_folder(FATURAS_FOLDER)
    for fatura in faturas:
        logger.debug(f"Processando o arquivo: {fatura}")
        print(extract_text_from_pdf(fatura))
    

start_processing()
