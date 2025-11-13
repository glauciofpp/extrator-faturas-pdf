import json
import re

from .logger import logger
from .utils import treat_endereco, extract_value
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
        data["uc"] = extract_value(fatura_text = text, pattern_key="uc", patterns_dict=patterns)
        data["referencia"] = extract_value(fatura_text = text, pattern_key="referencia", patterns_dict=patterns)
        data["vencimento"] = extract_value(fatura_text = text, pattern_key="vencimento", patterns_dict=patterns)
        data["valor_total"] =extract_value(fatura_text = text, pattern_key="valor_total", patterns_dict=patterns)
        data["cod_cli"] = extract_value(fatura_text = text, pattern_key="cod_cli", patterns_dict=patterns)
        data["endereco"] = treat_endereco(endereco=extract_value(fatura_text = text, pattern_key="endereco", patterns_dict=patterns))
        data["dias_fat"] = extract_value(fatura_text = text, pattern_key="dias_fat", patterns_dict=patterns)
        data["consumo"] = extract_value(fatura_text = text, pattern_key="consumo", patterns_dict=patterns)
        data["medidor"] = extract_value(fatura_text = text, pattern_key="medidor", patterns_dict=patterns)
        data["cosip"] = extract_value(fatura_text = text, pattern_key="cosip", patterns_dict=patterns)
        data["pis"] = extract_value(fatura_text = text, pattern_key="pis", patterns_dict=patterns)
        data["cofins"] = extract_value(fatura_text = text, pattern_key="cofins", patterns_dict=patterns)
        data["icms"] = extract_value(fatura_text = text, pattern_key="icms", patterns_dict=patterns)

        return data
    except Exception as e:
        logger.error(f"Erro ao carregar padrões para a concessionária: {concessionaria}")
        return data