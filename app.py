import streamlit as st
import random
import time

st.set_page_config(layout="wide")

# ---------- ESTILO BOTÕES GIGANTES ----------
st.markdown("""
<style>
div.stButton > button {
    height: 200px;
    width: 200px;
    font-size: 60px !important;
    font-weight: bold;
    border-radius: 25px;
}
h1, h2, h3, p {
    text-align: center;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- BANCO DE SÍLABAS ----------
silabas = {
"BA":"BANANA","BE":"BETERRABA","BI":"BISCOITO","BO":"BOLO","BU":"BURRITO",
"CA":"CAMARÃO","CE":"CEBOLA","CO":"COGUMELO","CU":"CUSCUZ",
"DA":"DAMASCO","DO":"DOCE",
"FA":"FAROFA","FE":"FEIJÃO","FI":"FIGO","FO":"FOGÃO",
"GA":"GALINHA","GE":"GELO","GO":"GOIABA",
"JA":"JACA","JI":"JILÓ",
"LA":"LARANJA","LE":"LEITE","LI":"LIMÃO","LU":"LULA",
"MA":"MACARRÃO","ME":"MEL","MI":"MIOJO","MO":"MOLHO",
"PA":"PAÇOCA","PE":"PEPINO","PI":"PIPOCA","PO":"PORCO","PU":"PURÊ",
"RA":"RABANETE","RI":"RICOTA","RO":"ROMÃ",
"SA":"SALADA","SO":"SOPA",
"TA":"TABULE"
}

vogais = ["A","E","I","O","U"]

# ---------- ESTADOS ----------
if "fase" not in st.session_state:
    st.session_state.fase = "consoante"
    st.session_state.silaba_atual = random.choice(list(silabas.keys()))

silaba = st.session_state.silaba_atual
palavra = silabas[silaba]
consoante = silaba[0]
vogal = silaba[1]

# ---------- TÍTULO ----------
st.title("VAMOS FORMAR SÍLABAS!")
st.write("### CLIQUE PRIMEIRO NA CONSOANTE")

st.write("")
st.write("")

# ---------- FASE 1: ESCOLHER CONSOANTE ----------
if st.session_state.fase == "consoante":

    letras = [consoante, vogal]
    random.shuffle(letras)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(letras[0]):
            clique = letras[0]

            # ERRO → clicou vogal
            if clique in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
                time.sleep(2)
                st.rerun()

            # ACERTO → consoante correta
            else:
                st.session_state.fase = "vogal"
                st.rerun()

    with col2:
        if st.button(letras[1]):
            clique = letras[1]

            if clique in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
                time.sleep(2)
                st.rerun()
            else:
                st.session_state.fase = "vogal"
                st.rerun()

# ---------- FASE 2: ESCOLHER VOGAL ----------
elif st.session_state.fase == "vogal":

    st.header(f"CONSOANTE ESCOLHIDA: {consoante}")
    st.write("### AGORA CLIQUE NA VOGAL")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(vogal):
            st.success(f"🎉 {silaba} DE {palavra}")
            time.sleep(3)

            st.session_state.silaba_atual = random.choice(list(silabas.keys()))
            st.session_state.fase = "consoante"
            st.rerun()

    with col2:
        if st.button(consoante):
            st.error("ESSA NÃO É A VOGAL 😢")
            time.sleep(2)
            st.rerun()
