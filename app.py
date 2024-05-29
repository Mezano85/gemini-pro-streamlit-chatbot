import streamlit as st 
from pathlib import Path

# Streamlit multi-paginas
from st_pages import show_pages_from_config
show_pages_from_config()

# Contenido de la página
st.title("Detalle del Proyecto")
st.write(
    """
        ## Hola!
        
        Mi nombre es Francisco y me encuentro desarrollando este proyecto
        con la finalidad de aprender el uso de la herramienta **Streamlit**
        creo que esta es la mejor forma de conservar notas y compartir conocimiento
        a futuras personas que se quieran ver beneficiadas con esta herramienta.
        
        Intentaré dejar las paginas del proyecto lo mejor explicadas,
        pero es posible que como aprendiz algunas secciones las omita por desconocimiento
        o por la evolución de Streamlit se tengan nuevas funcionalidades. Eres 
        bienvenido a aportar al proyecto cuando gustes, estaré atento a la recepción de cambios.
        
        No pretende ser un mega-tutorial de streamlit. La documentación que tiene la herramienta 
        es muy buena, más bien la idea es tener una especie de notas (chuletillas) para busqueda rápida
        de algún tema... considerando tambien que existen varias formas de hacer lo mismo
        colocaré aquí solo las situaciones que se me hagan más convenientes tratando de que cada sección 
        quede explicada lo más simple posible.
    """
)
st.write(
    """
        ## Código
        
        La forma de acomodar el repocitorio será por páginas de streamlit, cada página será
        breve y enfocada a una funcionalidad específica. Dentro del contenido de la página se 
        describirá la funcionalidad y adicional, en todas las paginas agregaremos una referencia 
        al mismo codigo que la genera.
    """
)
