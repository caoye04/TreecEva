def calculate_final_score(entries, limits):
    temp_results = []
    outlier_count = 0
    scaling_factor = 1.75
    base_offset = 23
    
    for i, (val, flag) in enumerate(zip(entries, [x > limits[0] for x in entries])):
        adjusted = val * scaling_factor + base_offset
        if val < limits[1]:
            adjusted -= 10
        elif val > limits[0]:
            adjusted += 5
            outlier_count += 1
        
        if i % 2 == 0:
            adjusted = round(adjusted)
        else:
            adjusted = int(adjusted)
            
        temp_results.append(adjusted)
    
    # Irrelevant string processing as distractor
    status_labels = ['pass', 'fail', 'warn']
    label_map = {k: v.upper() for k, v in enumerate(status_labels)}
    unused_transformation = [s[::-1] for s in label_map.values()]
    
    # Dead code: this list comprehension has no effect
    [x * 2 for x in temp_results if x < 0]
    
    aggregate = sum(temp_results)
    penalty = outlier_count * 3
    final_score = aggregate - penalty - base_offset
    
    return final_score

# Input data
data_entries = [12, 45, 8, 52, 19, 61]
thresholds = (50, 20)

# Execution
current_state = 'active'
processing_mode = current_state == 'active'
final_score = 0

if processing_mode:
    final_score = calculate_final_score(data_entries, thresholds)

print(f"Result: {final_score}")