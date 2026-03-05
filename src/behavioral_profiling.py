import pandas as pd

def create_behavioral_features(df):
    df['transaction_hour'] = pd.to_datetime(df['timestamp']).dt.hour
    
    wallet_features = df.groupby('from_address').agg({
        'value': ['mean', 'sum', 'count'],
        'transaction_hour': 'mean'
    }).reset_index()

    wallet_features.columns = [
        'wallet',
        'avg_transaction',
        'total_volume',
        'transaction_count',
        'avg_hour'
    ]

    return wallet_features