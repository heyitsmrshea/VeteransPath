
import streamlit as st
import os
from resume_helper import translate_fitrep_to_resume

st.set_page_config(page_title="VeteranPath", layout="centered")
st.title("Welcome to VeteranPath")
st.subheader("Your Personal Transition Assistant")

# Step 1: Onboarding
with st.form("onboarding"):
    st.write("Tell us a bit about your background:")
    branch = st.selectbox("Branch of Service", ["Army", "Navy", "Air Force", "Marines", "Coast Guard", "Space Force"])
    mos = st.text_input("MOS / Job Code")
    rank = st.text_input("Last Rank Held")
    years = st.number_input("Years of Service", min_value=0, step=1)
    goal = st.selectbox("What’s your current goal?", [
        "Build my resume",
        "Prep for interviews",
        "Explore civilian careers"
    ])
    submitted = st.form_submit_button("Continue")

if submitted:
    st.success(f"Awesome! Let’s help you {goal.lower()}.")

    if goal == "Build my resume":
        st.header("Resume Builder")
        with st.form("resume_form"):
            uploaded_file = st.file_uploader("Upload a FITREP / Evaluation (TXT or PDF)", type=["txt", "pdf"])
            manual_input = st.text_area("Or paste a summary of your experience")
            target_role = st.text_input("What role are you targeting? (e.g., Cybersecurity Analyst)")
            submit_resume = st.form_submit_button("Generate Resume Bullets")

        if submit_resume:
            if uploaded_file:
                text = uploaded_file.read().decode("utf-8")
            elif manual_input:
                text = manual_input
            else:
                st.warning("Please upload a file or paste your experience.")
                st.stop()

            if target_role:
                bullets = translate_fitrep_to_resume(text, target_role)
                st.subheader("Generated Resume Bullets")
                for bullet in bullets:
                    st.write(f"- {bullet}")
            else:
                st.warning("Please enter a target role.")

    elif goal == "Prep for interviews":
        st.header("Interview Prep")
        st.info("Coming soon: Role-specific mock questions and STAR-style practice.")

    elif goal == "Explore civilian careers":
        st.header("Career Exploration")
        st.info("Coming soon: Job matches based on MOS, skills, and interests.")

# Resume Template Picker
st.header("Choose a Resume Template")
template_files = [f for f in os.listdir("templates") if f.endswith((".docx", ".pdf", ".txt"))]
selected_template = st.selectbox("Select a resume template to download:", template_files)

if selected_template:
    with open(f"templates/{selected_template}", "rb") as f:
        st.download_button(
            label="📄 Download Resume Template",
            data=f,
            file_name=selected_template,
            mime="application/octet-stream"
        )
