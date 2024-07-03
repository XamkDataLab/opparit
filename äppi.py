import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re
from streamlit_option_menu import option_menu
from datanhaku import *
#----------------
st.title('TheseusAMK visualisointi')
valinnat = option_menu(None, ["Toimeksiannot", 'Koulutusohjelmat', 'Muut'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#13a872"},
        "icon": {"color": "orange", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#45a240", "padding": "10px 20px"},
        "nav-link-selected": {"background-color": "#5ed9ac"},
    }
)

df = get_toimeksiantaja_oppilaitos()

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

df = get_poistettavatyritykset()

poistettavat_arvot = [
        'Anonyymi yritys', 'Anonyymit Yritys A ja Yritys B', 'Case yritys X', 'Case-yritys', 'Case-yritys Oy',
        'Fysioterapiayritys X', 'IT- ja taloushallinnon palveluita tarjoava yritys', 'Kiinteistönvälitysyritys X',
        'Kohdeyritys', 'Kohdeyritys Oy', 'Kuljetusyritys', 'Kunnossapitoyritys', 'Luottamuksellinen yritys',
        'LVI-suunnitteluyritys', 'LVIS-yritys', 'Markkinatutkimusyritys (salainen)', 'Metallialan yritys',
        'Metalliteollisuuden yritys', 'Metalliteollisuusalan yritys', 'Nimetön, suomalainen palkanlaskentayritys',
        'OP:n tilaajayritys X', 'Oululainen tarkkuusmekaniikkayritys', 'Suomessa toimiva finanssialan yritys',
        'Tanssialan yritys', 'Teknologiayritys', 'Tilintarkastusyhteisö Yritys X', 'Tuntematon yritys',
        'Työasujen jälleenmyyntiyritys (yritys x)', 'Yritys A', 'Yritys Oy', 'Yritys Oy (nimi muutettu)', 'Yritys X',
        'Yritys X (Salattu yritys)', 'Yritys X / päivittäistavarakaupan tulosyksikkö Jyväskylässä', 'Yritys X Oy',
        'YritysX', 'Osakeyhtiö X', 'Vakuutusyhtiö X', 'Yhdistys X', 'xxxx', 'X', 'X company', 'X Oy',
        'Tilintarkastusyhteisö Yritys X', 'Tilitoimisto X', 'Tilitoimisto X Oy', 'Tilitoimisto X Tmi', 'Rakennusliike X',
        'Pikaruokaravintola x', 'Perheyhteisö X', 'Parturi-kampaaja X Tmi', 'Pankki X', 'Palvelinkeskus x',
        'Osakeyhtiö X', 'Organisaatio X', 'Organisation X', 'Organization X', 'Marjatila x', 'Kaupunki X',
        'Insinööritoimisto X', 'Finanssialan toimija X', 'Ehdokas X', 'Company X', 'Case company X',
        'Asiantuntijaorganisaatio X', 'Salainen', 'Urheiluseura (salainen)', 'Nimeltä mainitsematon henkilöautokorjaamo',
        'Ei mainita', 'nimetön', 'yhteistyöpäiväkoti (salattu)', 'Tilaajan tiedot salattuja', 'Toimeksiantajan tiedot salattu',
        'Salassa pidettävä', 'Anonym uppdragsgivare', 'Anonyymi', 'Anonyymi hankeorganisaatio', 'Anonyymi toimeksiantaja',
        'Case Anonymous', 'Nimettömänä pysyttelevä taho', 'Toimeksiantajaa ei nimetä',
        'yksityinen henkilö -jo toimivan yrityksen nimeen.', 'A case company', 'An engineering company',
        'Oma aihe', 'Confidential', 'Yksityinen henkilö', 'Yksityinen metsäomistaja', 'Ei ole', 'Case company X', 'Company Y',
        'Yksityinen', 'Yksityinen asiakas', 'Yksityinen palveluasumisen yksikkö', 'Yksityinen taho', 'Yksityinen tilaaja',
        'Yksityinen toimeksiantaja', 'Yksityinen toimija', 'Yksityinen työterveyshuollon organisaatio',
        'Yksityinen lääkäriasema', 'Yksityinen lastenkoti Etelä-Suomessa', 'Yksityinen lastensuojelulaitos',
        'Yksityinen lastensuojeluyksikkö', 'Ei mainita', 'Anonym uppdragsgivare', 'Eräs Etelä-Suomessa sijaitseva päiväkoti (salassapidettävä)'
        'Markkinatutkimusyritys (salainen)', '-', '*', 'Eräs Pirkanmaan sairaanhoitopiirin yksikkö', 'Eräs pohjoissavolainen perusterveydenhuollon päivystys'
        'Yksityishenkilö', 'Yksityisyrittäjänä toimiva psykoterapeutti']

df = df[~df['toimeksiantaja'].isin(poistettavat_arvot)]

df = get_oppilaitos_ta()

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

df = get_kielet()

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

#-----------------------
if valinnat == "Toimeksiannot":
    df = get_vis1()
    toimeksiantaja_lkm = df["toimeksiantaja"].notna().value_counts()
    labels = ["Toimeksiantaja löytyy", "Toimeksiantaja puuttuu"]
    values = [toimeksiantaja_lkm.get(True, 0), toimeksiantaja_lkm.get(False, 0)]

    fig = go.Figure(data=[go.Bar(x=labels, y=values, marker_color=['#66c2a5', '#fc8d62'])])
    fig.update_layout(
        xaxis_title='Toimeksiantaja',
        yaxis_title='Lukumäärä'
    )
    st.title('TheseusAMK visualisointi')
    st.subheader('Opinnäytetyöt joista löytyy ja joista puuttuu toimeksiantajatieto.')
    st.plotly_chart(fig)

    df = get_vis2()
    df["oppilaitos"] = df["oppilaitos"].replace(
        "Karelia-ammattikorkeakoulu (Pohjois-Karjalan ammattikorkeakoulu)", 
        "Karelia-ammattikorkeakoulu"
    )
    opl_tma = df.dropna(subset=["toimeksiantaja"])
    toimeksiantajat_oppilaitoksittain = opl_tma["oppilaitos"].value_counts()
    
    fig2 = go.Figure(data=[go.Bar(
        x=toimeksiantajat_oppilaitoksittain.index,
        y=toimeksiantajat_oppilaitoksittain.values,
        marker_color='teal'
    )])

    fig2.update_layout(
        xaxis={'tickangle': -90}
    )
    st.subheader('Toimeksiantajien määrä oppilaitoksittain')
    st.plotly_chart(fig2)

    df = get_vis3()
    vuosittaiset_toimeksiantajat = df.groupby("vuosi")["toimeksiantaja"].nunique().reset_index()
    fig = px.bar(vuosittaiset_toimeksiantajat, x="vuosi", y="toimeksiantaja", 
              labels={"vuosi": "Vuosi", "toimeksiantaja": "Toimeksiantajien määrä"})
    st.subheader("Vuosittainen toimeksiantajien määrä")
    st.plotly_chart(fig)

    df = get_vis4()
    st.subheader('Isoimmat toimeksiantajat')
    on_amk = st.selectbox('On AMK:', options=[True, False], key='on_amk_selectboxi')
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


    df = get_vis5()
    filtteri = df[(df["koulutusala_fi"] == "Tietojenkäsittely") & (df["on_amk"] == False)]
    ala10_toimeksiantajat = filtteri["toimeksiantaja"].value_counts().head(10).reset_index()
    ala10_toimeksiantajat.columns = ["toimeksiantaja", "count"]
    fig = go.Figure(go.Bar(
        x=ala10_toimeksiantajat["count"],
        y=ala10_toimeksiantajat["toimeksiantaja"],
        orientation='h',
        marker=dict(color=ala10_toimeksiantajat["count"], colorscale='dense')
    ))
    fig.update_layout(
        xaxis_title="Toimeksiantojen määrä",
        yaxis_title="Toimeksiantaja",
        yaxis=dict(autorange='reversed'),
        template='plotly_dark'
    )
    st.subheader("Tietojenkäsittely koulutuksen 10 suurinta toimeksiantajaa")
    st.plotly_chart(fig)

    df = get_vis6()
    st.subheader("10 suurinta toimeksiantajaa koulutuksen mukaan")
    koulutusala = st.selectbox("Valitse koulutusala", df["koulutusala_fi"].unique())
    def int_kokeilu(koulutusala):
            filtteri = df[(df["koulutusala_fi"] == koulutusala) & (df['on_amk'] == False)]
            ala10_toimeksiantajat = filtteri["toimeksiantaja"].value_counts().head(10).reset_index()
            ala10_toimeksiantajat.columns = ["toimeksiantaja", "count"]    
            fig = go.Figure(go.Bar(
            x=ala10_toimeksiantajat["count"],
            y=ala10_toimeksiantajat["toimeksiantaja"],
            orientation='h',
            marker=dict(color=ala10_toimeksiantajat["count"], colorscale='inferno')
        ))

            fig.update_layout(
            xaxis_title="Toimeksiantojen määrä",
            yaxis_title="Toimeksiantaja",
            yaxis=dict(autorange='reversed'),
            xaxis=dict(type='linear'),
            template='plotly_white'
        )
            st.plotly_chart(fig)
    int_kokeilu(koulutusala)



    df = get_vis7()
    st.subheader('Eniten toimeksiantoja vuosittain')
    vuodet = [year for year in range(2019, 2024)]
    year = st.slider('Valitse vuosi', min_value=min(vuodet), max_value=max(vuodet), step=1, value=min(vuodet))
    def plot_top_10_toimeksiantajat(year):
            filtteri = df[(df["vuosi"] == year) & (df["on_amk"] == False)]
            toimeksiantajat19_23 = filtteri["toimeksiantaja"].value_counts().head(10).reset_index()
            toimeksiantajat19_23.columns = ["toimeksiantaja", "count"]
            fig = go.Figure(go.Bar(
                x=toimeksiantajat19_23["count"],
                y=toimeksiantajat19_23["toimeksiantaja"],
                orientation='h',
                marker=dict(color=toimeksiantajat19_23["count"], colorscale='inferno')
        ))

            fig.update_layout(
            title=f'Eniten toimeksiantoja vuonna {year}',
            xaxis_title="Toimeksiantojen määrä",
            yaxis_title="Toimeksiantaja",
            template='plotly_white'
        )

            st.plotly_chart(fig)
    plot_top_10_toimeksiantajat(year)

#-----------------------

elif valinnat == "Koulutusohjelmat & oppilaitokset":
    df = get_vis8()
    Koulutusohjelmat_top15 = df["koulutusohjelma"].value_counts().nlargest(15)
    data = Koulutusohjelmat_top15.values
    keys = Koulutusohjelmat_top15.index
    explode = [0.05] + [0] * (len(keys) - 1)

    fig, px = plt.subplots(figsize=(8, 8), facecolor='none')
    px.pie(data, autopct='%.1f%%', pctdistance=0.9, explode=explode, shadow=True,
       wedgeprops={'edgecolor': "none"})
    px.set_facecolor('none')
    px.legend(keys, title="Koulutusohjelmat", loc="center right", bbox_to_anchor=(1.1, 0, 0.5, 1))
    st.subheader("15 suosituinta koulutusohjelmaa")
    st.pyplot(fig)

    df = get_vis9()
    st.subheader('Opinnäytetöiden määrä oppilaitoksittain')
    opinnäytetyöt_oppilaitoksittain = df.groupby("oppilaitos")["id"].nunique().reset_index()
    opinnäytetyöt_oppilaitoksittain = opinnäytetyöt_oppilaitoksittain.sort_values(by="id", ascending=False)
    fig3, px = plt.subplots(figsize=(12, 7))
    px.bar(opinnäytetyöt_oppilaitoksittain["oppilaitos"], opinnäytetyöt_oppilaitoksittain["id"], color=plt.cm.coolwarm(range(len(opinnäytetyöt_oppilaitoksittain))))
    px.set_xlabel("Oppilaitos", fontsize=15, color='white')
    px.set_ylabel("Opinnäytteiden määrä", fontsize=15, color='white')
    px.tick_params(axis='x', rotation=85, labelsize=12, color='white')
    px.tick_params(axis='y', labelsize=12, color='white')
    fig3.patch.set_alpha(0)
    px.patch.set_alpha(0)
    for label in px.get_yticklabels():
        label.set_color('white')
    for label in px.get_xticklabels():
        label.set_color('white')
    plt.tight_layout()
    st.pyplot(fig3)


    df = get_vis10()
    teksti = df["koulutusala_fi"].str.cat(sep=' ')
    plt.rcParams["figure.figsize"] = (10,15)
    stopwords = ["ja"]
    wordcloud = WordCloud(max_font_size = 50, max_words = 75, background_color = "white", colormap = "Blues", stopwords=stopwords).generate(teksti)
    plt.plot()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    st.subheader("Koulutusalojen sanapilvi")
    st.pyplot(plt)

    df = get_vis11()
    st.subheader('Opinnäytetöiden määrä oppilaitoksittain')
    vuodet = [year for year in range(2008, 2024)]
    year = st.slider('Valitse vuosi', min_value=min(vuodet), max_value=max(vuodet), step=1, value=min(vuodet))
    def plot_opinnäytetyöt_oppilaitoksittain(year):
            filtteri = df[df["vuosi"] == year]
            opinnäytetyöt_oppilaitoksittain = filtteri.groupby("oppilaitos")["id"].nunique().reset_index()
            opinnäytetyöt_oppilaitoksittain = opinnäytetyöt_oppilaitoksittain.sort_values(by="id", ascending=False).head(10)

            fig = go.Figure(go.Bar(
            x=opinnäytetyöt_oppilaitoksittain["id"],
                y=opinnäytetyöt_oppilaitoksittain["oppilaitos"],
                orientation='h',
                marker=dict(color=opinnäytetyöt_oppilaitoksittain["id"], colorscale='Viridis')
        ))
            fig.update_layout(
        title=f'Opinnäytetöiden määrä oppilaitoksittain vuonna {year}',
        xaxis_title="Opinnäytteiden määrä",
        yaxis_title="Oppilaitos",
        yaxis=dict(autorange='reversed'),
        template='plotly_white'
        )
            st.plotly_chart(fig)
    plot_opinnäytetyöt_oppilaitoksittain(year)



    df = get_vis12()
    st.subheader('Suosituimmat koulutusalat kielen mukaan')
    kielet = df["kieli"].unique()
    kieli = st.selectbox('Valitse kieli', options=kielet)

    def plot_top_10_koulutusalat(kieli):
            filtteri = df[df["kieli"] == kieli]
            top_10_koulutusalat = filtteri["koulutusala_fi"].value_counts().head(10).reset_index()
            top_10_koulutusalat.columns = ["koulutusala_fi", "count"]
            fig = go.Figure(go.Bar(
        x=top_10_koulutusalat["count"],
        y=top_10_koulutusalat["koulutusala_fi"],
        orientation='h',
        marker=dict(color=top_10_koulutusalat["count"], colorscale='Bluered')
    ))

            fig.update_layout(
        title=f'Suosituimmat koulutusalat kielellä {kieli}',
        xaxis_title="Suoritetuttujen opinnäytetöiden määrä",
        yaxis_title="Koulutusala",
        yaxis=dict(autorange='reversed'),
        template='plotly_white'
    )

            st.plotly_chart(fig)
    plot_top_10_koulutusalat(kieli)

#-----------------------

elif valinnat == "Muut":
    df = get_vis13()
    kieli_lkm = df["kieli"].value_counts()
    suurimmat_kielet = kieli_lkm[kieli_lkm.index.isin(['fi', 'en', 'sv'])]
    muut = kieli_lkm[~kieli_lkm.index.isin(['fi', 'en', 'sv'])].sum()
    kieli_lkm_yhdistetty = pd.concat([suurimmat_kielet, pd.Series({'muut': muut})])
    fig = px.pie(kieli_lkm_yhdistetty, values=kieli_lkm_yhdistetty.values, names=kieli_lkm_yhdistetty.index)
    st.subheader('Opinnäytetöissä käytetyt kielet')
    st.plotly_chart(fig)

    df = get_vis14()
    from wordcloud import WordCloud, STOPWORDS
    teksti = df['avainsanat'].str.cat(sep=' ').replace("'", "")
    wordcloud = WordCloud(max_font_size=50, max_words=75, background_color="white", colormap="CMRmap", stopwords=STOPWORDS).generate(teksti)
    plt.figure(figsize=(10, 15))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    st.subheader("Avainsanojen sanapilvi")
    st.pyplot(plt)
    
#----------------

def clean_company_name(name):
    stopwords = ['oy', 'ab', 'ky', 'oyj', 'gmbh', 'ltd', 'rf', 'seura', 'ry', 
                 'r y', 'inc', 'corp', 'oy ab', 'ltd oy', 'plc',
                'llc', 'corporation']
    name = str(name).lower()
    name = re.sub(r'[^a-z0-9åäöü]', ' ', name)
    name = re.sub(r' {2,}', ' ', name)
    name = re.sub(r'(\b' + r'\b|\b'.join(stopwords) + r'\b)$', '', name)
    return name.strip()
df['toimeksiantaja'] = df['toimeksiantaja'].apply(clean_company_name)

