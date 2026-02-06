import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "PARTIES": [],
        "DATES": [],
        "AMOUNTS": [],
        "LOCATIONS": []
    }

    for ent in doc.ents:
        if ent.label_ == "ORG":
            entities["PARTIES"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["DATES"].append(ent.text)
        elif ent.label_ == "MONEY":
            entities["AMOUNTS"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            entities["LOCATIONS"].append(ent.text)

    return entities
