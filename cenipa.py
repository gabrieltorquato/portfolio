# importar bibliotecas
import streamlit as st
import pandas as pd
import pydeck as pdk


DATA_URL = "https://raw.githubusercontent.com/carlosfab/curso_data_science_na_pratica/master/modulo_02/ocorrencias_aviacao.csv"
st.set_page_config(page_title="Dashboard - CENIPA", page_icon="✈️", layout="centered", initial_sidebar_state="auto", menu_items=None)

@st.cache
def load_data():
    """
    Carrega os dados de ocorrências aeronáuticas do CENIPA.

    :return: DataFrame com colunas selecionadas.
    """
    columns = {
        'ocorrencia_latitude': 'latitude',
        'ocorrencia_longitude': 'longitude',
        'ocorrencia_dia': 'data',
        'ocorrencia_classificacao': 'classificacao',
        'ocorrencia_tipo': 'tipo',
        'ocorrencia_tipo_categoria': 'tipo_categoria',
        'ocorrencia_tipo_icao': 'tipo_icao',
        'ocorrencia_aerodromo': 'aerodromo',
        'ocorrencia_cidade': 'cidade',
        'ocorrencia_uf': 'estado',
        'investigacao_status': 'status',
        'divulgacao_relatorio_numero': 'relatorio_numero',
        'total_aeronaves_envolvidas': 'aeronaves_envolvidas'
    }

    data = pd.read_csv(DATA_URL, index_col='codigo_ocorrencia')
    data = data.rename(columns=columns)
    data.data = data.data + " " + data.ocorrencia_horario
    data.data = pd.to_datetime(data.data)
    data = data[list(columns.values())]

    return data


# carregar os dados
df = load_data()
labels = df.classificacao.unique().tolist() #busca de todos tipos de classificação no df
labels2 = df.estado.unique().tolist() #busca de todos estados presentes no df

# SIDEBAR
# Parâmetros e número de ocorrências
st.sidebar.header("Parâmetros")
info_sidebar = st.sidebar.empty()    # placeholder, para informações filtradas que só serão carregadas depois

# Slider de seleção do ano
st.sidebar.subheader("Ano")
year_to_filter = st.sidebar.slider('Escolha o ano desejado', 2008, 2018, 2017)

# Checkbox da Tabela
st.sidebar.subheader("Tabela")
tabela = st.sidebar.empty()    # placeholder que só vai ser carregado com o df_filtered

# Multiselect com os labels únicos dos tipos de classificação
label_to_filter = st.sidebar.multiselect(
    label="Escolha a classificação da ocorrência",
    options=labels,
    default=["INCIDENTE", 'ACIDENTE']
)

# Multiselect com os lables únicos dos estados
estados_filtro = st.sidebar.multiselect(
    label="Escolha o estado da ocorrência",
    options=labels2,
    default=['RO', 'AC','AM','RR','PA','AP','TO','MA','PI','CE',
             'RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP',
             'PR','SC','RS','MS','MT','GO','DF',]
)


# Informação no rodapé da Sidebar
st.sidebar.markdown("""
A base de dados de ocorrências aeronáuticas é gerenciada pelo ***Centro de Investigação e Prevenção de Acidentes 
Aeronáuticos (CENIPA)***.
""")
st.sidebar.markdown("""
Meus contatos:\n
[Portfolio](https://github.com/gabrieltorquato/portfolio)\n
[Linkedin](https://www.linkedin.com/in/gabrieltorquato/)
""")

# Somente aqui os dados filtrados por ano são atualizados em novo dataframe
filtered_df = df[(df.data.dt.year == year_to_filter) & (df.classificacao.isin(label_to_filter)) & (df.estado.isin(estados_filtro))]

# Aqui o placehoder vazio finalmente é atualizado com dados do filtered_df
info_sidebar.info("{} ocorrências selecionadas.".format(filtered_df.shape[0]))


# MAIN
st.title("CENIPA - Acidentes Aeronáuticos")
st.markdown(f"""
            ℹ️ Estão sendo exibidas as ocorrências classificadas como **{", ".join(label_to_filter)}**
            para o ano de **{year_to_filter}**.
            """)

# raw data (tabela) dependente do checkbox
if tabela.checkbox("Mostrar tabela de dados"):
    st.write(filtered_df)


# mapa
st.subheader("Mapa de ocorrências")
st.map(filtered_df)
