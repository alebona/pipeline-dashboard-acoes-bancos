import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()


# Lista de ações dos principais bancos
acoes = ["ITUB4", "BBDC4", "BBAS3", "SANB11", "BPAC11"]

# Sua chave da API
TOKEN = os.getenv("BRAPI_TOKEN")

# Arquivo onde os dados crus serão salvos
ARQUIVO_SAIDA = "dados_brutos.json"

def extrair_dados():
    resultados = []
    for acao in acoes:
        url = f"https://brapi.dev/api/quote/{acao}?token={TOKEN}"
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            resultados.append(dados["results"][0])  # pega só a parte útil
            print(f"✅ Extraído {acao}")
        else:
            print(f"❌ Erro ao extrair {acao}: {response.status_code}")

        time.sleep(2)  # evita erro 429 (Too Many Requests)

    # Salva os dados crus em JSON
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    extrair_dados()
