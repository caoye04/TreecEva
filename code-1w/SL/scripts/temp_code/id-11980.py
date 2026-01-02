def evaluate_performance(data):
    base_weight = 0.6
    bonus_weight = 0.4
    
    # Irrelevant transformation (distractor)
    normalized = {k: v / max(data.values()) for k, v in data.items()}
    adjusted = {k: v * 1.1 if v < 0.5 else v for k, v in normalized.items()}
    
    # Real computation path
    raw_mean = sum(data.values()) / len(data)
    peak_metric = max(data['throughput'], data['accuracy'], data['latency'])
    stability = min(data.values()) / raw_mean if raw_mean > 0 else 0
    
    # Conditional logic affecting final result
    if stability > 0.8:
        bonus_factor = 1.2
    elif stability > 0.6:
        bonus_factor = 1.1
    else:
        bonus_factor = 0.9
    
    # Secondary distractor: unused helper calculation
    def calculate_efficiency(x):
        return (x.get('throughput', 0) * x.get('accuracy', 0)) / (x.get('energy', 1) + 0.1)
    
    efficiency_estimate = calculate_efficiency(data)  # Not used
    decay_rate = 0.95 ** len(data)  # Distractor variable
    
    # Core formula with weighted components
    performance_component = (data['throughput'] * 0.4 + data['accuracy'] * 0.4 + data['latency'] * 0.2)
    reliability_component = (1 - abs(data['latency'] - 50) / 50)  # Assume ideal latency is 50
    
    if data['accuracy'] >= 90 and data['throughput'] >= 80:
        reliability_component *= 1.15
    
    composite = (performance_component * base_weight + reliability_component * bonus_weight)
    
    # Final adjustment using bonus factor from stability
    final_score = int(composite * bonus_factor)
    
    # Dead code branch (never reached due to logic above)
    if False and efficiency_estimate > 100:
        final_score += 10
        
    return final_score

# Input data
metric_data = {
    'throughput': 85,
    'accuracy': 92,
    'latency': 45,
    'energy': 78,
    'jitter': 12
}

# Execution point of interest
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")