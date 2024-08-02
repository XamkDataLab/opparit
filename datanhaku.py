import pyodbc
import streamlit as st
import pandas as pd

driver = st.secrets["driver"]
server = st.secrets["server"]
database = st.secrets["database"]
username = st.secrets["username"]
password = st.secrets["password"]

def get_julkaisupaiva():
    query = "SELECT julkaisupäivä FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df
    
def get_toimeksiantaja_oppilaitos():
    query = "SELECT toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_poistettavatyritykset():
    query = "SELECT toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_oppilaitos_ta():
    query = "SELECT toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_kielet():
    query = "SELECT kieli FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis1():
    query = "SELECT toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis2():
    query = "SELECT oppilaitos, toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis3():
    query = "SELECT julkaisupäivä, toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis4():
    query = "SELECT toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis5():
    query = "SELECT koulutusala_fi, toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis6():
    query = "SELECT koulutusala_fi, toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis7():
    query = "SELECT julkaisupäivä, toimeksiantaja FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis8():
    query = "SELECT koulutusohjelma, oppilaitos FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis9():
    query = "SELECT oppilaitos, id FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis10():
    query = "SELECT koulutusala_fi FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis11():
    query = "SELECT oppilaitos, julkaisupäivä, id FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis12():
    query = "SELECT koulutusala_fi, kieli FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis13():
    query = "SELECT kieli FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis14():
    query = "SELECT avainsanat FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis15():
    query = "SELECT oppilaitos FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis16():
    query = "SELECT oppilaitos, koulutusala_fi, id FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis17():
    query = "SELECT julkaisupäivä, id, kieli FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis18():
    query = "SELECT julkaisupäivä, id FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis19():
    query = "SELECT julkaisupäivä, tiivistelmä1 FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis20():
    query = "SELECT julkaisupäivä, id FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis21():
    query = "SELECT julkaisupäivä, oppilaitos FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis22():
    query = "SELECT julkaisupäivä, tiivistelmä1 FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df

def get_vis23():
    query = "SELECT julkaisupäivä, id, kieli FROM theseusAMK;"
    with pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}') as conn:
        df = pd.read_sql(query, conn)
    return df
