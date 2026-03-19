import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

print("Loading dataset...")
data = pd.read_csv("dataset/transactions.csv")

print("Columns in dataset:", data.columns)

print("Selecting features...")
X = data[
    [
        'Sent tnx',
        'Received Tnx',
        'total Ether sent',
        'total ether received',
        'total ether balance'
    ]
]

print("Training model...")
model = IsolationForest(contamination=0.02)
model.fit(X)

print("Saving model...")
pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully ✅")
