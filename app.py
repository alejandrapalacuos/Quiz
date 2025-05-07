import streamlit as st
import plotly.graph_objects as go

# Define las preguntas y respuestas del quiz
questions = [
    {
        "question": "¿Qué tan importante es para ti que los objetos coleccionados tengan un valor emocional?",
        "options": ["Nada importante", "Poco importante", "Algo importante", "Muy importante"],
        "scores": {"Nostálgico": 1, "Emocional": 1, "Social": 0, "Estético": 0, "Maximalista": 0, "Minimalista": 0, "Histórico": 0, "Inversor": 0, "Nuevo": 0, "Heredero": 0, "Apasionado": 0, "Obsesivo": 0}
    },
    {
        "question": "¿Prefieres coleccionar piezas únicas o una gran cantidad de objetos similares?",
        "options": ["Una pieza única", "Varias piezas similares", "Ambas opciones por igual", "No tengo preferencia"],
        "scores": {"Nostálgico": 0, "Emocional": 0, "Social": 0, "Estético": 1, "Maximalista": 2, "Minimalista": 1, "Histórico": 0, "Inversor": 0, "Nuevo": 0, "Heredero": 0, "Apasionado": 0, "Obsesivo": 0}
    },
    {
        "question": "¿Qué te motiva a coleccionar?",
        "options": ["El valor sentimental de los objetos", "Su estética y cómo combinan con mi espacio", "El desafío de acumular y completar colecciones", "El potencial de inversión o el valor futuro de los objetos"],
        "scores": {"Nostálgico": 2, "Emocional": 2, "Social": 1, "Estético": 1, "Maximalista": 1, "Minimalista": 0, "Histórico": 1, "Inversor": 2, "Nuevo": 0, "Heredero": 0, "Apasionado": 1, "Obsesivo": 1}
    },
    {
        "question": "¿Cuánto te importa que tus colecciones sean visualmente armónicas?",
        "options": ["Nada", "Un poco", "Bastante", "Mucho"],
        "scores": {"Nostálgico": 0, "Emocional": 0, "Social": 0, "Estético": 2, "Maximalista": 0, "Minimalista": 2, "Histórico": 1, "Inversor": 0, "Nuevo": 0, "Heredero": 0, "Apasionado": 0, "Obsesivo": 0}
    },
    {
        "question": "¿Cuál es tu enfoque principal al coleccionar?",
        "options": ["Conectar con mi pasado", "Mostrar mis objetos a mis amigos y familiares", "Acumular lo que me guste", "Obtener objetos que puedan tener valor con el tiempo"],
        "scores": {"Nostálgico": 2, "Emocional": 2, "Social": 2, "Estético": 0, "Maximalista": 0, "Minimalista": 0, "Histórico": 2, "Inversor": 2, "Nuevo": 1, "Heredero": 2, "Apasionado": 1, "Obsesivo": 0}
    }
]

# Variables para almacenar las puntuaciones de cada tipo de coleccionista
scores = { "Nostálgico": 0, "Emocional": 0, "Social": 0, "Estético": 0, "Maximalista": 0, "Minimalista": 0, "Histórico": 0, "Inversor": 0, "Nuevo": 0, "Heredero": 0, "Apasionado": 0, "Obsesivo": 0 }

# Título de la app
st.title("Descubre qué tipo de coleccionista eres")

# Loop para mostrar las preguntas y capturar respuestas
for i, question in enumerate(questions):
    st.subheader(f"Pregunta {i + 1}: {question['question']}")
    response = st.radio(f"Selecciona una opción:", question["options"])

    # Asignar puntuaciones basadas en la respuesta seleccionada
    for option, score in zip(question['options'], [0, 1, 2, 3]):
        if response == option:
            for key, value in question["scores"].items():
                scores[key] += value

# Calcular el total de puntos
total_points = sum(scores.values())

# Calcular el porcentaje para cada tipo
percentages = {key: (value / total_points) * 100 if total_points > 0 else 0 for key, value in scores.items()}

# Mostrar el resultado solo al final
st.subheader("Tus resultados:")
st.write(f"Total de puntos: {total_points}")

# Crear gráfica de dona con los resultados
labels = list(percentages.keys())
values = list(percentages.values())

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
fig.update_layout(title="Distribución de tus tipos de coleccionista", template="plotly_dark")

# Mostrar la gráfica
st.plotly_chart(fig)
