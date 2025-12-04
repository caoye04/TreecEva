def process_transactions(accounts, adjustments):
    base_accounts = {'checking': 1500, 'savings': 3200, 'investment': 5800}
    adjustment_factors = [1.05, 0.92, 1.12, 0.88]
    
    # Distractor calculations that don't affect final result
    temp_sum = sum(base_accounts.values()) + len(adjustment_factors)
    irrelevant_metric = temp_sum * 0.15
    
    # Main processing logic
    account_transactions = {}
    for i, (acc_type, balance) in enumerate(base_accounts.items()):
        adjustment_idx = i % len(adjustment_factors)
        adjusted_balance = balance * adjustment_factors[adjustment_idx]
        account_transactions[acc_type] = round(adjusted_balance, 2)
    
    # More distractor operations
    processed_keys = list(account_transactions.keys())
    processed_range = processed_keys[1:3]
    
    # Critical execution point
    final_balance = account_transactions[processed_range[0]] + account_transactions[processed_range[1]]
    
    print(f"Target result: {final_balance}")
    return final_balance

# Execute the function
accounts_data = ['checking', 'savings', 'investment']
adjustment_values = [0.05, -0.08, 0.12]
result = process_transactions(accounts_data, adjustment_values)