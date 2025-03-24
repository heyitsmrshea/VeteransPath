import streamlit as st
import os
from resume_helper import translate_fitrep_to_resume

st.set_page_config(page_title="VeteranPath Debug", layout="centered")
st.title("VeteranPath Debug")
st.subheader("Debugging the Resume Form Section")

# Initialize session state for onboarding
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

# Onboarding Form
if not st.session_state.onboarded:
    with st.form("onboarding"):
        st.write("DEBUG: Onboarding Form")
        st.selectbox("Branch of Service", ["Army", "Navy", "Air Force", "Marines", "Coast Guard", "Space Force"], key="branch")
        st.text_input("MOS / Job Code", key="mos")
        st.text_input("Last Rank Held", key="rank")
        st.number_input("Years of Service", min_value=0, step=1, key="years")
        st.selectbox("What’s your current goal?", ["Build my resume", "Prep for interviews", "Explore civilian careers"], key="goal")
        if st.form_submit_button("Continue"):
            st.session_state.onboarded = True
            st.write("DEBUG: Onboarding Completed")
            st.rerun()  # Force rerun so UI updates cleanly

# Check onboarding state
if st.session_state.get("onboarded", False):
    goal = st.session_state.get("goal", "")
    st.write("DEBUG: Onboarding state is true, goal:", goal)

    if goal == "Build my resume":
        st.header("DEBUG: Resume Builder")
        with st.form("resume_form"):
            uploaded_file = st.file_uploader("Upload a FITREP / Evaluation (TXT or PDF)", type=["txt", "pdf"], key="uploaded_file")
            st.text_area("Or paste a summary of your experience", key="manual_input")
            st.text_input("What role are you targeting? (e.g., Cybersecurity Analyst)", key="target_role")
            submit_resume = st.form_submit_button("Generate Resume Bullets")
            st.write("DEBUG: Form submitted value:", submit_resume)

        if submit_resume:
            st.write("DEBUG: Resume form button clicked")
            text = None
            if uploaded_file is not None:
                text = uploaded_file.read().decode("utf-8")
                st.write("DEBUG: Uploaded file detected")
            elif st.session_state.get("manual_input"):
                text = st.session_state.manual_input
                st.write("DEBUG: Manual input detected")
            else:
                st.warning("Please upload a file or paste your experience.")
                st.stop()

            if st.session_state.get("target_role"):
                st.write("DEBUG: Target role provided:", st.session_state.target_role)
                with st.spinner("Translating FITREP to resume bullets..."):
                    bullets = translate_fitrep_to_resume(text, st.session_state.target_role)
                st.write("DEBUG: GPT returned bullets:", bullets)
                st.subheader("Generated Resume Bullets")
                for bullet in bullets:
                    st.write(f"- {bullet}")
            else:
                st.warning("Please enter a target role.")

    elif goal == "Prep for interviews":
        st.header("DEBUG: Interview Prep")
        st.info("Interview prep coming soon.")

    elif goal == "Explore civilian careers":
        st.header("DEBUG: Career Exploration")
        st.info("Career exploration coming soon.")

# Resume Template Picker Section
st.header("DEBUG: Resume Template Picker")
template_files = [f for f in os.listdir("templates") if f.endswith((".docx", ".pdf", ".txt"))]
selected_template = st.selectbox("Select a resume template to download:", template_files, key="template_select")
st.write("DEBUG: Selected template:", selected_template)
if selected_template:
    with open(f"templates/{selected_template}", "rb") as f:
        st.download_button(
            label="📄 Download Resume Template",
            data=f,
            file_name=selected_template,
            mime="application/octet-stream"
        )
