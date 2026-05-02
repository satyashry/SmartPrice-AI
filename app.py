import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

st.set_page_config(
    page_title="SmartPrice AI",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background: #080c14;
    color: #e8eaf0;
}

/* Top accent bar */
.stApp::before {
    content: '';
    display: block;
    height: 3px;
    background: linear-gradient(90deg, #00f5a0, #00d9f5, #7b61ff);
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 999;
}

/* Header */
.hero {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}
.hero-badge {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    color: #00f5a0;
    border: 1px solid #00f5a030;
    background: #00f5a008;
    padding: 5px 14px;
    border-radius: 20px;
    margin-bottom: 16px;
    text-transform: uppercase;
}
.hero h1 {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 40%, #00f5a0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 8px;
    line-height: 1.1;
}
.hero p {
    color: #6b7280;
    font-size: 0.95rem;
    margin: 0;
    font-family: 'Space Mono', monospace;
}

/* Card */
.card {
    background: #0e1420;
    border: 1px solid #1e2535;
    border-radius: 16px;
    padding: 1.75rem;
    margin-bottom: 1.25rem;
}
.card-title {
    font-size: 11px;
    font-family: 'Space Mono', monospace;
    letter-spacing: 0.12em;
    color: #00d9f5;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* Labels */
label, .stSelectbox label, .stNumberInput label {
    font-size: 12px !important;
    font-family: 'Space Mono', monospace !important;
    letter-spacing: 0.08em !important;
    color: #9ca3af !important;
    text-transform: uppercase !important;
}

/* Inputs */
.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: #131926 !important;
    border: 1px solid #1e2535 !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
    font-family: 'Syne', sans-serif !important;
}
.stSelectbox > div > div:hover,
.stNumberInput > div > div > input:focus {
    border-color: #00f5a040 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #00f5a0, #00d9f5) !important;
    color: #080c14 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    letter-spacing: 0.05em !important;
    padding: 14px !important;
    border-radius: 12px !important;
    border: none !important;
    margin-top: 0.5rem;
    transition: opacity 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
}

/* Result box */
.result-box {
    background: linear-gradient(135deg, #00f5a010, #00d9f508);
    border: 1px solid #00f5a030;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1.5rem;
}
.result-label {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    color: #6b7280;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.result-price {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00f5a0, #00d9f5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}
.result-sub {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #4b5563;
    margin-top: 10px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #2d3748;
}

/* Hide streamlit branding */
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">🧠 AI-Powered · India Market</div>
    <h1>SmartPrice AI</h1>
    <p>Predict fair laptop prices from specs — powered by XGBoost</p>
</div>
""", unsafe_allow_html=True)


# ── Inputs ────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">⚙ Laptop Specifications</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Brand", [
        "ASUS", "HP", "Lenovo", "DELL", "Acer",
        "MICROSOFT", "MOTOROLA", "MSI", "Samsung", "Apple"
    ])
    ram = st.selectbox("RAM", [4, 8, 16, 24, 32, 64], index=2,
                       format_func=lambda x: f"{x} GB")
    storage = st.selectbox("Storage", [128, 256, 512, 1024, 2048], index=2,
                           format_func=lambda x: f"{x} GB" if x < 1000 else f"{x//1024} TB")

with col2:
    processor = st.selectbox("Processor", [
        "Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
        "Intel Core Ultra", "AMD Ryzen 3", "AMD Ryzen 5",
        "AMD Ryzen 7", "AMD Ryzen 9", "Snapdragon X"
    ], index=1)
    graphics = st.selectbox("Graphics", [
        "Integrated", "2 GB Graphics", "4 GB Graphics",
        "6 GB Graphics", "8 GB Graphics", "AMD Radeon"
    ])
    os = st.selectbox("Operating System", ["Windows 11", "Windows 10", "DOS"])

st.markdown('</div>', unsafe_allow_html=True)

# ── Predict ───────────────────────────────────────────────────
predict_clicked = st.button("Predict Fair Price →")

if predict_clicked:
    with st.spinner("Analysing specs..."):
        data = CustomData(
            brand=brand,
            ram=ram,
            storage=storage,
            processor=processor,
            graphics=graphics,
            os=os
        )
        df = data.get_data_as_dataframe()
        pipeline = PredictPipeline()
        result = pipeline.predict(df)
        price = result[0]

    st.markdown(f"""
    <div class="result-box">
        <div class="result-label">Predicted Fair Market Price</div>
        <div class="result-price">₹{price:,.0f}</div>
        <div class="result-sub">Based on {brand} · {ram}GB RAM · {storage}GB · {processor}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
     · Trained on real Flipkart data · SmartPrice AI v1.0
</div>
""", unsafe_allow_html=True)
