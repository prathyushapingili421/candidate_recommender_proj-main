import streamlit as st
from utils.file_parser import parse_resume
from utils.embeddings import get_embedding
from utils.similarity import compute_similarity
from utils.summarizer import generate_fit_summary

st.set_page_config(page_title="Candidate Recommendation Engine", layout="wide")

st.title("📄 Candidate Recommendation Engine")
st.write("Upload resumes and paste the job description to find the best matches.")

job_description = st.text_area("Enter Job Description", height=200)

uploaded_files = st.file_uploader(
    "Upload Candidate Resumes (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write("### Uploaded Resumes:")
    for file in uploaded_files:
        st.write(f"- {file.name}")

if st.button("Run Recommendation Engine"):
    if not job_description:
        st.warning("⚠ Please enter a job description.")
    elif not uploaded_files:
        st.warning("⚠ Please upload at least one resume.")
    else:
        st.success(" Processing resumes...")

        # Step 1: Embed job description
        job_vector = get_embedding(job_description)

        # Step 2: Parse & embed resumes
        resume_data = []
        resume_vectors = []

        for file in uploaded_files:
            resume_text = parse_resume(file)
            resume_vector = get_embedding(resume_text)
            resume_vectors.append(resume_vector)
            resume_data.append({
                "name": file.name,
                "text": resume_text
            })

        # Step 3: Compute similarity
        scores = compute_similarity(job_vector, resume_vectors)

        # Step 4: Attach scores and sort
        for i, score in enumerate(scores):
            resume_data[i]["score"] = score
        resume_data = sorted(resume_data, key=lambda x: x["score"], reverse=True)

        # Step 5: Display results
        st.write("### Top Matches")
        for candidate in resume_data[:10]:
            with st.expander(f"📄 {candidate['name']} — Similarity: {candidate['score']}%"):
                st.markdown("**Why this candidate is a good fit:**")
                summary = generate_fit_summary(job_description, candidate["text"])
                st.write(summary)

