def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count


def smooth_data(values):
    smoothed = [values[0]]
    for i in range(1, len(values)-1):
        avg = (values[i-1] + values[i] + values[i+1]) / 3
        smoothed.append(round(avg))
    smoothed.append(values[-1])
    return smoothed


def calculate_final_score(raw_data, limits):
    # Irrelevant transformation
    processed = [x * 2 for x in raw_data if x > 0]
    processed = processed[::-1]  # Reverse using slicing
    
    # Distractor: complex but unused computation
    outlier_count = 0
    temp_vals = []
    for val in processed:
        if val > limits['max'] * 1.5:
            outlier_count += 1
        temp_vals.append(val ** 0.5)
    
    # Actual logic begins
    clipped = [min(max(x, limits['min']), limits['max']) for x in raw_data]
    filtered = [x for x in clipped if x % 2 == 1]  # Keep only odds
    
    # More distraction
    stats = {
        'sum_temp': sum(temp_vals),
        'peaks': analyze_pattern(clipped)
    }
    
    # Core calculation
    base_score = sum(filtered)
    penalty = 0
    if len(filtered) > 5:
        mid_section = filtered[2:6]  # Slicing used meaningfully
        penalty = sum(mid_section) // 2
    else:
        penalty = len([x for x in clipped if x < limits['min'] + 10])
    
    # Bitwise interference (semi-relevant)
    adjustment = len(processed) ^ 3
    final_score = base_score - penalty + (adjustment & 7)
    
    # Dead code path (never reached due to logic)
    if False and outlier_count > 100:
        final_score *= 0.5
        
    return final_score

# Main execution
raw_input = [12, -5, 8, 19, 22, 13, 7, 4, 16]
dummy_thresholds = {'min': 6, 'max': 20}

# Unused helper call (distractor)
smoothed_data = smooth_data(raw_input)

# Key computation
final_score = calculate_final_score(raw_input, dummy_thresholds)

print(f"Result: {final_score}")