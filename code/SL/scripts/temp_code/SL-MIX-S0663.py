def calculate_fee(amount):
    # Distractor function - never actually used
    return amount * 0.02 + 5

def verify_transaction(transaction):
    # Misleading verification that doesn't affect main logic
    return transaction > 0

def process_transaction_data(accounts, transactions):
    # Main processing function
    account_balances = {acc: details['balance'] for acc, details in accounts.items()}
    
    # Irrelevant intermediate calculations
    total_transactions = len(transactions)
    max_transaction = max(transactions) if transactions else 0
    
    # Distractor operations with no effect on final result
    temp_sum = sum(range(1, 10))
    processed_count = 0
    
    # Core logic - process transactions
    for transaction in transactions:
        # Update balance for primary account only
        account_balances['primary'] += transaction
        processed_count += 1
    
    # More irrelevant calculations
    average_transaction = sum(transactions) / len(transactions) if transactions else 0
    
    # Dead code path that's never executed
    if processed_count == 0:
        account_balances['primary'] -= 100
    
    # Final balance calculation
    final_balance = account_balances['primary']
    
    # Distractor operations that don't change the result
    formatted_balance = f"${final_balance:.2f}"
    
    return final_balance

# Account data with multiple accounts (distraction)
account_data = {
    'primary': {'balance': 1000, 'type': 'checking'},
    'secondary': {'balance': 500, 'type': 'savings'},
    'investment': {'balance': 2500, 'type': 'brokerage'}
}

# Transaction log - only primary account transactions matter
# Secondary transactions are distractors
primary_transactions = [150, -75, 300, -50, 125, -25, 200]
secondary_transactions = [100, -30, 75]

# Combine transactions (distraction - secondary don't affect primary)
transaction_log = primary_transactions + secondary_transactions

# Irrelevant preprocessing
sorted_transactions = sorted(transaction_log)
filtered_transactions = [t for t in transaction_log if t > 0]

# Key execution point
final_balance = process_transaction_data(account_data, transaction_log)

# Print result
print(f"Result: {final_balance}")