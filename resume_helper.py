
import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("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")

def translate_fitrep_to_resume(text, target_role):
    prompt = f"""
You are a resume coach for military veterans. Translate the following FITREP text into 3 strong civilian resume bullets.
Use impactful action verbs, include measurable outcomes, and tailor it to a {target_role} role.

FITREP text:
{text}

Resume bullets:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"].strip().split("\n")
