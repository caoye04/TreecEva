def process_financial_transactions(initial_capital, transaction_series):
    # Distractor: misleading intermediate calculations
    temp_buffer = initial_capital * 2.5
    processing_fee = temp_buffer * 0.15
    
    # Irrelevant variables for interference
    monthly_interest = 0.08
    annual_growth = initial_capital * monthly_interest * 12
    compound_factor = (1 + monthly_interest) ** 6
    
    # Main logic path with slicing operations
    transaction_pool = [initial_capital]
    for i, amount in enumerate(transaction_series):
        if i % 2 == 0:
            transaction_pool.append(transaction_pool[-1] + amount * 1.2)
        else:
            transaction_pool.append(transaction_pool[-1] - amount * 0.8)
    
    # Dead code path - never executed
    if initial_capital > 100000:
        bonus_funds = initial_capital * 0.25
    else:
        bonus_funds = 0
    
    # Key computations with slicing
    processed_transactions = transaction_pool[1::2]
    adjusted_funds = [x * 0.95 for x in processed_transactions]
    
    # Misleading intermediate result
    temporary_holdings = sum(transaction_pool) - initial_capital
    
    # Critical execution point
    transaction_overflow = adjusted_funds[0] * 0.1 if len(adjusted_funds) > 3 else 0
    final_balance = adjusted_funds[-1] + transaction_overflow
    
    print(f"Target result: {final_balance}")

# Execute the function
initial_deposit = 5000
transactions = [1200, 800, 2500, 1500, 1800, 900]
process_financial_transactions(initial_deposit, transactions)