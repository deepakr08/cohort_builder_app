import streamlit as st
import base64
from parser import parse_protocol

st.set_page_config(layout="wide")

# ---------- LOGO ----------
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64_of_bin_file("jjlogo.png")

st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{logo_base64}" width="250">
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- TITLE ----------
st.markdown(
    """
    <h1 style='text-align: center; 
               font-family: "Times New Roman"; 
               font-size: 45px; 
               font-weight: bold;'>
        ATTRITION SQL AGENT
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h3 style='text-align: center; 
               font-family: "Times New Roman"; 
               color: grey;'>
        Clinical Protocol → Attrition → Cohort
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- FILE UPLOAD ----------
st.markdown("## 📂 Upload Clinical Protocol")

file = st.file_uploader("Upload Protocol (.docx)", type=["docx"])

st.markdown("---")

# ---------- MAIN LOGIC ----------
if file:

    inc_steps, exc_steps, attrition, data_sources = parse_protocol(file)

    # ---------- DATA SOURCE ----------
    st.markdown("##  Data Source")

    if data_sources:
        for ds in data_sources:
            st.success(ds)
    else:
        st.warning("No Data Source Detected")

    st.markdown("---")

    # ---------- INCLUSION / EXCLUSION ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("###  Inclusion Criteria")
        for i, step in enumerate(inc_steps, 1):
            st.write(f"{i}. {step}")

    with col2:
        st.markdown("###  Exclusion Criteria")
        for i, step in enumerate(exc_steps, 1):
            st.write(f"{i}. {step}")

    # ---------- ATTRITION ----------
    st.markdown("---")
    st.markdown("##  Attrition Steps")

    for step_no, step_type, desc in attrition:
        st.write(f"Step {step_no} ({step_type}): {desc}")

    st.markdown("---")

    st.markdown(
    """
    <h1 style='text-align: center; 
               font-family: "Times New Roman"; 
               font-size: 45px; 
               font-weight: bold;'>
        ATTRITION (SQL) w/ QC's
    </h1>
    """,
    unsafe_allow_html=True
)      
