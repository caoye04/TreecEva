def process_transactions(log_entries):
    from collections import Counter
    
    # Initialize balances with irrelevant data
    account_balances = {'checking': 1500, 'savings': 3500, 'investment': 7500}
    irrelevant_counter = Counter(['deposit', 'withdrawal', 'transfer', 'fee'])
    
    # Misleading intermediate calculations
    temp_sum = sum(account_balances.values())
    adjusted_temp = temp_sum * 0.85 + 250  # Dead code path - never used
    
    transaction_log = log_entries
    fee_log = []
    balance_adjustments = {'deposit': 0, 'withdrawal': 0, 'fee': 0}
    
    for entry in transaction_log:
        operation, amount = entry
        
        if operation == 'deposit':
            balance_adjustments['deposit'] += amount
        elif operation == 'withdrawal':
            balance_adjustments['withdrawal'] -= amount
        elif operation == 'fee':
            balance_adjustments['fee'] -= amount
            fee_log.append(amount)
        
        # Distractor: irrelevant tracking
        irrelevant_counter[operation] += 1
    
    # Misleading intermediate result
    gross_adjustment = sum(balance_adjustments.values())
    misleading_total = gross_adjustment * 2 - 500  # Never used
    
    # Critical path with bitwise operations
    initial_balance = 10000
    deposit_total = balance_adjustments['deposit']
    withdrawal_total = balance_adjustments['withdrawal']
    fee_total = balance_adjustments['fee']
    
    # Complex calculation with bitwise and modular arithmetic
    net_change = deposit_total + withdrawal_total + fee_total
    final_balance = initial_balance + net_change
    
    # More distractions
    unused_result = (final_balance & 0xFF) | 0x80  # Bitwise operations - never used
    redundant_check = final_balance % 1000  # Never used
    
    print(f"Final balance: {final_balance}")
    return final_balance

# Transaction data with mixed operations
transaction_data = [
    ('deposit', 2500),
    ('withdrawal', 1200),
    ('deposit', 1800),
    ('fee', 150),
    ('withdrawal', 800),
    ('deposit', 3200),
    ('fee', 75)
]

# Execute the critical statement
final_balance = process_transactions(transaction_data)