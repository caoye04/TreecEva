def analyze_performance(metrics, weights):
    combined = 0
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        adjusted = metric * weight
        combined += adjusted
    
    # Irrelevant distraction: unused smoothing factor
    smoothing_factor = 0.85
    offset = 2
    
    if combined > 70:
        level = 'high'
        bonus = 10
    else:
        level = 'standard'
        bonus = 0
    
    result = int(combined + bonus)
    return result

# Main execution
data_stream = [85, 90, 78, 88]
weights = [0.2, 0.3, 0.2, 0.3]

# Slice to exclude first element (not used in final logic but included for context)
trimmed_metrics = data_stream[1:]

# Actual metrics used
metrics = data_stream

# Extra irrelevant variable
baseline = sum(data_stream) / len(data_stream)

threshold_score = analyze_performance(metrics, weights)
print(f"Result: {threshold_score}")