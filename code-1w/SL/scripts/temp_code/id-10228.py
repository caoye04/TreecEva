def analyze_pattern(sequence):
    temp_results = []
    running_total = 0
    
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            running_total += val ** 2
        else:
            running_total -= val // 2
        temp_results.append(running_total)
    
    # Distractor: irrelevant transformation
    scaled_vals = [x * 0.95 for x in temp_results if x > 0]
    average_temp = sum(scaled_vals) / len(scaled_vals) if scaled_vals else 0

    # Real processing branch
    filtered = [x for x in temp_results if x % 3 == 0]
    return filtered if filtered else [0]


def calculate_rating(data, factors):
    base_rating = 0
    adjustments = []
    
    for idx, (val, weight) in enumerate(zip(data, factors)):
        contribution = val * weight
        adjustments.append(contribution)
        
        if idx > 0 and contribution < adjustments[idx-1]:
            base_rating -= 1
        else:
            base_rating += val % 5
    
    # Dead code path - misleading
    if len(adjustments) > 10:
        normalization = sum(adjustments) / 100
    else:
        normalization = 0  # never used
    
    # Final computation
    final_rating = base_rating + sum(adjustments) % 17
    return int(final_rating)

# Main execution
readings = [4, 7, 2, 9, 6, 3, 8]
weights = [0.8, 1.2, 0.5, 1.0, 0.7, 1.1, 0.9]

# Irrelevant preprocessing
processed_readings = [x + 1 for x in readings]
duplicate_check = {x: processed_readings.count(x) for x in set(processed_readings)}

convergence_list = analyze_pattern(readings)

# Key state tracking
status_flags = [True if x > 0 else False for x in convergence_list]
flag_summary = sum(1 for f in status_flags if f)

final_score = calculate_rating(convergence_list, weights)

print(f"Result: {final_score}")