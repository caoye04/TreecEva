def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [x['metric'] for x in data]
    weights = [0.1, 0.2, 0.3, 0.4]  # assumed distribution

    # Irrelevant distraction: calculating cumulative products (not used)
    cumprod = 1
    for val in raw_values:
        cumprod *= val + 1

    # Secondary distraction: tracking state that doesn't affect output
    temp_buffer = []
    for i, v in enumerate(raw_values):
        if i % 2 == 0:
            temp_buffer.append(v ** 0.5)

    # Actual logic begins: weighted sum with conditional boost
    base_sum = sum(a * b for a, b in zip(raw_values[:4], weights))

    # Conditional performance boost based on threshold pattern
    threshold_met = sum(1 for x in raw_values if x > 50)
    boost_factor = 1.0
    if threshold_met >= 2:
        boost_factor = 1.25

    # Additional red herring: unused min/max analysis
    max_val = max(raw_values)
    min_val = min(raw_values)
    range_val = max_val - min_val  # not used

    # Core calculation
    adjusted_score = base_sum * boost_factor

    # Normalize by number of entries (even though only 4 used)
    normalization_factor = len(data) or 1
    normalized_score = adjusted_score / normalization_factor

    # Final transformation using lambda (irrelevant for most cases but applied uniformly)
    transform = lambda x: x + 10 if x < 20 else x
    final_score = transform(normalized_score)

    return final_score

# Simulated benchmark data
benchmark_data = [
    {'id': 'A', 'metric': 60, 'flag': False},
    {'id': 'B', 'metric': 75, 'flag': True},
    {'id': 'C', 'metric': 30, 'flag': False},
    {'id': 'D', 'metric': 80, 'flag': True},
    {'id': 'E', 'metric': 20, 'flag': False}
]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")