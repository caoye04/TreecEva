from collections import defaultdict

def calculate_account_balance():
    transactions = [('deposit', 1500), ('withdrawal', 450), ('deposit', 800), ('withdrawal', 300), ('service_fee', 25)]
    account_summary = defaultdict(int)
    temp_calculations = []
    
    # Process transactions
    for transaction_type, amount in transactions:
        if transaction_type == 'deposit':
            account_summary['balance'] += amount
            temp_calculations.append(amount * 1.1)  # Irrelevant calculation
        elif transaction_type == 'withdrawal':
            account_summary['balance'] -= amount
            temp_calculations.append(amount * 0.9)  # Irrelevant calculation
        elif transaction_type == 'service_fee':
            account_summary['fees'] += amount
    
    # Calculate interim values (some are distractors)
    base_balance = account_summary['balance']
    total_fees = account_summary['fees']
    calculated_interest = base_balance * 0.02  # Distractor - not used
    
    # Apply adjustments
    balance_adjustment = 100
    adjusted_balance = base_balance + balance_adjustment
    service_fee = total_fees + 5  # Additional fixed fee
    
    # Final calculation
    final_balance = adjusted_balance - service_fee
    
    # Print irrelevant intermediate values
    print(f"Temp calculations sum: {sum(temp_calculations)}")
    print(f"Calculated interest: {calculated_interest}")
    
    return final_balance

result = calculate_account_balance()
print(f"Target result: {result}")