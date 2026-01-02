def analyze_sequence(data, threshold):
    above_threshold = [x for x in data if x > threshold]
    squared_evens = [x**2 for x in above_threshold if x % 2 == 0]
    total_power = sum(squared_evens)
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_analysis = { 'count': len(data), 'max_val': max(data) }
    
    return total_power


def calculate_performance(logs):
    base_values = [len(entry.split('-')) for entry in logs]
    adjusted = [val + 1 for val in base_values if val < 5]
    raw_score = sum(adjusted)
    
    # Conditional expression with meaningful logic
    final_score = raw_score * 1.5 if len(adjusted) > 3 else raw_score * 0.8
    
    return final_score

# Main execution
input_logs = ['a-b', 'x-y-z', 'm-n-o-p', 'q-r', 's-t-u-v-w']
data_stream = [3, 7, 4, 9, 6, 2]
threshold_level = 5

interim_result = analyze_sequence(data_stream, threshold_level)
final_score = calculate_performance(input_logs)

print(f"Result: {final_score}")