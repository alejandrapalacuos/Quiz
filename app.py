import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

# Configuración de la página con tema oscuro
st.set_page_config(
    page_title="Quiz de Coleccionistas", 
    layout="wide",
    page_icon="🧮"
)

# Aplicar tema oscuro personalizado
st.markdown("""
    <style>
    :root {
        --primary-color: #9AE6B4;
        --background-color: #1A1A1A;
        --secondary-background-color: #2D2D2D;
        --text-color: #F0F2F6;
        --font: sans-serif;
    }
    
    body {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .stRadio > div {
        flex-direction: row;
        flex-wrap: wrap;
    }
    
    .stRadio label {
        margin-right: 15px;
        margin-bottom: 10px;
        padding: 12px 18px;
        border-radius: 12px;
        background: var(--secondary-background-color);
        color: var(--text-color);
        border: 1px solid #444;
        transition: all 0.3s ease;
    }
    
    .stRadio label:hover {
        background: #3D3D3D;
        border-color: var(--primary-color);
    }
    
    .stRadio [data-baseweb="radio"] div:first-child {
        background-color: var(--secondary-background-color);
        border-color: #666;
    }
    
    .stButton button {
        background-color: var(--primary-color);
        color: #1A1A1A;
        border-radius: 8px;
        padding: 12px 28px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background-color: #68D89B;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--primary-color);
    }
    
    .stDataFrame {
        background-color: var(--secondary-background-color);
    }
    
    .stExpander {
        background-color: var(--secondary-background-color);
        border: 1px solid #444;
        border-radius: 8px;
    }
    
    .stAlert {
        background-color: var(--secondary-background-color);
    }
    
    /* Personalizar gráficos para tema oscuro */
    .stPlotlyChart, .stPyplot {
        background-color: transparent;
    }
    
    /* Personalizar la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #1E1E1E !important;
        border-right: 1px solid #444;
    }
    
    /* Personalizar las tarjetas de resultados */
    .custom-card {
        background: var(--secondary-background-color) !important;
        border-left: 4px solid var(--primary-color) !important;
    }
    
    /* Ajustar colores de la tabla */
    .dataframe {
        background-color: var(--secondary-background-color) !important;
        color: var(--text-color) !important;
    }
    
    .dataframe th {
        background-color: #333 !important;
    }
    
    .dataframe tr:nth-child(even) {
        background-color: #2A2A2A !important;
    }
    
    .dataframe tr:hover {
        background-color: #3D3D3D !important;
    }
    </style>
""", unsafe_allow_html=True)

# [Resto del código permanece igual hasta la función crear_grafica]

def crear_grafica(porcentajes):
    # Filtrar tipos con porcentaje mayor a 0
    datos_grafica = {k: v for k, v in porcentajes.items() if v > 0}
    
    if not datos_grafica:
        return None
    
    # Ordenar de mayor a menor
    datos_ordenados = dict(sorted(datos_grafica.items(), key=lambda item: item[1], reverse=True))
    
    # Crear DataFrame para facilitar el plotting
    df = pd.DataFrame({
        'Tipo': datos_ordenados.keys(),
        'Porcentaje': datos_ordenados.values(),
        'Color': [tipos_coleccionista[tipo]["color"] for tipo in datos_ordenados.keys()]
    })
    
    # Configurar estilo oscuro para matplotlib
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#1A1A1A')
    ax.set_facecolor('#1A1A1A')
    
    # Crear las barras
    bars = ax.barh(df['Tipo'], df['Porcentaje'], color=df['Color'])
    
    # Personalizar ejes y etiquetas
    ax.spines['bottom'].set_color('#444')
    ax.spines['left'].set_color('#444')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.tick_params(axis='x', colors='#F0F2F6')
    ax.tick_params(axis='y', colors='#F0F2F6')
    
    ax.xaxis.label.set_color('#F0F2F6')
    ax.yaxis.label.set_color('#F0F2F6')
    ax.title.set_color('#9AE6B4')
    
    # Añadir etiquetas
    ax.bar_label(bars, fmt='%.1f%%', padding=3, color='#F0F2F6')
    ax.set_xlim(0, 100)
    ax.set_xlabel('Porcentaje', fontweight='bold')
    ax.set_title('Tu perfil de coleccionista', fontweight='bold', pad=20)
    ax.invert_yaxis()  # Mostrar el más alto primero
    
    plt.tight_layout()
    return fig

# [Resto del código permanece igual hasta la visualización de resultados]

# Dentro del bloque if st.button("📊 Ver resultados"):
        with col1:
            st.subheader("🔍 Tu perfil principal:")
            # Mostrar los 3 tipos principales
            principales = sorted(porcentajes.items(), key=lambda x: x[1], reverse=True)[:3]
            
            for tipo, porcentaje in principales:
                if porcentaje > 0:
                    st.markdown(f"""
                    <div style='background-color:#2D2D2D; 
                                padding: 15px; 
                                border-radius: 10px; 
                                margin: 10px 0;
                                border-left: 5px solid {tipos_coleccionista[tipo]["color"]};
                                color: #F0F2F6;'>
                        <h4 style='color:{tipos_coleccionista[tipo]["color"]}; margin-bottom: 8px;'>{tipo} ({porcentaje:.1f}%)</h4>
                        <p style='margin-bottom: 0;'>{tipos_coleccionista[tipo]["descripcion"]}</p>
                    </div>
                    """, unsafe_allow_html=True)

# [Resto del código permanece igual]
