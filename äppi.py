import streamlit as st
import pandas as pd
from datanhaku import *

st.write("Terve maailma!")

df = get_theseus_data()
st.dataframe(df)

df['on_amk'] = df['toimeksiantaja'].str.contains('AMK|ammattikorkea', case=False, na=False)
oppilaitokset = (
    'AMK|ammattikorkea|Centria ammattikorkeakoulu|Diakonia-ammattikorkeakoulu|'
    'HAAGA-HELIA ammattikorkeakoulu|Humanistinen ammattikorkeakoulu|Hämeen ammattikorkeakoulu|'
    'Jyväskylän ammattikorkeakoulu|Kaakkois-Suomen ammattikorkeakoulu|Kajaanin ammattikorkeakoulu|'
    'Karelia-ammattikorkeakoulu|Lab-ammattikorkeakoulu|Lapin ammattikorkeakoulu|Laurea-ammattikorkeakoulu|'
    'Metropolia Ammattikorkeakoulu|Oulun Ammattikorkeakoulu|Satakunnan ammattikorkeakoulu|'
    'Savonia-ammattikorkeakoulu|Seinäjoen ammattikorkeakoulu|Tampereen ammattikorkeakoulu|'
    'Turun ammattikorkeakoulu|Vaasan ammattikorkeakoulu|Yrkeshögskolan Arcada|Yrkeshögskolan Novia'
)

df['on_amk'] = df['toimeksiantaja'].str.contains(oppilaitokset, case=False, na=False)

st.subheader('Isoimmat toimeksiantajat')
on_amk = st.selectbox('On AMK:', options=[True, False])
def plot_pie(on_amk):
    filtteri = df[df["on_amk"] == on_amk]
    Eniten_toimeksiantoja = filtteri["toimeksiantaja"].value_counts().nlargest(15)
    data = Eniten_toimeksiantoja.values
    keys = Eniten_toimeksiantoja.index

fig = go.Figure(go.Pie(
    labels=keys,
    values=data,
    hole=.3,
    hoverinfo="label+percent+value",
    textinfo="label+percent",
    marker=dict(line=dict(color='white', width=2)),
    pull=[0.08] + [0] * 14
))
st.plotly_chart(fig)
plot_pie(on_amk)
