def analyze_investment_fluctuations(trend_data, volatility_index):
    # Simulate portfolio balance tracking with noise filtering
    initial_capital = 10000
    current_balance = initial_capital
    peak_balance = initial_capital
    loss_count = 0
    recovery_phase = False
    debug_trace = []

    # Auxiliary calculation: irrelevant moving average
    ma_window = [trend_data[i] for i in range(3)]
    moving_avg = sum(ma_window) / len(ma_window)

    scaling_factor = 0.01 * volatility_index
    adjustment_log = []

    for i, (trend, vol) in enumerate(zip(trend_data[3:], volatility_index)):
        # Real signal based on trend and scaled volatility
        signal_strength = trend * (1 + scaling_factor * vol)

        # Balance update logic
        if signal_strength > 0:
            current_balance += int(signal_strength * 100)
            if recovery_phase and current_balance > peak_balance:
                recovery_phase = False
        else:
            current_balance -= int(abs(signal_strength) * 50)
            loss_count += 1
            if current_balance < peak_balance * 0.9:
                recovery_phase = True

        # Critical statement: track peak balance
        peak_balance = max(peak_balance, current_balance)

        # Logging irrelevant intermediate states
        adjustment_log.append(current_balance * 0.05 + vol * 2)
        if i % 2 == 0:
            debug_trace.append((i, current_balance))

    # Post-processing: unrelated smoothing
    smoothed_trace = [x for x in adjustment_log if x > 100]
    if len(smoothed_trace) > 5:
        avg_adjustment = sum(smoothed_trace[:5]) / 5
    else:
        avg_adjustment = 0

    # Dummy loop: distractor computation
    cumulative_shift = 0
    for j in range(3):
        cumulative_shift += j * 2

    print(f"Target result: {peak_balance}")

# Input data
trends = [1.2, -0.8, 0.5, 2.1, -1.3, 0.9, 1.7, -0.4, 3.0, 1.1]
volatility = [3, 7, 2, 8, 6, 4, 9, 1, 10, 5]

analyze_investment_fluctuations(trends, volatility)