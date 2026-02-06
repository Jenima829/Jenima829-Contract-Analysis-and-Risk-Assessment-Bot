def calculate_contract_risk(risk_results):

    total = len(risk_results)

    if total == 0:
        return {
            "High": 0,
            "Medium": 0,
            "Low": 0,
            "Overall": "Low"
        }

    high = sum(1 for r in risk_results if r["Risk"] == "High")
    medium = sum(1 for r in risk_results if r["Risk"] == "Medium")
    low = sum(1 for r in risk_results if r["Risk"] == "Low")

    high_pct = round((high / total) * 100, 2)
    medium_pct = round((medium / total) * 100, 2)
    low_pct = round((low / total) * 100, 2)

    # ---- Overall Score Logic ---- #
    if high_pct > 40:
        overall = "High"
    elif medium_pct > 40:
        overall = "Medium"
    else:
        overall = "Low"

    return {
        "High": high_pct,
        "Medium": medium_pct,
        "Low": low_pct,
        "Overall": overall
    }
