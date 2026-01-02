def analyze_financial_sequence():
    # Simulated daily transaction sequence over a 2-week period
    raw_transactions = [120, -45, 200, -180, 50, -30, 300, -250, -80, 400, -150, -70, 600, -500]
    
    # Irrelevant auxiliary data: red herring involving time stamps
    timestamps = [1690000000 + i*86400 for i in range(len(raw_transactions))]
    weekday_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] * 2
    
    # Compute cumulative balance per day
    cumulative_balance = 0
    daily_balances = []
    for amount in raw_transactions:
        cumulative_balance += amount
        daily_balances.append(cumulative_balance)
    
    # Misleading intermediate: average volatility (not used later)
    total_fluctuation = 0
    for i in range(1, len(raw_transactions)):
        total_fluctuation += abs(raw_transactions[i] - raw_transactions[i-1])
    avg_volatility = total_fluctuation / (len(raw_transactions) - 1) if len(raw_transactions) > 1 else 0
    
    # Distractor loop: categorize transaction magnitudes (unused)
    large_tx_count = 0
    medium_tx_count = 0
    for tx in raw_transactions:
        if abs(tx) >= 200:
            large_tx_count += 1
        elif abs(tx) >= 100:
            medium_tx_count += 1
    
    # Focus on last 7 days using slicing
    recent_balances = daily_balances[-7:]
    
    # Compute rolling 3-day balance window to detect spending peaks
    rolling_window = []
    for i in range(len(recent_balances) - 2):
        window_sum = sum(recent_balances[i:i+3])
        rolling_window.append(window_sum)
    
    # Introduce dead code path: redundant check with no impact
    if len(rolling_window) == 0:
        fallback_value = daily_balances[-1]
        rolling_window.append(fallback_value)
    
    # Key computation point
    peak_balance = max(rolling_window)
    
    # Additional irrelevant statistic
    balance_variance = sum((x - sum(rolling_window)/len(rolling_window))**2 for x in rolling_window) / len(rolling_window)
    
    # Output target result
    print(f"Result: {peak_balance}")

analyze_financial_sequence()