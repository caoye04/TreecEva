import math

# Simulated system performance metrics (some are red herrings)
def collect_metrics():
    raw_data = [120, 85, 90, 77, 110, 64, 95]
    outliers = [x for x in raw_data if x > 100]
    filtered = [x for x in raw_data if x >= 70 <= 100]  # Remove outliers
    
    # Irrelevant transformations (distractors)
    squared = [x**2 for x in raw_data]
    normalized = [round(x / max(raw_data), 3) for x in raw_data]
    entropy = -sum(p * math.log(p) for p in normalized if p > 0)

    # Real metrics used later
    return {
        'response_time': filtered[0],
        'accuracy': filtered[1],
        'throughput': filtered[2],
        'latency': filtered[3],
        'reliability': sum(filtered) // len(filtered),  # Base score
        'dummy_metric_1': entropy,
        'dummy_metric_2': len(squared)
    }

# Weighting function with dead paths and decoys
def calculate_weights(n):
    primes = [i for i in range(2, n) if all(i % j != 0 for j in range(2, int(i**0.5)+1))]
    weights = {}
    
    for i in range(n):
        if i == 0:
            weights['response_time'] = 0.3
        elif i == 1:
            weights['accuracy'] = 0.25
        elif i == 2:
            weights['throughput'] = 0.2
        elif i == 3:
            weights['latency'] = 0.15
        elif i == 4:
            weights['reliability'] = 0.1
        else:
            # Dead code branch - never reached
            key = f'dummy_{i}'
            weights[key] = round(1 / (i * 1.5), 3)
    
    # Decoy normalization (not actually used)
    total = sum(weights.values())
    normalized_weights = {k: round(v / total, 3) for k, v in weights.items()}
    
    # Return original weights, not normalized (trap for inattentive tracing)
    return weights

# Core evaluation logic
def evaluate_performance(metrics, weights):
    score = 0.0
    
    # Only these keys contribute to final score
    relevant_keys = ['response_time', 'accuracy', 'throughput', 'latency', 'reliability']
    
    # Distractor: string processing with no impact
    key_names = [k.upper() for k in metrics.keys()]
    valid_keys = set(k.lower() for k in key_names if 'DUMMY' not in k)
    sorted_keys = sorted(valid_keys & set(relevant_keys))
    
    # Actual scoring
    for key in relevant_keys:
        if key in metrics and key in weights:
            contribution = metrics[key] * weights[key]
            score += contribution
    
    # Final adjustment based on hidden rule: if base reliability > 85, add bonus
    base_reliability = metrics['reliability']
    threshold_met = base_reliability > 85
    bonus = 5.0 if threshold_met else 0.0
    score += bonus
    
    # Red herring: complex bit manipulation with no effect
    binary_rep = bin(hash(str(score)))[2:]
    flipped = ''.join('1' if b == '0' else '0' for b in binary_rep[-8:])
    inverted_value = int(flipped, 2)
    dummy_adjustment = inverted_value * 0.001
    
    return round(score, 4)

# Unused recursive function (dead code path)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Unused set operations (distractor)
available_metrics = {'response_time', 'accuracy', 'throughput', 'latency', 'reliability'}
required_metrics = {'response_time', 'accuracy', 'throughput'}
optional_metrics = available_metrics - required_metrics

# Main execution flow
metrics = collect_metrics()
weights = calculate_weights(5)  # Only indices 0-4 are used
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")