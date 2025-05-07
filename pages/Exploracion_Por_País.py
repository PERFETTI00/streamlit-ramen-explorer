# pages/Exploracion_Por_Pais.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Ruta al archivo CSV
DATA_URL = "ramen-ratings.csv"

# Función para cargar los datos
@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    return data

# Cargar los datos
data = load_data(DATA_URL)
data['Stars'] = pd.to_numeric(data['Stars'], errors='coerce')

st.sidebar.header("✅ Listado de Países")
countries = sorted(data['Country'].unique())
selected_country = st.sidebar.selectbox("Selecciona un País:", countries)

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

st.title("🌎 Exploración de Ramen por País")
st.markdown("Selecciona un país del menú desplegable de la barra lateral para ver información detallada sobre sus ramen.")

# Calcular las estadísticas necesarias por país para el mapa 
country_stats = data.groupby('Country').agg(
    num_reviews=('Review #', 'count'),
    avg_rating=('Stars', 'mean')
).reset_index()


# Crear el mapa interactivo 
fig = px.choropleth(country_stats,
                    locations='Country',
                    locationmode='country names',
                    color='num_reviews',  
                    hover_name='Country',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Mapa Interactivo')

fig.update_layout(
    annotations=[
        dict(
            x=0.5,
            y=-0.15,  
            xref="paper",
            yref="paper",
            text="Pasa el ratón por encima de los países",
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

st.plotly_chart(fig)

if selected_country:
    country_data = data[data['Country'] == selected_country].copy()

    st.subheader(f"🍜 Información de Ramen en {selected_country}")

    # Número de Reseñas
    num_reviews = country_data.shape[0]
    st.metric("Número de Reseñas", num_reviews)

    # Rating Promedio
    avg_rating = country_data['Stars'].mean()
    st.metric("Rating Promedio", f"{avg_rating:.2f} ⭐")

    # Marcas Más Populares
    brand_counts = country_data['Brand'].value_counts().nlargest(5)
    st.subheader("🏢 Marcas Más Populares")
    st.dataframe(brand_counts)

    # Estilos Predominantes
    style_counts = country_data['Style'].value_counts().nlargest(5)
    st.subheader("🍜 Estilos Predominantes")
    st.dataframe(style_counts)

    # Ramen Mejor Calificados
    top_ramen = country_data.nlargest(5, 'Stars')[['Brand', 'Variety', 'Stars']]
    st.subheader("🏆 Ramen Mejor Calificados")
    st.dataframe(top_ramen)


