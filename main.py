import json
import re
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime as dt

arquivo = Path("./jsons/jsonteste.json") # <-- Substitua pelo nome do seu arquivo JSON // Replace with the name of your JSON file.

if not arquivo.exists():
    print("Aviso: Arquivo não encontrado.")
else:
    try:
        with open(arquivo, 'r', encoding='utf8') as f:
            dados = json.load(f)

        for campo in dados:
            for chave, valor in campo.items():
                if isinstance(valor, str):
                    soup = BeautifulSoup(valor, 'html.parser')
                    campo[chave] = soup.get_text().strip().replace('\xa0', '')
                    campo[chave] = re.sub(r'\s+', ' ', campo[chave])
                
            # Desativa o comentario abaixo se quiser formatar a data padrão brasileiro para o padrão americano (YYYY-MM-DD HH:MM:SS)
            # Uncomment the line below if you want to change the format from Brazilian to American (YYYY-MM-DD HH:MM:SS)
            if campo['data']:
                campo['data'] = dt.strptime(campo['data'].strip(), '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') # <-- Substitua o formato da data conforme necessário // Replace the date format as needed.
            else:
                campo['data'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(f'./jsons/{arquivo.stem}Tratado.json', 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        
        print(f"Arquivo '{arquivo.stem}Tratado.json' criado com sucesso.")

    except json.JSONDecodeError:
        print("Erro: O arquivo não contém um JSON válido.")