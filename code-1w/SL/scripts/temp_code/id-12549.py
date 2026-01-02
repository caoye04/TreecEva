def analyze_efficiency(data):
    adjusted = list(map(lambda x: (x + 1) ** 0.5, data))
    return [val for val in adjusted if val > 2]

# Simulate system performance metrics
data_points = [3, 5, 7, 9, 11, 14, 18]
efficient_vals = analyze_efficiency(data_points)

baseline = sum(data_points) / len(data_points)
deviations = [abs(x - baseline) for x in data_points]
normalized_dev = [d / baseline for d in deviations]

# Weighting function for metric importance
weight_func = lambda x: 0.5 + (x / 100)
weights = [weight_func(i * 2) for i in range(len(efficient_vals))]

# Auxiliary calculation - not directly used but adds cognitive load
aux_total = 0
for i in range(len(deviations)):
    aux_total += deviations[i] * (i + 1)
threshold_map = {i: aux_total / (i + 1) for i in range(3)}

# Core evaluation logic
def evaluate_performance(metrics, weights):
    if not metrics or not weights:
        return 0
    
    weighted_sum = 0
    scaling_factor = 1.0
    
    for i in range(min(len(metrics), len(weights))):
        temp_val = metrics[i] * weights[i]
        if temp_val > 3:
            scaling_factor *= 1.1
        weighted_sum += temp_val
    
    # Apply scaling based on consistency
    consistency = sum([1 for x in normalized_dev if x < 0.5])
    adjustment = 1.05 if consistency > 4 else 1.0
    
    # Red herring computation
    dummy_calc = 0
    for x in threshold_map.values():
        dummy_calc += x * 0.1
    
    return int(weighted_sum * scaling_factor * adjustment)

metrics = efficient_vals[:len(weights)]
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")