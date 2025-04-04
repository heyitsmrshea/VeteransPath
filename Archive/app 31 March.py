import streamlit as st
from resume_helper import translate_fitrep_to_resume
import base64

# --- Set page config and app title ---
st.set_page_config(page_title="OperationMOS", layout="centered")
st.title("Welcome to OperationMOS")
st.subheader("Your Personal Transition Assistant")

# --- Set background image and clean readable container ---
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        section.main > div {{
            background-color: white;
            padding: 3rem;
            border-radius: 16px;
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
            max-width: 750px;
            margin: auto;
        }}

        .stTextInput > div > div > input,
        .stTextArea > div > textarea,
        .stSelectbox > div {{
            background-color: #f7f7f7;
            border-radius: 8px;
            padding: 0.5rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# set_background("mainpagebackground.jpg")

# --- Session state ---
if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False
if "bullets" not in st.session_state:
    st.session_state["bullets"] = []
if "follow_up_question" not in st.session_state:
    st.session_state["follow_up_question"] = ""
if "original_input" not in st.session_state:
    st.session_state["original_input"] = ""
if "target_role" not in st.session_state:
    st.session_state["target_role"] = ""

# --- Intake form ---
if not st.session_state["form_submitted"]:
    with st.form("background_form"):
        st.markdown("### Tell us a bit about your background:")
        branch = st.selectbox("Branch of Service", ["Army", "Navy", "Marine Corps", "Air Force", "Coast Guard", "Space Force"])
        mos = st.text_input("MOS / Job Code")
        rank = st.text_input("Last Rank Held")
        years = st.number_input("Years of Service", min_value=0, step=1)
        goal = st.selectbox("What's your current goal?", [
            "Build my resume",
            "Prepare for interviews",
            "Map to civilian career",
            "Explore networking tips"
        ])
        submitted = st.form_submit_button("Continue")

    if submitted:
        st.session_state["form_submitted"] = True
        st.session_state["goal"] = goal
        st.success(f"Awesome! Let’s help you {goal.lower()}.")

# --- Resume Builder ---
if st.session_state["form_submitted"] and st.session_state["goal"] == "Build my resume":
    st.header("Resume Builder")

    if not st.session_state["follow_up_question"]:
        st.markdown("### 🧠 Describe your experience in 3 parts")

        high_level = st.text_area("1. What was your role or mission context?")
        responsibilities = st.text_area("2. What were your primary duties or technologies used?")
        impact = st.text_area("3. What outcomes or impact did your work have? (include metrics if possible)")

        target_role = st.text_input("🎯 What role are you targeting? (e.g., Cybersecurity Analyst)")

        if st.button("Generate Resume Bullets"):
            if high_level and responsibilities and impact and target_role:
                full_input = f"""
High-Level Overview:
{high_level}

Roles and Responsibilities:
{responsibilities}

Impact and Outcomes:
{impact}
"""
                st.session_state["original_input"] = full_input
                st.session_state["target_role"] = target_role

                result = translate_fitrep_to_resume(full_input, target_role)

                if "follow_up" in result:
                    st.session_state["follow_up_question"] = result["follow_up"]
                elif "bullets" in result:
                    st.session_state["bullets"] = result["bullets"]
            else:
                st.warning("Please complete all fields.")
    else:
        # Follow-up interaction
        st.warning(f"🧠 GPT needs more info: {st.session_state['follow_up_question']}")
        follow_up_answer = st.text_area("Your answer:")

        if st.button("Submit clarification"):
            combined_input = (
                f"{st.session_state['original_input']}\n\n"
                f"Follow-up Clarification:\n{follow_up_answer}"
            )
            result = translate_fitrep_to_resume(combined_input, st.session_state["target_role"])

            if "bullets" in result:
                st.session_state["bullets"] = result["bullets"]
                st.session_state["follow_up_question"] = ""
            elif "follow_up" in result:
                st.session_state["follow_up_question"] = result["follow_up"]

    # Display results
    if st.session_state["bullets"]:
        st.subheader("✅ Your Structured Resume Content:")
        if len(st.session_state["bullets"]) >= 3:
            st.markdown("### ▸ **Mission Overview**")
            st.markdown(f"- {st.session_state['bullets'][0]}")

            st.markdown("### ▸ **Key Responsibilities**")
            st.markdown(f"- {st.session_state['bullets'][1]}")

            st.markdown("### ▸ **Measurable Impact**")
            st.markdown(f"- {st.session_state['bullets'][2]}")
        else:
            for bullet in st.session_state["bullets"]:
                st.markdown(f"- {bullet}")

# --- Resume Template Download ---
st.header("Choose a Resume Template")

template = st.selectbox("Select a resume template to download:", [
    "Project Manager Template.docx",
    "Cybersecurity Analyst Template.docx",
    "Operations Manager Template.docx"
])

if st.button("Download Resume Template"):
    try:
        with open(f"templates/{template}", "rb") as file:
            st.download_button("📄 Download Resume Template", file, file_name=template)
    except FileNotFoundError:
        st.error(f"Template file '{template}' not found.")
