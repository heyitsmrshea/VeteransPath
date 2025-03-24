import streamlit as st
from resume_helper import translate_fitrep_to_resume

"""
A minimal Streamlit app for debugging GPT resume bullet generation.

How to run:
1. Place this file in the same folder as `resume_helper.py`.
2. In Terminal:
   export OPENAI_API_KEY="sk-REPLACE_WITH_YOUR_KEY"
   streamlit run simple_app.py
3. Paste text or upload a file, enter a target role, and click "Generate".
4. Check debug messages if it fails.
"""

st.title("Simple GPT Resume Bullets Debug App")

# Single form for FITREP input + target role
with st.form("resume_form"):
    st.write("**Upload a FITREP** or **paste text**:")
    uploaded_file = st.file_uploader("Upload (TXT or PDF)", type=["txt", "pdf"])
    st.text_area("Or paste your experience here:", key="manual_input")

    st.text_input("Target role (e.g., Cybersecurity Analyst):", key="target_role")

    generate_btn = st.form_submit_button("Generate Resume Bullets")

if generate_btn:
    st.write("DEBUG: Generate button clicked.")
    text = None

    # Check file upload vs. manual input
    if uploaded_file is not None:
        st.write("DEBUG: Using uploaded file text.")
        text = uploaded_file.read().decode("utf-8")
    elif st.session_state.get("manual_input"):
        st.write("DEBUG: Using manual input text.")
        text = st.session_state["manual_input"]
    else:
        st.warning("No input provided (file or pasted text).")
        st.stop()

    # Check if target role is provided
    role = st.session_state.get("target_role")
    if not role:
        st.warning("No target role provided.")
        st.stop()

    st.write(f"DEBUG: Target role: {role}")

    # Make GPT call
    with st.spinner("Generating bullets via GPT..."):
        try:
            bullets = translate_fitrep_to_resume(text, role)
            st.write("DEBUG: GPT returned bullets:", bullets)
        except Exception as e:
            st.error(f"GPT Error: {e}")
            st.stop()

    # Display results
    st.subheader("Resume Bullets")
    for bullet in bullets:
        st.write(f"- {bullet}")
