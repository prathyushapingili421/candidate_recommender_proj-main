# Embedding generation
from sentence_transformers import SentenceTransformer

# Load the model once (global)
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    """
    Converts text into a numerical embedding vector.
    """
    return model.encode(text, convert_to_tensor=False)  # returns a list/array
