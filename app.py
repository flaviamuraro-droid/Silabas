import streamlit as st
import random
import time
from gtts import gTTS
from io import BytesIO

st.set_page_config(layout="centered")

CONSOANTES = list("BPM LFTDNS".replace(" ",""))
VOGAIS = list("AEIOU")

COMIDAS = {
"BA":"🍌 BANANA","BE":"🥗 BETERRABA","BI":"🍪 BISCOITO","BO":"🎂 BOLO","BU":"🌯 BURRITO",
"PA":"🍞 PÃO","PE":"🍐 PERA","PI":"🍕 PIZZA","PO":"🍿 PIPOCA","PU":"🥔 PURÊ",
"MA":"🍎 MAÇÃ","ME":"🍯 MEL","MI":"🌽 MILHO","MO":"🍓 MORANGO","MU":"🧁 MUFFIN",
"LA":"🍝 LASANHA","LE":"🥛 LEITE","LI":"🍋 LIMÃO","LO":"🍖 LOMBO","LU":"🦑 LULA",
"FA":"🍛 FAROFA","FE":"🫘 FEIJÃO","FI":"🍈 FIGO","FO":"🫓 FOCACCIA","FU":"🍲 CALDO"
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
    st.session_state.c = random.choice(CONSOANTES)
    st.session_state.v = random.choice(VOGAIS)
    st.session_state.etapa = 1

if "c" not in st.session_state:
    nova()

# 🔥 BOTÕES MUITO GRANDES
st.markdown("""
<style>
div.stButton > button {
height:220px;
font-size:120px;
border-radius:40px;
}
.big {font-size:70px;text-align:center;}
.food {font-size:110px;text-align:center;}
</style>
""", unsafe_allow_html=True)

st.title("🍎 MONTE A SÍLABA")
st.write(f"## ⭐ PONTOS: {st.session_state.pontos}")

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
    comida = COMIDAS.get(silaba, "🍓 COMIDA")

    st.balloons()
    st.markdown(f"<div class='big'>🎉 {silaba} 🎉</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='food'>{comida}</div>", unsafe_allow_html=True)
    falar(silaba)

    if st.button("🔊 OUVIR DE NOVO"):
        falar(silaba)

    if st.button("🍽️ NOVA RODADA"):
        nova()
        st.rerun()
