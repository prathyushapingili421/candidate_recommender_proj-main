#AI Summarizer
import os
from openai import OpenAI
import streamlit as st

api_key = st.secrets["open_api_key"]
client = OpenAI(api_key=api_key)

def generate_fit_summary(job_description, resume_text, model="gpt-3.5-turbo"):
    """
    Uses OpenAI API to generate a short summary explaining candidate fit.
    """
    prompt = f"""
    JOB DESCRIPTION:
    {job_description}

    CANDIDATE RESUME:
    {resume_text[:3000]}

    TASK: Write 2-3 sentences explaining why this candidate is a good fit for the job.
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error generating summary: {e}]"
