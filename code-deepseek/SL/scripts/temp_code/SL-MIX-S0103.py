from collections import Counter

def process_transactions():
    transactions = [150, -45, 78, -120, 200, -30, 89, -15, 42, -68]
    conversion_rate = 0.85
    
    # Distractor operations
    transaction_count = len(transactions)
    positive_txns = [txn for txn in transactions if txn > 0]
    negative_txns = [txn for txn in transactions if txn < 0]
    
    # Counter analysis (distractor)
    freq_analysis = Counter(transactions)
    most_common_txn = freq_analysis.most_common(1)[0][0]
    
    # Main calculation
    total_balance = sum(transactions)
    adjustment_factor = 1.07  # Distractor
    adjusted_total = total_balance * adjustment_factor
    
    # Unused intermediate
    temp_calculation = adjusted_total * conversion_rate
    
    # Final processing
    fee_deduction = 2.5  # Distractor
    processed_total = adjusted_total - fee_deduction
    
    # Target variable
    final_balance = round(processed_total / conversion_rate, 2)
    
    print(f"Result: {final_balance}")
    return final_balance

process_transactions()