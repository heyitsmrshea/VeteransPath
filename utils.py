# utils.py
import base64
import streamlit as st

def get_branch_logo(branch):
    logos = {
        "Army": "assets/army_seal.png",
        "Navy": "assets/navy_seal.png",
        "Air Force": "assets/airforce_seal.png",
        "Marines": "assets/marinecorps_seal.png",
        "Coast Guard": "assets/coastguard_seal.png",
        "Space Force": "assets/spaceforce_seal.png",
    }
    return logos.get(branch, "")

def load_custom_css():
    st.markdown("""
        <style>
        body {
            background: #f4f7fa;
            font-family: "Segoe UI", sans-serif;
        }
        .hero-banner {
            display: flex;
            align-items: center;
            justify-content: center;
            background: white;
            border-radius: 1rem;
            padding: 2rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
            gap: 2rem;
        }
        .hero-text h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }
        .typewriter {
            font-size: 1.2rem;
            border-right: .15em solid orange;
            white-space: nowrap;
            overflow: hidden;
            width: 0;
            animation: typing 3s steps(40, end) forwards, blink-caret .75s step-end infinite;
        }
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: orange; }
        }
        .features-grid {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }
        .features-grid .feature {
            display: flex;
            align-items: center;
        }
        .features-grid .icon {
            margin-right: 0.6rem;
            font-size: 1.5rem;
        }
        .track-button {
            padding: 1rem;
            text-align: center;
            border-radius: 0.75rem;
            background-color: #f0f0f0;
            transition: all 0.2s ease;
        }
        .disabled-button {
            color: #999;
            background: #f3f3f3;
        }
        </style>
    """, unsafe_allow_html=True)
