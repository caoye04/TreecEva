def process_metrics(values, scaling_factors):
    weighted_sum = sum(x * y for x, y in zip(values, scaling_factors))
    total_scale = sum(scaling_factors)
    normalize = lambda a, b: round(a / b, 3)
    return normalize(weighted_sum, total_scale)

# Irrelevant auxiliary data (minimal distraction)
baseline = [0.8, 0.9, 0.7]
temp_log = {'run_id': 101, 'status': 'completed'}

# Core input data
data = [150, 200, 175]
weights = [0.3, 0.5, 0.2]

# Computation chain
aggregated = sum(data) // len(data)
efficiency_score = aggregated * 0.1  # Intermediate metric
final_output = process_metrics(data, weights)
efficiency_score = final_output + efficiency_score

print(f"Result: {efficiency_score}")