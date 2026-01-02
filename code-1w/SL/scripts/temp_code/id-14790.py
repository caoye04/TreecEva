def calculate_performance(data):
    base_score = 0
    adjustments = []
    
    # Process each metric in the benchmark data
    for metric, values in data.items():
        raw = sum(values) / len(values)
        weight = 1.0
        
        if raw > 80:
            weight += 0.2
        elif raw < 60:
            weight -= 0.1
        
        adjusted = raw * weight
        adjustments.append(adjusted)
    
    base_score = sum(adjustments) / len(adjustments)
    
    # Apply final scaling based on consistency
    consistency = min(adjustments) / max(adjustments)
    if consistency > 0.9:
        base_score *= 1.05
    
    return int(base_score)

# Irrelevant auxiliary variable (minor distraction)
startup_message = "System initialized"

# Benchmark data for performance evaluation
benchmark_data = {
    "latency": [85, 78, 92],
    "throughput": [90, 88, 85],
    "memory_usage": [55, 60, 50],
    "cpu_efficiency": [70, 75, 80]
}

# Calculation entry point
final_score = calculate_performance(benchmark_data)

# Output result
print(f"Result: {final_score}")