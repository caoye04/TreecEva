from collections import Counter

def analyze_pattern(sequence):
    count = Counter(sequence)
    modes = [k for k, v in count.items() if v == max(count.values())]
    return modes[0] if len(modes) == 1 else min(modes)

def calculate_performance_rating():
    raw_data = [3, 5, 7, 5, 9, 5, 12, 7, 5]
    filtered_data = [x for x in raw_data if x > 4]
    
    # Some auxiliary operations (minimal interference)
    temp_offset = len(filtered_data) - len(raw_data)
    adjustment_factor = sum(filtered_data[:3]) / 3
    
    mode_value = analyze_pattern(filtered_data)
    average_value = sum(filtered_data) / len(filtered_data)
    
    # Core computation
    base_score = average_value * 0.6 + mode_value * 0.4
    final_score = int(base_score + adjustment_factor * 0.1)  # Final assignment
    
    # Irrelevant tracking variable (light distraction)
    record_timestamp = "2023-11-05"
    
    return final_score

# Main execution
result = calculate_performance_rating()
print(f"Result: {result}")