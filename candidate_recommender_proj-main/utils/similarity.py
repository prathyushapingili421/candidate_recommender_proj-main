# Similarity calculations
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_similarity(job_vector, resume_vectors):
    """
    Compares the job description vector with each resume vector.
    Returns a list of similarity scores (0–100%).
    """
    scores = cosine_similarity([job_vector], resume_vectors)[0]
    return np.round(scores * 100, 2)  # convert to % and round