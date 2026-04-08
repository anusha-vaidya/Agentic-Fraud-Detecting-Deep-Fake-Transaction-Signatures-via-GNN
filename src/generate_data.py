import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_agentic_fraud_data(n_rows=10000):
    # 1. Generate Base Data (The "Humans")
    data = {
        'transaction_id': range(n_rows),
        'timestamp': [datetime.now() - timedelta(minutes=np.random.randint(0, 10000)) for _ in range(n_rows)],
        'amount': np.round(np.random.uniform(10, 5000, n_rows), 2),
        'user_id': np.random.randint(1000, 9000, n_rows),
        'is_fraud': 0
    }
    df = pd.DataFrame(data)

    # 2. Inject "Agentic" Fraud (The "Deep-Fake" Signature)
    # We simulate a "Hydra" attack: 100 accounts acting at the EXACT same millisecond
    fraud_time = datetime.now()
    fraud_rows = []
    for i in range(500):
        fraud_rows.append({
            'transaction_id': n_rows + i,
            'timestamp': fraud_time, # Identical timestamp = Bot signature
            'amount': 1000.00,       # Identical amounts
            'user_id': 9999 + (i % 50), # 50 accounts rotating quickly
            'is_fraud': 1
        })
    
    fraud_df = pd.DataFrame(fraud_rows)
    final_df = pd.concat([df, fraud_df]).sample(frac=1).reset_index(drop=True)
    
    # Save to the data folder
    final_df.to_csv('data/raw/transactions.csv', index=False)
    print(f"Successfully generated {len(final_df)} transactions.")

if __name__ == "__main__":
    generate_agentic_fraud_data()
