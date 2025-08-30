import json
import pandas as pd

# Arquivos
ARQUIVO_ENTRADA = "dados_brutos.json"
ARQUIVO_SAIDA = "dados_tratados.csv"

def transformar_dados():
    with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Converte para DataFrame
    df = pd.DataFrame(dados)

    # Seleciona e renomeia colunas relevantes
    df_tratado = df[[
        "symbol",
        "longName",
        "regularMarketPrice",
        "regularMarketChange",
        "regularMarketChangePercent",
        "regularMarketDayHigh",
        "regularMarketDayLow",
        "regularMarketVolume",
        "marketCap",
        "priceEarnings"
    ]].rename(columns={
        "symbol": "Ticker",
        "longName": "Empresa",
        "regularMarketPrice": "Preço Atual",
        "regularMarketChange": "Variação Absoluta",
        "regularMarketChangePercent": "Variação %",
        "regularMarketDayHigh": "Máxima do Dia",
        "regularMarketDayLow": "Mínima do Dia",
        "regularMarketVolume": "Volume",
        "marketCap": "Valor de Mercado",
        "priceEarnings": "P/L"
    })

    # Divide colunas de percentual por 100
    colunas_percentuais = ["Variação %"]
    for col in colunas_percentuais:
        df_tratado[col] = df_tratado[col] / 100

    # Salva como CSV pronto para Power BI com ; como delimitador e vírgula decimal
    df_tratado.to_csv(ARQUIVO_SAIDA, index=False, sep=';', encoding="utf-8-sig", decimal=",")

    print(f"✅ Dados transformados e salvos em {ARQUIVO_SAIDA}")

if __name__ == "__main__":
    transformar_dados()
