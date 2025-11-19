from dataclasses import dataclass
from typing import List
import math

def secure_data_access():
    class SecureContext:
        def __enter__(self):
            return [
                Transaction(1000, 'A', 1623456789),
                Transaction(2500, 'B', 1623456790),
                Transaction(500, 'A', 1623456788),
                Transaction(3000, 'C', 1623456791)
            ]
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
    return SecureContext()

@dataclass
class Transaction:
    amount: int
    category: str
    timestamp: int

category_weights = {'A': 1.2, 'B': 1.5, 'C': 1.1}

with secure_data_access() as transactions:
    # Sort transactions by timestamp
    sorted_transactions = sorted(transactions, key=lambda t: t.timestamp)
    
    # Calculate weighted scores
    weighted_scores = []
    for tx in sorted_transactions:
        weight = category_weights[tx.category]
        score = tx.amount * weight
        weighted_scores.append(score)
    
    # Apply compliance adjustment based on total score
    total_score = sum(weighted_scores)
    if total_score > 7000:
        adjustment_factor = 0.95
    elif total_score > 5000:
        adjustment_factor = 0.98
    else:
        adjustment_factor = 1.0
    
    # Compute final compliance score
    final_compliance_score = math.floor(total_score * adjustment_factor)

print(f'Result: {final_compliance_score}')