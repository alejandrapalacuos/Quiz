import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

# Configuración de la página para un diseño más amplio
st.set_page_config(
    page_title="Quiz de Coleccionistas", 
    layout="wide",
    page_icon="🧮"
)

# Definir los tipos de coleccionista con descripciones y colores
tipos_coleccionista = {
    "Nostálgico": {
        "puntos": 0,
        "descripcion": "Colecciona por conexión emocional con el pasado, valora los recuerdos.",
        "color": "#FF9AA2"
    },
    "El que no sabe": {
        "puntos": 0,
        "descripcion": "No tiene claro por qué colecciona, simplemente acumula objetos.",
        "color": "#FFB7B2"
    },
    "Heredero": {
        "puntos": 0,
        "descripcion": "Ha heredado la colección y la mantiene por tradición más que por interés propio.",
        "color": "#FFDAC1"
    },
    "Maximalista": {
        "puntos": 0,
        "descripcion": "Prefiere colecciones grandes y expansivas, más es mejor.",
        "color": "#E2F0CB"
    },
    "Minimalista": {
        "puntos": 0,
        "descripcion": "Prefiere colecciones pequeñas pero significativas, calidad sobre cantidad.",
        "color": "#B5EAD7"
    },
    "Inversor": {
        "puntos": 0,
        "descripcion": "Colecciona pensando en el valor financiero futuro de los objetos.",
        "color": "#C7CEEA"
    },
    "Nuevo": {
        "puntos": 0,
        "descripcion": "Coleccionista novato que está empezando y descubriendo su estilo.",
        "color": "#F8B195"
    },
    "Histórico": {
        "puntos": 0,
        "descripcion": "Valora la historia detrás de cada pieza más que el objeto en sí.",
        "color": "#F67280"
    },
    "Apasionado": {
        "puntos": 0,
        "descripcion": "Colecciona por pura pasión y emoción, sin pensar en valor o lógica.",
        "color": "#C06C84"
    },
    "Obsesivo": {
        "puntos": 0,
        "descripcion": "Busca completar colecciones de manera compulsiva y meticulosa.",
        "color": "#6C5B7B"
    },
    "Social": {
        "puntos": 0,
        "descripcion": "Disfruta compartir su colección con otros y participar en comunidades.",
        "color": "#355C7D"
    },
    "Estético": {
        "puntos": 0,
        "descripcion": "Valora principalmente la belleza y disposición visual de las piezas.",
        "color": "#A8E6CE"
    }
}

# Definir las 20 preguntas del quiz con mapeo a tipos
preguntas = [
    {
        "pregunta": "1. ¿Cómo prefieres que sea tu colección?",
        "opciones": [
            {"texto": "Pequeña pero significativa", "tipos": ["Minimalista"]},
            {"texto": "Grande y expansiva", "tipos": ["Maximalista"]},
            {"texto": "Lo que tenga valor para el futuro", "tipos": ["Inversor"]}
        ]
    },
    {
        "pregunta": "2. ¿Qué te motiva más al coleccionar?",
        "opciones": [
            {"texto": "Recuerdos y emociones del pasado", "tipos": ["Nostálgico", "Apasionado"]},
            {"texto": "La historia detrás de las piezas", "tipos": ["Histórico"]},
            {"texto": "La belleza estética de los objetos", "tipos": ["Estético"]}
        ]
    },
    {
        "pregunta": "3. ¿Qué tan obsesionado estás con completar tu colección?",
        "opciones": [
            {"texto": "No me importa si la colección está completa", "tipos": ["Minimalista", "El que no sabe"]},
            {"texto": "Me esfuerzo por tenerlo todo", "tipos": ["Obsesivo", "Maximalista"]},
            {"texto": "Busco piezas únicas que hablen de mí", "tipos": ["Estético", "Apasionado"]}
        ]
    },
    {
        "pregunta": "4. ¿Te gustaría tener una colección muy grande?",
        "opciones": [
            {"texto": "No, prefiero una colección pequeña y significativa", "tipos": ["Minimalista"]},
            {"texto": "Sí, más siempre es mejor", "tipos": ["Maximalista"]},
            {"texto": "No me interesa el tamaño, solo el valor", "tipos": ["Inversor"]}
        ]
    },
    {
        "pregunta": "5. ¿Cómo te sientes al ver algo de tu pasado?",
        "opciones": [
            {"texto": "Nostálgico, me gusta recordar", "tipos": ["Nostálgico"]},
            {"texto": "No me interesa mucho, prefiero el presente", "tipos": ["Nuevo", "Inversor"]},
            {"texto": "Me gusta ver cómo lo antiguo puede tener valor", "tipos": ["Histórico", "Inversor"]}
        ]
    },
    {
        "pregunta": "6. Cuando compras algo, ¿lo haces por impulso o por razón?",
        "opciones": [
            {"texto": "Por impulso, me gusta lo que me emociona", "tipos": ["Apasionado"]},
            {"texto": "Por razones prácticas, busco la oportunidad", "tipos": ["Inversor"]},
            {"texto": "Por impulso, pero también tengo una idea de lo que quiero", "tipos": ["Estético", "Social"]}
        ]
    },
    {
        "pregunta": "7. ¿Qué tan importante es para ti la exclusividad de una pieza?",
        "opciones": [
            {"texto": "Es muy importante, me gusta tener lo que otros no tienen", "tipos": ["Obsesivo", "Social"]},
            {"texto": "No me importa mucho, no busco exclusividad", "tipos": ["El que no sabe", "Heredero"]},
            {"texto": "Es algo que valoro, pero no es lo más importante", "tipos": ["Estético", "Minimalista"]}
        ]
    },
    {
        "pregunta": "8. ¿Cuánto espacio le das a tu colección en tu hogar?",
        "opciones": [
            {"texto": "Muy poco, la colecciono en un lugar específico", "tipos": ["Minimalista"]},
            {"texto": "Bastante, mi colección ocupa varios rincones", "tipos": ["Maximalista"]},
            {"texto": "El espacio no es lo más importante, me interesa lo que cada pieza representa", "tipos": ["Estético", "Histórico"]}
        ]
    },
    {
        "pregunta": "9. ¿Qué tan importante es la historia detrás de una pieza que coleccionas?",
        "opciones": [
            {"texto": "Es lo más importante para mí", "tipos": ["Histórico"]},
            {"texto": "No me interesa mucho la historia, solo la pieza", "tipos": ["El que no sabe", "Nuevo"]},
            {"texto": "Me gusta conocer la historia, pero no es crucial", "tipos": ["Nostálgico", "Apasionado"]}
        ]
    },
    {
        "pregunta": "10. ¿Coleccionas cosas por su valor financiero?",
        "opciones": [
            {"texto": "No, solo por lo que significan para mí", "tipos": ["Nostálgico", "Apasionado"]},
            {"texto": "Sí, siempre estoy pensando en la posible apreciación de valor", "tipos": ["Inversor"]},
            {"texto": "Depende, si tiene valor sentimental y financiero, mejor", "tipos": ["Heredero", "Social"]}
        ]
    },
    {
        "pregunta": "11. ¿Con qué frecuencia buscas añadir nuevas piezas a tu colección?",
        "opciones": [
            {"texto": "Solo cuando encuentro algo realmente especial", "tipos": ["Minimalista", "Estético"]},
            {"texto": "Todo el tiempo, me encanta encontrar cosas nuevas", "tipos": ["Maximalista", "Obsesivo"]},
            {"texto": "De vez en cuando, cuando considero que es el momento adecuado", "tipos": ["Inversor", "Social"]}
        ]
    },
    {
        "pregunta": "12. ¿Cómo te describes en cuanto a la organización de tu colección?",
        "opciones": [
            {"texto": "Muy organizada y cuidada", "tipos": ["Obsesivo", "Estético"]},
            {"texto": "Un poco desordenada, pero en su mayoría bien", "tipos": ["Apasionado", "Nuevo"]},
            {"texto": "Tengo un sistema, pero no siempre es perfecto", "tipos": ["Social", "Histórico"]}
        ]
    },
    {
        "pregunta": "13. ¿Qué tan importante es el estado de conservación de las piezas en tu colección?",
        "opciones": [
            {"texto": "Es lo más importante para mí", "tipos": ["Obsesivo", "Inversor"]},
            {"texto": "No me importa tanto, mientras se vea bien", "tipos": ["El que no sabe", "Nuevo"]},
            {"texto": "Prefiero que se conserve, pero no soy tan exigente", "tipos": ["Apasionado", "Social"]}
        ]
    },
    {
        "pregunta": "14. ¿Te entusiasma compartir tu colección con otros coleccionistas?",
        "opciones": [
            {"texto": "Sí, me gusta mostrarla y compartirla", "tipos": ["Social"]},
            {"texto": "No, prefiero mantenerla para mí", "tipos": ["Nostálgico", "El que no sabe"]},
            {"texto": "Depende, me gusta compartir con personas que realmente aprecien lo que colecciono", "tipos": ["Estético", "Histórico"]}
        ]
    },
    {
        "pregunta": "15. ¿Qué tan importante es la estética de una pieza?",
        "opciones": [
            {"texto": "Es lo más importante, busco belleza", "tipos": ["Estético"]},
            {"texto": "No es lo más importante, pero sí la valoro", "tipos": ["Social", "Apasionado"]},
            {"texto": "Me importa, pero no es lo único", "tipos": ["Histórico", "Minimalista"]}
        ]
    },
    {
        "pregunta": "16. ¿Qué haces cuando encuentras una pieza que te gusta?",
        "opciones": [
            {"texto": "La compro inmediatamente, no puedo esperar", "tipos": ["Apasionado", "Nuevo"]},
            {"texto": "La investigo primero para asegurarme de que es valiosa", "tipos": ["Inversor", "Histórico"]},
            {"texto": "Me la llevo si siento que encaja con mi colección", "tipos": ["Estético", "Minimalista"]}
        ]
    },
    {
        "pregunta": "17. ¿Qué tan dispuesto estás a pagar más por una pieza única?",
        "opciones": [
            {"texto": "Estoy dispuesto a pagar un precio alto por algo único", "tipos": ["Obsesivo", "Estético"]},
            {"texto": "Solo si el precio es razonable", "tipos": ["Social", "Heredero"]},
            {"texto": "Prefiero no gastar tanto en una sola pieza", "tipos": ["Minimalista", "El que no sabe"]}
        ]
    },
    {
        "pregunta": "18. ¿Cuál es tu principal motivación al coleccionar?",
        "opciones": [
            {"texto": "Emoción personal", "tipos": ["Apasionado", "Nostálgico"]},
            {"texto": "Valor histórico o de inversión", "tipos": ["Histórico", "Inversor"]},
            {"texto": "Estética y belleza", "tipos": ["Estético"]}
        ]
    },
    {
        "pregunta": "19. ¿Cómo defines tu relación con los objetos de tu colección?",
        "opciones": [
            {"texto": "Son una extensión de mí", "tipos": ["Apasionado", "Nostálgico"]},
            {"texto": "Son una inversión y un legado", "tipos": ["Inversor", "Heredero"]},
            {"texto": "Son una forma de expresar mi gusto por lo bello", "tipos": ["Estético"]}
        ]
    },
    {
        "pregunta": "20. ¿Qué harías si tuvieras que deshacerte de parte de tu colección?",
        "opciones": [
            {"texto": "Guardaría solo lo más significativo", "tipos": ["Minimalista", "Nostálgico"]},
            {"texto": "Intentaría conservar todo, no podría deshacerme de nada", "tipos": ["Maximalista", "Obsesivo"]},
            {"texto": "Vendería lo que tenga valor para reinvertir", "tipos": ["Inversor"]}
        ]
    }
]

# Función para calcular los porcentajes
def calcular_porcentajes(respuestas):
    total_puntos = sum(tipo["puntos"] for tipo in respuestas.values())
    if total_puntos == 0:
        return {k: 0 for k in respuestas.keys()}
    
    porcentajes = {k: (v["puntos"] / total_puntos) * 100 for k, v in respuestas.items()}
    return porcentajes

# Función para crear la gráfica
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
    
    # Crear la figura
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(df['Tipo'], df['Porcentaje'], color=df['Color'])
    
    # Añadir etiquetas
    ax.bar_label(bars, fmt='%.1f%%', padding=3)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Porcentaje')
    ax.set_title('Tu perfil de coleccionista')
    ax.invert_yaxis()  # Mostrar el más alto primero
    
    plt.tight_layout()
    return fig

# Diseño de la aplicación
st.title("🧮 ¿Qué tipo de coleccionista eres?")
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #2c3e50;}
    .stRadio > div {flex-direction: row; flex-wrap: wrap;}
    .stRadio label {margin-right: 20px; margin-bottom: 10px; background: #f5728d; padding: 10px 15px; border-radius: 10px;}
    .stRadio label:hover {background: #f5728d;}
    .stButton button {background-color: #4CAF50; color: black; border-radius: 5px; padding: 10px 24px;}
    .stButton button:hover {background-color: #45a049;}
    </style>
""", unsafe_allow_html=True)

# Barra lateral con información
with st.sidebar:
    st.header("ℹ️ Acerca de este quiz")
    st.write("""
        Este quiz te ayudará a descubrir qué tipo de coleccionista eres 
        basado en tus preferencias y comportamientos al coleccionar objetos.
        
        Responde cada pregunta honestamente para obtener los mejores resultados!
    """)
    st.image("https://cdn.pixabay.com/photo/2017/08/06/22/52/compass-2596999_640.jpg", 
             caption="Descubre tu estilo de coleccionista")
    st.markdown("---")
    st.write("**Instrucciones:**")
    st.write("1. Responde todas las preguntas")
    st.write("2. Haz clic en 'Ver resultados' al final")
    st.write("3. Descubre tu perfil de coleccionista")

# Inicializar respuestas si no existen en session state
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {tipo: 0 for tipo in tipos_coleccionista.keys()}

# Mostrar las preguntas
for i, pregunta in enumerate(preguntas):
    st.subheader(pregunta["pregunta"])
    f"Selecciona una opción para la pregunta {i+1}:",
    # Mostrar opciones como radio buttons
    opcion_seleccionada = st.radio(
       
        [op["texto"] for op in pregunta["opciones"]],
        key=f"pregunta_{i}",
        index=None
    )
    
    # Actualizar puntos según la selección
    if opcion_seleccionada:
        for opcion in pregunta["opciones"]:
            if opcion["texto"] == opcion_seleccionada:
                for tipo in opcion["tipos"]:
                    st.session_state.respuestas[tipo] += 1

# Botón para ver resultados
if st.button("📊 Ver resultados", type="primary"):
    if any(st.session_state.respuestas.values()):
        st.balloons()
        porcentajes = calcular_porcentajes({k: {"puntos": v} for k, v in st.session_state.respuestas.items()})
        
        # Mostrar resultados en dos columnas
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("🔍 Tu perfil principal:")
            # Mostrar los 3 tipos principales
            principales = sorted(porcentajes.items(), key=lambda x: x[1], reverse=True)[:3]
            
            for tipo, porcentaje in principales:
                if porcentaje > 0:
                    st.markdown(f"""
                    <div style='background-color:{tipos_coleccionista[tipo]["color"] + "30"}; 
                                padding: 15px; border-radius: 10px; margin: 10px 0;
                                border-left: 5px solid {tipos_coleccionista[tipo]["color"]}'>
                        <h4>{tipo} ({porcentaje:.1f}%)</h4>
                        <p>{tipos_coleccionista[tipo]["descripcion"]}</p>
                    </div>
                    """, unsafe_allow_html=True)
        
        with col2:
            st.subheader("📈 Distribución de tu perfil:")
            # Mostrar gráfica
            fig = crear_grafica(porcentajes)
            if fig:
                st.pyplot(fig)
            else:
                st.warning("No hay suficientes datos para mostrar la gráfica.")
        
        # Mostrar todos los porcentajes en una tabla expandible
        with st.expander("📋 Ver todos los resultados detallados"):
            df_resultados = pd.DataFrame([
                {
                    "Tipo": tipo,
                    "Porcentaje": f"{porcentaje:.1f}%",
                    "Descripción": tipos_coleccionista[tipo]["descripcion"]
                }
                for tipo, porcentaje in porcentajes.items() if porcentaje > 0
            ]).sort_values("Porcentaje", ascending=False)
            
            st.dataframe(
                df_resultados, 
                hide_index=True, 
                use_container_width=True,
                column_config={
                    "Tipo": st.column_config.TextColumn("Tipo"),
                    "Porcentaje": st.column_config.ProgressColumn(
                        "Porcentaje",
                        format="%.1f%%",
                        min_value=0,
                        max_value=100,
                    ),
                    "Descripción": st.column_config.TextColumn("Descripción")
                }
            )
    else:
        st.warning("Por favor responde al menos una pregunta para ver los resultados.")

# Botón para reiniciar el quiz
if st.button("🔄 Reiniciar quiz"):
    st.session_state.respuestas = {tipo: 0 for tipo in tipos_coleccionista.keys()}
    st.rerun()
