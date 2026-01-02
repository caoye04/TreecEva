def calculate_performance(data_map):
    base_offset = 17
    temp_result = 0
    final_score = 0
    adjustment_factor = 0
    
    # Irrelevant pre-processing: dead computation on unused list
    shadow_buffer = [i ** 2 for i in range(15)]
    cumulative_shift = sum(shadow_buffer) % 97
    
    # Real logic begins: process benchmark data with conditional weighting
    for idx, (key, value) in enumerate(data_map.items()):
        if idx % 2 == 0:
            temp_result += value * (idx + 1)
        else:
            temp_result -= value // 2

    # Secondary processing using dictionary operations and conditional expression
    performance_bins = {i: [] for i in range(5)}
    for k, v in data_map.items():
        bin_key = v % 5
        performance_bins[bin_key].append(v)

    # Distractor: complex but unused sorting operation
    sorted_bins = {}
    for b, vals in performance_bins.items():
        if vals:
            sorted_vals = sorted(vals, reverse=True)
            smoothed = [x - base_offset for x in sorted_vals if x > base_offset]
            sorted_bins[b] = sum(smoothed) if smoothed else 0

    # Adjustment based on modular arithmetic and enumeration
    for i, val in enumerate(data_map.values()):
        if val > 10:
            adjustment_factor += (val % 7) * (i % 3)

    # Critical decision point using conditional expression
    final_score = temp_result + (adjustment_factor if adjustment_factor > 0 else base_offset)

    # Red herring: tuple unpacking that doesn't affect result
    metadata_log = [(k, v, len(str(v))) for k, v in data_map.items()]
    for entry in metadata_log:
        tag, num, size = entry
        size_check = size * 2  # unused

    return final_score

# Main execution
benchmark_data = {'alpha': 12, 'beta': 8, 'gamma': 15, 'delta': 6, 'epsilon': 20}
intermediate_total = sum(benchmark_data.values()) * 2  # irrelevant
scaling_constant = 0.95  # unused
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")