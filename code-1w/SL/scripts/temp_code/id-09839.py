def calculate_performance(base, data):
    filtered = {k: v for k, v in data.items() if v > base * 1.2}
    adjustments = set(data.keys()) - set(filtered.keys())
    penalty = len(adjustments) * 0.85
    base += penalty
    
    # Irrelevant distraction: unused variable
    temp_result = [x * 0.1 for x in data.values()]
    
    total = sum(filtered.values())
    final = total / base if base != 0 else 0
    return int(final)

# Input data
dataset = {'sensor_A': 15, 'sensor_B': 23, 'sensor_C': 11, 'sensor_D': 30, 'sensor_E': 8}
baseline = 12

# Key computation step
final_score = calculate_performance(baseline, dataset)

# Output result
print(f"Result: {final_score}")