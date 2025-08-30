import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------
# Configurações
# ------------------------------------
st.set_page_config(page_title="Dashboard Bancos", layout="wide")
st.title("📊 Dashboard Ações Bancos - B3")
st.markdown("Dados atualizados de ações dos principais bancos brasileiros")

# CSV
CSV_FILE = "dados_tratados.csv"
df = pd.read_csv(CSV_FILE, sep=";", decimal=",")

# ------------------------------------
# Filtro de Ticker
# ------------------------------------
tickers = st.multiselect(
    "Selecione os Tickers",
    df["Ticker"].unique(),
    default=df["Ticker"].unique()
)
df_filtered = df[df["Ticker"].isin(tickers)]

# ------------------------------------
# Tabela de Dados
# ------------------------------------
st.subheader("📋 Dados das Ações")
st.dataframe(df_filtered)

# ------------------------------------
# Layout com Gráficos
# ------------------------------------
col1, col2, col3 = st.columns(3)

# Gráfico 1 - P/L
df_pl = df_filtered[df_filtered["P/L"].notnull()].sort_values("P/L")
with col1:
    fig_pl = px.bar(
        df_pl, 
        x="P/L",         
        y="Empresa",     
        orientation="h", 
        title="📈 P/L por Empresa",
        text="P/L"
    )
    st.plotly_chart(fig_pl, use_container_width=True)

# Gráfico 2 - Volume
df_vol = df_filtered[df_filtered["Volume"].notnull()].sort_values("Volume")
with col2:
    fig_vol = px.bar(
        df_vol, 
        x="Volume", 
        y="Empresa", 
        orientation="h",
        title="📊 Volume Negociado",
        text="Volume"
    )
    st.plotly_chart(fig_vol, use_container_width=True)

# Gráfico 3 - Valor de Mercado
df_valor = df_filtered[df_filtered["Valor de Mercado"].notnull()].sort_values("Valor de Mercado")
with col3:
    fig_valor = px.bar(
        df_valor, 
        x="Valor de Mercado", 
        y="Empresa", 
        orientation="h",
        title="💰 Valor de Mercado",
        text="Valor de Mercado"
    )
    st.plotly_chart(fig_valor, use_container_width=True)

# ------------------------------------
# TreeMap - Variação %
# ------------------------------------
df_filtered["Variação % Texto"] = (df_filtered["Variação %"]*100).round(2).astype(str) + "%"

st.subheader("🌳 Variação % por Empresa")
fig_var = px.treemap(
    df_filtered,
    path=["Empresa"],
    values="Variação %",
    color="Variação %",
    color_continuous_scale="RdYlGn",
    title="🌳 Variação % por Empresa"
)

# Adicionar valores dentro das caixas
fig_var.data[0].text = df_filtered["Variação % Texto"]
fig_var.data[0].textinfo = "label+text"
fig_var.update_traces(textfont_size=14)
st.plotly_chart(fig_var, use_container_width=True)

# ------------------------------------
# Gráfico de Área - Mínima e Máxima
# ------------------------------------
st.subheader("📉 Máxima e Mínima do Dia")
df_area = df_filtered.melt(
    id_vars=["Empresa"], 
    value_vars=["Mínima do Dia", "Máxima do Dia"],  # inverter a ordem aqui
    var_name="Tipo", 
    value_name="Preço"
)

fig_area = px.area(
    df_area, 
    x="Empresa", 
    y="Preço", 
    color="Tipo", 
    title="Máxima e Mínima por Empresa",
    line_group="Tipo"
)

st.plotly_chart(fig_area, use_container_width=True)
