# risk/risk_mitigation.py

def suggest_mitigation(risk_results):
    """
    Suggest mitigation suggestions for risky clauses.
    Expects:
    {
        Clause,
        Risk,
        Reason
    }
    """

    suggestions = []

    for r in risk_results:
        risk = r["Risk"]
        clause_text = r["Clause"].lower()

        if risk == "High":

            if "liability" in clause_text:
                fix = "Limit liability to the contract value or insured amount."

            elif "indemnify" in clause_text:
                fix = "Convert one-sided indemnity into mutual indemnity."

            elif "terminate" in clause_text:
                fix = "Add a reasonable notice period before termination."

            elif "payment" in clause_text:
                fix = "Include late payment interest or penalty protection."

            else:
                fix = "Review and renegotiate this clause with a legal expert."

            suggestions.append({
                "risk": risk,
                "clause": r["Clause"],
                "text": r["Reason"],
                "fix": fix
            })

    return suggestions
