from collections import defaultdict, Counter

# Simulate sensor readings with some noise and metadata
def process_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    counts = Counter(filtered)
    most_common_val = counts.most_common(1)[0][1] if counts else 0

    # Irrelevant statistic
    avg_duplicate_frequency = sum(counts.values()) / len(counts) if counts else 0
    
    temp_store = {}
    for k, v in counts.items():
        temp_store[k] = v * (k % 3)

    # Actual processing path
    squared_total = sum(x**2 for x in filtered if x % 2 == 1)
    adjusted_total = squared_total // (most_common_val if most_common_val > 0 else 1)

    # Dead code branch - never used
    if len(filtered) > 100:
        backup_result = sum(temp_store.values())
    else:
        backup_result = None

    return {'data': filtered, 'adjusted': adjusted_total, 'temp': temp_store}

# Secondary transformation step
def transform_processed(data_obj):
    raw_data = data_obj['data']
    shift_offset = len(raw_data) % 7

    shifted = [(x + shift_offset) * 2 for x in raw_data]
    unique_shifted = list(set(shifted))
    sorted_shifted = sorted(unique_shifted, reverse=True)

    # Distractor: complex but unused structure
    stats_map = defaultdict(int)
    for val in sorted_shifted:
        if val % 4 == 0:
            stats_map['divisible_by_4'] += 1
        elif val % 3 == 0:
            stats_map['divisible_by_3'] += 1

    # Real computation
    selected_vals = [v for v in sorted_shifted if v < 50]
    sum_selected = sum(selected_vals)
    count_above_10 = len([v for v in selected_vals if v > 10])

    return {
        'transformed': sorted_shifted,
        'sum_filtered': sum_selected,
        'valid_count': count_above_10
    }

# Final scoring logic
def calculate_final_score(transformed_obj):
    base = transformed_obj['sum_filtered']
    modifier = transformed_obj['valid_count']

    # Some irrelevant caching simulation
    cache_key = f"score_{base % 5}_{modifier % 4}"
    cache_hint = hash(cache_key) % 1000

    # Core formula
    raw_score = base + (modifier * 11)
    final_score = raw_score if raw_score > 0 else 0

    return final_score

# Main execution flow
if __name__ == "__main__":
    # Input data - simulated sensor array
    sensor_input = [
        3, 5, 2, 8, 5, 3, 9, 5, 7, 2, 4, 6, 5, 3, 1, 9, 5, 3, 8, 7,
        4, 2, 6, 8, 9, 3, 5, 7, 1, 4, 2, 3, 5, 6, 8, 9, 7, 5, 3, 2
    ]

    # Step 1: Process raw data
    processed_data = process_sensor_data(sensor_input)

    # Step 2: Transform the result
    transformed_data = transform_processed(processed_data)

    # Step 3: Calculate final score
    final_score = calculate_final_score(transformed_data)
    
    print(f"Result: {final_score}")