def calculate_account_metrics(accounts):
    processing_results = {}
    temp_analysis = {}
    account_ids = []
    
    # Irrelevant data processing
    dummy_data = [15, 27, 8, 42, 33, 19]
    filtered_dummy = [x for x in dummy_data if x % 3 == 0]
    dummy_sum = sum(filtered_dummy)  # This is unused
    
    # Main account processing
    for i, (account_id, transactions) in enumerate(accounts):
        account_ids.append(account_id)
        
        # Misleading intermediate calculation
        if len(transactions) > 2:
            temp_sum = sum(transactions)
            temp_analysis[account_id] = temp_sum * 2  # Red herring
        
        # Actual processing logic
        net_flow = transactions[-1] - transactions[0] if transactions else 0
        for j, trans in enumerate(transactions):
            if j > 0:
                net_flow += trans * (1 if j % 2 == 0 else -1)
        
        # Conditional branch with early optimization
        if net_flow > 50:
            processing_results[account_id] = net_flow // 2
        elif net_flow < -20:
            processing_results[account_id] = net_flow * 3
        else:
            processing_results[account_id] = abs(net_flow)
    
    # Distractor operations
    unused_calc = [x**2 for x in range(10)]
    dummy_multiplier = len(unused_calc) * 2  # Dead code path
    
    # Critical computation
    multiplier = 2 if len(account_ids) % 2 == 0 else 3
    final_balance = processing_results.get(account_ids[-1], 0) * multiplier
    
    print(f"Target result: {final_balance}")

# Sample execution
accounts_data = [
    (101, [100, 25, 75, 50]),
    (102, [200, 80, 120]),
    (103, [150, 90, 60, 30]),
    (104, [300, 150, 50])
]
calculate_account_metrics(accounts_data)