from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: TextRequest):
    doc = nlp(request.text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}