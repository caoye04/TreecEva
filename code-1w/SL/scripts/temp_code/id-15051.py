def calculate_final_score(data, limits):
    above_limit = list(filter(lambda x: x > limits[0], data))
    below_limit = list(filter(lambda x: x < limits[1], data))
    
    unique_high = set(above_limit)
    unique_low = set(below_limit)
    
    overlap = unique_high & unique_low
    
    score = len(unique_high) * 2 - len(unique_low)
    if len(overlap) > 0:
        score -= 5
    return score

# Sensor readings in degrees Celsius
temperatures = [18, 25, 19, 30, 17, 21, 16, 33]
thresholds = (24, 20)

result = calculate_final_score(temperatures, thresholds)
print(f"Result: {result}")