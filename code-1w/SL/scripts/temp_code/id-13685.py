from collections import defaultdict

def calculate_performance(data_log):
    base_points = 0
    penalty = 0
    bonus_tracker = defaultdict(int)
    temp_sum = 0  # irrelevant accumulator

    for entry in data_log:
        size = entry['size']
        latency = entry['latency']
        errors = entry['errors']

        # Core scoring logic
        if latency < 50:
            base_points += 10
            bonus_tracker['speed_bonus'] += 5
        elif latency < 100:
            base_points += 5
        else:
            penalty += 2

        # Irrelevant computation (distractor)
        for i in range(3):
            temp_sum += i * size % 7

        # Real contribution to result
        if errors == 0:
            base_points += 3
        else:
            penalty += errors

    # Another red herring: complex but unused structure
    stats_summary = {f'metric_{k}': v * 2 for k, v in enumerate(bonus_tracker.values())}

    # Actual answer derivation
    raw_score = base_points - penalty
    adjustment = len(bonus_tracker) * 1.5
    final_score = raw_score + adjustment

    return final_score

# Simulated benchmark dataset
benchmark_data = [
    {'size': 120, 'latency': 45, 'errors': 0},
    {'size': 80, 'latency': 95, 'errors': 1},
    {'size': 150, 'latency': 120, 'errors': 0},
    {'size': 60, 'latency': 30, 'errors': 0},
    {'size': 200, 'latency': 110, 'errors': 2}
]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")