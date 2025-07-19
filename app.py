import streamlit as st
import pandas as pd

# Carregar a base
df = pd.read_excel("TABELA DE LENTES DE CONTATO - BUSCA.XLSX", sheet_name="BASE DE DADOS")

st.title("🔍 Consulta de Lentes de Contato")

# Seletor de descarte
descarte = st.selectbox("Tipo de descarte", options=sorted(df["Descarte"].dropna().unique()))

# Entradas de grau
esferico = st.text_input("Esférico (ex: -02.00 ou +01.25)")
cilindrico = st.text_input("Cilíndrico (ex: -00.75 ou 00)", value="0")
eixo = st.text_input("Eixo (ex: 180)", value="0")

# Botão para buscar
if st.button("Buscar"):
    # Padronizar valores
    esferico = esferico.replace(",", ".").strip()
    cilindrico = cilindrico.replace(",", ".").strip()
    eixo = eixo.strip()

    # Filtrar dados
    resultado = df[
        (df["Descarte"] == descarte) &
        (df["Esférico"] == esferico) &
        (df["Cilindrico"].astype(str) == cilindrico) &
        (df["Eixo"].astype(str) == eixo)
    ]

    if not resultado.empty:
        st.success(f"{len(resultado)} resultado(s) encontrado(s):")
        st.dataframe(resultado[["Código", "Descrição", "TabelaOficial"]])
    else:
        st.warning("Nenhum resultado encontrado com os critérios informados.")
