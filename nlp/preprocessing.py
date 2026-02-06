# nlp/preprocessing.py

import re
import spacy
import nltk

from nltk.corpus import stopwords
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


# Download stopwords (first time only)
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


# ---------------- TEXT CLEANING ---------------- #

def clean_text(text):

    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s₹]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text


# ---------------- STOPWORD REMOVAL ---------------- #

def remove_stopwords(text):

    tokens = text.split()

    filtered = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(filtered)


# ---------------- LEMMATIZATION ---------------- #

def lemmatize_text(text):

    doc = nlp(text)

    lemmas = [
        token.lemma_
        for token in doc
    ]

    return " ".join(lemmas)


# ---------------- HINDI NORMALIZATION ---------------- #
# Basic transliteration Hindi → English script

def normalize_hindi(text):

    try:
        normalized = transliterate(
            text,
            sanscript.DEVANAGARI,
            sanscript.ITRANS
        )
        return normalized

    except:
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
