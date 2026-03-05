def generate_alert(wallet, risk_score):
    if risk_score > 75:
        return f"🚨 HIGH RISK ALERT: Wallet {wallet} flagged!"
    elif risk_score > 40:
        return f"⚠️ MEDIUM RISK: Wallet {wallet} suspicious."
    return None