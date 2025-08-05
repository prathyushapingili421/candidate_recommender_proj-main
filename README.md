# 📄 Candidate Recommendation Engine

A simple **Streamlit-based web app** that recommends the most relevant candidates for a job based on **semantic similarity** between a job description and uploaded resumes.

The app:
- Accepts a **job description** (text input)
- Accepts **candidate resumes** (PDF, DOCX, TXT)
- Extracts text from resumes
- Generates **embeddings** using Sentence Transformers
- Computes **cosine similarity** between the job description and each resume
- Displays the **Top 5–10 most relevant candidates** with similarity scores
- *(Bonus – Optional)* Generates AI summaries explaining **why each candidate is a good fit**.

---

##  Features
- **Multi-file upload** (PDF, DOCX, TXT)
- **Resume parsing** (PyPDF2, docx2txt)
- **Semantic matching** using `sentence-transformers`
- **Cosine similarity ranking**
- **Top matches display**
- *(Optional)* AI-generated fit summaries using OpenAI GPT models

---

##  Tech Stack
| Component          | Technology Used |
|--------------------|-----------------|
| Frontend + Backend | [Streamlit](https://streamlit.io) |
| Embeddings         | [Sentence Transformers](https://www.sbert.net) – `all-MiniLM-L6-v2` |
| Similarity         | scikit-learn (`cosine_similarity`) |
| File Parsing       | PyPDF2, docx2txt |
| AI Summaries (Bonus) | OpenAI GPT models |

---

##  Project Structure
candidate_recommender/
├── app.py # Main Streamlit app
├── requirements.txt # Project dependencies
├── utils/
│ ├── init.py
│ ├── file_parser.py # Resume text extraction
│ ├── embeddings.py # Embedding generation
│ ├── similarity.py # Similarity computation
│ └── summarizer.py # AI fit summary (optional)
├── sample_resumes/ # Test resumes
├── .env # API keys (if using OpenAI)
└── README.md


---

##  Installation & Setup

### 1 Clone the Repository
git clone 
cd candidate_recommender

### 2 Create a Virtual Environment
python -m venv venv
Activate it:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

### 3 Install Dependencies
pip install -r requirements.txt

### 4  Set Up OpenAI API Key
If you want AI-generated summaries:
Place you open_api_key in the .env file:
OPENAI_API_KEY=your_openai_api_key_here

### Running the App
streamlit run app.py
The app will open in your browser at:
http://localhost:8501

### How It Works
Upload resumes (PDF, DOCX, TXT).

Paste job description.

Click Run Recommendation Engine.

The app:

Extracts text from resumes

Generates embeddings for the job description & resumes

Computes similarity scores

Ranks candidates from highest to lowest match

(Optional) Generates AI summaries of why the candidate fits

### Future Improvements
Skill keyword highlighting

PDF scanning with OCR for scanned resumes

Batch processing for large datasets

Export results as CSV or Excel


### Author
Prathyusha Pingili
