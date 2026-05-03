import streamlit as st
import random
from gtts import gTTS
from io import BytesIO

st.set_page_config(layout="wide")

# 🔤 SÍLABAS DISPONÍVEIS (apenas as que você enviou)
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

# 🍎 PALAVRAS / COMIDAS
COMIDAS = {
"BA":"🍌 BANANA",
"BE":"🥗 BETERRABA",
"BI":"🍪 BISCOITO",
"BO":"🎂 BOLO",
"BU":"🌯 BURRITO",

"CA":"🍤 CAMARÃO",
"CE":"🧅 CEBOLA",
"CO":"🍄 COGUMELO",
"CU":"🍚 CUSCUZ",

"DA":"🍑 DAMASCO",
"DO":"🍬 DOCE",

"FA":"🍛 FAROFA",
"FE":"🫘 FEIJÃO",
"FI":"🍈 FIGO",
"FO":"🍳 FOGÃO",

"GA":"🍗 GALINHA",
"GE":"🧊 GELO",
"GO":"🍈 GOIABA",

"JA":"🍈 JACA",
"JI":"🥬 JILÓ",

"LA":"🍊 LARANJA",
"LE":"🥛 LEITE",
"LI":"🍋 LIMÃO",
"LU":"🦑 LULA",

"MA":"🍝 MACARRÃO",
"ME":"🍯 MEL",
"MI":"🍜 MIOJO",
"MO":"🍅 MOLHO",

"PA":"🥜 PAÇOCA",
"PE":"🥒 PEPINO",
"PI":"🍿 PIPOCA",
"PO":"🐷 PORCO",
"PU":"🥔 PURÊ",

"RA":"🥗 RABANETE",
"RI":"🧀 RICOTA",
"RO":"🍎 ROMÃ",

"SA":"🥗 SALADA",
"SO":"🍲 SOPA",

"TA":"🥗 TABULE"
}

def falar(txt):
    tts = gTTS(text=txt, lang="pt-br")
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    st.audio(mp3.getvalue(), autoplay=True)

# estado do jogo
if "etapa" not in st.session_state:
    st.session_state.etapa = 1
    st.session_state.pontos = 0

def nova():
    silaba = random.choice(SILABAS)
    st.session_state.c = silaba[0]
    st.session_state.v = silaba[1]
    st.session_state.etapa = 1

if "c" not in st.session_state:
    nova()

# 🎨 CSS BOTÕES GIGANTES
st.markdown("""
<style>
.block-container {padding-top:0rem;}
.stButton {width:100%;}
div.stButton > button {
    width:100%;
    height:350px;
    font-size:180px;
    border-radius:50px;
}
.big {font-size:90px;text-align:center;}
.food {font-size:150px;text-align:center;}
</style>
""", unsafe_allow_html=True)

st.title("🍎 MONTE A SÍLABA")
st.write(f"# ⭐ PONTOS: {st.session_state.pontos}")

col1, col2, col3 = st.columns([1,2,1])

with col2:

    # ETAPA 1
    if st.session_state.etapa == 1:
        st.markdown("<div class='big'>1️⃣ TOQUE NA CONSOANTE</div>", unsafe_allow_html=True)
        if st.button(st.session_state.c):
            falar(st.session_state.c)
            st.session_state.etapa = 2
            st.rerun()

    # ETAPA 2
    elif st.session_state.etapa == 2:
        st.markdown("<div class='big'>2️⃣ TOQUE NA VOGAL</div>", unsafe_allow_html=True)
        if st.button(st.session_state.v):
            falar(st.session_state.v)
            st.session_state.etapa = 3
            st.session_state.pontos += 1
            st.rerun()

    # FESTA 🎉
    elif st.session_state.etapa == 3:
        silaba = st.session_state.c + st.session_state.v
        comida = COMIDAS[silaba]

        st.balloons()
        st.markdown(f"<div class='big'>🎉 {silaba} 🎉</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='food'>{comida}</div>", unsafe_allow_html=True)
        falar(silaba)

        if st.button("🔊 OUVIR DE NOVO"):
            falar(silaba)

        if st.button("🍽️ NOVA RODADA"):
            nova()
            st.rerun()
