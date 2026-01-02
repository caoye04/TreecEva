def analyze_performance(raw_data, threshold=50):
    processed = [x for x in raw_data if x > threshold]
    processed_count = len(processed)
    
    # Irrelevant auxiliary calculation (minimal distraction)
    avg_value = sum(raw_data) / len(raw_data) if raw_data else 0
    temp_offset = int(avg_value % 7)

    sorted_values = sorted(processed)
    final_scores = sorted_values[::-1]  # Reverse using slicing
    
    scaling_factor = 3
    result = final_scores[processed_count // 2] // 10 * scaling_factor
    
    return result

# Main execution
data_input = [45, 78, 63, 88, 52, 91, 67, 74]
output = analyze_performance(data_input)
print(f"Target result: {output}")