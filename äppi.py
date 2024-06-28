import streamlit as st
import pandas as pd
from datanhaku import *

st.write("Terve maailma!")

df = get_theseus_data()
st.dataframe(df)
