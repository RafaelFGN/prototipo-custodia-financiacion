
# Prototipo Streamlit para selección de financiación en custodia del territorio
import streamlit as st
import pandas as pd

# Simulación de tabla de puntuación (a completar con más datos)
data = {
    "Instrumento": [
        "Tasas de uso",
        "Distritos de mejora empresarial",
        "Contribuciones por plusvalía",
        "Derechos y concesiones de desarrollo",
        "Venta de productos del mercado"
    ],
    "ONG": [5, 2, 1, 3, 4],
    "Administración": [3, 4, 5, 5, 2],
    "Empresa": [2, 5, 4, 4, 5],
    "Pequeña": [5, 2, 1, 2, 5],
    "Media": [4, 4, 2, 3, 5],
    "Grande": [3, 5, 4, 5, 4],
    "Baja": [5, 2, 1, 2, 5],
    "MediaComp": [4, 3, 3, 4, 4],
    "Alta": [3, 5, 5, 5, 3],
    "Ecológico": [5, 3, 3, 4, 4],
    "Económico": [2, 5, 5, 5, 5],
    "Social": [4, 4, 3, 3, 5]
}
df = pd.DataFrame(data)

# Interfaz de usuario
st.title("Selector de financiación para custodia del territorio")
st.write("Completa los siguientes campos para obtener recomendaciones ajustadas:")

entidad = st.selectbox("Tipo de entidad promotora", ["ONG", "Administración", "Empresa"])
escala = st.selectbox("Escala del proyecto", ["Pequeña", "Media", "Grande"])
complejidad = st.selectbox("Complejidad financiera disponible", ["Baja", "MediaComp", "Alta"])
retorno = st.selectbox("Tipo de retorno esperado", ["Ecológico", "Económico", "Social"])

# Cálculo de puntuación
peso = 1  # Peso uniforme por ahora
df["Puntuación total"] = (
    df[entidad] * peso +
    df[escala] * peso +
    df[complejidad] * peso +
    df[retorno] * peso
)

# Ordenar resultados
resultado = df[["Instrumento", "Puntuación total"]].sort_values(by="Puntuación total", ascending=False)

# Mostrar resultados
st.subheader("Instrumentos recomendados")
st.dataframe(resultado.reset_index(drop=True))
