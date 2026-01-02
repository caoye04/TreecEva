def analyze_trends(data, threshold=5):
    trend_count = 0
    temp_result = 0
    for val in data:
        if val > threshold:
            trend_count += 1
            temp_result += val ** 0.5
    return trend_count

# Irrelevant helper function (decoy)
def compute_projection(x):
    return (x * 1.2 + 3.7) % 100

# Unused but plausible-looking transformation
def normalize_values(arr):
    max_val = max(arr) if arr else 1
    return [v / max_val for v in arr]

# Main processing chain with distractors
def transform_metrics(raw):
    shifted = [x << 1 for x in raw]  # Bit manipulation red herring
    filtered = [x for x in shifted if x % 3 == 0]
    aggregated = sum(filtered) // len(filtered) if filtered else 0
    
    # Complex conditional expression (required feature)
    status_flag = 'valid' if aggregated > 20 else 'pending'
    
    # Dictionary operations (required feature)
    metadata = {
        'size': len(raw),
        'aggregated': aggregated,
        'flag': status_flag,
        'aux': sum(x*x for x in raw)  # Distractor computation
    }
    
    return metadata

# Core logic buried among noise
def evaluate_performance(metrics):
    base = metrics['aggregated']
    size_factor = metrics['size']
    
    # Real calculation path
    if size_factor > 0:
        intermediate = base * size_factor
        adjustment = 0
        
        # Nested conditional with early exit red herring
        for i in range(3):
            if intermediate > 100:
                adjustment += i * 2
                break
            adjustment -= 1
        
        # Multi-step reasoning
        score_component = intermediate + adjustment
        penalty = 0
        
        # Another distraction layer
        for k, v in metrics.items():
            if isinstance(v, int) and v % 2 == 1 and k != 'size':
                penalty += 1  # Minor penalty logic
        
        final_score = score_component - penalty
        
        # Dead code path (never reached due to prior logic)
        if final_score < 0:
            backup_calc = metrics.get('aux', 0) // 10
            final_score = backup_calc  # Not triggered in this case
        
        return final_score
    
    return -1

# Irrelevant data transformations
historical_data = [12, 15, 18, 22, 25]
dummy_weights = [0.1, 0.3, 0.5, 0.7, 0.9]

# Unused but realistic-looking analysis
correlation_score = sum(historical_data[i] * dummy_weights[i] for i in range(len(historical_data)))

# Actual input data
input_raw = [4, 5, 6, 7]

# Key execution steps
metric_metadata = transform_metrics(input_raw)
# Critical statement: final_score = evaluate_performance(metric_metadata)
final_score = evaluate_performance(metric_metadata)

# Print result as required
print(f"Result: {final_score}")