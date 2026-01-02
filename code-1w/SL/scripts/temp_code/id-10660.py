def evaluate_performance(metrics, base):
    adjustment = 0
    temp_result = 0
    
    # Baseline calibration (irrelevant to final logic but looks important)
    calib_factor = sum([base[i] % (i+1) for i in range(1, len(base))])
    dummy_offset = calib_factor * 0.1
    
    # Key computation path
    if len(metrics) > 3:
        high_vals = {x for x in metrics if x > base[0]}
        low_vals = {x for x in metrics if x <= base[1]}
        
        # Distraction: unused symmetric difference
        symm_diff = high_vals.symmetric_difference(low_vals)
        union_size = len(high_vals.union(low_vals))
        
        # Actual contribution
        intersection_count = len(high_vals.intersection(low_vals))
        
        scale = len(metrics) - len(base)
        
        # Secondary distraction: complex-looking but unused transformation
        transformed = [x * scale + 2 for x in base]
        avg_transformed = sum(transformed) / len(transformed)
        
        temp_result = union_size * 3.5 - intersection_count * 1.2
    else:
        temp_result = min(metrics) * 2
    
    # Final adjustment using irrelevant dummy_offset (no effect due to override)
    final_adjustment = 5
    final_score = int(temp_result + final_adjustment)

    return final_score

# Initial data
baseline = [8, 5, 12, 7]
metric_set = {6, 9, 15, 4, 11}

# Extraneous variables and dead-end calculations
aux_data = [x ** 2 for x in baseline if x % 2 == 0]
dummy_sum = sum(aux_data) * 0.5
flag = False
for x in aux_data:
    if x > 100:
        flag = True

# Key execution point
final_score = evaluate_performance(metric_set, baseline)
print(f"Result: {final_score}")