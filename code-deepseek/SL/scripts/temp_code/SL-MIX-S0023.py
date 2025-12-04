def account_manager(transactions, rules):
    # Distractor: unused validation logic
    validation_status = {}
    for rule in rules:
        validation_status[rule] = len(rule) > 5
    
    # Distractor: misleading intermediate calculations
    temp_sum = sum(len(tx) for tx in transactions) * 3.14159
    processed_data = [tx.upper() if tx.isalpha() else tx for tx in transactions]
    
    # Relevant: actual balance calculation
    balance_tracker = 1000  # Starting balance
    for operation in transactions:
        if operation.startswith('DEPOSIT_'):
            amount = int(operation.split('_')[1])
            balance_tracker += amount
        elif operation.startswith('WITHDRAW_'):
            amount = int(operation.split('_')[1])
            balance_tracker -= amount
        else:
            # Distractor: unused error handling
            error_count = len([c for c in operation if c.isdigit()])
    
    # Distractor: irrelevant bonus calculation
    bonus_amount = (len(transactions) ** 2) / 4
    seasonal_adjustment = bonus_amount * 0.75
    
    # Key operation: final balance with service fee
    service_fee = max(10, len(transactions) * 2)
    final_balance = balance_tracker - service_fee
    
    print(f"Result: {final_balance}")
    return final_balance

# Main execution
transaction_log = ['DEPOSIT_250', 'WITHDRAW_100', 'DEPOSIT_75', 'WITHDRAW_50']
validation_rules = ['amount_limit', 'frequency_check', 'suspicious_activity']
final_balance = account_manager(transaction_log, validation_rules)