def analyze_trends(data, threshold=0.5):
    trends = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1]
        if change > threshold:
            trends.append('UP')
        elif change < -threshold:
            trends.append('DOWN')
        else:
            trends.append('FLAT')
    return trends

# Irrelevant helper function (decoy)
def normalize_vector(v):
    mag = sum(x**2 for x in v) ** 0.5
    return [x / mag for x in v] if mag else v

# Unused transformation (dead code path)
def transform_signal(signal):
    transformed = [signal[i] * (0.9 ** i) for i in range(len(signal))]
    return [round(x, 3) for x in transformed]

# Another red herring: complex but unused calculation
def compute_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).bit_length()  # Simulated log2 approximation
    return round(entropy, 4)

# Real computation begins here
def preprocess_metrics(raw_scores):
    # Apply sigmoid-like compression to scores
    processed = []
    for s in raw_scores:
        if s >= 0:
            compressed = 1 - (1 / (1 + s))
        else:
            compressed = -1 + (1 / (1 - s))
        processed.append(round(compressed, 6))
    return processed

# Weight adjustment with slicing distraction
def adjust_weights(w, window=3):
    adjusted = w[:]
    for i in range(len(w)):
        neighbors = adjusted[max(0, i - window//2):min(len(adjusted), i + window//2 + 1)]
        adjusted[i] = sum(neighbors) / len(neighbors)
    return adjusted

# Core logic obscured by multiple layers
def evaluate_performance(m, w):
    # Preprocess inputs
    processed_metrics = preprocess_metrics(m)
    smoothed_weights = adjust_weights(w)
    
    # Misleading intermediate (not used in final calc)
    peak_metric = max(processed_metrics)
    avg_weight = sum(smoothed_weights) / len(smoothed_weights)
    
    # Actual computation hidden among distractions
    score_components = []
    for i in range(len(processed_metrics)):
        contribution = processed_metrics[i] * smoothed_weights[i]
        score_components.append(contribution)
    
    # Final aggregation
    raw_sum = sum(score_components)
    penalty = 0
    if len([c for c in score_components if c < 0]) > 2:
        penalty = 0.1 * abs(raw_sum)
    
    final_score = raw_sum - penalty
    return round(final_score, 6)

# Main execution
if __name__ == '__main__':
    # Real input data
    metrics = [8.2, -1.5, 6.0, 3.3, -2.1, 7.7, 0.5]
    weights = [0.1, 0.15, 0.2, 0.1, 0.2, 0.15, 0.1]
    
    # Distractor variables
    baseline_data = [10, 9.5, 11.2, 8.7, 9.0, 10.5, 12.1]
    signal_noise = [0.01, -0.03, 0.02, 0.01, -0.01, 0.04, -0.02]
    trend_analysis = analyze_trends(baseline_data)
    normalized_weights = normalize_vector(weights)
    
    # Key execution point
    final_score = evaluate_performance(metrics, weights)
    
    # Print required result
    print(f"Target result: {final_score}")