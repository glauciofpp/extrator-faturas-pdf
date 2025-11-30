import argparse
import json
from Modulos import data_extraction_pipeline


def main():
    parser = argparse.ArgumentParser(description="Extrai alguns dados relevantes de faturas eletricas em PDF.")
    parser.add_argument("input_file", type=str, help="Aquivo de fatura eletrica em PDF.")
    parser.add_argument("output_file", type=str, help="Local onde os dados extraidos serao salvos.")
    parser.add_argument("-f", "--format", type=str, choices=["json", "txt"], default="txt", help="Tipo do aquivo de saida, JSON ou TXT. Padrao: TXT.")

    args = parser.parse_args()
    try:
        data = data_extraction_pipeline(args.input_file)
        if args.format == "json":
            save_json(data, args.output_file)
        else:
            save_txt(data, args.output_file)
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        return

def save_json(data: dict, output_file: str):
    with open(f"{output_file}", "w", encoding="utf-8") as file:
        file.write(json.dumps(data))

def save_txt(data: dict, output_file: str):
    with open(f"{output_file}", "w", encoding="utf-8") as file:
        for item, value in data.items():
            file.write(f"{item}: {value}\n")

if __name__ == "__main__":
    main()