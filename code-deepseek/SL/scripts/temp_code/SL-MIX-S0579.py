def process_accounts():
    accounts = {
        'checking': 2450,
        'savings': 1875,
        'investment': 4200,
        'emergency': 3250
    }
    
    # Distractor operations that don't affect final result
    total_assets = sum(accounts.values())
    average_balance = total_assets / len(accounts)
    max_account = max(accounts, key=accounts.get)
    
    # Sort accounts by balance and create ordered dictionary
    sorted_accounts = dict(sorted(accounts.items(), key=lambda x: x[1]))
    account_keys = list(sorted_accounts.keys())
    
    # Additional intermediate calculations (some irrelevant)
    temp_adjustment = 150
    calculated_fee = 25
    net_gain = temp_adjustment - calculated_fee
    
    # Critical execution point
    adjustment = 125
    final_balance = sorted_accounts[account_keys[1]] + adjustment
    
    print(f"Final result: {final_balance}")

process_accounts()