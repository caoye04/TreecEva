def calculate_financial_summary(transactions):
    base_amount = 1000
    transaction_total = 0
    processed_count = 0
    
    # Process transactions with enumerate
    for idx, amount in enumerate(transactions):
        if amount > 0:
            transaction_total += amount
            processed_count += 1
    
    # Create temporary calculation (distractor)
    temp_adjustment = base_amount * 0.1
    adjustment_factor = temp_adjustment + 50
    
    # Calculate net amount
    net_amount = base_amount + transaction_total
    
    # Bonus calculation using logical operations
    bonus_threshold = 5
    eligible_for_bonus = processed_count > bonus_threshold
    bonus_amount = 200 if eligible_for_bonus else 100
    
    # Final calculation
    final_balance = net_amount + bonus_amount
    
    # Unused intermediate variable (distractor)
    potential_deduction = base_amount - transaction_total
    
    print(f"Final balance: {final_balance}")
    return final_balance

# Transaction data
transaction_data = [150, 75, -30, 200, 50, 125, 25, -10]
result = calculate_financial_summary(transaction_data)
print(f"Target result: {result}")