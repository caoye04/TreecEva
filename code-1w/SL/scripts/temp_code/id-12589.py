from itertools import combinations

# Simulate system health metrics from sensor array
def collect_diagnostics():
    base_metrics = {
        'latency': 120,
        'throughput': 850,
        'error_rate': 0.03,
        'cpu_load': 75.4,
        'memory_usage': 68.2
    }
    return base_metrics

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

def calculate_efficiency_rating(data):
    # Irrelevant helper function for alternative pathway
    rating = 0
    if data['throughput'] > 800:
        rating += 20
    if data['latency'] < 150:
        rating += 15
    return rating

def adjust_for_outliers(values):
    # Dead code path - never actually used in final calculation
    mean_val = sum(values) / len(values)
    filtered = [v for v in values if abs(v - mean_val) < 20]
    return filtered if filtered else values

def generate_combinations(dimensions):
    # Distractor: creates unused combinatorial data
    keys = list(dimensions.keys())
    combo_pairs = list(combinations(keys, 2))
    entropy = len(combo_pairs) * 0.75
    return entropy

def validate_integrity(checksum_data):
    # Misleading computation: looks important but unused
    total = sum(len(str(v)) for v in checksum_data.values())
    return total % 9 == 0

def evaluate_performance(metrics, weights):
    # Core logic begins
    normalized = {}
    config = {
        'latency': (0, 200),
        'throughput': (0, 1000),
        'error_rate': (0, 0.1),
        'cpu_load': (0, 100),
        'memory_usage': (0, 100)
    }
    
    for key in metrics:
        if key in config:
            norm_val = normalize(metrics[key], config[key][0], config[key][1])
            normalized[key] = round(norm_val, 3)
    
    # Apply weighted aggregation
    raw_score = 0
    for k in weights:
        if k in normalized:
            raw_score += normalized[k] * weights[k]
    
    # Secondary adjustment based on threshold logic
    multiplier = 1.0
    if metrics['error_rate'] < 0.05:
        multiplier *= 1.1
    if normalized['latency'] < 0.6:
        multiplier *= 1.05
    
    adjusted_score = raw_score * multiplier
    
    # Final clamping and scaling
    final = int(max(0, min(100, adjusted_score * 10)))
    
    return final

# Main execution flow
diag_data = collect_diagnostics()

# Unused intermediate processing steps (distractors)
efficiency = calculate_efficiency_rating(diag_data)
entropy_value = generate_combinations(diag_data)
valid = validate_integrity(diag_data)

# Weight configuration for performance model
weights = {
    'latency': 0.3,
    'throughput': 0.25,
    'error_rate': 0.2,
    'cpu_load': 0.15,
    'memory_usage': 0.1
}

# Key statement
final_score = evaluate_performance(diag_data, weights)

print(f"Result: {final_score}")