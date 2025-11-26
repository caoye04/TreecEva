def process_transactions(transaction_list):
    fee_calculator = lambda amount: amount * 0.02 if amount > 100 else amount * 0.01
    processed_amounts = []
    
    total_before_fees = sum(transaction_list)
    irrelevant_check = len([x for x in transaction_list if x % 2 == 0])
    
    for transaction in transaction_list:
        fee = fee_calculator(transaction)
        net_amount = transaction - fee
        processed_amounts.append(net_amount)
        
    # Distractor calculation that doesn't affect final result
    potential_bonus = sum(transaction_list) * 0.005
    bonus_applicable = len(transaction_list) > 3
    
    if bonus_applicable:
        final_net = sum(processed_amounts) + potential_bonus
    else:
        final_net = sum(processed_amounts)
    
    transaction_categories = {'high': [t for t in transaction_list if t > 200], 
                            'medium': [t for t in transaction_list if 100 < t <= 200]}
    high_count = len(transaction_categories['high'])
    
    return round(final_net, 2)

transactions = [150.0, 75.5, 300.0, 45.25, 180.75]
final_result = process_transactions(transactions)
print(f"Result: {final_result}")