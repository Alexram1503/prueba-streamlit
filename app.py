
import streamlit as st
import numpy as np
import pandas as pd

st.title("Prueba de despliegue - Alex")
n = st.slider("Número de simulaciones", 100, 5000, 1000)
datos = pd.DataFrame(np.random.randn(n, 2).cumsum(axis=0), columns=["A", "B"])
st.line_chart(datos)
st.success("Si ves esto, GitHub + Streamlit funcionan ✅")
