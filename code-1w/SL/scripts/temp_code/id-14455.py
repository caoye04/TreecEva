def calculate_performance(data):
    adjusted_values = [x * 1.5 for x in data['metrics'] if x > 10]
    trimmed = adjusted_values[1:4]  # Slice to keep only middle values
    base = sum(trimmed) / len(trimmed)
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_result = base * 0.9
    
    penalty = 0
    if data['threshold'] < base:
        penalty = 5
    
    return base - penalty

# Input data structure with dictionary operations
data_input = {
    'metrics': [8, 12, 15, 18, 6],
    'threshold': 14,
    'version': '2.1'
}

final_score = calculate_performance(data_input)
print(f"Target result: {final_score}")