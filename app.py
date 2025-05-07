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

# Definir las 20 preguntas del quiz
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
    },
    {
        "pregunta": "¿Te gustaría tener una colección muy grande?",
        "opciones": ["No, prefiero una colección pequeña y significativa", "Sí, más siempre es mejor", "No me interesa el tamaño, solo el valor"]
    },
    {
        "pregunta": "¿Cómo te sientes al ver algo de tu pasado?",
        "opciones": ["Nostálgico, me gusta recordar", "No me interesa mucho, prefiero el presente", "Me gusta ver cómo lo antiguo puede tener valor"]
    },
    {
        "pregunta": "Cuando compras algo, ¿lo haces por impulso o por razón?",
        "opciones": ["Por impulso, me gusta lo que me emociona", "Por razones prácticas, busco la oportunidad", "Por impulso, pero también tengo una idea de lo que quiero"]
    },
    {
        "pregunta": "¿Qué tan importante es para ti la exclusividad de una pieza?",
        "opciones": ["Es muy importante, me gusta tener lo que otros no tienen", "No me importa mucho, no busco exclusividad", "Es algo que valoro, pero no es lo más importante"]
    },
    {
        "pregunta": "¿Cuánto espacio le das a tu colección en tu hogar?",
        "opciones": ["Muy poco, la colecciono en un lugar específico", "Bastante, mi colección ocupa varios rincones", "El espacio no es lo más importante, me interesa lo que cada pieza representa"]
    },
    {
        "pregunta": "¿Qué tan importante es la historia detrás de una pieza que coleccionas?",
        "opciones": ["Es lo más importante para mí", "No me interesa mucho la historia, solo la pieza", "Me gusta conocer la historia, pero no es crucial"]
    },
    {
        "pregunta": "¿Coleccionas cosas por su valor financiero?",
        "opciones": ["No, solo por lo que significan para mí", "Sí, siempre estoy pensando en la posible apreciación de valor", "Depende, si tiene valor sentimental y financiero, mejor"]
    },
    {
        "pregunta": "¿Con qué frecuencia buscas añadir nuevas piezas a tu colección?",
        "opciones": ["Solo cuando encuentro algo realmente especial", "Todo el tiempo, me encanta encontrar cosas nuevas", "De vez en cuando, cuando considero que es el momento adecuado"]
    },
    {
        "pregunta": "¿Cómo te describes en cuanto a la organización de tu colección?",
        "opciones": ["Muy organizada y cuidada", "Un poco desordenada, pero en su mayoría bien", "Tengo un sistema, pero no siempre es perfecto"]
    },
    {
        "pregunta": "¿Qué tan importante es el estado de conservación de las piezas en tu colección?",
        "opciones": ["Es lo más importante para mí", "No me importa tanto, mientras se vea bien", "Prefiero que se conserve, pero no soy tan exigente"]
    },
    {
        "pregunta": "¿Te entusiasma compartir tu colección con otros coleccionistas?",
        "opciones": ["Sí, me gusta mostrarla y compartirla", "No, prefiero mantenerla para mí", "Depende, me gusta compartir con personas que realmente aprecien lo que colecciono"]
    },
    {
        "pregunta": "¿Qué tan importante es la estética de una pieza?",
        "opciones": ["Es lo más importante, busco belleza", "No es lo más importante, pero sí la valoro", "Me importa, pero no es lo único"]
    },
    {
        "pregunta": "¿Qué haces cuando encuentras una pieza que te gusta?",
        "opciones": ["La compro inmediatamente, no puedo esperar", "La investigo primero para asegurarme de que es valiosa", "Me la llevo si siento que encaja con mi colección"]
    },
    {
        "pregunta": "¿Qué tan dispuesto estás a pagar más por una pieza única?",
        "opciones": ["Estoy dispuesto a pagar un precio alto por algo único", "Solo si el precio es razonable", "Prefiero no gastar tanto en una sola pieza"]
    },
    {
        "pregunta": "¿Cuál es tu principal motivación al coleccionar?",
        "opciones": ["Emoción personal", "Valor histórico o de inversión", "Estética y belleza"]
    },
    {
        "pregunta": "¿Cómo defines tu relación con los objetos de tu colección?",
        "opciones": ["Son una extensión de mí", "Son una inversión y un legado", "Son una forma de expresar mi gusto por lo bello"]
    }
]

# Inicializar el estado de la sesión
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {tipo: 0 for tipo in tipos_coleccionista}

# Función para calcular los porcentajes
def calcular_porcentajes(respuestas):
    total_respuestas = sum(respuestas.values())
    porcentajes = {k: (v / total_respuestas) * 100 for k, v in respuestas.items()}
    return porcentajes

# Título de la aplicación
st.title("¿Qué tipo de coleccionista eres?")

# Mostrar la pregunta actual
pregunta = preguntas[st.session_state.pregunta_actual]
st.write(f"Pregunta {st.session_state.pregunta_actual + 1}: {pregunta['pregunta']}")

# Mostrar opciones
respuesta = st.radio("Selecciona una opción:", pregunta["opciones"])

# Acción cuando el usuario presiona el botón "Continuar"
if st.button("Continuar"):
    # Guardar la respuesta seleccionada y actualizar el contador de respuestas
    if respuesta == pregunta["opciones"][0]:
        st.session_state.respuestas["Nostálgico"] += 1
    elif respuesta == pregunta["opciones"][1]:
        st.session_state.respuestas["Maximalista"] += 1
    elif respuesta == pregunta["opciones"][2]:
        st.session_state.respuestas["Inversor"] += 1
    
    # Avanzar a la siguiente pregunta
    if st.session_state.pregunta_actual < len(preguntas) - 1:
        st.session_state.pregunta_actual += 1
    else:
        # Al terminar el quiz, calcular y mostrar los resultados
        porcentajes = calcular_porcentajes(st.session_state.respuestas)
        st.write("Tus porcentajes por tipo de coleccionista:")
        for tipo, porcentaje in porcentajes.items():
            st.write(f"{tipo}: {porcentaje:.2f}%")
