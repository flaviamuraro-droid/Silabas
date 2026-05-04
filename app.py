import streamlit as st
import random
from gtts import gTTS

st.set_page_config(layout="wide")

# ---------- FUNÇÃO SOM ----------
def tocar_audio(texto):
    frase = texto.upper()
    tts = gTTS(text=frase, lang="pt-br", slow=True)
    arquivo = "som.mp3"
    tts.save(arquivo)
    audio_file = open(arquivo, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

# ---------- ESTILO VISUAL ----------
st.markdown("""
<style>

/* BOTÕES GIGANTES */
div.stButton > button {
    height: 220px !important;
    width: 220px !important;
    border-radius: 30px !important;
}

/* TEXTO DENTRO DO BOTÃO (AUMENTA A LETRA!) */
div.stButton > button p {
    font-size: 120px !important;
    font-weight: 900 !important;
}

/* SÍLABA FINAL */
.big {
    font-size:150px;
    text-align:center;
    font-weight:bold;
}

.center {
    text-align:center;
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

# ---------- FASE 1: ESCOLHER CONSOANTE ----------
if st.session_state.fase == "consoante":

    letras = [consoante, vogal]
    random.shuffle(letras)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(letras[0]):
            if letras[0] in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
                st.rerun()
            else:
                st.session_state.fase = "vogal"
                st.rerun()

    with col2:
        if st.button(letras[1]):
            if letras[1] in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
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
            st.session_state.fase = "acertou"
            st.rerun()

    with col2:
        if st.button(consoante):
            st.error("ESSA NÃO É A VOGAL 😢")

# ---------- FASE 3: TELA DE ACERTO ----------
elif st.session_state.fase == "acertou":

    st.balloons()
    st.markdown(f"<div class='big'>{silaba}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='center'>{silaba} DE {palavra}</h2>", unsafe_allow_html=True)

    if st.button("🔊 OUVIR NOVAMENTE"):
        tocar_audio(f"{silaba} DE {palavra}")

    st.write("")
    st.write("")

    if st.button("➡️ PRÓXIMA SÍLABA"):
        st.session_state.silaba_atual = random.choice(list(silabas.keys()))
        st.session_state.fase = "consoante"
        st.rerun()
