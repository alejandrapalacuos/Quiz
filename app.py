import streamlit as st

# Definir los tipos de coleccionista
tipos_coleccionista = {
    "Nostálgico": 0,
    "El que no sabe": 0,
    "Heredero": 0,
    "Maximalista": 0,
    "Minimalista": 0,
    "Inversor": 0,
    "Nuevo": 0,
    "Histórico": 0,
    "Apasionado": 0,
    "Obsesivo": 0,
    "Social": 0,
    "Estético": 0
}

# Preguntas del quiz
preguntas = [
    {
        "pregunta": "¿Cómo prefieres que sea tu colección?",
        "opciones": ["Pequeña pero significativa", "Grande y expansiva", "Lo que tenga valor para el futuro"]
    },
    {
        "pregunta": "¿Qué te motiva más al coleccionar?",
        "opciones": ["Recuerdos y emociones del pasado", "La historia detrás de las piezas", "La belleza estética de los objetos"]
    },
    {
        "pregunta": "¿Qué tan obsesionado estás con completar tu colección?",
        "opciones": ["No me importa si la colección está completa", "Me esfuerzo por tenerlo todo", "Busco piezas únicas que hablen de mí"]
    }
    # Añadir más preguntas si lo deseas
]

# Función para calcular el porcentaje
def calcular_porcentajes(respuestas):
    total_respuestas = sum(respuestas.values())
    porcentajes = {k: (v / total_respuestas) * 100 for k, v in respuestas.items()}
    return porcentajes

# Título de la aplicación
st.title("¿Qué tipo de coleccionista eres?")

# Respuestas del usuario
respuestas = {tipo: 0 for tipo in tipos_coleccionista}

# Mostrar las preguntas
for pregunta in preguntas:
    respuesta = st.radio(pregunta["pregunta"], pregunta["opciones"])
    if respuesta == pregunta["opciones"][0]:
        respuestas["Nostálgico"] += 1
    elif respuesta == pregunta["opciones"][1]:
        respuestas["Maximalista"] += 1
    elif respuesta == pregunta["opciones"][2]:
        respuestas["Inversor"] += 1

# Botón para ver resultados
if st.button("Ver resultados"):
    porcentajes = calcular_porcentajes(respuestas)
    
    # Mostrar resultados
    st.write("Tus porcentajes por tipo de coleccionista:")
    
    for tipo, porcentaje in porcentajes.items():
        st.write(f"{tipo}: {porcentaje:.2f}%")
