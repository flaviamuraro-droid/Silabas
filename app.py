import streamlit as st
import random
import time

st.set_page_config(layout="wide")

# ---------- ESTILO (BOTÕES GIGANTES) ----------
st.markdown("""
<style>
div.stButton > button {
    height: 200px;
    width: 200px;
    font-size: 60px !important;
    font-weight: bold;
    border-radius: 25px;
}
h1, h2, h3, p {
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

# ---------- SORTEAR NOVA SÍLABA ----------
if "silaba_atual" not in st.session_state:
    st.session_state.silaba_atual = random.choice(list(silabas.keys()))
    st.session_state.ordem = []

silaba = st.session_state.silaba_atual
palavra = silabas[silaba]

consoante = silaba[0]
vogal = silaba[1]

# ---------- TÍTULO ----------
st.title("🍎 VAMOS FORMAR SÍLABAS!")

st.header(f"QUAL A PRIMEIRA LETRA DE:")
st.header(f"🍽️ {palavra} ?")

st.write("")
st.write("")

# ---------- EMBARALHAR POSIÇÃO ----------
letras = [consoante, vogal]
random.shuffle(letras)

col1, col2 = st.columns(2)

with col1:
    if st.button(letras[0]):
        st.session_state.ordem.append(letras[0])

with col2:
    if st.button(letras[1]):
        st.session_state.ordem.append(letras[1])

# ---------- VERIFICAR RESPOSTA ----------
if len(st.session_state.ordem) == 1:
    primeira = st.session_state.ordem[0]

    # ❌ clicou na vogal primeiro
    if primeira in ["A","E","I","O","U"]:
        st.error("😢 CLIQUE PRIMEIRO NA CONSOANTE!")

        time.sleep(2)
        st.session_state.ordem = []
        st.rerun()

    # ✅ clicou na consoante primeiro
    else:
        st.success("🎉 MUITO BEM!!!")

        time.sleep(2)
        st.session_state.silaba_atual = random.choice(list(silabas.keys()))
        st.session_state.ordem = []
        st.rerun()
