import streamlit as st
import random
import time
from gtts import gTTS
import base64
from pathlib import Path

st.set_page_config(layout="wide")

# ---------- FUNÇÃO DE SOM ----------
def tocar_audio(texto):
    tts = gTTS(text=texto, lang="pt-br")
    arquivo = "som.mp3"
    tts.save(arquivo)
    audio_file = open(arquivo, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

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
h1, h2, h3 {
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

# ---------- FASE 1 ----------
if st.session_state.fase == "consoante":

    letras = [consoante, vogal]
    random.shuffle(letras)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(letras[0]):
            if letras[0] in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
                time.sleep(2)
                st.rerun()
            else:
                st.session_state.fase = "vogal"
                st.rerun()

    with col2:
        if st.button(letras[1]):
            if letras[1] in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
                time.sleep(2)
                st.rerun()
            else:
                st.session_state.fase = "vogal"
                st.rerun()

# ---------- FASE 2 ----------
elif st.session_state.fase == "vogal":

    st.header(f"CONSOANTE ESCOLHIDA: {consoante}")
    st.write("### AGORA CLIQUE NA VOGAL")

    col1, col2 = st.columns(2)

    # CLICOU CERTO → MOSTRA SÍLABA + SOM
    with col1:
        if st.button(vogal):
            st.balloons()

            st.markdown(f"<h1 style='font-size:120px'>{silaba}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h2> {silaba} DE {palavra} </h2>", unsafe_allow_html=True)

            tocar_audio(silaba)        # 🔊 SOM DA SÍLABA
            time.sleep(4)

            st.session_state.silaba_atual = random.choice(list(silabas.keys()))
            st.session_state.fase = "consoante"
            st.rerun()

    # CLICOU ERRADO
    with col2:
        if st.button(consoante):
            st.error("ESSA NÃO É A VOGAL 😢")
            time.sleep(2)
            st.rerun()
