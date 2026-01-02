from collections import defaultdict

# Simulate daily temperature fluctuations and analyze significant deviations
def process_fluctuations(changes, limit):
    positive_jumps = []
    negative_drops = []
    volatility_map = defaultdict(int)
    cumulative_shift = 0
    spike_count = 0  # irrelevant to final result

    for day, change in enumerate(changes):
        cumulative_shift += change
        volatility_map[day] = abs(change)

        if change > limit:
            positive_jumps.append(change)
            spike_count += 1
        elif change < -limit:
            negative_drops.append(change)

    # Misleading computation: uses spike_count but doesn't affect output
    phantom_score = spike_count * 1.5 if len(positive_jumps) > 3 else 0

    # Actual logic: net effect of large movements
    total_surge = sum(positive_jumps)
    total_decline = sum(negative_drops)
    net_volatility = total_surge - abs(total_decline)

    # Secondary red herring: complex conditional with no impact
    adjustment_factor = 0
    if len(positive_jumps) >= len(negative_drops) and cumulative_shift > 0:
        adjustment_factor = 2
    else:
        adjustment_factor = -1  # never used

    # Core result based on processed data
    final_tally = net_volatility + len(volatility_map)  # len adds days with any fluctuation

    return final_tally

# Input data
daily_changes = [3.2, -1.1, 4.5, -2.3, 0.9, 5.1, -6.0, 2.2]
threshold = 2.0

# Execution point of interest
final_tally = process_fluctuations(daily_changes, threshold)

print(f"Result: {final_tally}")