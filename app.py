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
            <a href='/?branch={name}' class='branch-link'>
                <div class='branch-card fadein'>
                    <img src='data:image/png;base64,{encoded}' width='100' class='branch-img'/><br>
                    <div class='branch-title'>{name}</div>
                    <div class='branch-motto'>{motto}</div>
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
    <div class='icon-card animate'><span style='font-size: 2rem;'>🎯</span><br><span class='icon-label'>Translate your experience</span></div>
    <div class='icon-card animate'><span style='font-size: 2rem;'>📄</span><br><span class='icon-label'>Build a Word resume</span></div>
    <div class='icon-card animate'><span style='font-size: 2rem;'>🚀</span><br><span class='icon-label'>Target your next mission</span></div>
</div>

<style>
.icon-row {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-top: 2rem;
}
.icon-card {
    width: 180px;
    text-align: center;
    font-size: 16px;
    opacity: 0;
    transform: translateY(30px);
    animation: flyIn 1s ease-out forwards;
}
.icon-card:nth-child(2) { animation-delay: 0.2s; }
.icon-card:nth-child(3) { animation-delay: 0.4s; }

@keyframes flyIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
.branch-card {
    text-align: center;
    padding: 1rem;
    border-radius: 16px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInLogo 1s ease forwards;
}
.branch-card:nth-child(1) { animation-delay: 0.2s; }
.branch-card:nth-child(2) { animation-delay: 0.3s; }
.branch-card:nth-child(3) { animation-delay: 0.4s; }
.branch-card:nth-child(4) { animation-delay: 0.5s; }
.branch-card:nth-child(5) { animation-delay: 0.6s; }
.branch-card:nth-child(6) { animation-delay: 0.7s; }

@keyframes fadeInLogo {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
.branch-img {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.branch-link:hover .branch-img {
    transform: scale(1.1);
    box-shadow: 0 0 20px rgba(0, 128, 255, 0.3);
}
.branch-title {
    font-weight: bold;
    margin-top: 0.5rem;
}
.branch-motto {
    font-size: 13px;
    color: gray;
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
st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)

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
