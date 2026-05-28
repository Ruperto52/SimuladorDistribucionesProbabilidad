import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import io

from logica.distribuciones import SimuladorDistribuciones
from logica.simulaciones import ejecutar_ley_grandes_numeros, ejecutar_teorema_limite_central

# ==========================================
# CONFIGURACION GLOBAL DE COLORES
# ==========================================
COLOR_PRIMARIO = "#F14AC8"
COLOR_SECUNDARIO = "#333333"
COLOR_FONDO = "#FFFFFF"
COLOR_FONDO_SECUNDARIO = "#F8F9FA"

st.set_page_config(page_title="Simulador Estadistico", layout="wide")

# Inyeccion dinamica de CSS utilizando las variables de color definidas arriba
estilos_css = f"""
    <style>
        .main {{ background-color: {COLOR_FONDO}; color: {COLOR_SECUNDARIO}; }}
        h1, h2, h3, h4 {{ color: {COLOR_PRIMARIO} !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
        .stButton>button {{ 
            background-color: {COLOR_PRIMARIO}; color: white; border-radius: 6px; 
            border: none; padding: 0.5rem 1rem; transition: 0.3s;
        }}
        .stButton>button:hover {{ opacity: 0.8; color: white; }}
        .stTabs [data-baseweb="tab"] {{ color: {COLOR_SECUNDARIO}; font-weight: 600; }}
        .stTabs [data-baseweb="tab"][aria-selected="true"] {{ color: {COLOR_PRIMARIO} !important; border-bottom-color: {COLOR_PRIMARIO} !important; }}
        div[data-testid="stSidebar"] {{ background-color: {COLOR_FONDO_SECUNDARIO}; }}
    </style>
"""
st.markdown(estilos_css, unsafe_allow_html=True)

st.title("Simulador Computacional de Distribuciones de Probabilidad")
st.markdown("---")

st.sidebar.header("Configuracion General")
tamano_muestra = st.sidebar.number_input("Tamano de Muestra (N)", min_value=1, max_value=100000, value=1000, step=100)

opciones_distribucion = ["Binomial", "Poisson", "Geometrica", "Normal", "Uniforme", "Exponencial"]
distribucion_seleccionada = st.sidebar.selectbox("Seleccione Distribucion", opciones_distribucion)

parametros = {}

if distribucion_seleccionada == "Binomial":
    parametros['n'] = st.sidebar.number_input("Numero de ensayos (n)", min_value=1, value=10, step=1)
    parametros['p'] = st.sidebar.slider("Probabilidad de exito (p)", 0.0, 1.0, 0.5, 0.01)
elif distribucion_seleccionada == "Poisson":
    parametros['lambda'] = st.sidebar.number_input("Parametro Lambda", min_value=0.01, value=4.0, step=0.5)
elif distribucion_seleccionada == "Geometrica":
    parametros['p'] = st.sidebar.slider("Probabilidad de exito (p)", 0.01, 1.0, 0.3, 0.01)
elif distribucion_seleccionada == "Normal":
    parametros['mu'] = st.sidebar.number_input("Media (mu)", value=0.0, step=0.5)
    parametros['sigma'] = st.sidebar.number_input("Desviacion estandar (sigma)", min_value=0.01, value=1.0, step=0.1)
elif distribucion_seleccionada == "Uniforme":
    parametros['a'] = st.sidebar.number_input("Limite inferior (a)", value=0.0, step=1.0)
    parametros['b'] = st.sidebar.number_input("Limite superior (b)", value=10.0, step=1.0)
elif distribucion_seleccionada == "Exponencial":
    parametros['beta'] = st.sidebar.number_input("Escala (beta)", min_value=0.01, value=2.0, step=0.5)

pestana1, pestana2, pestana3, pestana4 = st.tabs([
    "Simulacion Individual", "Comparacion Simultanea", 
    "Ley de los Grandes Numeros", "Teorema del Limite Central"
])

simulador = SimuladorDistribuciones(tamano_muestra)

with pestana1:
    st.subheader(f"Analisis de Distribucion {distribucion_seleccionada}")
    
    try:
        if distribucion_seleccionada == "Binomial":
            resultado = simulador.simular_binomial(parametros['n'], parametros['p'])
        elif distribucion_seleccionada == "Poisson":
            resultado = simulador.simular_poisson(parametros['lam'])
        elif distribucion_seleccionada == "Geometrica":
            resultado = simulador.simular_geometrica(parametros['p'])
        elif distribucion_seleccionada == "Normal":
            resultado = simulador.simular_normal(parametros['mu'], parametros['sigma'])
        elif distribucion_seleccionada == "Uniforme":
            resultado = simulador.simular_uniforme(parametros['a'], parametros['b'])
        elif distribucion_seleccionada == "Exponencial":
            resultado = simulador.simular_exponencial(parametros['beta'])
            
        datos = resultado["datos"]
        df_estadisticas = resultado["estadisticas"]
        
        columna1, columna2 = st.columns([1, 1])
        
        with columna1:
            st.markdown("#### Comparacion Numerica")
            st.dataframe(df_estadisticas.style.format({"Valor teórico": "{:.4f}", "Valor simulado": "{:.4f}", "Diferencia": "{:.4f}"}))
            
            buffer_csv = io.StringIO()
            pd.DataFrame(datos, columns=["Valores_Simulados"]).to_csv(buffer_csv, index=False)
            st.download_button(
                label="Exportar Datos (.CSV)",
                data=buffer_csv.getvalue(),
                file_name=f"simulacion_{distribucion_seleccionada.lower()}.csv",
                mime="text/csv"
            )
            
        with columna2:
            st.markdown("#### Visualizacion Grafica del Modelo")
            figura, eje = plt.subplots(figsize=(6, 4))
            
            if resultado["tipo"] == "Discreta":
                valores, conteos = np.unique(datos, return_counts=True)
                pmf_empirica = conteos / len(datos)
                eje.bar(valores, pmf_empirica, alpha=0.6, color=COLOR_PRIMARIO, label='Empirica (Simulacion)')
                
                if distribucion_seleccionada == "Binomial":
                    eje_x = np.arange(0, parametros['n'] + 1)
                    y_teorica = stats.binom.pmf(eje_x, parametros['n'], parametros['p'])
                elif distribucion_seleccionada == "Poisson":
                    eje_x = np.arange(0, np.max(valores) + 1)
                    y_teorica = stats.poisson.pmf(eje_x, parametros['lam'])
                elif distribucion_seleccionada == "Geometrica":
                    eje_x = np.arange(1, np.max(valores) + 1)
                    y_teorica = stats.geom.pmf(eje_x, parametros['p'])
                eje.step(eje_x, y_teorica, where='mid', color=COLOR_SECUNDARIO, linestyle='--', label='Teorica (PMF)')
                
            else: 
                sns.histplot(datos, bins=30, stat="density", kde=False, color=COLOR_PRIMARIO, alpha=0.5, label='Empirica', ax=eje)
                eje_x = np.linspace(np.min(datos), np.max(datos), 200)
                if distribucion_seleccionada == "Normal":
                    y_teorica = stats.norm.pdf(eje_x, loc=parametros['mu'], scale=parametros['sigma'])
                elif distribucion_seleccionada == "Uniforme":
                    y_teorica = stats.uniform.pdf(eje_x, loc=parametros['a'], scale=parametros['b']-parametros['a'])
                elif distribucion_seleccionada == "Exponencial":
                    y_teorica = stats.expon.pdf(eje_x, scale=parametros['beta'])
                eje.plot(eje_x, y_teorica, color=COLOR_SECUNDARIO, linewidth=2, label='Teorica (PDF)')
            
            eje.set_title(f"Simulacion vs Curva Teorica - {distribucion_seleccionada}", fontsize=11, color=COLOR_PRIMARIO, weight='bold')
            eje.set_xlabel("Variable Aleatoria")
            eje.set_ylabel("Densidad / Probabilidad")
            eje.legend(fontsize=9)
            eje.grid(True, linestyle=':', alpha=0.6)
            st.pyplot(figura)
            
            buffer_img = io.BytesIO()
            figura.savefig(buffer_img, format='png', dpi=300, bbox_inches='tight')
            st.download_button(
                label="Guardar Grafica (.PNG)",
                data=buffer_img.getvalue(),
                file_name=f"grafica_{distribucion_seleccionada.lower()}.png",
                mime="image/png"
            )
            
        st.markdown("#### Cuadro de Interpretacion Estadistica")
        st.info(f"Analisis de convergencia: Al evaluar la distribucion {distribucion_seleccionada} con un tamano de muestra de "
                f"N = {tamano_muestra}, se observa que las desviaciones relativas entre las medias empiricas y teoricas tienden "
                f"a disminuir segun se incrementa el volumen de muestreo.")
        
    except ValueError as error_validacion:
        st.error(f"Error de validacion: {error_validacion}")

with pestana2:
    st.subheader("Comparacion Grafica de Dos Modelos Simultaneos")
    columna_c1, columna_c2 = st.columns(2)
    with columna_c1:
        distribucion_1 = st.selectbox("Distribucion A", opciones_distribucion, index=3)
    with columna_c2:
        distribucion_2 = st.selectbox("Distribucion B", opciones_distribucion, index=4)
        
    figura_comp, eje_comp = plt.subplots(figsize=(10, 4))
    
    for dist, color, etiqueta in zip([distribucion_1, distribucion_2], [COLOR_PRIMARIO, COLOR_SECUNDARIO], ['Modelo A', 'Modelo B']):
        sim_local = SimuladorDistribuciones(1000)
        if dist == "Normal": datos_arr = sim_local.simular_normal(0, 1)["datos"]
        elif dist == "Binomial": datos_arr = sim_local.simular_binomial(10, 0.5)["datos"]
        elif dist == "Poisson": datos_arr = sim_local.simular_poisson(4)["datos"]
        elif dist == "Geometrica": datos_arr = sim_local.simular_geometrica(0.5)["datos"]
        elif dist == "Uniforme": datos_arr = sim_local.simular_uniforme(0, 10)["datos"]
        else: datos_arr = sim_local.simular_exponencial(2)["datos"]
        
        sns.kdeplot(datos_arr, color=color, label=f"{etiqueta} ({dist})", fill=True, alpha=0.2, ax=eje_comp)
        
    eje_comp.set_title("Comparacion de Densidades de Probabilidad", color=COLOR_PRIMARIO, weight='bold')
    eje_comp.set_xlabel("Eje X")
    eje_comp.set_ylabel("Densidad")
    eje_comp.legend()
    st.pyplot(figura_comp)

with pestana3:
    st.subheader("Demostracion Practica de la Ley de los Grandes Numeros")
    st.markdown("Esta simulacion muestra como la media empirica converge al valor teorico esperado conforme la muestra crece.")
    
    trayectoria_medias, valor_teorico = ejecutar_ley_grandes_numeros(distribucion_seleccionada, parametros, iteraciones_maximas=10000)
    
    figura_lln, eje_lln = plt.subplots(figsize=(10, 4))
    eje_lln.plot(trayectoria_medias, color=COLOR_PRIMARIO, label='Media Empirica Acumulada')
    eje_lln.axhline(valor_teorico, color=COLOR_SECUNDARIO, linestyle='--', linewidth=2, label=f'Media Teorica ({valor_teorico:.2f})')
    eje_lln.set_title(f"Convergencia para Distribucion {distribucion_seleccionada}", color=COLOR_PRIMARIO, weight='bold')
    eje_lln.set_xlabel("Cantidad de Muestras")
    eje_lln.set_ylabel("Valor de la Media")
    eje_lln.legend()
    eje_lln.grid(True, linestyle=':', alpha=0.5)
    st.pyplot(figura_lln)

with pestana4:
    st.subheader("Analisis del Teorema del Limite Central")
    st.markdown("La distribucion de los promedios de las muestras tiende a modelar una distribucion normal.")
    
    columna_t1, columna_t2 = st.columns(2)
    with columna_t1:
        total_simulaciones = st.slider("Numero de simulaciones", 100, 5000, 1000, 100)
    with columna_t2:
        tamano_muestra_individual = st.slider("Tamano de cada muestra", 2, 100, 30, 1)
        
    medias_tlc = ejecutar_teorema_limite_central(distribucion_seleccionada, parametros, total_simulaciones=total_simulaciones, tamano_muestra=tamano_muestra_individual)
    
    figura_tlc, eje_tlc = plt.subplots(figsize=(10, 4))
    sns.histplot(medias_tlc, kde=True, color=COLOR_PRIMARIO, stat="density", ax=eje_tlc)
    eje_tlc.set_title(f"Distribucion Muestral de Medias", color=COLOR_PRIMARIO, weight='bold')
    eje_tlc.set_xlabel("Valores de las Medias")
    eje_tlc.set_ylabel("Densidad de Frecuencia")
    eje_tlc.grid(True, linestyle=':', alpha=0.5)
    st.pyplot(figura_tlc)