import spacy

# ============================================================
# 🔹 Load spaCy model
# ============================================================
nlp = spacy.load("en_core_web_sm")

# ============================================================
# 🔹 CLAUSE KEYWORDS DICTIONARY
# ============================================================

CLAUSE_TYPES = {

    "Payment": [
        "payment",
        "fee",
        "invoice",
        "compensation",
        "amount",
        "salary"
    ],

    "Termination": [
        "terminate",
        "termination",
        "breach",
        "end contract",
        "notice period"
    ],

    "Liability": [
        "liability",
        "damages",
        "loss",
        "responsible"
    ],

    "Confidentiality": [
        "confidential",
        "non disclosure",
        "nda",
        "trade secret"
    ],

    "Indemnity": [
        "indemnify",
        "indemnity",
        "legal claims"
    ],

    "Arbitration": [
        "arbitration",
        "dispute resolution",
        "tribunal"
    ],

    "Intellectual Property": [
        "intellectual property",
        "ip rights",
        "ownership",
        "work product"
    ],

    "Non-Compete": [
        "non compete",
        "competing business"
    ],

    "Auto-Renewal": [
        "auto renew",
        "automatic renewal"
    ],

    "Lock-in Period": [
        "lock in period",
        "minimum term"
    ],
}

# ============================================================
# 🔹 CLAUSE EXTRACTION FUNCTION
# ============================================================

def extract_clauses(text: str):
    """
    Extracts important legal clauses from contract text
    using sentence segmentation + keyword matching.
    Returns a list of clause strings.
    """

    doc = nlp(text)
    clauses = []

    for sent in doc.sents:
        sentence = sent.text.strip().lower()

        for clause_type, keywords in CLAUSE_TYPES.items():
            for keyword in keywords:
                if keyword in sentence:
                    clauses.append(f"[{clause_type}] {sent.text.strip()}")
                    break

    # Remove duplicates while preserving order
    clauses = list(dict.fromkeys(clauses))

    return clauses
