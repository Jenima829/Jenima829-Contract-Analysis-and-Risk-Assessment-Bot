# risk/risk_analysis.py

def analyze_risk(clauses):
    """
    Analyzes risk at clause level.
    Expects clauses as a list of strings.
    """

    risk_results = []

    for clause in clauses:
        clause_lower = clause.lower()

        risk = "Low"
        reason = "Standard clause"

        # -------------------------------
        # HIGH RISK RULES
        # -------------------------------
        if "indemnify" in clause_lower:
            risk = "High"
            reason = "Indemnity obligation detected"

        elif "penalty" in clause_lower or "liquidated damages" in clause_lower:
            risk = "High"
            reason = "Penalty clause detected"

        elif "terminate" in clause_lower and "without notice" in clause_lower:
            risk = "High"
            reason = "Unilateral termination without notice"

        # -------------------------------
        # MEDIUM RISK RULES
        # -------------------------------
        elif "liability" in clause_lower:
            risk = "Medium"
            reason = "Liability exposure clause"

        elif "confidential" in clause_lower or "nda" in clause_lower:
            risk = "Medium"
            reason = "Confidentiality obligation"

        elif "auto renew" in clause_lower or "automatic renewal" in clause_lower:
            risk = "Medium"
            reason = "Auto-renewal clause"

        # -------------------------------
        # SAVE RESULT
        # -------------------------------
        risk_results.append({
            "Clause": clause,
            "Risk": risk,
            "Reason": reason
        })

    return risk_results
