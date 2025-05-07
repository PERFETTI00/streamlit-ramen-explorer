# Inicio.py 
import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO
from PIL import Image
import random

# Título de la aplicación
st.title("🍜 Explorando el Mundo del Ramen a Través de sus Ratings 📊")

# Subtítulo o descripción
st.subheader("🗺️ Dataset de ratings de diferentes tipos de ramen de todo el mundo. 🌎")

# Ruta al archivo CSV
DATA_URL = "ramen-ratings.csv"
DATA_SOURCE = "Kaggle (Ramen Ratings)"

# Función para cargar los datos
@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    return data

# Cargar los datos
data = load_data(DATA_URL)
data['Style'] = data['Style'].astype(str)
data['Stars'] = pd.to_numeric(data['Stars'], errors='coerce')

# Abre la imagen y la muestra en la barra lateral
try:
    image = Image.open("images/ramen_logo.png")
    st.sidebar.image(image, caption="Disfruta del Ramen!", use_container_width=True)
except FileNotFoundError:
    st.sidebar.error("Imagen 'ramen_logo.png' no encontrada. Asegúrate de que esté en la misma carpeta.")

# --- Sidebar para Filtros y Personalización ---
st.sidebar.header("⚙️ Filtros")

all_countries = sorted(data['Country'].unique())
selected_countries = st.sidebar.multiselect("🌍 País:", all_countries, default=[])
filtered_by_country = data[data['Country'].isin(selected_countries)]

available_brands = sorted(filtered_by_country['Brand'].unique())
selected_brands = st.sidebar.multiselect("🏢 Marca:", available_brands, default=available_brands if selected_countries else [])
filtered_by_brand = filtered_by_country[filtered_by_country['Brand'].isin(selected_brands)]

available_styles = sorted(filtered_by_brand['Style'].unique())
selected_styles = st.sidebar.multiselect("🍜 Estilo:", available_styles, default=available_styles if selected_brands and selected_countries else [])

final_filtered_data = data[data['Country'].isin(selected_countries) &
                            data['Brand'].isin(selected_brands) &
                            data['Style'].isin(selected_styles)].copy()
final_filtered_data['Stars'] = pd.to_numeric(final_filtered_data['Stars'], errors='coerce')

st.sidebar.header("🎨 Personalización")
theme_choice = st.sidebar.radio("Selecciona un tema:", ["Claro", "Oscuro"])

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

st.sidebar.header("🧭 Navegación")
menu = ["📊 Explorar Datos", "📈 Visualizaciones", "📝 Resumen", "🎲 Ramen Aleatorio"]
choice = st.sidebar.radio("➡️ Ir a:", menu)

# --- Contenido Principal ---
if choice == "📊 Explorar Datos":
    st.subheader("🔍 Dataset de Ratings de Ramen (Filtrado)")
    st.markdown("Aquí puedes explorar y filtrar los datos de los ratings de ramen según tus selecciones.")

    columns_to_show = st.multiselect("Seleccionar columnas a mostrar:", final_filtered_data.columns.tolist(), default=final_filtered_data.columns.tolist())
    st.dataframe(final_filtered_data[columns_to_show])

    def convert_df_to_csv(df):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False, encoding='utf-8')
        return csv_buffer.getvalue()

    csv_data = convert_df_to_csv(final_filtered_data[columns_to_show])

    st.download_button(
        label="Descargar datos filtrados como CSV",
        data=csv_data,
        file_name='ramen_ratings_filtrado.csv',
        mime='text/csv',
    )

elif choice == "📈 Visualizaciones":
    st.subheader("📉 Distribución de Ratings")
    st.markdown("Este gráfico muestra la distribución de las puntuaciones de ramen según los filtros aplicados.")
    if not final_filtered_data.empty:
        fig_ratings = px.histogram(final_filtered_data.dropna(subset=['Stars']), x='Stars', title='Distribución de las Puntuaciones de Ramen')
        st.plotly_chart(fig_ratings)
    else:
        st.info("No hay datos para mostrar con los filtros seleccionados para la distribución de ratings.")

    st.subheader("🌎 Rating Promedio por País")
    st.markdown("Este gráfico de barras muestra el rating promedio de los ramen por país, según los filtros aplicados.")
    if not final_filtered_data.empty:
        # Calcular la cantidad de reseñas por país
        review_counts = final_filtered_data['Country'].value_counts().reset_index()
        review_counts.columns = ['Country', 'Review Count']

        # Calcular el ramen mejor calificado por país
        best_ramen_per_country = final_filtered_data.loc[final_filtered_data.groupby('Country')['Stars'].idxmax()][['Country', 'Brand', 'Variety', 'Stars']]
        best_ramen_per_country.columns = ['Country', 'Best Brand', 'Best Variety', 'Best Rating']

        # Fusionar los datos para tenerlos disponibles en el gráfico
        avg_ratings_country = final_filtered_data.groupby('Country')['Stars'].mean().sort_values(ascending=False).reset_index()
        avg_ratings_country = pd.merge(avg_ratings_country, review_counts, on='Country', how='left')
        avg_ratings_country = pd.merge(avg_ratings_country, best_ramen_per_country, on='Country', how='left')

        fig_avg_country = px.bar(avg_ratings_country, x='Country', y='Stars',
                                 title='Rating Promedio de Ramen por País',
                                 labels={'Stars': 'Rating Promedio', 'Country': 'País'},
                                 hover_data=['Review Count', 'Best Brand', 'Best Variety', 'Best Rating']) # Información al pasar el ratón
        st.plotly_chart(fig_avg_country)
    else:
        st.info("No hay datos para mostrar con los filtros seleccionados para la distribución de ratings.")

elif choice == "📝 Resumen":
    st.subheader("📊 Resumen de los Datos")
    st.markdown("En esta sección, se muestran resúmenes y estadísticas clave sobre los datos de ratings de ramen.")
    if not final_filtered_data.empty:
        avg_rating = final_filtered_data['Stars'].mean()
        max_rated = final_filtered_data.loc[final_filtered_data['Stars'].idxmax()]
        country_with_highest_avg = final_filtered_data.groupby('Country')['Stars'].mean().idxmax()

        st.metric("Rating Promedio", f"{avg_rating:.2f} ⭐")
        st.metric("Mejor Ramen", f"{max_rated['Brand']} - {max_rated['Variety']} ({max_rated['Stars']:.2f} ⭐) de {max_rated['Country']}")
        st.metric("País con Rating Promedio Más Alto", country_with_highest_avg)
    else:
        st.info("No hay datos para mostrar con los filtros seleccionados para el resumen.")

elif choice == "🎲 Ramen Aleatorio":
    st.subheader("🍜 ¡Descubre un Ramen al Azar! 🍀")
    st.markdown("Pulsa el botón para obtener información sobre un ramen seleccionado aleatoriamente de todo el dataset.")
    if st.button("Mostrar Ramen Aleatorio"):
        if not data.empty:
            random_ramen = data.sample(1).iloc[0]
            st.write(f"**Marca:** {random_ramen['Brand']}")
            st.write(f"**Variedad:** {random_ramen['Variety']}")
            st.write(f"**Estilo:** {random_ramen['Style']}")
            st.write(f"**País:** {random_ramen['Country']}")
            st.write(f"**Puntuación:** {random_ramen['Stars']:.2f} ⭐")
        else:
            st.info("El dataset de ramen está vacío.")

elif choice == "🌍 Exploración por País":
    st.markdown("Redirigiendo a la Exploración por País...")
    st.markdown(f'<meta http-equiv="refresh" content="0;url=pages/exploracion_pais" />', unsafe_allow_html=True)

# Sección de Recomendaciones Basadas en Filtros
if not final_filtered_data.empty:
    st.subheader("🍜 Recomendaciones Basadas en tus Filtros ✨")
    st.markdown("Aquí tienes algunos de los ramen mejor calificados que coinciden con tus selecciones:")

    # Obtener los 5 ramen mejor calificados dentro de los filtros
    top_ramen = final_filtered_data.nlargest(5, 'Stars')

    if not top_ramen.empty:
        for index, row in top_ramen.iterrows():
            st.write(f"**{row['Brand']} - {row['Variety']}** ({row['Stars']:.2f} ⭐) de {row['Country']} ({row['Style']})")
    else:
        st.info("No se encontraron ramen que coincidan con los filtros aplicados.")
elif selected_countries != sorted(data['Country'].unique()) or \
     selected_brands != sorted(filtered_by_country['Brand'].unique()) or \
     selected_styles != sorted(filtered_by_brand['Style'].unique()):
    st.info("Aplica filtros en la barra lateral para ver recomendaciones de ramen.")

st.markdown("---")