def calculate_fees(amounts):
    # Distractor: complex fee calculation that's not actually used
    fee_total = sum([amt * 0.02 if amt > 100 else amt * 0.01 for amt in amounts])
    penalty = max(amounts) * 0.05 if len(amounts) > 3 else 0
    return fee_total + penalty

def process_transactions(accounts, transactions):
    balance = accounts['initial']
    processed_count = 0
    
    # Misleading: process deposits first (dead code path)
    for i, trans in enumerate(transactions):
        if trans['type'] == 'deposit':
            balance += trans['amount'] * 0.8  # Wrong multiplier
            processed_count += 1
    
    # Actual processing with zip
    for account_ref, trans in zip(accounts['references'], transactions):
        if trans['type'] == 'deposit':
            balance += trans['amount']
        elif trans['type'] == 'withdrawal':
            balance -= trans['amount']
        
        # Irrelevant: track something that doesn't affect result
        processed_count += account_ref % 2
    
    # Distractor: unused interest calculation
    interest = balance * 0.03 if balance > 500 else balance * 0.01
    
    # Misleading intermediate result
    temp_adjustment = balance - sum([t['amount'] for t in transactions if t['type'] == 'deposit'])
    
    return balance

# Main execution
account_data = {
    'initial': 1000,
    'references': [101, 102, 103, 104]
}

transaction_log = [
    {'type': 'deposit', 'amount': 200},
    {'type': 'withdrawal', 'amount': 150},
    {'type': 'deposit', 'amount': 300},
    {'type': 'withdrawal', 'amount': 75}
]

# Irrelevant: calculate fees that won't be used
unused_fees = calculate_fees([t['amount'] for t in transaction_log])

final_balance = process_transactions(account_data, transaction_log)
print(f"Target result: {final_balance}")