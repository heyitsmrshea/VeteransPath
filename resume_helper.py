def generate_sample_resume_bullets(text):
    return [
        "Led cross-functional team to improve network security across 10+ bases, reducing threats by 40%.",
        "Managed $5M cybersecurity budget, aligning initiatives with operational readiness goals.",
        "Trained and mentored 20+ junior personnel in incident response best practices and cyber hygiene."
    ]

def mock_interview_questions(role):
    if "cyber" in role.lower():
        return [
            "Tell me about a time you responded to a critical incident.",
            "How do you prioritize threats in a large network?",
            "Describe a project where you improved cybersecurity posture."
        ]
    elif "manager" in role.lower():
        return [
            "How do you lead under pressure?",
            "Tell me about a time you dealt with conflict on your team.",
            "How do you manage competing priorities?"
        ]
    else:
        return [
            "Tell me about yourself.",
            "What are your strengths and weaknesses?",
            "Why do you want this job?"
        ]

def suggest_career_paths(interests, mos):
    if "intel" in mos.lower():
        return [
            "Threat Intelligence Analyst",
            "Cybersecurity Consultant",
            "Incident Response Specialist"
        ]
    elif "logistics" in mos.lower():
        return [
            "Supply Chain Analyst",
            "Operations Manager",
            "Project Coordinator"
        ]
    else:
        return [
            "Veteran Transition Coach",
            "IT Support Specialist",
            "Field Service Technician"
        ]