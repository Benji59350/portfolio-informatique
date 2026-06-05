import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Informatique Facile", page_icon="💻")

# Header
st.title("💻 Votre aide pour l'informatique de base")
st.write("---")

# À propos
st.header("À propos de moi")
st.write("""
Fort de **15 ans d'expérience dans le service client**, dont 5 ans chez **Orange et SFR**, 
j'ai développé une patience et une pédagogie à toute épreuve. 
Mon objectif est de vous rendre autonome, sans jargon technique et avec le sourire.
""")

# Services & Tarifs
st.header("Mes Services")

# Mise en page en colonnes
col1, col2 = st.columns(2)

with col1:
    st.subheader("Démarrage & Connexion")
    st.write("- **Prise en main PC** : 30€ (2h) (Présentiel) ")
    st.write("- **Connexion Wi-Fi/Imprimantes** : 15€ (Présentiel)")

with col2:
    st.subheader("Navigation & Assistance")
    st.write("- **Navigation Web/Mails** : 25€ (Visio) | 35€ (Présentiel)")
    st.write("- **Résolution de lenteurs** : 10€ / heure")

st.info("💡 **Offre spéciale :** Pack Navigation - 5 séances de 2h pour 300€")

# Contact
st.header("📞 Me contacter")
st.write("Intervention sur Saint-André-lez-Lille et alentours (10km).")
st.write("Email : [votre_benji059@outlook.com]")
st.write("Téléphone : [0685341160]")