import streamlit as st
import random
import time

st.set_page_config(layout="centered")

CONSOANTES = list("BCDFGLMNPRSTVZ")
VOGAIS = list("AEIOU")

# estado do jogo
if "etapa" not in st.session_state:
    st.session_state.etapa = 1
    st.session_state.pontos = 0

def nova_rodada():
    st.session_state.consoante = random.choice(CONSOANTES)
    st.session_state.vogal = random.choice(VOGAIS)
    st.session_state.etapa = 1

if "consoante" not in st.session_state:
    nova_rodada()

# CSS para botões gigantes 💛
st.markdown("""
<style>
div.stButton > button {
    height:150px;
    width:100%;
    font-size:70px;
    border-radius:25px;
}
.big-text {
    font-size:60px;
    text-align:center;
}
.center {
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("🧩 Monte a Sí­laba")

# ⭐ Pontuação
st.markdown(f"<h2 class='center'>⭐ Pontos: {st.session_state.pontos}</h2>", unsafe_allow_html=True)

st.write("")

# ETAPA 1 — CONSOANTE
if st.session_state.etapa == 1:
    st.markdown("<div class='big-text'>1️⃣ Toque na CONSOANTE</div>", unsafe_allow_html=True)
    
    if st.button(st.session_state.consoante):
        st.session_state.etapa = 2
        st.rerun()

# ETAPA 2 — VOGAL
elif st.session_state.etapa == 2:
    st.markdown("<div class='big-text'>2️⃣ Agora toque na VOGAL</div>", unsafe_allow_html=True)
    
    if st.button(st.session_state.vogal):
        st.session_state.etapa = 3
        st.session_state.pontos += 1
        st.rerun()

# ETAPA 3 — CELEBRAÇÃO 🎉
elif st.session_state.etapa == 3:
    silaba = st.session_state.consoante + st.session_state.vogal
    
    st.balloons()
    st.markdown(f"<div class='big-text'>🎉 {silaba} 🎉</div>", unsafe_allow_html=True)
    st.markdown("<div class='big-text'>Muito bem!!</div>", unsafe_allow_html=True)
    
    time.sleep(1)
    
    if st.button("Jogar novamente"):
        nova_rodada()
        st.rerun()
