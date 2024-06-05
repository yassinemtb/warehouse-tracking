import streamlit as st
import pandas as pd
import numpy as np
import time

# Configuration de la page
st.set_page_config(
    page_title="Interface de gestion d'inventaire",
    page_icon="📦",
    layout="wide",
)

# Titre de la page
st.title("Interface de gestion d'inventaire")

# Création de conteneurs pour les différentes sections
placeholder = st.empty()

# Simulation des données de capteurs
def get_sensor_data():
    data = {
        'timestamp': pd.Timestamp.now(),
        'temperature': round(np.random.uniform(20, 30), 2),
        'humidity': round(np.random.uniform(30, 50), 2),
        'motion_detected': np.random.choice([True, False])
    }
    return data

# Stockage initial des données
data = pd.DataFrame([get_sensor_data()])

# Boucle pour mise à jour des données en temps réel
while True:
    new_data = pd.DataFrame([get_sensor_data()])
    data = pd.concat([data, new_data], ignore_index=True)
    
    with placeholder.container():
        st.subheader("Données des capteurs")
        
        # Affichage des données de capteurs
        st.write(data.tail(1))
        
        # Graphiques
        st.subheader("Graphiques en temps réel")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.line_chart(data[['timestamp', 'temperature']].set_index('timestamp'))
        
        with col2:
            st.line_chart(data[['timestamp', 'humidity']].set_index('timestamp'))
        
        st.subheader("Détection de mouvement")
        st.write("Mouvement détecté: ", data['motion_detected'].iloc[-1])
        
    time.sleep(2)
