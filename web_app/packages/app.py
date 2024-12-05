import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
 #import psycopg2

st.title('Initiation au dashboarding')
st.subheader('Auteur: PAKA Fabrice')
st.subheader('***Introduction***')
st.write("Bienvenu sur mon dashboard! Ce dashboard est un outil de visualisation de données avec streamlit. " )
st.write("***:blue[Ci-dessous un exemple de données a traiter:]***" )

data = np.random.normal(size= 1000)
df = pd.DataFrame(data, columns=['dist_norm'])
st.write(df.head())

st.write('La distribution de ces données se presentent comme suit:')
fig, ax = plt.subplots(figsize= (6,4))
n_bins = st.number_input(label='**Choisisez le nombre de bins**', min_value= 5, value= 5)
df.hist(ax= ax, bins=n_bins)
graph_title = st.text_input(label= '**entrer le titre du graphique**')
plt.title(graph_title)
ax.set_xlabel('distances')
st.pyplot(fig)

st.subheader("***Etude d'un autre jeu de donnees***")

############# Utilisation d'un jeu de données externe #########################

titanic = pd.read_csv('../data/data_titanic.csv')
st.write(titanic.head())


############### Connection de streamlit avec ma base de donnée #####################
conn = st.connection("postgres", type="sql")
df_db = conn.query('SELECT * FROM fabrice_table;', ttl=0)
print(df_db)
for row in df_db.itertuples():
    
    st.write(f"{row}")
   