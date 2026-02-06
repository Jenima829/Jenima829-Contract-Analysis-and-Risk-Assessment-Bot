# utils/highlighter.py

def highlight_text(text, risk_results):
    """
    Highlights risky clauses in the contract text.
    Expects risk_results as a list of dicts:
    {
        Clause,
        Risk,
        Reason
    }
    """

    highlighted = text

    for r in risk_results:
        clause = r["Clause"]
        risk = r["Risk"]

        if risk == "High":
            color = "#ffcccc"   # red
        elif risk == "Medium":
            color = "#fff3cd"   # yellow
        else:
            continue

        highlighted = highlighted.replace(
            clause,
            f"<span style='background-color:{color}; padding:2px;'>{clause}</span>"
        )

    return highlighted
