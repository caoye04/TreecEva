import math

def analyze_efficiency(data):
    # Irrelevant analysis function (dead code path)
    total = sum(x ** 2 for x in data if x > 0)
    return total // len(data) if data else 0

def preprocess_signal(signal):
    # Distractor: signal processing with no impact on final result
    filtered = [s * 0.9 for s in signal]
    normalized = [(s - min(filtered)) / (max(filtered) - min(filtered) + 1e-6) for s in filtered]
    return [round(n * 100) for n in normalized]

def transform_features(features):
    # Unused transformation logic (red herring)
    encoded = {}
    for i, f in enumerate(features):
        encoded[f'dim_{i}'] = hash(f) % 1000
    return list(encoded.values())

def calculate_entropy(seq):
    # Misleading mathematical computation
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    adjusted = []
    for i in range(len(metrics)):
        if i % 2 == 0:
            adjusted.append(metrics[i] * weights[i] * 1.1)
        else:
            adjusted.append(metrics[i] * weights[i] * 0.9)
    
    base_score = sum(adjusted)
    
    # Conditional modification based on threshold
    if base_score > 85:
        bonus = 12.5
    elif base_score > 70:
        bonus = 7.3
    else:
        bonus = 0
    
    # Additional adjustment using bit manipulation (non-obvious but relevant)
    modifier = (len(metrics) << 2) ^ 5  # Bit shift and XOR
    final_score = base_score + bonus + (modifier / 10.0)
    
    # Dead branch - never executed due to above conditions
    if base_score < 0:
        fallback = math.exp(base_score)
        final_score = fallback  # unreachable
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Real input data
    metrics = [88, 76, 92, 81, 79]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    
    # Irrelevant auxiliary data
    sensor_data = [0.12, 0.88, 0.45, 0.99, 0.01]
    feature_names = ['latency', 'throughput', 'jitter', 'loss', 'stability']
    event_log = [(1, 'start'), (2, 'pause'), (3, 'resume'), (4, 'end')]
    
    # Unused intermediate calculations (distractors)
    avg_metric = sum(metrics) / len(metrics)
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    squared_deviations = [(m - avg_metric)**2 for m in metrics]
    variance = sum(squared_deviations) / len(metrics)
    std_dev = math.sqrt(variance)
    
    # Preprocessing unrelated data (misdirection)
    processed_signal = preprocess_signal(sensor_data)
    transformed_feats = transform_features(feature_names)
    log_ids = [x[0] for x in event_log]
    
    # Key execution point
    final_score = evaluate_performance(metrics, weights)
    
    # Print target result
    print(f"Result: {final_score}")