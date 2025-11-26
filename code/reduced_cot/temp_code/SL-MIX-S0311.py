import itertools

def account_processor(transactions):
    # Distractor: complex-looking but ultimately unused calculations
    base_balance = 1000
    fee_multiplier = 1.05
    monthly_charges = [25, 15, 30, 20]
    
    # Misleading intermediate results
    processed_fees = sum(monthly_charges) * fee_multiplier
    adjusted_base = base_balance - processed_fees
    
    # Relevant processing logic
    valid_transactions = [tx for tx in transactions if tx > 0]
    grouped_transactions = itertools.groupby(valid_transactions, key=lambda x: x // 100)
    
    # Dead code path
    if len(valid_transactions) > 10:
        bonus_amount = 50
        adjusted_base += bonus_amount
    
    # Core calculation
    transaction_total = sum(valid_transactions)
    balance_adjustment = transaction_total - (len(valid_transactions) * 2)
    
    # Final calculation (this is the relevant one)
    final_result = base_balance + balance_adjustment
    
    # More distractions
    unused_calculation = adjusted_base * 1.1
    redundant_check = final_result if final_result > 500 else 500
    
    return final_result

# Transaction data
transaction_data = [150, 75, -25, 200, 50, -10, 125, 80, 175]

# Process transactions
final_balance = account_processor(transaction_data)
print(f"Result: {final_balance}")