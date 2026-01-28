# analysis_agent/test_phase2.py

from analyzer import analyze_news

dummy_news = {
    "supplier_name": "Alpha Metals",
    "headline": "Fire breaks out at Alpha Metals factory",
    "content": "Production of steel rods halted due to major fire incident"
}

result = analyze_news(dummy_news)

print("Phase 2 Analysis Result:")
print(result)