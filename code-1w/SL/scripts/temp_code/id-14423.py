def calculate_performance(data):
    # Preprocessing phase with some irrelevant transformations
    normalized = [x * 1.05 for x in data if x > 0]
    offset_values = [abs(x - 50) for x in data]
    filtered = [x for x in normalized if x < 100]

    # Irrelevant helper computation (distractor)
    outlier_count = 0
    temp_sum = 0
    for val in offset_values:
        if val > 75:
            outlier_count += 1
        temp_sum += val

    # Core logic: compute weighted score using modular and bitwise ops
    base_total = sum(filtered)
    adjustment_factor = len(data) % 7
    bit_flag = len(filtered) & 3

    # Simulate performance decay based on input size
    decay_rate = 1.0
    if len(data) > 5:
        decay_rate = 0.95
    elif len(data) > 3:
        decay_rate = 0.98

    # Secondary distractor: unused state tracking
    state_log = []
    running_avg = 0
    for i, x in enumerate(normalized):
        running_avg = (running_avg * i + x) / (i + 1) if i > 0 else x
        if i % 2 == 0:
            state_log.append(running_avg * 0.1)

    # Real scoring formula
    raw_score = base_total * decay_rate
    if bit_flag == 1:
        raw_score += adjustment_factor * 2
    elif bit_flag == 2:
        raw_score -= adjustment_factor

    # Final scaling with red herring conditional
    multiplier = 1.1
    if len(offset_values) != len(data):  # Always true, but looks meaningful
        multiplier = 1.05

    final_score = int(raw_score * multiplier)
    
    # Additional misleading accumulation
    dummy_acc = 0
    for x in range(len(state_log)):
        dummy_acc += x * 0.5  # Dead-end calculation

    return final_score

# Input data with mixed characteristics
benchmark_data = [12, -5, 45, 67, 0, 34, 78]

# Execute main logic
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")