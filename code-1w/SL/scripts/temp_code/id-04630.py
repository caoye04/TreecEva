def analyze_financial_sequence():
    transactions = [120, -50, 200, -180, 95, -30, 210, -110, 65, -40]
    window_size = 3
    smoothed = []

    # Apply moving average smoothing (irrelevant to final result but adds complexity)
    for i in range(len(transactions) - window_size + 1):
        avg = sum(transactions[i:i+window_size]) / window_size
        smoothed.append(round(avg, 2))

    # Noise threshold filter (distractor computation)
    noise_floor = 75
    filtered_peaks = [x for x in smoothed if abs(x) > noise_floor]

    # Core logic: simulate account balance with peak tracking
    initial_capital = 500
    current_balance = initial_capital
    peak_balance = initial_capital
    withdrawal_penalty_rate = 0.02

    # Simulate daily transaction impacts
    for day, amount in enumerate(transactions):
        if amount < 0:
            penalty = abs(amount) * withdrawal_penalty_rate
            current_balance -= abs(amount) + penalty
        else:
            current_balance += amount

        # Track highest balance observed
        if current_balance > peak_balance:
            peak_balance = current_balance

        # Early exit heuristic (never triggers - dead code path)
        if current_balance < 0.5 * initial_capital and day > 5:
            print("Risk threshold breached")
            break

        # Irrelevant state tracking
        days_remaining = len(transactions) - day - 1
        projected_final = current_balance + sum(t for t in transactions[day+1:] if t > 0)

    # Misleading secondary calculation
    cumulative_inflow = sum(t for t in transactions if t > 0)
    cumulative_outflow = sum(abs(t) for t in transactions if t < 0)
    net_flow = cumulative_inflow - cumulative_outflow

    # Final adjustment unrelated to peak_balance
    final_efficiency = (net_flow / cumulative_inflow) if cumulative_inflow != 0 else 0

    # Output target variable
    print(f"Result: {peak_balance}")

analyze_financial_sequence()