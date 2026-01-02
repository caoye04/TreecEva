from itertools import combinations

# Simulate system performance metrics from a distributed task pipeline
def collect_metrics(base_load, efficiency_factor):
    raw_data = [base_load * (1.5 ** i) for i in range(5)]
    adjusted = [x * efficiency_factor for x in raw_data]
    normalized = [round(x / sum(adjusted), 4) for x in adjusted]
    return normalized

def calculate_redundancy_score(data_stream):
    # Irrelevant helper: analyzes pattern redundancy (not used in final score)
    pairs = list(combinations(data_stream, 2))
    redundant_count = sum(1 for a, b in pairs if abs(a - b) < 0.05)
    return redundant_count

def smooth_signal readings(signal):
    # Dead code path — never called
    return [round((signal[i-1] + signal[i] + signal[i+1]) / 3, 4) for i in range(1, len(signal)-1)]

def assess_stability(metric_window):
    variance = sum((x - sum(metric_window)/len(metric_window))**2 for x in metric_window) / len(metric_window)
    stability = 100 * (1 - min(variance, 0.25))
    return stability

def compute_entropy(values):
    # Unused distractor function involving lambda and slicing
    positive_vals = [v for v in values if v > 0]
    freq_map = {x: positive_vals.count(x) for x in set(positive_vals)}
    total = len(positive_vals)
    entropy_fn = lambda p: -p * (p).bit_length()  # Simplified placeholder
    entropy = sum(entropy_fn(count/total) for count in freq_map.values())
    return round(entropy, 4)

def evaluate_performance(metrics, weights):
    # Core logic begins
    weighted_components = [
        metrics[i] * weights[i] for i in range(len(metrics))
    ]
    
    # Intermediate irrelevant transformation
    shifted = [(w * 1.1) % 0.9 for w in weights]
    dummy_effect = sum(shifted[i] * metrics[-(i+1)] for i in range(3))

    # Actual scoring uses only first three metrics
    primary_impact = sum(weighted_components[:3])

    # Stability bonus from window slice
    stability_metrics = metrics[1:4]
    bonus = assess_stability(stability_metrics) / 1000  # Small additive factor

    # Final computation
    base_score = primary_impact * 1000
    final_score = int(base_score + bonus)  # Truncated integer result

    # Red herring: complex entropy ignored
    _ = compute_entropy(metrics)

    return final_score

# Main execution
if __name__ == '__main__':
    initial_load = 120
    efficiency = 0.88
    
    # Generate metrics
    metrics = collect_metrics(initial_load, efficiency)
    
    # Weight vector (aligned with top 5 components)
    weights = [0.3, 0.25, 0.2, 0.15, 0.1]
    
    # Irrelevant data structures
    audit_trail = {'timestamps': [1, 2, 3], 'status': ['ok']*3}
    temp_snapshot = metrics[::2]  # Slicing not used later
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Distractor computation
    outlier_check = list(filter(lambda x: x > 0.5, metrics))
    
    print(f"Result: {final_score}")