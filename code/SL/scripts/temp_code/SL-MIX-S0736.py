def process_accounts(transactions, initial_amount):
    # Distractor variables and computations
    service_fee = 2.5
    monthly_charges = [5, 10, 15]
    temp_sum = sum(monthly_charges) * 3  # Unused computation
    bonus_multiplier = 1.1
    
    # Relevant processing
    processed = []
    for t in transactions:
        amount = t['amount']
        if t['type'] == 'credit':
            processed.append(amount * bonus_multiplier)
        else:
            processed.append(amount * 0.9)  # 10% fee for debits
    
    # More distractors
    account_ids = [101, 102, 103, 104]
    unused_total = len(account_ids) * service_fee
    
    # Critical computation
    net_change = sum(processed)
    balance = initial_amount + net_change
    
    # Conditional expression and final adjustment
    final_balance = balance - service_fee if balance > 50 else balance + service_fee
    
    # Dead code path
    if balance > 1000:
        extra_bonus = 25
        # This branch never executes with current data
        final_balance += extra_bonus
    
    print(f"Target result: {final_balance}")
    return final_balance

# Transaction data
base_funds = 100
transactions = [
    {'type': 'credit', 'amount': 25},
    {'type': 'debit', 'amount': 40},
    {'type': 'credit', 'amount': 15},
    {'type': 'debit', 'amount': 30}
]

# Execute the key statement
final_balance = process_accounts(transactions, base_funds)