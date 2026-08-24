import streamlit as st

st.title("🚨 Detector de Falhas")

temperatura = st.number_input(
    "Digite a temperatura do sensor:",
    min_value=0.0,
    max_value=150.0,
    value=25.0
)

if temperatura > 80:
    st.error("🔴 FALHA DETECTADA!")
else:
    st.success("🟢 Sensor funcionando normalmente")
