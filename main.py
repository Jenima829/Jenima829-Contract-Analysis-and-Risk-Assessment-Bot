# ============================================================
# 📦 IMPORTS
# ============================================================
import streamlit as st

st.set_page_config(
    page_title="Contract Analysis Bot",
    layout="wide",
    initial_sidebar_state="expanded"
)
with st.spinner("⏳ Initializing AI models... Please wait"):
    from nlp.preprocessing import preprocess_text


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from parsers.file_parser import parse_contract
from nlp.preprocessing import preprocess_text
from nlp.contract_classification import classify_contract
from nlp.clause_extraction import extract_clauses
from nlp.entity_extractor import extract_entities
from risk.risk_analysis import analyze_risk
from risk.risk_mitigation import suggest_mitigation
from pdf.report_generator import export_pdf
from utils.highlighter import highlight_text

# ============================================================
# ⚙️ PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Legal Contract Risk Analyzer",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ GenAI Legal Assistant for Indian SMEs")

# ============================================================
# 🎨 CUSTOM CSS
# ============================================================

st.markdown("""
<style>
h1 {
    background: linear-gradient(90deg,#ff4b4b,#ffa500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card {
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(145deg,#1c1f26,#111318);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    text-align:center;
    border: 1px solid #2a2f3a;
}
.high {color:#ff4b4b;}
.medium {color:#ffa500;}
.low {color:#00c853;}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 📥 INPUT SECTION
# ============================================================

input_option = st.radio(
    "Choose Input Method",
    ["Upload Contract File", "Paste Contract Text"]
)

text = ""

if input_option == "Upload Contract File":
    uploaded_file = st.file_uploader(
        "Upload Contract",
        type=["pdf", "docx", "txt"]
    )
    if uploaded_file:
        text = parse_contract(uploaded_file)
else:
    text = st.text_area("Paste Contract Content", height=300)

# ============================================================
# 🚀 PROCESS CONTRACT
# ============================================================

if text:
    processed_text = preprocess_text(text)
    contract_type = classify_contract(processed_text)
    st.success(f"📑 Detected Contract Type: {contract_type}")

    clauses = extract_clauses(processed_text)
    entities = extract_entities(processed_text)
    risk_results = analyze_risk(clauses)

    # ========================================================
    # 🧮 RISK COUNTS
    # ========================================================

    high = sum(1 for r in risk_results if r["Risk"] == "High")
    medium = sum(1 for r in risk_results if r["Risk"] == "Medium")
    low = sum(1 for r in risk_results if r["Risk"] == "Low")
    total = high + medium + low

    risk_percentage = ((high*3 + medium*2 + low) / (total*3)) * 100 if total else 0

    # ========================================================
    # 🃏 KPI CARDS
    # ========================================================

    col1, col2, col3 = st.columns(3)
    col1.markdown(f"<div class='card'><h3 class='high'>🔴 High Risk</h3><h1>{high}</h1></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='card'><h3 class='medium'>🟠 Medium Risk</h3><h1>{medium}</h1></div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='card'><h3 class='low'>🟢 Low Risk</h3><h1>{low}</h1></div>", unsafe_allow_html=True)

    st.metric("Overall Risk Score", f"{risk_percentage:.2f}%")
    st.progress(int(risk_percentage))

    # ========================================================
    # 📑 TABS
    # ========================================================

    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Clauses",
        "⚠ Risk Analysis",
        "📊 Charts",
        "📑 Report"
    ])

    # ========================================================
    # 📄 TAB 1 — CLAUSES
    # ========================================================

    with tab1:
        st.subheader("Extracted Clauses")
        st.write(clauses)

        st.subheader("📌 Entities")
        st.json(entities)

        st.subheader("📑 Highlighted Contract")
        highlighted_text = highlight_text(text, risk_results)
        st.markdown(f"<div style='padding:15px'>{highlighted_text}</div>", unsafe_allow_html=True)

    # ========================================================
    # ⚠ TAB 2 — RISK ANALYSIS
    # ========================================================

    with tab2:
        df = pd.DataFrame(risk_results)
        st.dataframe(df, use_container_width=True)

        st.subheader("🛠 Mitigation Suggestions")
        mitigations = suggest_mitigation(risk_results)

        for m in mitigations:
            st.error(f"{m['risk']} → [{m['clause']}] {m['text']}")
            st.success(f"✔ Fix: {m['fix']}")

    # ========================================================
    # 📊 TAB 3 — ENHANCED PIE / DONUT CHART
    # ========================================================

    with tab3:
        st.subheader("Risk Distribution")

        labels = ["High", "Medium", "Low"]
        values = [high, medium, low]

        fig, ax = plt.subplots(figsize=(2.8, 2.8), dpi=100)
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

        wedges, texts, autotexts = ax.pie(
            values,
            labels=labels,
            autopct="%1.0f%%",
            startangle=90,
            textprops={"fontsize": 8},
            wedgeprops=dict(width=0.35, edgecolor="white")
        )

        for t in autotexts:
            t.set_fontsize(8)

        centre_circle = plt.Circle((0, 0), 0.65, fc="white")
        ax.add_artist(centre_circle)

        ax.set_title("Contract Risk Split", fontsize=9, pad=6)
        ax.axis("equal")
        plt.tight_layout(pad=0.4)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.pyplot(fig, clear_figure=True)

    # ========================================================
    # 📑 TAB 4 — REPORT
    # ========================================================

    with tab4:
        if st.button("Generate Legal Report PDF"):
            summary_text = f"Contract Type: {contract_type}\nOverall Risk Score: {risk_percentage:.2f}%"
            file_path = export_pdf(summary_text, risk_results, [])
            st.success("✅ Report generated!")
            with open(file_path, "rb") as f:
                st.download_button("📥 Download Report", f, file_name="Legal_Report.pdf")

# ============================================================
# 📊 MULTI CONTRACT COMPARISON
# ============================================================

st.divider()
st.header("📊 Multi-Contract Comparison")

files = st.file_uploader(
    "Upload Multiple Contracts",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

comparison_data = []

if files:
    for file in files:
        text = parse_contract(file)
        clauses = extract_clauses(text)
        risks = analyze_risk(clauses)

        comparison_data.append({
            "Contract": file.name,
            "High": sum(1 for r in risks if r["Risk"] == "High"),
            "Medium": sum(1 for r in risks if r["Risk"] == "Medium"),
            "Low": sum(1 for r in risks if r["Risk"] == "Low")
        })

    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("Contract"))

