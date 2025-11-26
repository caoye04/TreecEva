def process_financial_records(transactions):
    # Initialize account data
    base_balance = 1000
    processed_amounts = []
    temp_calculations = {}
    
    # Process transactions (distractor - not used in final result)
    for trans in transactions:
        if trans > 0:
            processed_amounts.append(trans * 1.1)  # 10% processing fee
        else:
            processed_amounts.append(trans * 0.9)  # 10% discount on withdrawals
    
    # Set operations to find unique transaction values
    unique_transactions = set(transactions)
    duplicate_check = len(transactions) - len(unique_transactions)
    
    # Core calculation with some irrelevant intermediate steps
    total_deposits = sum([t for t in transactions if t > 0])
    total_withdrawals = sum([abs(t) for t in transactions if t < 0])
    
    # This calculation is partially relevant but not fully used
    net_flow = total_deposits - total_withdrawals
    adjusted_flow = net_flow * 0.95  # 5% adjustment (distractor)
    
    # The key calculation chain
    remaining_balance = base_balance + total_deposits - total_withdrawals
    processed_data = {'remaining': remaining_balance, 'adjusted': adjusted_flow}
    
    # Final assignment
    final_balance = processed_data['remaining']
    
    print(f"Target result: {final_balance}")
    return final_balance

# Test data
transaction_records = [200, -50, 300, -150, 100, -75, -25]
result = process_financial_records(transaction_records)