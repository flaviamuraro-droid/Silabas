import streamlit as st
import random
import time
from gtts import gTTS
import base64
from io import BytesIO

st.set_page_config(layout="centered")

CONSOANTES = list("BDFGLMNPRSTV")
VOGAIS = list("AEIOU")

# banco de comidas por sílaba
COMIDAS = {
    "BA":"🍌 Banana","BE":"🧁 Bolo","BI":"🥤 Bebida","BO":"🍩 Bolacha","BU":"🍔 Burger",
    "MA":"🍎 Maçã","ME":"🍯 Mel","MI":"🥛 Milkshake","MO":"🍫 Mousse","MU":"🧁 Muffin",
    "PA":"🍞 Pão","PE":"🍐 Pera","PI":"🍕 Pizza","PO":"🍿 Pipoca","PU":"🥞 Panqueca",
    "LA":"🥗 Lasanha","LE":"🍋 Limão","LI":"🍭 Lollipop","LO":"🍪 Lollipop","LU":"🍝 Macarrão",
}

def falar(texto):
    tts = gTTS(text=texto, lang="pt-br")
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    st.audio(mp3.getvalue(), format="audio/mp3", autoplay=True)

# estado
if "etapa" not in st.session_state:
    st.session_state.etapa = 1
    st.session_state.pontos = 0

def nova_rodada():
    st.session_state.consoante = random.choice(CONSOANTES)
    st.session_state.vogal = random.choice(VOGAIS)
    st.session_state.etapa = 1

if "consoante" not in st.session_state:
    nova_rodada()

# estilo botões gigantes
st.markdown("""
<style>
div.stButton > button {
    height:150px;
    width:100%;
    font-size:70px;
    border-radius:25px;
}
.big-text {font-size:60px;text-align:center;}
.center {text-align:center;}
.food {font-size:80px;text-align:center;}
</style>
""", unsafe_allow_html=True)

st.title("🍎 Monte a Sí­laba da Comida")

st.markdown(f"<h2 class='center'>⭐ Pontos: {st.session_state.pontos}</h2>", unsafe_allow_html=True)
st.write("")

# ETAPA 1
if st.session_state.etapa == 1:
    st.markdown("<div class='big-text'>1️⃣ Toque na CONSOANTE</div>", unsafe_allow_html=True)
    if st.button(st.session_state.consoante):
        falar(st.session_state.consoante)
        st.session_state.etapa = 2
        st.rerun()

# ETAPA 2
elif st.session_state.etapa == 2:
    st.markdown("<div class='big-text'>2️⃣ Agora toque na VOGAL</div>", unsafe_allow_html=True)
    if st.button(st.session_state.vogal):
        falar(st.session_state.vogal)
        st.session_state.etapa = 3
        st.session_state.pontos += 1
        st.rerun()

# ETAPA 3 — festa + comida 🍔
elif st.session_state.etapa == 3:
    silaba = st.session_state.consoante + st.session_state.vogal
    comida = COMIDAS.get(silaba, "🍓 Comidinha")

    st.balloons()
    st.markdown(f"<div class='big-text'>🎉 {silaba} 🎉</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='food'>{comida}</div>", unsafe_allow_html=True)

    falar(silaba)

    st.write("")
    if st.button("🔊 Ouvir novamente"):
        falar(silaba)

    if st.button("🍽️ Jogar novamente"):
        nova_rodada()
        st.rerun()
