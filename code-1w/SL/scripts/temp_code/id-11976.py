def process_data(data, threshold):
    temp_accum = 0
    secondary_cache = []
    meta_state = [0] * len(data)
    backup_sum = 0

    for i in range(len(data)):
        if data[i] < 0:
            backup_sum += abs(data[i])
            continue

        transformed = data[i] ** 0.5 if data[i] % 2 == 0 else data[i] * 2
        meta_state[i] = transformed + 3

        if threshold(transformed):
            temp_accum += int(transformed)
            secondary_cache.append(transformed * 0.5)

    # Distractor: complex-looking but unused reduction
    reduction_factor = sum(secondary_cache) / (len(secondary_cache) + 1e-8)
    decay_adjustment = 0
    for j in range(3):
        decay_adjustment += reduction_factor * (0.9 ** j)

    # Actual logic path
    clean_values = [v for v in meta_state if v > 5]
    aggregate = sum(clean_values) - temp_accum

    # Final computation with lambda-influenced logic
    modifier = (lambda x: x * 1.5 if x > 100 else x * 0.8)(aggregate)
    final_output = int(modifier) - len(secondary_cache)

    return final_output

# Initialization with realistic context
stream_buffer = [16, -5, 9, 25, 4, 0, 36, -12, 49]
threshold_func = lambda x: x > 4
interim_snapshot = [x * 2 for x in stream_buffer if x > 0]  # red herring
baseline_offset = sum(interim_snapshot) // 10  # unused distraction

final_output = process_data(stream_buffer, threshold_func)
print(f"Target result: {final_output}")