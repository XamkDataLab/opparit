import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re
from datanhaku import *

st.write("Terve maailma!")

df = get_theseus_data()
st.dataframe(df)

df = get_ot_lkm_ol()
df["oppilaitos"] = df["oppilaitos"].replace("Karelia-ammattikorkeakoulu (Pohjois-Karjalan ammattikorkeakoulu)", "Karelia-ammattikorkeakoulu")
st.subheader('Opinnäytetöiden määrä oppilaitoksittain')
opinnäytetyöt_oppilaitoksittain = df.groupby("oppilaitos")["id"].nunique().reset_index()
opinnäytetyöt_oppilaitoksittain = opinnäytetyöt_oppilaitoksittain.sort_values(by="id", ascending=False)
fig, px = plt.subplots(figsize=(10, 5))
px.bar(opinnäytetyöt_oppilaitoksittain["oppilaitos"], opinnäytetyöt_oppilaitoksittain["id"], color=plt.cm.coolwarm(range(len(opinnäytetyöt_oppilaitoksittain))))
px.set_xlabel("Oppilaitos", fontsize=15, color='white')
px.set_ylabel("Opinnäytteiden määrä", fontsize=15, color='white')
px.tick_params(axis='x', rotation=85, labelsize=12, color='white')
px.tick_params(axis='y', labelsize=12, color='white')
fig.patch.set_alpha(0)
px.patch.set_alpha(0)
for label in px.get_yticklabels():
    label.set_color('white')
for label in px.get_xticklabels():
    label.set_color('white')
plt.tight_layout()
st.pyplot(fig)
