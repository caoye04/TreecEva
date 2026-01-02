from itertools import compress, cycle

# Simulate financial transaction analysis with noise filtering
def analyze_portfolio_flow():
    base_values = [120, -45, 200, -300, 50, 170, -80, 90, -60]
    timestamps = [1623456000, 1623459600, 1623463200, 1623466800, 1623470400,
                  1623474000, 1623477600, 1623481200, 1623484800]
    transaction_types = ['debit', 'credit', 'credit', 'debit', 'credit',
                         'credit', 'debit', 'credit', 'debit']

    # Irrelevant auxiliary data (distractor)
    user_preferences = {'theme': 'dark', 'notifications': True, 'auto_save': False}
    config_flags = [True, False, True, True, False]

    # Misleading intermediate calculation (dead computation)
    avg_gap = sum(timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))) // (len(timestamps) - 1)
    volatility_estimate = sum(abs(x) for x in base_values) / len(base_values)

    # Filter only credit movements above threshold (semi-relevant)
    filtered_moves = [v for v, t in zip(base_values, transaction_types) if t == 'credit' and abs(v) > 40]

    # Augment with cyclical pattern to simulate daily rhythm (distractor)
    daily_cycle = cycle([1.05, 1.02, 0.98, 0.95, 1.01, 1.03])
    augmented_moves = [move * next(daily_cycle) for move in filtered_moves]

    # Convert back to integers (simulate rounding in system)
    rounded_moves = [int(round(x)) for x in augmented_moves]

    # Core logic: compute running balance and track peak
    current_balance = 1000
    peak_balance = current_balance
    temp_shadow = 0  # Unused accumulator (red herring)

    for amount in rounded_moves:
        current_balance += amount
        if current_balance > peak_balance:
            peak_balance = current_balance
        temp_shadow += amount * 0.1  # Distracting side computation

    # Secondary irrelevant structure (nested loop red herring)
    audit_trail = []
    for i in range(len(rounded_moves)):
        for j in range(i, min(i + 2, len(rounded_moves))):
            audit_trail.append(abs(rounded_moves[i] - rounded_moves[j]))

    # Final processing step (key statement)
    final_tally = process_transactions(filtered_moves)

    # Print required result
    print(f"Result: {peak_balance}")


def process_transactions(txns):
    # Helper function that computes weighted score (not used in peak_balance)
    weights = [0.9 ** i for i in range(len(txns))]
    return sum(t * w for t, w in zip(txns, weights))

# Initialize and run
analyze_portfolio_flow()