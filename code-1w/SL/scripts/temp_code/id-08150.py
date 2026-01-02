from itertools import accumulate

def analyze_financial_sequence(transactions, thresholds):
    # Simulate running balance with compound interest on positive days
    running_balance = 0
    daily_balances = []
    compound_factor = 1.0

    for amount in transactions:
        running_balance += amount * compound_factor
        if amount > 0:
            compound_factor *= 1.02  # Interest on gains
        daily_balances.append(round(running_balance, 4))

    # Track peak balance during the period
    peak_balance = max(daily_balances) if daily_balances else 0

    # Irrelevant tracking: count threshold crossings (not used in final result)
    threshold_crossings = 0
    for t in thresholds:
        threshold_crossings += sum(1 for b in daily_balances if b > t)

    # Compute volatility (distractor calculation)
    avg_balance = sum(daily_balances) / len(daily_balances) if daily_balances else 0
    variance = sum((b - avg_balance) ** 2 for b in daily_balances) / len(daily_balances) if daily_balances else 0
    volatility = round(variance ** 0.5, 4)

    # Analyze trend using accumulated changes
    daily_changes = [round(b - a, 4) for a, b in zip(daily_balances, daily_balances[1:])] + [0]

    def analyze_trend(changes, current_peak):
        cum_changes = list(accumulate(changes))
        positive_days = sum(1 for c in changes if c > 0)
        negative_days = sum(1 for c in changes if c < 0)

        # Early return based on strong momentum (logic red herring)
        if positive_days > negative_days and cum_changes[-1] > 50:
            return "GROWING"

        adjustment_factor = 0.85 if len([c for c in changes if c < -10]) > 2 else 1.0
        return "STABLE" if abs(cum_changes[-1] * adjustment_factor) < 20 else "VOLATILE"

    final_trend = analyze_trend(daily_changes, peak_balance)

    # Unused conditional expression (dead logic path)
    status = "Active" if peak_balance > 100 else "Idle"
    backup_check = "Valid" if volatility < 50 else "Review"

    # Final output
    print(f"Result: {peak_balance}")
    return final_trend

# Input data
transaction_flow = [120, -45, 67, -30, 89, 10, -50, 100, -20, 75]
limit_levels = [50, 100, 150]

# Execute function
analyze_financial_sequence(transaction_flow, limit_levels)