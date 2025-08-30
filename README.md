# 📊 Dashboard de Ações dos Principais Bancos - B3

Este projeto tem como objetivo criar dashboards de análise de ações dos principais bancos brasileiros, utilizando **Power BI** e **Streamlit**. Os dados são extraídos automaticamente da API [BRAPI](https://brapi.dev), tratados, armazenados e exibidos de forma visualmente intuitiva para facilitar o acompanhamento do mercado.

---

## 🗂 Estrutura do Projeto

```

pipeline-dashboard-acoes-bancos/
│
├─ img/                      # Capturas, gifs ou imagens para README ou apresentação
│
├─ pipeline/                 # Código-fonte e dados do pipeline
│   ├─ venv/                 # Virtualenv (não versionar)
│   ├─ .gitignore            # Ignorar venv, .env e arquivos temporários
│   ├─ app.py                # Script principal para execução do pipeline completo
│   ├─ dashboard.py          # Dashboard em Streamlit
│   ├─ extracao.py           # Extração de dados da API BRAPI
│   ├─ transformacao.py      # Tratamento e limpeza de dados
│   ├─ dados_brutos.json     # Dados coletados da API antes da transformação
│   ├─ dados_tratados.csv    # Dados tratados prontos para análise
│   ├─ logger.py             # Configuração do log de execução
│   ├─ pipeline.log          # Arquivo de log com histórico de execução e erros
│   └─ email_sender.py       # Função para envio de e-mail em caso de erro
│
├─ dashboard_acoes.pbix       # Arquivo Power BI
├─ README.md                  # Documentação do projeto

```

---

## ⚙ Funcionalidades do Pipeline

1. **Extração**  
   - Coleta dados da API BRAPI de ações de bancos brasileiros.
   - Armazena os dados brutos em `dados_brutos.json`.

2. **Transformação**  
   - Limpeza e padronização dos dados (valores numéricos, datas, tratamento de nulos).
   - Salva os dados tratados em `dados_tratados.csv`.

3. **Dashboard**  
   - **Power BI**: visualizações interativas com filtros por ticker e métricas de ações.
   - **Streamlit**: versão web pública do dashboard para visualização em tempo real.

4. **Logs e Monitoramento**  
   - Todos os scripts registram execução, erros e alertas no `pipeline.log` através de `logger.py`.
   - Em caso de erro crítico, um e-mail é enviado automaticamente via `email_sender.py`.

---

## 📊 Métricas e Visualizações

- **Cartões:** Preço atual, variação absoluta e % de variação.  
- **Gráficos de barras:** P/L, Volume e Valor de Mercado por empresa.  
- **TreeMap:** Variação % por empresa.  
- **Gráfico de área empilhado:** Máxima e mínima do dia por empresa.  
- **Filtros:** Ticker selecionável pelo usuário.

---

## 🖼 Seção de Prints

### Power BI
<img width="1363" height="751" alt="frame1" src="https://github.com/user-attachments/assets/1ada9b46-c269-487b-bb44-accbc5e77066" />

### Streamlit
<img width="1823" height="692" alt="print1" src="https://github.com/user-attachments/assets/8eb586f5-2574-4699-a6d1-a08c44982bf5" />
<img width="1823" height="600" alt="print2" src="https://github.com/user-attachments/assets/d8ca4dfd-465d-455f-a199-3912f3e528d9" />
<img width="1797" height="642" alt="print3" src="https://github.com/user-attachments/assets/0a9bc089-8027-4515-88b9-93c535a71972" />
<img width="1826" height="663" alt="print4" src="https://github.com/user-attachments/assets/9f748cca-df32-48f8-9f8c-d5a84c4dbbaf" />

---

## 🔹 Tecnologias Utilizadas

- **Python:** extração, tratamento e dashboard (Streamlit + Plotly).  
- **Power BI:** análise interativa offline e apresentação profissional.  
- **BRAPI:** API gratuita para cotações de ações brasileiras.  
- **SQLite / CSV:** armazenamento de dados tratados.  
- **Logger e E-mail:** monitoramento de falhas e alertas automáticos.

---

## 📌 Observações

- O pipeline é modular e escalável, permitindo adicionar novos tickers ou métricas facilmente.  
- Os dashboards foram desenvolvidos para **facilitar a análise e comparação de ações** dos principais bancos.  
- O Streamlit permite que o dashboard seja público, enquanto o Power BI oferece funcionalidades avançadas de visualização offline.


