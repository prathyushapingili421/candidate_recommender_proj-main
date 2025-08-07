# Candidate Recommendation Engine

This is a Streamlit app I built to help recommend the most relevant candidates for a job, based on how well their resumes match a job description. It uses NLP embeddings to calculate similarity scores and also generates short AI summaries explaining why each candidate is a good fit.

### What it does:
- Accepts a job description (text input)
- Lets you upload resumes (PDF, DOCX, TXT)
- Extracts and parses resume text
- Converts both the job description and resumes into embeddings
- Computes cosine similarity to rank candidates
- Shows the top matches (only those above 50% similarity)
- Uses OpenAI to generate a short fit summary for each top candidate

---

## Features
- Multiple file upload (PDF, DOCX, TXT)
- Resume parsing using PyPDF2 and docx2txt
- Semantic similarity using Sentence Transformers (`all-MiniLM-L6-v2`)
- Cosine similarity ranking
- GPT-generated summaries for top candidates
- Streamlit UI for ease of use

---

## Tech Stack

- Streamlit (frontend + backend)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Scikit-learn (`cosine_similarity`)
- PyPDF2, docx2txt (file parsing)
- OpenAI API (for generating summaries)
- Deployed on Streamlit Cloud

---

## Project Structure

candidate_recommender/
- ├── app.py # Main Streamlit app
- ├── requirements.txt # Python dependencies
- ├── .streamlit/
- │  └── secrets.toml # Used for OpenAI API key on Streamlit Cloud
- ├── utils/
- │ ├── file_parser.py # Resume parsing
- │ ├── embeddings.py # Embedding logic
- │ ├── similarity.py # Cosine similarity
- │ └── summarizer.py # GPT summaries
- ├── sample_resumes/ # Example resumes
- ├── .env # Local secret key file (not uploaded)
- └── README.md


---

## How to Run Locally

1. Clone the repo  
```bash
git clone https://github.com/prathyushapingili421/candidate_recommender_proj-main.git
cd candidate_recommender_proj-main
```
2. Create a virtual environment
 ```bash
   python -m venv venv
```
3. Activate it
```bash
  - Windows: venv\Scripts\activate
  - Mac/Linux: source venv/bin/activate
```
4. Install dependencies
```bash
  pip install -r requirements.txt
```
5. Add your OpenAI API key in a .env file
```bash
   open_api_key=your_key_here
   ```
6. Run the app
```bash
    streamlit run app.py
```
### How to Deploy on Streamlit Cloud
- Push your project to GitHub (don’t include .env)
- Go to https://streamlit.io/cloud and create a new app
- Point it to your GitHub repo and app.py file
- Under the Secrets tab, add:
    ```bash
    open_api_key = "your_key_here"
    ```
- Deploy and share the link

### How it works
Once you upload the resumes and paste the job description:
  - It reads and parses all the files
  - Uses Sentence Transformers to create embeddings
  - Compares each resume with the job description using cosine similarity
  - Ranks the resumes based on score
  - For the ones scoring above 50%, it uses GPT to summarize why the candidate is a good fit

### Improvements I'd like to make later
- CSV export of the top candidates
- Highlight matching skills/keywords
- OCR support for scanned resumes
- Possibly add login/auth for private team use

### Author:  Prathyusha Pingili
### GitHub: https://github.com/prathyushapingili421/candidate_recommender_proj-main
### Deployed streamlit app: https://candidaterecommenderproj-main-9ptjt3e4dh5vqzwrtaxffg.streamlit.app/
---

