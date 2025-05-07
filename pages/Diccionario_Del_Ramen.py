# pages/Diccionario_Del_Ramen.py
import streamlit as st
import pandas as pd

st.sidebar.header("🎨 Personalización")
theme_choice = st.sidebar.radio("Selecciona un tema:", ["Claro", "Oscuro"], key="theme_choice_diccionario")

if theme_choice == "Oscuro":
    st.markdown(
        """
        <style>
        body {
            color: #eee;
            background-color: #222;
        }
        .stApp {
            background-color: #222;
        }
        .streamlit-expander-content {
            color: #eee;
        }
        .st-bb { /* Dataframes */
            color: #eee !important;
            background-color: #444 !important;
        }
        .st-bq { /* Markdown */
            color: #eee;
            background-color: #333;
            border-left-color: #666;
        }
        .st-bt button { /* Botones */
            color: #eee;
            background-color: #444;
            border-color: #666;
        }
        .st-bt button:hover {
            background-color: #555;
        }
        .st-br { /* Selectores y Radios */
            color: #eee;
        }
        h1, h2, h3, h4, h5, h6 { /* Títulos */
            color: #f39c12 !important; /* Dorado suave */
        }
        p, div, span, label { /* Otros elementos de texto comunes */
            color: #eee !important;
        }
        /* Estilos específicos para la barra lateral */
        [data-testid="stSidebar"] {
            background-color: #333; /* Fondo de la barra lateral */
            color: #eee; /* Texto en la barra lateral */
        }
        [data-testid="stSidebar"] * { /* Aplica el color de texto a todos los elementos dentro */
            color: #eee !important;
        }
        /* Es posible que necesitemos añadir más selectores específicos según la estructura de Streamlit */
        </style>
        """,
        unsafe_allow_html=True,
    )
else: # Tema Claro
    st.markdown(
        """
        <style>
        body {
            color: #333;
            background-color: #f8f8f8;
        }
        .stApp {
            background-color: #f8f8f8;
        }
        .streamlit-expander-content {
            color: #333;
        }
        .st-bb { /* Dataframes */
            color: #333 !important;
            background-color: #fff !important;
        }
        .st-bq { /* Markdown */
            color: #555;
            background-color: #eee;
            border-left-color: #2ecc71;
        }
        .st-bt button { /* Botones */
            color: #fff;
            background-color: #2ecc71;
            border-color: #27ae60;
        }
        .st-bt button:hover {
            background-color: #27ae60;
        }
        .st-br { /* Selectores y Radios */
            color: #333;
        }
        h1, h2, h3, h4, h5, h6 { /* Títulos */
            color: #000 !important;
        }
        p, div, span, label { /* Otros elementos de texto comunes */
            color: #333 !important;
        }
        /* Estilos específicos para la barra lateral */
        [data-testid="stSidebar"] {
            background-color: #f0f0f0; /* Fondo de la barra lateral */
            color: #333; /* Texto en la barra lateral */
        }
        [data-testid="stSidebar"] * { /* Aplica el color de texto a todos los elementos dentro */
            color: #333 !important;
        }
        /* Es posible que necesitemos añadir más selectores específicos según la estructura de Streamlit */
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("🍜 El Diccionario del Ramen 📚")
st.subheader("Descubre los términos y estilos del fascinante mundo del ramen.")
st.markdown("---")

# Definir un diccionario de términos y sus definiciones
diccionario = {
    "Shoyu": "Un tipo de sopa de ramen a base de salsa de soja. Generalmente tiene un caldo claro y sabroso.",
    "Miso": "Ramen con una sopa rica y sabrosa sazonada con pasta de miso (soja fermentada).",
    "Tonkotsu": "Un caldo de ramen espeso y cremoso hecho hirviendo huesos de cerdo durante muchas horas.",
    "Shio": "Ramen con un caldo claro y ligero sazonado principalmente con sal.",
    "Instant Ramen": "Fideos de ramen precocidos y deshidratados que se preparan rápidamente añadiendo agua caliente.",
    "Cup Noodles": "Ramen instantáneo envasado en un vaso, al que solo se le añade agua caliente.",
    "Nori": "Alga marina seca comestible, a menudo utilizada como guarnición en el ramen.",
    "Menma": "Brotes de bambú fermentados, un topping común en el ramen.",
    "Chashu": "Panceta de cerdo estofada o asada, cortada en rodajas y utilizada como topping.",
    "Tamago": "Huevo cocido (a menudo marinado), un topping popular en el ramen. Puede ser Ajitama (marinado) o Onsen Tamago (a baja temperatura).",
    "Negi": "Cebolla verde picada, utilizada como topping para añadir frescura.",
    "Gyoza": "Empanadillas japonesas rellenas de carne y verduras, a menudo servidas como acompañamiento del ramen.",
    "Kaeshi": "Una salsa base concentrada que se mezcla con el caldo para sazonar el ramen. Varía según el tipo de ramen (shoyu kaeshi, miso dare, etc.).",
    "Dashi": "Un caldo de sopa japonés hecho típicamente de algas kombu, hojuelas de bonito seco (katsuobushi), sardinas secas (niboshi) o setas shiitake. A menudo forma la base del caldo de ramen.",
    "Umami": "Uno de los cinco sabores básicos (junto con dulce, ácido, salado y amargo). A menudo se describe como un sabor sabroso, carnoso o glutamato, y es una característica importante de un buen caldo de ramen.",
}

# Mostrar el diccionario
st.subheader("Términos Comunes del Ramen")
for termino, definicion in diccionario.items():
    st.markdown(f"**{termino}:** {definicion}")

st.markdown("---")
st.subheader("Estilos Populares de Ramen")
st.markdown("Estos son algunos de los estilos de ramen más comunes que podrías encontrar:")

estilos = {
    "Hakata Ramen (Fukuoka)": "Famoso por su caldo Tonkotsu rico y cremoso, fideos finos y a menudo servido con toppings como chashu y beni shoga (jengibre encurtido).",
    "Sapporo Ramen (Hokkaido)": "Conocido por su caldo Miso robusto, a menudo incluye maíz, mantequilla y brotes de soja.",
    "Kitakata Ramen (Fukushima)": "Caracterizado por sus fideos planos y ondulados y un caldo claro a base de cerdo y pescado.",
    "Tokyo Ramen": "Un estilo clásico con un caldo Shoyu claro a base de pollo y pescado, fideos rizados y toppings como chashu, menma y nori.",
    "Hiroshima Ramen": "A menudo presenta un caldo a base de pollo y verduras, a veces con la adición de marisco.",
    "Wakayama Ramen": "Conocido por su caldo a base de salsa de soja y cerdo, que puede variar en espesor y sabor.",
}

for estilo, descripcion in estilos.items():
    st.markdown(f"**{estilo}:** {descripcion}")

st.markdown("---")
st.info("Este es un diccionario básico y el mundo del ramen es vasto y diverso. ¡Sigue explorando para descubrir más!")