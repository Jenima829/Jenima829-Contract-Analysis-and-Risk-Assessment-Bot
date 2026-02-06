# nlp/preprocessing.py

import re
import spacy
import nltk

from nltk.corpus import stopwords
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


# ---------------- NLTK SETUP ---------------- #

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))


# ---------------- SPACY SAFE LOADER ---------------- #
# IMPORTANT: No downloads at runtime (Streamlit-safe)

def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        # Fallback if model is unavailable
        return spacy.blank("en")


nlp = load_spacy_model()


# ---------------- TEXT CLEANING ---------------- #

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s₹]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ---------------- STOPWORD REMOVAL ---------------- #

def remove_stopwords(text):
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]
    return " ".join(filtered)


# ---------------- LEMMATIZATION ---------------- #

def lemmatize_text(text):
    doc = nlp(text)
    return " ".join(token.lemma_ for token in doc)


# ---------------- HINDI NORMALIZATION ---------------- #

def normalize_hindi(text):
    try:
        return transliterate(
            text,
            sanscript.DEVANAGARI,
            sanscript.ITRANS
        )
    except Exception:
        return text


# ---------------- LEGAL KEYWORD NORMALIZATION ---------------- #

def normalize_legal_terms(text):
    replacements = {
        "terminate": "termination",
        "ended": "termination",
        "breach": "violation",
        "fees": "payment",
        "compensation": "payment",
        "liable": "liability",
    }

    for word, replacement in replacements.items():
        text = text.replace(word, replacement)

    return text


# ---------------- MAIN PREPROCESS PIPELINE ---------------- #

def preprocess_text(raw_text):

    text = normalize_hindi(raw_text)
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    text = normalize_legal_terms(text)

    return text
