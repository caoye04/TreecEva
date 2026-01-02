def calculate_efficiency(data):
    base = sum(data) / len(data)
    adjustment = 0
    
    # Irrelevant transformation (distractor)
    transformed = list(map(lambda x: x ** 0.5 + 2, data))
    temp_sum = sum(transformed) * 0.1
    
    # Semi-relevant filtering (only some elements affect result)
    filtered = [x for x in data if x > base]
    
    # Core logic hidden among distractions
    if len(filtered) > 0:
        adjustment = (max(filtered) - min(filtered)) / base
    
    # Secondary distractor: string processing with no impact
    status_codes = ['OK', 'FAIL', 'RETRY']
    code_map = {s: s.lower().replace('i', '1') for s in status_codes}
    joined = ''.join(code_map.values())
    dummy_hash = sum([ord(c) for c in joined]) % 17
    
    # Actual efficiency formula
    return base * 0.8 + adjustment * 2

# Main execution
raw_input = "12,15,9,20,14,18"

# Parsing and preprocessing (relevant)
values = raw_input.split(',')
data_stream = [int(v.strip()) for v in values]

# Distractor: unused statistical measures
mean_val = sum(data_stream) / len(data_stream)
variance = sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)
std_dev = variance ** 0.5

# Additional irrelevant assignment
buffer_size = len(data_stream) * 4
padding = [0] * (buffer_size - len(data_stream))

# Key processing steps
normalized = [x * 0.95 for x in data_stream]
processed_data = [int(x) for x in normalized if x > 10]  # Filtering affects final input

# Final calculation
intermediate_result = sum(processed_data) + len(processed_data)
efficiency_score = calculate_efficiency(processed_data)

# Output required value
print(f"Target result: {efficiency_score}")