import streamlit as st
from resume_helper import translate_fitrep_to_resume, generate_professional_summary
from fill_resume_template import fill_resume_template
from io import BytesIO
import base64

# --- Page setup ---
st.set_page_config(page_title="OperationMOS", layout="wide")

# --- Session state ---
def init_session():
    keys = [
        "form_submitted", "executive_summary", "job_entries", "started_app",
        "full_name", "email", "phone", "linkedin", "clearance",
        "branch", "mos", "rank", "years",
        "education", "certifications", "resume_file", "fitrep_file"
    ]
    for key in keys:
        if key not in st.session_state:
            if key in ["job_entries", "certifications"]:
                st.session_state[key] = []
            elif key in ["form_submitted", "started_app"]:
                st.session_state[key] = False
            else:
                st.session_state[key] = ""
init_session()

# --- Intro screen ---
if not st.session_state.started_app:
    st.title("Welcome to OperationMOS")
    st.subheader("Your Personal Transition Assistant")
    st.markdown("""
    **OperationMOS** is a free web-based tool designed to help transitioning service members create powerful, civilian-ready resumes.

    💡 In just a few minutes, you’ll:
    - Translate your military experience into civilian language
    - Build a polished, downloadable Word resume
    - Be one step closer to your next mission

    Select a track below to get started:
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Build My Resume"):
            st.session_state.started_app = True
    with col2:
        st.button("Interview Prep (Coming Soon)", disabled=True)
    with col3:
        st.button("LinkedIn Makeover (Coming Soon)", disabled=True)
    st.stop()

# --- Intake Form ---
if not st.session_state.form_submitted:
    st.header("Step 1: Your Background")
    with st.form("background_form"):
        st.markdown("### Military Background")
        st.session_state.branch = st.selectbox("Branch of Service", ["Army", "Navy", "Marine Corps", "Air Force", "Coast Guard", "Space Force"])
        st.session_state.mos = st.text_input("MOS / Job Code")
        st.session_state.rank = st.text_input("Last Rank Held")
        st.session_state.years = st.number_input("Years of Service", min_value=0, step=1)

        st.markdown("### Contact Information")
        st.session_state.full_name = st.text_input("Full Name")
        st.session_state.email = st.text_input("Email")
        st.session_state.phone = st.text_input("Phone Number")
        st.session_state.linkedin = st.text_input("LinkedIn URL")
        st.session_state.clearance = st.text_input("Clearance (optional)")

        st.markdown("### Education")
        st.session_state.education = st.text_input("School, Degree, Graduation Year")
        st.session_state.certifications = st.text_area("Certifications (one per line)").splitlines()

        st.markdown("### Optional Uploads")
        st.session_state.resume_file = st.file_uploader("Upload your existing resume (optional)", type=["pdf", "docx"])
        st.session_state.fitrep_file = st.file_uploader("Upload a FITREP or Eval (optional)", type=["pdf", "docx"])

        submitted = st.form_submit_button("Continue")

    if submitted:
        st.session_state.form_submitted = True
        st.success("Awesome. Now let’s walk through your positions.")

# --- Job Entry Form ---
def job_entry_form(index):
    st.markdown(f"## Position #{index + 1}")
    job = {}
    col1, col2 = st.columns(2)
    with col1:
        job["title"] = st.text_input(f"Job Title", key=f"job_title_{index}")
        job["unit"] = st.text_input(f"Unit / Command", key=f"unit_{index}")
        job["start_date"] = st.text_input(f"Start Date", key=f"start_{index}")
    with col2:
        job["location"] = st.text_input(f"Location", key=f"loc_{index}")
        job["end_date"] = st.text_input(f"End Date", key=f"end_{index}")

    st.markdown("### Describe your experience")
    high_level = st.text_area("1. What was your role or mission context?", key=f"high_{index}")
    responsibilities = st.text_area("2. What were your responsibilities or tools used?", key=f"resp_{index}")
    impact = st.text_area("3. What measurable results did you drive?", key=f"impact_{index}")

    combined_input = f"""
High-Level Overview:
{high_level}

Roles and Responsibilities:
{responsibilities}

Impact and Outcomes:
{impact}
"""
    result = translate_fitrep_to_resume(combined_input, job["title"])
    job["bullets"] = result["bullets"] if "bullets" in result else []
    return job

# --- Builder UI ---
if st.session_state.form_submitted:
    st.header("Step 2: Add Your Positions")
    job_count = st.selectbox("How many past jobs do you want to include?", options=[1, 2, 3], index=0)
    st.session_state.job_entries.clear()
    for i in range(job_count):
        job = job_entry_form(i)
        st.session_state.job_entries.append(job)

    if st.button("Generate Resume (.docx)"):
        st.session_state.executive_summary = generate_professional_summary(
            branch=st.session_state.branch,
            rank=st.session_state.rank,
            mos=st.session_state.mos,
            years=st.session_state.years,
            target_role=st.session_state.job_entries[0]["title"]
        )
        try:
            doc = fill_resume_template(
                template_path="templates/Project Manager Template.docx",
                summary=st.session_state.executive_summary,
                experience_blocks=st.session_state.job_entries,
                full_name=st.session_state.full_name,
                email=st.session_state.email,
                phone=st.session_state.phone,
                linkedin=st.session_state.linkedin,
                clearance=st.session_state.clearance,
                education=st.session_state.education,
                certifications=st.session_state.certifications
            )
            buf = BytesIO()
            doc.save(buf)
            st.download_button("📄 Download Final Resume (.docx)", data=buf.getvalue(), file_name="OperationMOS_Resume.docx")
        except Exception as e:
            st.error(f"❌ Resume generation failed: {e}")
