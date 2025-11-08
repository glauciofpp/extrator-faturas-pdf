import re
from .logger import logger


def extract_single_value(text: str, pattern: str) -> str|None:
    match = re.search(pattern, text, re.IGNORECASE)
    logger.debug(f"Extração com o padrão: {pattern} | Resultado: {match.group(1).strip() if match else 'Nenhum resultado encontrado'}")  
    if match:
        return match.group(1).strip()
    return None

def extract_multiple_value(text: str, pattern: str) -> str|None:
    match = re.search(pattern, text, re.IGNORECASE)
    multi_value = ""
    logger.debug(f"Extração com o padrão: {pattern} | Resultado: {match.group if match else 'Nenhum resultado encontrado'}")  
    if match:
        for group in match.groups():
            multi_value += group
        return multi_value
    return None

def treat_endereco(endereco: str) -> str|None:
    if endereco:
        clean_endereco = endereco.split(" ")
        clean_endereco = ' '.join([space.strip() for space in clean_endereco if space.strip()])
        return clean_endereco
    return None