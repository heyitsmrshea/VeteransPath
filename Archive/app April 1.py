import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="OperationMOS", layout="wide")

# --- Branch Info ---
branches = {
    "Army": {
        "image": "static/seals/army.png",
        "color": "#4B5320",
        "motto": "This We'll Defend"
    },
    "Navy": {
        "image": "static/seals/navy.png",
        "color": "#000080",
        "motto": "Forged by the Sea"
    },
    "Air Force": {
        "image": "static/seals/air_force.png",
        "color": "#5D8AA8",
        "motto": "Fly-Fight-Win"
    },
    "Marine Corps": {
        "image": "static/seals/marines.png",
        "color": "#B22222",
        "motto": "Semper Fidelis"
    },
    "Coast Guard": {
        "image": "static/seals/coast_guard.png",
        "color": "#2E8B57",
        "motto": "Semper Paratus"
    },
    "Space Force": {
        "image": "static/seals/space_force.png",
        "color": "#708090",
        "motto": "Semper Supra"
    }
}

# --- Helper Function ---
def show_branch_card(name, image_path, motto):
    try:
        img_bytes = Path(image_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        st.markdown(f"""
            <a href='/?branch={name}'>
                <div style='text-align: center;'>
                    <img src='data:image/png;base64,{encoded}' width='100'/><br>
                    <div style='font-weight:bold; margin-top:0.5rem;'>{name}</div>
                    <div style='font-size:13px; color:gray;'>{motto}</div>
                </div>
            </a>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Image not found for {name}: {image_path}")

# --- Title ---
st.markdown("<h1 style='text-align: center;'>Welcome to OperationMOS</h1>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 18px;'>
    <strong>Your Personal Transition Assistant</strong>
</p>
<p style='text-align: center; font-style: italic; font-size: 16px;'>
    OperationMOS is built by veterans, for veterans — to help you take your service history and turn it into mission-ready civilian resumes.
</p>
""", unsafe_allow_html=True)

# --- Icons Row ---
st.markdown("""
<div class='icon-row'>
    <div class='icon-card'>🎯<br>Translate your experience</div>
    <div class='icon-card'>📄<br>Build a Word resume</div>
    <div class='icon-card'>🚀<br>Target your next mission</div>
</div>
<style>
.icon-row {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1.5rem;
}
.icon-card {
    width: 180px;
    text-align: center;
    padding: 0.5rem;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# --- Choose Branch Header ---
st.markdown("<h2 style='text-align: center; margin-top: 3rem;'>Choose Your Branch</h2>", unsafe_allow_html=True)

# --- Render branches in 2 rows with spacing ---
branches_ordered = list(branches.items())

first_row = st.columns(3)
for i, col in enumerate(first_row):
    name, data = branches_ordered[i]
    with col:
        show_branch_card(name, data["image"], data["motto"])

# Add a spacer between rows
st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

second_row = st.columns(3)
for i, col in enumerate(second_row):
    name, data = branches_ordered[i + 3]
    with col:
        show_branch_card(name, data["image"], data["motto"])

# --- Handle selection ---
query_params = st.query_params
selected_branch = query_params.get("branch", "")

if selected_branch in branches:
    st.markdown(f"<h3 style='text-align: center; color: {branches[selected_branch]['color']}; margin-top: 3rem;'>You selected the <strong>{selected_branch}</strong></h3>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='text-align: center; margin-top: 2rem;'>
            <a href="/Build_Resume" target="_self">
                <button style='padding: 1rem 2rem; font-size: 1.2rem; background-color: {branches[selected_branch]['color']}; color: white; border: none; border-radius: 8px;'>
                    Proceed to Resume Builder
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align:center; margin-top:2rem;'>Click a seal above to get started.</p>", unsafe_allow_html=True)
