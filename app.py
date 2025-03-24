import streamlit as st
from resume_helper import generate_sample_resume_bullets, mock_interview_questions, suggest_career_paths

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
        "Explore civilian careers",
        "Improve my networking presence (coming soon)"
    ])
    submitted = st.form_submit_button("Continue")

if submitted:
    st.success(f"Awesome! Let’s help you {goal.lower()}.")

    if goal == "Build my resume":
        st.header("Resume Builder")
        uploaded_file = st.file_uploader("Upload a FITREP / Evaluation (TXT or PDF)", type=["txt", "pdf"])
        manual_input = st.text_area("Or paste a summary of your experience")

        if st.button("Generate Resume Bullets"):
            if uploaded_file:
                text = uploaded_file.read().decode("utf-8")
            elif manual_input:
                text = manual_input
            else:
                st.warning("Please upload a file or paste your experience.")
                st.stop()

            bullets = generate_sample_resume_bullets(text)
            resume_text = "\n".join([f"- {bullet}" for bullet in bullets])
            st.text_area("Generated Resume Bullets", value=resume_text, height=200)

            st.download_button(
                label="📄 Download Resume Bullets as .txt",
                data=resume_text,
                file_name="resume_bullets.txt",
                mime="text/plain"
            )

    elif goal == "Prep for interviews":
        st.header("Interview Prep")
        target_role = st.text_input("What role are you interviewing for?")
        if st.button("Show Practice Questions"):
            questions = mock_interview_questions(target_role)
            st.subheader(f"Practice Questions for a {target_role} Role")
            for q in questions:
                st.write(f"• {q}")

    elif goal == "Explore civilian careers":
        st.header("Career Exploration")
        interests = st.text_input("What are you interested in?")
        if st.button("Suggest Career Paths"):
            paths = suggest_career_paths(interests, mos)
            st.subheader("Suggested Career Paths")
            for path in paths:
                st.write(f"• {path}")