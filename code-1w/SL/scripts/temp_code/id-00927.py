from itertools import combinations

def analyze_component(data, threshold):
    count = 0
    temp_sum = 0
    for i, val in enumerate(data):
        if val > threshold:
            count += 1
            temp_sum += val * 0.1
    return count

def validate_sequence(seq):
    valid = True
    for a, b in zip(seq, seq[1:]):
        if abs(a - b) > 5:
            valid = False
    return valid

def calculate_performance(results):
    baseline = [3, 7, 4, 8, 5]
    adjustment_factor = 0.0
    outlier_count = 0

    # Irrelevant combination analysis (distractor)
    for combo in combinations(baseline, 3):
        combo_sum = sum(combo)
        if combo_sum > 15:
            adjustment_factor += 0.1

    # Real logic begins: counting how many sublists exceed threshold
    high_performers = 0
    for result in results:
        if analyze_component(result, 6) >= 2:
            high_performers += 1

    # Dummy validation pass (semi-relevant but not used directly)
    for result in results:
        validate_sequence(result)

    # Accumulation with red herring variables
    total_aggregate = 0
    peak_values = []
    for idx, res in enumerate(results):
        max_val = max(res)
        peak_values.append(max_val)
        if max_val > 9:
            total_aggregate += max_val

    # Final computation using actual logic path
    scaling_multiplier = len(peak_values) if high_performers > 0 else 1
    final_score = high_performers * scaling_multiplier + total_aggregate // 2

    # Dead code path (never executed - mild interference)
    if False:
        fallback = sum(peak_values) / len(peak_values)
        final_score = fallback

    return final_score

# Input data
benchmark_results = [
    [5, 6, 7, 8, 6],
    [9, 4, 3, 7, 8],
    [10, 11, 12, 6, 8],
    [2, 3, 4, 5, 6]
]

# Key execution point
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")