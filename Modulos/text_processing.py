import json
import re

from .logger import logger
from .utils import extract_single_value, extract_multiple_value, treat_endereco
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
        data["cod_cli"] = extract_cod_cli(text, patterns)
        data["endereco"] = extract_endereco(text, patterns)
        data["dias_fat"] = extract_dia_fat(text, patterns)
        data["consumo"] = extract_consumo(text, patterns)
        data["medidor"] = extract_medidor(text, patterns)
        data["cosip"] = extract_cosip(text, patterns)
        data["pis"] = extract_pis(text, patterns)
        data["cofins"] = extract_cofins(text, patterns)
        data["icms"] = extract_icms(text, patterns)

        return data
    except Exception as e:
        logger.error(f"Erro ao carregar padrões para a concessionária: {concessionaria}")
        return data

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

def extract_cod_cli(text: str, patterns: dict) -> str|None:
    pattern_key = "cod_cli"
    logger.debug(f"Extraindo Codigo do cliente usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_endereco(text: str, patterns: dict) -> str|None:
    pattern_key = "endereco"
    logger.debug(f"Extraindo endereço usando o padrão: {patterns.get(pattern_key, '')}")
    endereco = extract_multiple_value(text, patterns.get(pattern_key, ""))
    return treat_endereco(endereco)

def extract_dia_fat(text: str, patterns: dict) -> str|None:
    pattern_key = "dias_fat"
    logger.debug(f"Extraindo dias faturados usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_consumo(text: str, patterns: dict) -> str|None:
    pattern_key = "consumo"
    logger.debug(f"Extraindo consumo usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_medidor(text: str, patterns: dict) -> str|None:
    pattern_key = "medidor"
    logger.debug(f"Extraindo medidor usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_cosip(text: str, patterns: dict) -> str|None:
    pattern_key = "cosip"
    logger.debug(f"Extraindo valor de cosip usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_pis(text: str, patterns: dict) -> str|None:
    pattern_key = "pis"
    logger.debug(f"Extraindo valor do pis usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_cofins(text: str, patterns: dict) -> str|None:
    pattern_key = "cofins"
    logger.debug(f"Extraindo valor do cofins usando o padrão: {patterns.get(pattern_key, '')}")
    return extract_single_value(text, patterns.get(pattern_key, ""))

def extract_icms(text: str, patterns: dict) -> str|None:
    pattern_key = "icms"
    logger.debug(f"Extraindo valor do icms usando o padrão: {patterns.get(pattern_key, '')}")
    endereco = extract_multiple_value(text, patterns.get(pattern_key, ""))
    return treat_endereco(endereco)