def process_temperatures(data):
    # Irrelevant transformation: Convert to Fahrenheit (not used in result)
    fahrenheit_data = [(temp * 9/5) + 32 for temp in data if temp > -273]
    
    # Distractor variable: counts positive temps but not used in final logic
    positive_count = sum(1 for temp in data if temp > 0)
    
    # Key processing: normalize and filter extreme values
    normalized = [round(temp / max(data), 4) for temp in data]
    
    # Conditional expression used: clamp values below threshold
    adjusted = [val if val >= 0.1 else 0.1 for val in normalized]
    
    # Intermediate calculation with semi-relevant logic
    magnitude_score = sum(abs(val) for val in adjusted) * len(data)
    
    # Simulate sensor reliability weighting (some dead computation)
    weights = {}
    for i, val in enumerate(data):
        if val < -50:
            weights[i] = 0.5
        elif val > 50:
            weights[i] = 0.7
        else:
            weights[i] = 1.0
    
    # Unused weighted average (red herring)
    weighted_avg = sum(normalized[i] * weights[i] for i in range(len(data))) / len(data)

    # Core logic: find first significant drop after peak
    peak_index = normalized.index(max(normalized))
    post_peak = normalized[peak_index + 1:]
    drop_found = False
    for i in range(1, len(post_peak)):
        if post_peak[i] < post_peak[i-1] * 0.95:  # 5% drop threshold
            drop_found = True
            break
    
    # Final output depends on whether a drop was detected and magnitude score
    final_output = int(magnitude_score) if drop_found else int(magnitude_score * 0.5)
    
    # Additional irrelevant state tracking
    status_log = {'processed': True, 'drop_detected': drop_found, 'size': len(data)}
    return final_output

# Input data
temperature_data = [-20, 10, 25, 45, 60, 30, 15, -10]

# Execution
final_output = process_temperatures(temperature_data)
print(f"Result: {final_output}")