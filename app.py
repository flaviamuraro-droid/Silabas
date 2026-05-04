import streamlit as st
import random
from gtts import gTTS

st.set_page_config(layout="wide")

# -------- FUNÇÃO DE SOM --------
def tocar_audio(texto):
    tts = gTTS(text=texto.upper(), lang="pt-br", slow=True)
    tts.save("som.mp3")
    st.audio(open("som.mp3","rb").read())

# -------- FUNÇÃO BOTÃO DE LETRA GIGANTE --------
def botao_letra(letra, key):
    return st.button(f"### {letra}", key=key, use_container_width=True)

# -------- BANCO DE SÍLABAS --------
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

# -------- ESTADOS --------
if "fase" not in st.session_state:
    st.session_state.fase = "consoante"
    st.session_state.silaba = random.choice(list(silabas.keys()))

silaba = st.session_state.silaba
palavra = silabas[silaba]
consoante = silaba[0]
vogal = silaba[1]

# -------- TÍTULO --------
st.title("VAMOS FORMAR SÍLABAS!")
st.subheader("CLIQUE PRIMEIRO NA CONSOANTE")

# =====================================================
# FASE 1 — ESCOLHER CONSOANTE
# =====================================================
if st.session_state.fase == "consoante":

    letras = [consoante, vogal]
    random.shuffle(letras)

    c1, c2 = st.columns(2)

    if c1.button(letras[0], use_container_width=True):
        if letras[0] in vogais:
            st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA CONSOANTE")
        else:
            st.session_state.fase = "vogal"
        st.rerun()

    if c2.button(letras[1], use_container_width=True):
        if letras[1] in vogais:
            st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA CONSOANTE")
        else:
            st.session_state.fase = "vogal"
        st.rerun()

# =====================================================
# FASE 2 — ESCOLHER VOGAL
# =====================================================
elif st.session_state.fase == "vogal":

    st.subheader(f"CONSOANTE ESCOLHIDA: {consoante}")
    st.write("### AGORA CLIQUE NA VOGAL")

    c1, c2 = st.columns(2)

    if c1.button(vogal, use_container_width=True):
        st.session_state.fase = "acertou"
        st.rerun()

    if c2.button(consoante, use_container_width=True):
        st.error("ESSA NÃO É A VOGAL")

# =====================================================
# FASE 3 — ACERTO
# =====================================================
elif st.session_state.fase == "acertou":

    st.balloons()
    st.markdown(f"# {silaba}")
    st.markdown(f"## {silaba} DE {palavra}")

    if st.button("🔊 OUVIR NOVAMENTE"):
        tocar_audio(f"{silaba} DE {palavra}")

    if st.button("➡️ PRÓXIMA SÍLABA"):
        st.session_state.silaba = random.choice(list(silabas.keys()))
        st.session_state.fase = "consoante"
        st.rerun()
