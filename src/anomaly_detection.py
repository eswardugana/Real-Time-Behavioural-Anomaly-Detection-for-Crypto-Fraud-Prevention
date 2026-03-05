from sklearn.ensemble import IsolationForest
import joblib

def train_model(X):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    joblib.dump(model, "models/anomaly_model.pkl")
    return model

def load_model():
    return joblib.load("models/anomaly_model.pkl")

def detect_anomalies(model, X):
    scores = model.decision_function(X)
    predictions = model.predict(X)
    return scores, predictions