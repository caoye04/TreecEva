def analyze_phase(data, threshold):
    count = 0
    temp_sum = 0
    for i, value in enumerate(data):
        if value > threshold:
            count += 1
            temp_sum += value
    return count, temp_sum


def validate_integrity(checksums):
    valid = True
    for c in checksums:
        if c % 2 == 0:
            valid = False
    return valid

# Simulated system benchmark results
benchmark_results = [85, 92, 78, 90, 88, 76, 94, 83]

# Auxiliary diagnostic data (partially irrelevant)
diagnostic_codes = [213, 404, 512, 301, 200]
error_flags = [False, True, False, False, True]
checksums = [111, 223, 335, 447]

# Phase 1: Initial filtering
threshold_a = 80
high_count, total_above = analyze_phase(benchmark_results, threshold_a)

# Misleading intermediate calculation (distractor)
weighted_average = sum(benchmark_results) / len(benchmark_results) * 1.05
adjustment_factor = 0.95 if high_count < 5 else 1.0

# Phase 2: Secondary analysis with tuple unpacking
indices_values = list(enumerate(benchmark_results))
filtered_pairs = [(i, v) for i, v in indices_values if v >= 85]
index_sum = sum(pair[0] for pair in filtered_pairs)
value_sum = sum(pair[1] for pair in filtered_pairs)

# Red herring: unused function call
validate_integrity(checksums)

# Additional distractor variables
baseline_offset = 10
scaling_factor = index_sum / len(filtered_pairs) if filtered_pairs else 0

# Core logic for performance score
def calculate_performance(data):
    score = 0
    for i, val in enumerate(data):
        contribution = 0
        if val >= 90:
            contribution = 4
        elif val >= 80:
            contribution = 3
        elif val >= 70:
            contribution = 2
        else:
            contribution = 1
        # Apply position-based weighting (increasing importance)
        weight = 1 + (i * 0.1)
        score += contribution * weight
    return int(score)

# Critical execution point
temp_diagnostic = sum(diagnostic_codes) // len(error_flags)
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")