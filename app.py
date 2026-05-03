import streamlit as st
import random

CONSOANTES = list("BCDFGLMNPRSTVZ")
VOGAIS = list("AEIOU")

# Estado do jogo (memória entre cliques)
if "fase" not in st.session_state:
    st.session_state.fase = "escolher"
    st.session_state.pontos = 0
    st.session_state.ordem = []
    st.session_state.msg = "Toque primeiro na CONSOANTE!"

def nova_rodada():
    st.session_state.consoante = random.choice(CONSOANTES)
    st.session_state.vogal = random.choice(VOGAIS)
    st.session_state.ordem = []
    st.session_state.fase = "escolher"
    st.session_state.msg = "Toque primeiro na CONSOANTE!"

if "consoante" not in st.session_state:
    nova_rodada()

st.title("🧩 Jogo das Sílabas")

st.subheader("Ordem: CONSOANTE → VOGAL")

col1, col2 = st.columns(2)

def clicar(tipo):
    if st.session_state.fase != "escolher":
        return
    
    st.session_state.ordem.append(tipo)
    
    if len(st.session_state.ordem) == 1:
        if tipo == "consoante":
            st.session_state.msg = "Ótimo! Agora a VOGAL!"
        else:
            st.session_state.msg = "Ops! Primeiro a CONSOANTE!"
    
    elif len(st.session_state.ordem) == 2:
        if st.session_state.ordem == ["consoante", "vogal"]:
            st.session_state.msg = f"🎉 Muito bem! {st.session_state.consoante + st.session_state.vogal}"
            st.session_state.pontos += 1
        else:
            st.session_state.msg = "Quase! A ordem é Consoante + Vogal"
        st.session_state.fase = "fim"

with col1:
    st.button(st.session_state.consoante, on_click=clicar, args=("consoante",))

with col2:
    st.button(st.session_state.vogal, on_click=clicar, args=("vogal",))

st.write("###", st.session_state.msg)
st.write("⭐ Pontos:", st.session_state.pontos)

if st.session_state.fase == "fim":
    if st.button("Nova rodada"):
        nova_rodada()