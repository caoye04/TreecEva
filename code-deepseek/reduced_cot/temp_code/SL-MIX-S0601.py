def calculate_account_changes(transactions, initial_deposit):
    total_deposits = initial_deposit
    withdrawal_sum = 0
    temp_accumulator = 0
    
    for idx, amount in enumerate(transactions):
        if amount > 0:
            total_deposits += amount * 1.1  # Red herring calculation
            temp_accumulator += idx * 2
        else:
            withdrawal_sum += abs(amount)
    
    # Unused intermediate calculation
    processed_count = len([x for x in transactions if x != 0])
    
    remaining_balance = total_deposits - withdrawal_sum
    interest_rate = 1.05  # 5% interest
    
    # Distractor operations that don't affect final result
    unused_adjustment = remaining_balance * 0.02
    placeholder_value = sum(range(5))
    
    final_balance = remaining_balance * interest_rate
    print(f"Result: {final_balance}")

# Test execution
transactions = [100, -50, 200, -30, 150, -20]
initial_deposit = 500
calculate_account_changes(transactions, initial_deposit)