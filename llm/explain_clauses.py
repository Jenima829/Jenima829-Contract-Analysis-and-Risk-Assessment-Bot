# llm/explain_clauses.py

def explain_clauses(clauses):

    explanations = {}
    summary_points = []

    for clause in clauses:

        if "payment" in clause or "fee" in clause:
            explanations[clause] = (
                "This clause explains payment obligations "
                "including amount, timeline, and penalties."
            )
            summary_points.append(
                "Contract defines clear payment responsibilities."
            )

        elif "terminate" in clause:
            explanations[clause] = (
                "This clause defines how the contract can be ended "
                "by either party."
            )
            summary_points.append(
                "Termination conditions are specified."
            )

        elif "liability" in clause:
            explanations[clause] = (
                "This clause outlines financial or legal responsibility "
                "for damages."
            )
            summary_points.append(
                "Liability exposure exists in the contract."
            )

        elif "confidential" in clause:
            explanations[clause] = (
                "This clause protects sensitive business information."
            )
            summary_points.append(
                "Confidentiality obligations are present."
            )

        else:
            explanations[clause] = (
                "This clause defines general contractual obligations."
            )

    # Plain language summary
    summary = " ".join(summary_points)

    return {
        "clause_explanations": explanations,
        "summary": summary
    }
