def calculate_performance(base, data):
    adjustment = lambda x: x * 1.5 if x > base else x * 0.8
    
    # Process each metric with conditional scaling
    processed = [adjustment(val) for val in data.values()]
    
    # Apply bonus if average exceeds threshold
    avg_val = sum(processed) / len(processed)
    bonus = 10 if avg_val > 75 else 0
    
    return int(avg_val + bonus)

# Baseline reference and performance metrics
dummy_var = "irrelevant"
baseline = 60
metrics = {
    "throughput": 70,
    "latency": 85,
    "accuracy": 90,
    "energy": 65
}

# Calculation entry point
final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")