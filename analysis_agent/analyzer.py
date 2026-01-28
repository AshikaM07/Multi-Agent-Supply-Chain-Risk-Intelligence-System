# analysis_agent/analyzer.py

from risk_scoring import calculate_risk_score
from planner import get_supplier_id_by_name, plan_alternatives

def analyze_news(article: dict):
    """
    Convert a news article into a risk decision.
    """

    supplier_name = article.get("supplier_name")
    headline = article.get("headline", "")
    content = article.get("content", "")

    if not supplier_name:
        return None

    full_text = f"{headline} {content}"

    risk_score = calculate_risk_score(full_text)
    supplier_id = get_supplier_id_by_name(supplier_name)

    if not supplier_id:
        return None

    alternatives = []
    if risk_score >= 70:
        alternatives = plan_alternatives(supplier_id)

    return {
        "supplier_name": supplier_name,
        "supplier_id": supplier_id,
        "risk_score": risk_score,
        "alternatives": alternatives,
        "reason": headline
    }