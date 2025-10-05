import streamlit as st
from PIL import Image
from montecarlo_simulation.main import main
from curl_cffi.requests.exceptions import HTTPError

st.set_page_config(layout="wide")

linkedin_url = "https://www.linkedin.com/in/rocco-rodriguez/"
linkedin_logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" 
linkedin_texto = "Rocco Rodriguez"

st.title("Montecarlo Simulation Stock Prices")

with st.container(border=True):
    col_precio_min, col_precio_max, col_pganancia, col_drift_historico, col_p10= st.columns(5)
    with col_precio_min:
        min_placeholder = st.empty()
        min_placeholder.metric("Mínimo ($)", "-")
    with col_precio_max:
        max_placeholder = st.empty()
        max_placeholder.metric("Máximo ($)", "-")
    with col_pganancia:
        pgan_placeholder = st.empty()
        pgan_placeholder.metric("Probabilidad de ganancia (%)", "-")
    with col_drift_historico:
        dh_placeholder = st.empty()
        dh_placeholder.metric("Drift histórico", "-")
    with col_p10:
        p10_placeholder = st.empty()
        p10_placeholder.metric("P10 (Percentil 10)", "-")

    col_retorno_min, col_retorno_max, col_pperdida, col_drift_simulado, col_p90 = st.columns(5)
    with col_retorno_min:
        ret_min_placeholder = st.empty()
        ret_min_placeholder.metric("Mínimo (%)", "-")
    with col_retorno_max:
        ret_max_placeholder = st.empty()
        ret_max_placeholder.metric("Máximo (%)", "-")
    with col_pperdida:
        pperd_placeholder = st.empty()
        pperd_placeholder.metric("Probabilidad de pérdida (%)", "-")
    with col_drift_simulado:
        ds_placeholder = st.empty()
        ds_placeholder.metric("Drift simulado", "-")
    with col_p90:
        p90_placeholder = st.empty()
        p90_placeholder.metric("P90 (Percentil 90)", "-")

st.sidebar.header("🧮 Montecarlo Simulation Stock Prices")
st.sidebar.markdown(
    f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-left: 3px; margin-bottom: 20px;">
        <a href="{linkedin_url}" target="_blank">
            <img 
                src="{linkedin_logo_url}" 
                alt="LinkedIn" 
                style="width:20px;height:20px;border-radius:5px;"
            />
        </a>
        <a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;">
            <p style="margin: 0; font-size: 16px; margin-top: 3px;">
                {linkedin_texto}
            </p>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

ticker = st.sidebar.text_input(
    "Ticker",
    value="MSFT"
)

iteraciones = st.sidebar.number_input(
    "Cantidad de días a simular",
    min_value=1,
    step=1,
    value=60
)
n_simulaciones = st.sidebar.number_input(
    "Cantidad de simulaciones",
    min_value=10,
    step=1,
    value=100
)

if st.sidebar.checkbox("Personalizar drift"):
    drift_simulado = st.sidebar.slider(
        "Personalizar drift", 
        min_value=-0.01, 
        max_value=0.01,
        step=0.00001,
        value=0.0,
        format="%.5f")
else: drift_simulado = None

def mostrar_simulacion():
    try:
        drift_historico, precio_min, precio_max, retorno_min, retorno_max, p_ganancia, p_perdida, p10, p90 = main(ticker, iteraciones, n_simulaciones, drift_simulado)
    except HTTPError:
        st.error(f"❌ El ticker '{ticker}' no existe o no se pudo obtener información.")
        return

    min_placeholder.metric("Mínimo ($)", f"{precio_min:.2f}")
    max_placeholder.metric("Máximo ($)", f"{precio_max:.2f}")
    ret_min_placeholder.metric("Mínimo (%)", f"{retorno_min:.2%}")
    ret_max_placeholder.metric("Máximo (%)", f"{retorno_max:.2%}")
    pgan_placeholder.metric("Probabilidad de ganancia (%)", f"{p_ganancia:.2%}")
    pperd_placeholder.metric("Probabilidad de pérdida (%)", f"{p_perdida:.2%}")
    dh_placeholder.metric("Drift histórico", f"{drift_historico:.5f}")
    if drift_simulado is not None:
        ds_placeholder.metric("Drift simulado", f"{drift_simulado:.5f}")
    else: ds_placeholder.metric("Drift simulado", "-")
    p10_placeholder.metric("P10 (Percentil 10)", f"{p10:.2f}")
    p90_placeholder.metric("P90 (Percentil 90)", f"{p90:.2f}")

    col1, col2 = st.columns(2)

    img1 = Image.open("grafico1.jpg")
    img2 = Image.open("grafico2.jpg")

    col1.image(img1, caption="Evolución de precios", width=600)
    col2.image(img2, caption="Distribución de precios finales", width=600)

if "primera_vez" not in st.session_state:
    st.session_state.primera_vez = True

if st.session_state.primera_vez:
    mostrar_simulacion()
    st.session_state.primera_vez = False

if st.sidebar.button("Correr simulación"):
    if not ticker.strip():
        st.warning("⚠️ Ingresá un ticker antes de correr la simulación.")
    else: mostrar_simulacion()