def apply_rule(amount, rule_type):
    # Misleading intermediate calculations
    temp_adjust = (amount % 7) * 3.14
    irrelevant_metric = temp_adjust ** 2 / 100
    
    if rule_type == 'premium':
        return amount * 0.85
    elif rule_type == 'standard':
        return amount * 0.95
    else:
        # Dead code path - never executed
        unused_computation = amount + irrelevant_metric
        return amount * 1.1

def process_transactions(transactions, discount_rules):
    processed_total = 0
    bonus_points = 0
    
    # Distractor operations
    running_sum = sum(transactions.values()) * 1.25
    temp_set = set(discount_rules.values())
    category_count = len(temp_set)
    
    for customer, amount in transactions.items():
        rule = discount_rules.get(customer, 'standard')
        discounted = apply_rule(amount, rule)
        
        # Relevant logic chain
        if amount > 500:
            bonus_points += int(amount * 0.02)
        
        processed_total += discounted
        
        # Misleading intermediate calculation
        if customer.startswith('C'):
            running_sum -= 50
    
    # Final computation with interference
    adjustment_factor = (bonus_points % 13) / 100
    final_amount = processed_total - adjustment_factor
    
    # Red herring - unused result
    potential_bonus = bonus_points * 2.5
    
    return round(final_amount, 2)

# Main execution
customer_transactions = {
    'C001': 750.0,
    'C002': 350.0,
    'B001': 1200.0,
    'A005': 280.0
}

discount_policies = {
    'C001': 'standard',
    'B001': 'premium',
    'A005': 'standard'
}

# Additional misleading variables
revenue_streams = [150, 200, 75, 300]
projected_growth = sum(revenue_streams) * 1.15

final_result = process_transactions(customer_transactions, discount_policies)
print(f"Result: {final_result}")