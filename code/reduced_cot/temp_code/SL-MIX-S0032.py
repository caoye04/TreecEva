def calculate_fees(amount, transaction_type):
    fee_multiplier = 0.02 if transaction_type == 'transfer' else 0.015
    processing_cost = amount * 0.008  # irrelevant calculation
    base_fee = 1.5  # unused variable
    return amount * fee_multiplier

def process_transactions(log_entries):
    balance = 1000.0
    daily_limit = 5000  # misleading variable
    fee_tracker = []  # unused list
    
    for idx, entry in enumerate(log_entries):
        amount, trans_type = entry
        fee = calculate_fees(amount, trans_type)
        
        # Distractor calculations
        temp_balance = balance - amount * 1.1  # incorrect calculation
        rolling_sum = sum([x[0] for x in log_entries[:idx+1]]) if idx > 0 else 0
        
        if trans_type == 'transfer':
            balance -= (amount + fee)
            verification_code = (amount * 3) % 17  # irrelevant operation
        else:
            balance -= (amount + fee)
            bonus_points = amount // 10  # unused calculation
    
    account_status = 'active' if balance > 0 else 'inactive'  # unused check
    monthly_fee = 25.0  # misleading variable
    
    return round(balance, 2)

transaction_log = [(200, 'transfer'), (150, 'purchase'), (75, 'transfer'), (300, 'purchase')]
shadow_log = [(100, 'transfer'), (50, 'purchase')]  # irrelevant data
account_summary = {'initial': 1000, 'transactions': 4}  # unused dict

final_balance = process_transactions(transaction_log)
print(f"Result: {final_balance}")