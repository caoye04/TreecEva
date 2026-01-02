import math

def analyze_signal(data, threshold=5.0):
    filtered = [x for x in data if abs(x) > threshold]
    magnitude = sum(abs(x) for x in filtered)
    normalized = magnitude / len(data) if data else 0
    return normalized

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if total > 0 and v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def shift_sequence(seq, offset):
    return seq[offset:] + seq[:offset]

def evaluate_performance(metrics, weights):
    # Core calculation path
    base = metrics['accuracy'] * weights[0]
    penalty = metrics['latency'] // 10
    bonus = int(math.sqrt(metrics['throughput']))
    adjusted = base - penalty + bonus
    
    # Distractor: irrelevant transformation
    temp_data = [math.sin(i) for i in range(1, 6)]
    dummy_sum = sum(temp_data)
    fake_adjustment = dummy_sum * 0.1  # Not used in final logic
    
    # Conditional red herring
    if metrics['accuracy'] > 90:
        shadow_bonus = 5  # Defined but not used
        redundant_calc = (metrics['throughput'] % 7) * 2  # Dead computation
    
    # Another decoy function call with no effect
    _ = compute_entropy([3, 5, 7, 11])
    
    # Key distractor: looks important but unused
    historical_avg = 87.2
    drift_correction = (metrics['accuracy'] - historical_avg) / 100
    
    # Real path continues
    stability_factor = metrics['jitter'] < 2
    reliability_bonus = 3 if stability_factor else 0
    
    # Final aggregation
    result = adjusted + reliability_bonus
    
    # Dead branch — never reached due to logic
    if len(str(result)) > 10:
        fallback = sum(int(d) for d in str(result))
        result = fallback  # Unreachable
    
    return int(result)

def main():
    # Simulated monitoring system metrics
    raw_signals = [-2.1, 6.5, -8.3, 4.0, 12.7, -1.5, 0.2]
    signal_strength = analyze_signal(raw_signals, threshold=4.0)
    
    # Irrelevant sequence manipulation
    sequence_a = [1, 2, 3, 4, 5]
    shifted_a = shift_sequence(sequence_a, 2)
    reversed_b = sequence_a[::-1]  # Unused
    
    # Actual input preparation
    metrics = {
        'accuracy': 94,
        'latency': 125,
        'throughput': 625,
        'jitter': 1
    }
    
    # Weight configuration (distraction: extra elements)
    weights = [0.6, 0.2, 0.1, 0.1]  # Only first used
    scaling_factors = [w * 10 for w in weights]  # Computed but unused
    
    # Distractor: entropy of arbitrary primes
    prime_set = [2, 3, 5, 7, 11, 13]
    _ = compute_entropy(prime_set)  # Called but result ignored
    
    # Key execution point
    final_score = evaluate_performance(metrics, weights)
    
    # Extra noise: slicing and list comprehension with no impact
    sample_range = list(range(10, 20))
    clipped = sample_range[3:-2]
    processed = [x * 1.5 for x in clipped if x % 2 == 0]
    cumulative = sum(processed) / len(processed) if processed else 0.0
    
    # Output only the target result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()