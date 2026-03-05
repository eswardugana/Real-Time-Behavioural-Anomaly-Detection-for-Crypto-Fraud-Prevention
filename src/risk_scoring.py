from src.config import ANOMALY_THRESHOLD

def compute_risk_score(anomaly_score, centrality):
    score = 0
    
    if anomaly_score < 0:
        score += 50
        
    if centrality > 0.1:
        score += 30
        
    return min(score, 100)