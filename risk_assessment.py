"""
Cybersecurity Risk Assessment Framework for Small Businesses
Safe academic implementation: calculates and ranks risk scores from
user-supplied qualitative values. No real systems are scanned.
"""
RISK_LEVELS = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}

def risk_score(likelihood, impact, exposure):
    return likelihood * impact * exposure

def risk_level(score):
    if score >= 81: return "Critical"
    if score >= 48: return "High"
    if score >= 20: return "Medium"
    return "Low"

def rank_risks(risks):
    ranked=[]
    for r in risks:
        score=risk_score(r["likelihood"], r["impact"], r["exposure"])
        ranked.append({**r, "score":score, "level":risk_level(score)})
    return sorted(ranked, key=lambda x:x["score"], reverse=True)

if __name__ == "__main__":
    sample = [
        {"threat":"Ransomware","likelihood":5,"impact":5,"exposure":5},
        {"threat":"Phishing","likelihood":5,"impact":4,"exposure":4},
        {"threat":"Insider threat","likelihood":3,"impact":4,"exposure":5},
        {"threat":"Unpatched systems","likelihood":4,"impact":4,"exposure":3},
    ]
    for r in rank_risks(sample):
        print(f'{r["threat"]}: {r["score"]} ({r["level"]})')
