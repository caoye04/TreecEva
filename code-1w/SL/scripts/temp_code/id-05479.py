def process_metrics(entries, scaling_factors):
    base_offset = 10
    temp_results = []
    cumulative = 0

    # Irrelevant pre-processing: dead code path (never used)
    outlier_buffer = [x for x in scaling_factors if x < 0]
    debug_mode = len(outlier_buffer) > 0

    for i, entry in enumerate(entries):
        # Distractor: complex but unused transformation
        transformed = [val ** 0.5 * scaling_factors[i % len(scaling_factors)] for val in entry['values']]
        avg_val = sum(entry['values']) / len(entry['values'])
        weight = scaling_factors[i % len(scaling_factors)]

        # Real computation path
        score = avg_val * weight + base_offset
        temp_results.append(score)

        # Side calculation with no effect on final result
        cumulative += avg_val * 0.1

    # Actual answer determined here via lambda and zip
    multiplier_map = list(map(lambda x: x * 1.5, scaling_factors))
    weighted_pairs = zip(temp_results, multiplier_map * 2)
    final_components = [a * b for a, b in weighted_pairs][:len(temp_results)]

    final_score = int(sum(final_components) // len(final_components)) if final_components else 0
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
data = [
    {'id': 'A1', 'values': [12, 15, 18]},
    {'id': 'B2', 'values': [20, 10, 30]},
    {'id': 'C3', 'values': [25, 25, 25]},
    {'id': 'D4', 'values': [8, 16, 24]}
]
weights = [2, 3, 1]

# Trigger execution
dummy_tracker = [process_metrics(data, weights) for _ in range(1)]
final_score = dummy_tracker[0]