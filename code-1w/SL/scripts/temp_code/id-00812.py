def calculate_final_score(data):
    tokens = data.split(',')
    values = [int(token.strip()) for token in tokens if token.strip().isdigit()]
    
    # Extract unique values and apply transformation
    unique_values = set(values)
    transformed = [v ** 2 for v in unique_values if v % 2 == 0]
    
    # Compute base score
    base_score = sum(transformed)
    
    # Adjust score based on count of distinct even numbers
    adjustment = len(transformed) * 3
    final_score = base_score - adjustment
    
    return final_score

# Simulated sensor data with noise
raw_data = "10, 20, abc, 20, 30, , 40, 15"

# Key computation
final_score = calculate_final_score(raw_data)
print(f"Result: {final_score}")