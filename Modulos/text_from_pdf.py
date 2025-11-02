import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text(layout=True)
        print(f"Aquivo processado com sucesso: {pdf_path}")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        text = ""
    return text