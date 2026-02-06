# llm/suggest_alternatives.py

def suggest_alternatives(clauses):

    alternatives = {}

    for clause in clauses:

        if "unlimited liability" in clause:
            alternatives[clause] = (
                "Suggest capping liability to contract value."
            )

        elif "terminate immediately" in clause:
            alternatives[clause] = (
                "Add 30-day notice period before termination."
            )

        elif "non-compete" in clause:
            alternatives[clause] = (
                "Limit non-compete to 6–12 months."
            )

        else:
            alternatives[clause] = (
                "No major risk. Clause acceptable."
            )

    return alternatives
