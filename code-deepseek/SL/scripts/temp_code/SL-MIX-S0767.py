transaction_records = {
    'customer_a': [('deposit', 1000), ('withdrawal', 200), ('deposit', 300)],
    'customer_b': [('deposit', 500), ('withdrawal', 150), ('fee', 25)],
    'customer_c': [('deposit', 800), ('withdrawal', 400), ('bonus', 50)]
}

key_customer = 'customer_b'
processed_transactions = {}

for customer, transactions in transaction_records.items():
    temp_balance = 0
    adjustment_factor = 1.05  # Not actually used in final calculation
    
    for trans_type, amount in transactions:
        if trans_type == 'deposit':
            temp_balance += amount
        elif trans_type == 'withdrawal':
            temp_balance -= amount
        elif trans_type == 'bonus':
            temp_balance += amount
        # Fee transactions are ignored in the calculation
    
    # Distractor: intermediate calculation that doesn't affect final result
    potential_interest = temp_balance * 0.02
    processed_transactions[customer] = temp_balance

# Final assignment - this is the key statement
final_balance = processed_transactions[key_customer]
print(f"Result: {final_balance}")