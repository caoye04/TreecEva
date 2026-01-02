def sensor_filter(criteria, readings):
    valid_set = {i for i in range(len(readings)) if readings[i] > criteria[i % len(criteria)]}
    adjust_fn = lambda x: x * 1.5 if x % 2 == 0 else x * 0.8
    adjusted_indices = set(map(adjust_fn, valid_set))
    
    # Irrelevant tracking variables (minimal distraction)
    log_count = len(valid_set)
    temp_buffer = [0] * 3
    
    base_score = sum(adjusted_indices) - min(adjusted_indices, default=0)
    if base_score > 10:
        base_score /= 2
    return int(base_score)

# Main execution
thresholds = [3, 7, 2]
diagnostics = [4, 8, 1, 6, 9, 3]

filtration_score = sensor_filter(thresholds, diagnostics)
print(f"Result: {filtration_score}")