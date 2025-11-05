import re
import json

from .logger import logger
from config import PATTERNS_FOLDER

def discover_concessionaria(text: str) -> str|bool:
    concessionarias = {
        "celesc": r"\bCelesc\b"
    }
    try:
        for name, pattern in concessionarias.items():
            if re.search(pattern, text, re.IGNORECASE):
                return name
        return "desconhecida"
    except Exception:
        return None

def get_data(text: str, concessionaria: str) -> dict:
    data = {}
    try:
        with open(f"{PATTERNS_FOLDER}/{concessionaria}.json", "r", encoding="utf-8") as file:
            patterns = json.load(file)["patterns"]
        data["uc"] = extract_uc(text, patterns)
        data["referencia"] = extract_referencia(text, patterns)
        data["vencimento"] = extract_vencimento(text, patterns)
        data["valor_total"] = extract_valor_total(text, patterns)
        return data
    except Exception:
        logger.error(f"Erro ao carregar padrões para a concessionária: {concessionaria}")
        return data

def extract_single_value(text: str, pattern: str) -> str|None:
    match = re.search(pattern, text, re.IGNORECASE)
    logger.debug(f"Extração com o padrão: {pattern} | Resultado: {match.group(1).strip() if match else 'Nenhum resultado encontrado'}")  
    if match:
        return match.group(1).strip()
    return None

def extract_uc(text: str, patterns: dict) -> str|None:
    pattern_key = "uc"
    logger.debug(f"Extraindo UC usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_referencia(text: str, patterns: dict) -> str|None:
    pattern_key = "referencia"
    logger.debug(f"Extraindo mês de referência usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_vencimento(text: str, patterns: dict) -> str|None:
    pattern_key = "vencimento"
    logger.debug(f"Extraindo data de vencimento usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_valor_total(text: str, patterns: dict) -> str|None:
    pattern_key = "valor_total"
    logger.debug(f"Extraindo valor total usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))