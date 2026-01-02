def analyze_component(x, y, z):
    if x == 0:
        return 0
    temp_val = (x ** 2 + y * z) / (x + 1)
    adjustment = 1.5 if temp_val > 10 else 0.8
    return temp_val * adjustment

# Simulate sensor data preprocessing
data_points = [3, 7, 2, 8, 5]
normalized = [val / max(data_points) for val in data_points]
weights = {i: normalized[i] for i in range(len(normalized))}

# Irrelevant helper function (dead code path)
calculate_efficiency = lambda a, b: a * b / (a + b) if a + b != 0 else 0

# Core processing pipeline
def process_metrics(records):
    base_scores = []
    penalty = 0
    for i, record in enumerate(records):
        score = analyze_component(record, i, len(records))
        base_scores.append(score)
        if score < 5 and i % 2 == 0:
            penalty += 1.2
    
    avg_score = sum(base_scores) / len(base_scores) if base_scores else 0
    adjusted_avg = avg_score - penalty
    
    # Distractor computation (not used in final result)
    outlier_count = len([s for s in base_scores if s > 15])
    scaling_factor = 1.1 if outlier_count > 1 else 1.0
    
    return adjusted_avg

# Benchmark configuration
benchmark_data = [4, 6, 1, 9]

# Secondary system state (misleading variables)
system_load = [0.4, 0.7, 0.9, 0.3]
reliability_index = min(system_load) * 100
consistency_check = reliability_index >= 30

# Main calculation with nested logic
def calculate_performance(data):
    processed = process_metrics(data)
    
    # Conditional transformation using lambda
    transform = lambda x: x * 1.5 if x < 8 else x * 1.1
    enhanced = transform(processed)
    
    # Additional conditional logic
    threshold = 7.5
    if enhanced > threshold:
        enhanced -= 2.0
    elif enhanced == threshold:
        enhanced += 1.0
    else:
        enhanced += 0.5
    
    # Red herring: unused intermediate
    temp_diagnostic = sum([i * 0.1 for i in range(5)]) if enhanced < 0 else 0
    
    # Final aggregation
    stability_bonus = 1.8 if consistency_check else 0.0
    final_value = enhanced + stability_bonus
    
    return final_value

# Execute main logic
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")