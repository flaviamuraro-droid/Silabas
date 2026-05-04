import streamlit as st
import random
from gtts import gTTS
from io import BytesIO

st.set_page_config(layout="wide")

SILABAS = [
"BA","BE","BI","BO","BU",
"CA","CE","CO","CU",
"DA","DO",
"FA","FE","FI","FO",
"GA","GE","GO",
"JA","JI",
"LA","LE","LI","LU",
"MA","ME","MI","MO",
"PA","PE","PI","PO","PU",
"RA","RI","RO",
"SA","SO",
"TA"
]

COMIDAS = {
"BA":"🍌 BANANA","BE":"🥗 BETERRABA","BI":"🍪 BISCOITO","BO":"🎂 BOLO","BU":"🌯 BURRITO",
"CA":"🍤 CAMARÃO","CE":"🧅 CEBOLA","CO":"🍄 COGUMELO","CU":"🍚 CUSCUZ",
"DA":"🍑 DAMASCO","DO":"🍬 DOCE",
"FA":"🍛 FAROFA","FE":"🫘 FEIJÃO","FI":"🍈 FIGO","FO":"🍳 FOGÃO",
"GA":"🍗 GALINHA","GE":"🧊 GELO","GO":"🍈 GOIABA",
"JA":"🍈 JACA","JI":"🥬 JILÓ",
"LA":"🍊 LARANJA","LE":"🥛 LEITE","LI":"🍋 LIMÃO","LU":"🦑 LULA",
"MA":"🍝 MACARRÃO","ME":"🍯 MEL","MI":"🍜 MIOJO","MO":"🍅 MOLHO",
"PA":"🥜 PAÇOCA","PE":"🥒 PEPINO","PI":"🍿 PIPOCA","PO":"🐷 PORCO","PU":"🥔 PURÊ",
"RA":"🥗 RABANETE","RI":"🧀 RICOTA","RO":"🍎 ROMÃ",
"SA":"🥗 SALADA","SO":"🍲 SOPA",
"TA":"🥗 TABULE"
}

def falar(txt):
    tts = gTTS(text=txt, lang="pt-br")
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    st.audio(mp3.getvalue(), autoplay=True)

if "etapa" not in st.session_state:
    st.session_state.etapa = 1
    st.session_state.pontos = 0

def nova():
    silaba = random.choice(SILABAS)
    letras = list(silaba)
    random.shuffle(letras)
    st.session_state.letra1 = letras[0]
    st.session_state.letra2 = letras[1]
    st.session_state.silaba = silaba
    st.session_state.etapa = 1
    st.session_state.erro = False

if "letra1" not in st.session_state:
    nova()

# CSS quadrados
st.markdown("""
<style>
.letra {
    font-size:24px;
    height:200px;
    width:200px;
}
div.stButton > button {
    height:200px;
    width:200px;
    font-size:24px;
    border-radius:20px;
}
.big {font-size:40px;text-align:center;}
</style>
""", unsafe_allow_html=True)

st.title("🍎 MONTE A SÍLABA")

if st.session_state.erro:
    st.error("😢 CLIQUE PRIMEIRO NA CONSOANTE!")
    st.write("### VOGAIS: A - E - I - O - U")
    st.session_state.erro = False

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button(st.session_state.letra1):
        letra = st.session_state.letra1
        if letra in "AEIOU":
            st.session_state.erro = True
            st.rerun()
        else:
            st.session_state.etapa = 2
            falar(letra)
            st.rerun()

with col3:
    if st.button(st.session_state.letra2):
        letra = st.session_state.letra2
        if letra in "AEIOU":
            st.session_state.erro = True
            st.rerun()
        else:
            st.session_state.etapa = 2
            falar(letra)
            st.rerun()

# SEGUNDO CLIQUE (VOGAL)
if st.session_state.etapa == 2:
    st.write("## AGORA CLIQUE NA VOGAL")

    if st.button("CONTINUAR"):
        st.session_state.etapa = 3
        st.rerun()

# ACERTO
if st.session_state.etapa == 3:
    st.balloons()
    silaba = st.session_state.silaba
    st.write(f"# 🎉 {silaba}")
    st.write(f"## {COMIDAS[silaba]}")
    falar(silaba)

    if st.button("NOVA RODADA"):
        nova()
        st.rerun()
