def analyze_financial_sequence(transactions, thresholds):
    initial_reserve = 1000
    current_balance = initial_reserve
    peak_balance = initial_reserve
    volatility_index = 0.0
    adjustment_factor = 1.5
    
    # Track transaction phases and apply conditional modifiers
    for i, amount in enumerate(transactions):
        if i % 3 == 0:
            amount = amount * adjustment_factor if amount > 0 else amount
        elif i % 3 == 1:
            amount = round(amount * 0.9)

        temp_offset = sum([amount % (j+2) for j in range(3)]) if amount > 50 else 0
        current_balance += int(amount) + temp_offset

        # Evaluate threshold crossings
        for threshold in thresholds:
            if current_balance > threshold:
                volatility_index += 0.1 * (current_balance / (threshold + 1))

        # Key statement: update peak balance
        peak_balance = current_balance if current_balance > peak_balance else peak_balance

        # Distractor: simulate audit log (no effect on balance)
        audit_flag = False
        if i in [1, 3]:
            backup_balance = current_balance * 0.95
            audit_flag = True

    # Irrelevant post-processing
    final_volatility = round(volatility_index, 4)
    normalized_peak = peak_balance / initial_reserve
    
    # Output target result
    print(f"Result: {peak_balance}")

# Input data
tx_list = [120, -50, 200, -30, 75]
thresh_values = [1100, 1200]

analyze_financial_sequence(tx_list, thresh_values)