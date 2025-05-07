# streamlit-ramen-explorer
Prototipo de aplicación de Streamlit para explorar y visualizar ratings de ramen. 
# Explorador de Ratings de Ramen con Streamlit 🍜📊

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tu-enlace-desplegado-de-streamlit-si-lo-tienes)

## Descripción del Proyecto

Este es un prototipo de aplicación web interactiva construido con Streamlit para explorar y visualizar un dataset de ratings de diferentes tipos de ramen alrededor del mundo. El objetivo principal de este proyecto es demostrar el uso de diversas funcionalidades de Streamlit y aplicar conocimientos de Python en un caso práctico de análisis de datos.

## Funcionalidades Principales

* **Exploración de Datos:** Permite a los usuarios filtrar el dataset por país, marca y estilo de ramen utilizando widgets interactivos.
* **Visualizaciones:** Genera gráficos informativos utilizando Plotly para mostrar la distribución de ratings y el rating promedio por país.
* **Resumen de Datos:** Presenta métricas clave como el rating promedio general, el ramen mejor calificado y el país con el rating promedio más alto.
* **Ramen Aleatorio:** Ofrece la posibilidad de descubrir un ramen al azar del dataset.
* **Diccionario de Ramen:** Contiene una página con definiciones de términos comunes y descripciones de estilos populares de ramen.
* **Exploración por País:** Permite seleccionar un país desde un menú desplegable para ver estadísticas específicas sobre los ramen de esa región (número de reseñas, rating promedio, marcas y estilos más populares, y ejemplos de ramen mejor calificados). Se incluye un mapa mundial como contexto visual.
* **Personalización de Tema:** Los usuarios pueden elegir entre un tema claro y un tema oscuro para la interfaz de la aplicación.

## Tecnologías Utilizadas

* **Streamlit:** Para la creación rápida y sencilla de la interfaz web interactiva.
* **Python:** El lenguaje de programación principal.
* **Pandas:** Para la manipulación y el análisis de datos tabulares.
* **Plotly Express:** Para la generación de gráficos interactivos.
* **PIL (Pillow):** Para la manipulación de imágenes (logo).
* **io (StringIO):** Para el manejo de datos en memoria (descarga de CSV).

## Cómo Ejecutar la Aplicación

1.  **Clona este repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO>
    cd streamlit-ramen-explorer
    ```
    Reemplaza `<URL_DE_TU_REPOSITORIO>` con la URL real de tu repositorio en GitHub.

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    Asegúrate de haber creado el archivo `requirements.txt` con las librerías necesarias (puedes generarlo con `pip freeze > requirements.txt` en tu entorno local).

4.  **Ejecuta la aplicación Streamlit:**
    ```bash
    streamlit run Inicio.py
    ```
    Esto debería abrir la aplicación en tu navegador web en `http://localhost:8501`.

## Estructura de Archivos
