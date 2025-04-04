import streamlit as st
import os
from resume_helper import translate_fitrep_to_resume

st.set_page_config(page_title="Simple GPT Resume Bullets Debug App", layout="centered")
st.title("Simple GPT Resume Bullets Debug App")

st.write("This app is for debugging GPT-based resume bullet generation. Please provide FITREP text and a target role.")

# Single form for debugging input
with st.form("debug_form"):
    uploaded_file = st.file_uploader("Upload a FITREP (TXT or PDF)", type=["txt", "pdf"], key="uploaded_file")
    manual_text = st.text_area("Or paste your FITREP text here:", key="manual_input")
    target_role = st.text_input("Target Role (e.g., Cybersecurity Analyst)", key="target_role")
    submit_debug = st.form_submit_button("Generate Resume Bullets")

st.write("DEBUG: Form submitted:", submit_debug)

if submit_debug:
    st.write("DEBUG: Resume form submission triggered.")
    
    # Determine input source
    if uploaded_file is not None:
        st.write("DEBUG: File uploaded.")
        try:
            text = uploaded_file.read().decode("utf-8")
        except Exception as e:
            st.error(f"DEBUG: Error decoding file: {e}")
            st.stop()
    elif manual_text:
        st.write("DEBUG: Manual text input detected.")
        text = manual_text
    else:
        st.warning("DEBUG: No FITREP input provided. Please upload a file or paste text.")
        st.stop()
    
    # Validate target role
    if not target_role:
        st.warning("DEBUG: No target role provided. Please enter a target role.")
        st.stop()
    else:
        st.write(f"DEBUG: Target role is: {target_role}")
    
    # Call GPT to generate resume bullets
    with st.spinner("DEBUG: Generating resume bullets using GPT..."):
        try:
            bullets = translate_fitrep_to_resume(text, target_role)
            st.write("DEBUG: GPT returned bullets:", bullets)
        except Exception as e:
            st.error(f"DEBUG: Error calling GPT: {e}")
            st.stop()
    
    # Display the generated bullets
    if bullets:
        st.subheader("Generated Resume Bullets")
        for bullet in bullets:
            st.write(f"- {bullet}")
    else:
        st.warning("DEBUG: No bullets were returned from GPT.")
