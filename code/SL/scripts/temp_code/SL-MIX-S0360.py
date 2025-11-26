def process_transactions(transactions, fee_fn):
    # Initialize account state
    base_balance = 1000
    processing_fee = 15
    bonus_amount = 50
    
    # Irrelevant calculations (distractors)
    temp_sum = sum(range(10))
    conversion_rate = 1.15
    pending_transfers = [25, 75, 100]
    
    # Actual processing logic
    total_credits = 0
    total_debits = 0
    
    for trans in transactions:
        if trans > 0:
            total_credits += trans
        else:
            total_debits += abs(trans)
    
    # Misleading intermediate calculation (dead code path)
    net_flow = total_credits - total_debits
    adjusted_net = net_flow * 0.95  # Never used
    
    # Apply fees using lambda
    total_fees = fee_fn(total_credits + total_debits)
    
    # Main calculation
    final_amount = base_balance + total_credits - total_debits - total_fees + bonus_amount
    
    # More irrelevant operations
    currency_converted = final_amount * conversion_rate
    pending_total = sum(pending_transfers)
    
    return final_amount

# Transaction data
account_data = [150, -25, 300, -100, -50, 200]
fee_calculator = lambda amount: (amount // 100) * 10

# Irrelevant variable initialization
dummy_counter = 0
temp_results = []

# Critical execution point
final_balance = process_transactions(account_data, fee_calculator)

# Print result
print(f"Result: {final_balance}")