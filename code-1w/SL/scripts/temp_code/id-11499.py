def analyze_financial_sequence():
    # Simulate a financial transaction sequence with noise filtering
    raw_transactions = [120, -50, 30, -10, 200, -250, 80, -40, 70, 60, -90, 110]
    filtered_movements = []
    
    # Apply threshold filter (ignore movements below 20 in magnitude)
    for amount in raw_transactions:
        if abs(amount) >= 20:
            filtered_movements.append(amount)

    # Initialize tracking variables
    current_balance = 100
    peak_balance = current_balance
    transaction_count = 0
    cumulative_drift = 0.0

    # Track index and value using enumerate; use zip for parallel tracking with shifted list
    shifted_movements = filtered_movements[1:] + [0]
    for idx, (move, next_move) in enumerate(zip(filtered_movements, shifted_movements)):
        # Update balance
        current_balance += move
        transaction_count += 1

        # Update peak balance if applicable
        peak_balance = current_balance if current_balance > peak_balance else peak_balance

        # Irrelevant cumulative drift calculation (distractor)
        drift = (move * 0.01) - (next_move * 0.005)
        cumulative_drift += drift

        # Nested conditional: check for recovery pattern (semi-relevant but not used in answer)
        if current_balance < peak_balance * 0.8:
            for recovery_attempt in range(2):
                if recovery_attempt == 1 and next_move > 0:
                    # Dummy correction logic (not actually correcting)
                    dummy_correction = next_move * 0.1
                    break

    # Additional irrelevant computations (dead-end paths)
    final_ratio = cumulative_drift / (transaction_count + 1) if transaction_count > 0 else 0
    snapshot_slice = filtered_movements[::2]  # Slicing distractor
    average_large_move = sum(snapshot_slice) / len(snapshot_slice)

    # Output the required result
    print(f"Target result: {peak_balance}")

analyze_financial_sequence()