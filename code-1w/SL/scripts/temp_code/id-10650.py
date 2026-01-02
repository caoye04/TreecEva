import itertools

def analyze_signal(data, threshold=0.75):
    """Irrelevant function analyzing signal strength."""
    filtered = [x for x in data if x > threshold]
    return len(filtered) * 0.33

def preprocess_metrics(raw):
    """Applies normalization and filtering to raw metrics."""
    normalized = [(x - min(raw)) / (max(raw) - min(raw) + 1e-8) for x in raw]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
    return smoothed[:len(raw)] + [0.0] * (len(raw) - len(smoothed))

def calculate_entropy(values):
    """Calculates entropy of a probability distribution."""
    from math import log
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

def generate_combinations(items):
    """Generates irrelevant combinations of items."""
    return list(itertools.combinations(items, 2))

def adjust_for_bias(arr, bias_factor=1.05):
    """Adjusts array values with a fixed bias factor."""
    return [x * bias_factor for x in arr]

def validate_stability(readings):
    """Checks if system readings are within stable range."""
    return all(0.1 <= r <= 0.9 for r in readings)

def simulate_feedback_loop(initial, iterations):
    """Simulates an unrelated feedback control loop."""
    state = initial
    for _ in range(iterations):
        state = state * 1.1 - 0.1
        if state > 1.0:
            state = 0.5
    return state

def evaluate_performance(metrics, weights):
    """Evaluates weighted performance score based on processed metrics."""
    # Preprocess the metrics
    processed = preprocess_metrics(metrics)
    
    # Irrelevant entropy calculation
    entropy = calculate_entropy(metrics)
    
    # Adjust for bias (partially relevant)
    adjusted = adjust_for_bias(processed, 1.02)
    
    # Apply weights using dictionary mapping
    weighted_sum = 0
    weight_map = {i: w for i, w in enumerate(weights)}
    for i, val in enumerate(adjusted):
        if i < len(weight_map):
            contribution = val * weight_map[i]
            weighted_sum += contribution
    
    # Additional logic involving list comprehension and filtering
    significant_contributions = [w * adjusted[i] for i, w in weight_map.items() if adjusted[i] > 0.5]
    bonus = len(significant_contributions) * 0.05
    
    # Final computation
    raw_score = weighted_sum + bonus
    clamped_score = max(0.0, min(100.0, raw_score))
    return round(clamped_score, 4)

# Main execution block
if __name__ == '__main__':
    # Simulated input data
    raw_metrics = [85, 72, 90, 61, 77, 88, 59]
    importance_weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.05, 0.1]
    
    # Irrelevant preprocessing steps
    signal_data = [0.8, 0.6, 0.9, 0.7]
    stability_check = validate_stability([0.2, 0.5, 0.8])
    signal_strength = analyze_signal(signal_data)
    feedback_state = simulate_feedback_loop(0.4, 10)
    
    # Generate unused combinations
    indices = list(range(len(raw_metrics)))
    pairs = generate_combinations(indices)
    
    # Core evaluation
    final_score = evaluate_performance(raw_metrics, importance_weights)
    
    # Print result
    print(f"Result: {final_score}")