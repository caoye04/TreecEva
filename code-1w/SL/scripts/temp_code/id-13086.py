def analyze_financial_trajectory():
    transactions = [120, -50, 200, -300, 180, -40, 250, -100, 30, 70]
    thresholds = [100, 200, 150, 300]
    
    # Irrelevant tracking variables (distractors)
    cumulative_drift = 0
    adjustment_factor = 1.05
    spike_count = 0
    normalized_flux = 0.0
    
    current_balance = 100
    peak_balance = current_balance
    recovery_phase = False
    grace_period_remaining = 3
    
    for i in range(len(transactions)):
        tx = transactions[i]
        
        # Simulate balance fluctuation with conditional logic
        if tx > 150:
            spike_count += 1
            recovery_phase = True
            grace_period_remaining = 2
        
        current_balance += tx
        
        # Update peak only if not in artificial suppression zone
        if grace_period_remaining <= 0 and current_balance > peak_balance:
            peak_balance = current_balance
        
        # Irrelevant normalization calculation (dead computation path)
        if current_balance != 0:
            normalized_flux += abs(tx / current_balance)
        
        # Decrement grace period
        if grace_period_remaining > 0:
            grace_period_remaining -= 1
        
        # Additional red herring: simulate drift correction
        cumulative_drift += tx * (adjustment_factor - 1)
        
        # Extra conditional with slicing distraction
        if i >= 3:
            recent_txs = transactions[i-2:i+1]
            avg_recent = sum(recent_txs) / len(recent_txs)
            if avg_recent > 50:
                current_balance += 10  # minor boost
        
        # Critical update point
        peak_balance = max(peak_balance, current_balance)
        
    # Print result as required
    print(f"Result: {peak_balance}")

analyze_financial_trajectory()