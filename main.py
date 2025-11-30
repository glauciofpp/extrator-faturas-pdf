import os
from Modulos import data_extraction_pipeline
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
        data = data_extraction_pipeline(fatura)
        print(f"Dados extraídos da fatura {fatura}: {data}")



#start_processing()

print(data_extraction_pipeline("Faturas/fatura_1762306934208.pdf"))