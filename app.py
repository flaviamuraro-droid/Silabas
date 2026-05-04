import streamlit as st
import random
from gtts import gTTS

st.set_page_config(layout="wide")

# ---------- FUNÇÃO SOM ----------
def tocar_audio(texto):
    frase = texto.upper()
    tts = gTTS(text=frase, lang="pt-br", slow=True)
    tts.save("som.mp3")
    audio_file = open("som.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# ---------- CSS ----------
st.markdown("""
<style>

/* BOTÕES NORMAIS (som e próxima) */
div.stButton > button {
    font-size:18px !important;
    height:50px;
}

/* BOTÕES DAS LETRAS (classe especial) */
.letra button {
    height:220px !important;
    width:220px !important;
    border-radius:30px !important;
}

.letra button p {
    font-size:120px !important;
    font-weight:900 !important;
}

.big {
    font-size:150px;
    text-align:center;
    font-weight:bold;
}

.center { text-align:center; }

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

st.title("VAMOS FORMAR SÍLABAS!")
st.write("### CLIQUE PRIMEIRO NA CONSOANTE")

# ---------- FASE CONSOANTE ----------
if st.session_state.fase == "consoante":

    letras = [consoante, vogal]
    random.shuffle(letras)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="letra">', unsafe_allow_html=True)
        if st.button(letras[0], key="l1"):
            if letras[0] in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
                st.rerun()
            else:
                st.session_state.fase = "vogal"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="letra">', unsafe_allow_html=True)
        if st.button(letras[1], key="l2"):
            if letras[1] in vogais:
                st.error("VAMOS TENTAR NOVAMENTE? CLIQUE PRIMEIRO NA **CONSOANTE**")
                st.rerun()
            else:
                st.session_state.fase = "vogal"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- FASE VOGAL ----------
elif st.session_state.fase == "vogal":

    st.header(f"CONSOANTE ESCOLHIDA: {consoante}")
    st.write("### AGORA CLIQUE NA VOGAL")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="letra">', unsafe_allow_html=True)
        if st.button(vogal, key="v1"):
            st.session_state.fase = "acertou"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="letra">', unsafe_allow_html=True)
        if st.button(consoante, key="v2"):
            st.error("ESSA NÃO É A VOGAL 😢")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- FASE ACERTO ----------
elif st.session_state.fase == "acertou":

    st.balloons()
    st.markdown(f"<div class='big'>{silaba}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='center'>{silaba} DE {palavra}</h2>", unsafe_allow_html=True)

    if st.button("🔊 OUVIR NOVAMENTE"):
        tocar_audio(f"{silaba} DE {palavra}")

    if st.button("➡️ PRÓXIMA SÍLABA"):
        st.session_state.silaba_atual = random.choice(list(silabas.keys()))
        st.session_state.fase = "consoante"
        st.rerun()
