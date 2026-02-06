# nlp/contract_classification.py


def classify_contract(text):

    text = text.lower()

    # Keyword dictionary
    contract_keywords = {

        "Employment Agreement": [
            "employee",
            "employer",
            "salary",
            "job role",
            "termination employment",
            "confidentiality employee",
            "non compete"
        ],

        "Vendor Agreement": [
            "vendor",
            "supply",
            "invoice",
            "purchase order",
            "delivery",
            "penalty",
            "indemnity"
        ],

        "Lease Agreement": [
            "lease",
            "rent",
            "premises",
            "security deposit",
            "lock in period",
            "lessee",
            "lessor"
        ],

        "Partnership Deed": [
            "partners",
            "profit share",
            "capital contribution",
            "partnership",
            "mutual consent"
        ],

        "Service Agreement": [
            "services",
            "deliverables",
            "service provider",
            "scope of work",
            "performance metrics"
        ],
    }

    scores = {}

    # Count keyword matches
    for contract_type, keywords in contract_keywords.items():

        score = 0

        for word in keywords:
            if word in text:
                score += 1

        scores[contract_type] = score

    # Get highest score
    detected_type = max(scores, key=scores.get)

    # If no keywords matched
    if scores[detected_type] == 0:
        return "Unknown Contract Type"

    return detected_type
