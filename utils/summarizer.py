# AI summary generator
# AI summary generator
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_fit_summary(job_description, resume_text, model="gpt-3.5-turbo"):
    """
    Uses OpenAI GPT model to generate a short summary of why the candidate is a good fit.
    """
    prompt = f"""
    JOB DESCRIPTION:
    {job_description}

    CANDIDATE RESUME:
    {resume_text[:3000]}  # Truncate to avoid hitting token limits

    TASK: Write 2-3 sentences explaining why this candidate is a good fit for the job.
    """

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        summary = response.choices[0].message['content'].strip()
        return summary
    except Exception as e:
        return f"[Error: {e}]"
