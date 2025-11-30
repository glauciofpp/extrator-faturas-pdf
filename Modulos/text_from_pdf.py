import pdfplumber
from .logger import logger
from .text_processing import discover_concessionaria, get_data

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text(layout=True)
        if not text or text.isspace():
            logger.warning(f"Nenhum texto extraído do arquivo PDF: {pdf_path}")
        else:
            logger.info(f"Texto extraído com sucesso do arquivo PDF: {pdf_path}")
    except Exception as e:
        logger.error(f"Erro ao extrair texto do arquivo PDF {pdf_path}: {e}")
        text = ""
    return text

def format_endereco(text: str) -> str:
    lines = text.splitlines()
    formatted_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(formatted_lines)

def data_extraction_pipeline(fatura: str) -> dict:
    try:
        text = extract_text_from_pdf(fatura)
        concessionaria = discover_concessionaria(text)
        logger.debug(f"Concessionária identificada para {fatura}: {concessionaria}")
        data = get_data(text, concessionaria)
        logger.info(f"Dados extraídos com sucesso da fatura {fatura}")
        return data
    except Exception as e:
        logger.error(f"Erro ao processar a fatura {fatura}: {e}")
    return {}