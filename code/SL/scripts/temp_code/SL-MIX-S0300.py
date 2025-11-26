from collections import Counter

def process_transactions(transactions, threshold):
    # Process transaction amounts and filter by threshold
    amounts = [t['amount'] for t in transactions]
    valid_amounts = [amt for amt in amounts if amt >= threshold]
    
    # Calculate some intermediate values (distraction)
    total_sum = sum(amounts)
    avg_transaction = total_sum / len(amounts) if amounts else 0
    
    # Count occurrences of each amount (relevant operation)
    amount_counts = Counter(valid_amounts)
    
    # Find most common valid amount
    if amount_counts:
        most_common = amount_counts.most_common(1)[0]
        base_result = most_common[0] * most_common[1]
    else:
        base_result = 0
    
    # Apply some transformations (mixed relevant/semi-relevant)
    tax_adjustment = base_result * 0.1  # 10% tax (distraction)
    processing_fee = len(valid_amounts) * 2  # $2 per transaction (semi-relevant)
    
    # Final calculation (relevant)
    result = base_result - processing_fee
    return result

# Sample transaction data
transactions = [
    {'amount': 150, 'type': 'purchase'},
    {'amount': 75, 'type': 'refund'},
    {'amount': 200, 'type': 'purchase'},
    {'amount': 150, 'type': 'purchase'},
    {'amount': 50, 'type': 'refund'},
    {'amount': 200, 'type': 'transfer'}
]

threshold = 100

# Process transactions
result = process_transactions(transactions, threshold)
final_result = int(result)

print(f"Target result: {final_result}")