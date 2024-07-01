import pyodbc
import streamlit as st
import pandas as pd

driver = st.secrets["driver"]
server = st.secrets["server"]
database = st.secrets["database"]
username = st.secrets["username"]
password = st.secrets["password"]

def get_theseus_data():
    query = "SELECT toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df;


def get_ta_lkm():
    query = "SELECT toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df;

def get_julkaisupäivä():
    query = "SELECT julkaisupäivä FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df;

def get_theseus_data_keywords():
    query = "SELECT id, julkaisupäivä, avainsanat FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df;

def get_kielilkm():
    query = "SELECT kieli FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df;

def get_ko_top10():
    query = "SELECT koulutusohjelma FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df;

def get_ot_lkm_ol():
    query = "SELECT oppilaitos, id FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_sanapilvi():
    query = "SELECT avainsanat FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_sanapilvi_ka():
    query = "SELECT koulutusala_fi FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_tk_tm():
    query = "SELECT koulutusala_fi, toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_top10_tmk():
    query = "SELECT koulutusala_fi, toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df
