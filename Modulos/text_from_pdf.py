import pdfplumber

from .logger import logger

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