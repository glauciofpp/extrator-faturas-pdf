import re
from .logger import logger

def extract_value(fatura_text: str, pattern_key: str, patterns_dict: dict) -> str|None:
    match = re.search(patterns_dict[pattern_key], fatura_text, re.IGNORECASE)
    multi_value = ""
    logger.debug(f"Extração de {pattern_key} com o padrão: {patterns_dict[pattern_key]} | Resultado: {match.groups() if match else 'Nenhum resultado encontrado'}")  
    if match:
        for group in match.groups():
            multi_value += group
        return multi_value.strip()
    return None

def treat_endereco(endereco: str) -> str|None:
    if endereco:
        clean_endereco = endereco.split(" ")
        clean_endereco = ' '.join([space.strip() for space in clean_endereco if space.strip()])
        return clean_endereco
    return None