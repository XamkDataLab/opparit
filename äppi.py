import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re
from datanhaku import *


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


df = get_julkaisupäivä()
df['julkaisupäivä'] = pd.to_datetime(df['julkaisupäivä'], format='%Y-%m-%d %H.%M.%S.%f')

df['julkaisupäivä'] = df['julkaisupäivä'].dt.normalize()

df['vuosi'] = df['julkaisupäivä'].dt.year
df['kuukausi'] = df['julkaisupäivä'].dt.month
df['julkaisupäivä'] = df['julkaisupäivä'].dt.strftime('%d-%m-%Y')

df = get_ta_lkm()
st.subheader('Opinnäytetyöt joista löytyy ja joista puuttuu toimeksiantajatieto.')
toimeksiantaja_lkm = df["toimeksiantaja"].notna().value_counts()
labels = ["Toimeksiantaja löytyy", "Toimeksiantaja puuttuu"]
values = [toimeksiantaja_lkm.get(True, 0), toimeksiantaja_lkm.get(False, 0)]

fig = go.Figure(data=[go.Bar(x=labels, y=values, marker_color=['#66c2a5', '#fc8d62'])])
fig.update_layout(
    xaxis_title='Toimeksiantaja',
    yaxis_title='Lukumäärä'
)
st.plotly_chart(fig);

vuosittaiset_toimeksiantajat = df.groupby("vuosi")["toimeksiantaja"].nunique().reset_index()
fig = px.bar(vuosittaiset_toimeksiantajat, x="vuosi", y="toimeksiantaja", 
             labels={"vuosi": "Vuosi", "toimeksiantaja": "Toimeksiantajien määrä"})
st.subheader("Vuosittainen toimeksiantajien määrä")
st.plotly_chart(fig);

df = get_kielilkm()

kieli_muutokset = {
    'fin': 'fi',
    'fi': 'fi',
    'swe': 'sv',
    'sv': 'sv',
    'rus': 'ru',
    'ru': 'ru',
    'en': 'en',
    'eng': 'en',
    'fr': 'fr',
    'fre': 'fr'
}
df["kieli"] = df["kieli"].replace(kieli_muutokset)
df = df[~df['kieli'].isin(["akuuttihoito", 'NULL'])]

kieli_lkm = df["kieli"].value_counts()

suurimmat_kielet = kieli_lkm[kieli_lkm.index.isin(['fi', 'en', 'sv'])]
muut = kieli_lkm[~kieli_lkm.index.isin(['fi', 'en', 'sv'])].sum()
kieli_lkm_yhdistetty = pd.concat([suurimmat_kielet, pd.Series({'muut': muut})])
fig = px.pie(kieli_lkm_yhdistetty, values=kieli_lkm_yhdistetty.values, names=kieli_lkm_yhdistetty.index)
st.subheader('Opinnäytetöissä käytetyt kielet')
st.plotly_chart(fig);

df = get_ko_top10()

Koulutusohjelmat_top15 = df["koulutusohjelma"].value_counts().nlargest(15)
data = Koulutusohjelmat_top15.values
keys = Koulutusohjelmat_top15.index
explode = [0.05] + [0] * (len(keys) - 1)

fig, px = plt.subplots(figsize=(8, 8), facecolor='none')
px.pie(data, autopct='%.1f%%', pctdistance=0.9, explode=explode, shadow=True,
       wedgeprops={'edgecolor': "none"})
px.set_facecolor('none')
px.legend(keys, title="Koulutusohjelmat", loc="center right", bbox_to_anchor=(1.1, 0, 0.5, 1))
st.subheader("Top 15 koulutusohjelmat")
st.pyplot(fig);




