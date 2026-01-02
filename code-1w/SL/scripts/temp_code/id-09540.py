def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [x['metric'] for x in data if x['active']]
    
    # Distractor: irrelevant transformation on auxiliary field
    aux_data = [x['aux'] ** 2 for x in data if x['aux'] > 5]  # not used later
    temp_offset = sum(aux_data[:3]) if len(aux_data) >= 3 else 0

    # Slicing and filtering real data
    filtered = raw_values[1:-1]  # exclude first and last
    smoothed = [filtered[i] + filtered[i-1] for i in range(1, len(filtered))]
    
    # Additional distraction: dead computation on unused list
    dummy_aggregate = 0
    for val in smoothed:
        if val % 2 == 0:
            dummy_aggregate += val * 0.1  # never used

    # Real logic: compute baseline trend
    baseline = sum(smoothed) / len(smoothed) if smoothed else 0
    variance = sum((x - baseline) ** 2 for x in smoothed) / len(smoothed) if smoothed else 0

    # Set of operations for noise reduction
    significant = {x for x in smoothed if x > baseline}
    enhancement_factor = len(significant) * 0.75

    # Final performance score with distractor-influenced adjustment
    adjustment = temp_offset * 0.001  # minimal impact but misleading
    final_score = int(baseline + enhancement_factor - adjustment)
    
    return final_score

# Input data construction
benchmark_data = [
    {'metric': 12, 'aux': 3, 'active': False},
    {'metric': 15, 'aux': 6, 'active': True},
    {'metric': 18, 'aux': 7, 'active': True},
    {'metric': 22, 'aux': 4, 'active': True},
    {'metric': 25, 'aux': 8, 'active': True},
    {'metric': 14, 'aux': 9, 'active': True},
    {'metric': 30, 'aux': 2, 'active': False}
]

# Execute main logic
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")