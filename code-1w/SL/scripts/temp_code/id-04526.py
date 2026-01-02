from itertools import combinations
from math import log

# Simulate sensor data with noise and valid readings
def preprocess_data(raw):
    cleaned = [x for x in raw if x > 0]
    noise_filter = list(map(lambda x: x * 0.9 + 2, cleaned))
    return sorted(noise_filter, reverse=True)

# Analyze patterns in top N values
def analyze_peaks(seq, n):
    if len(seq) < n:
        return 0
    top_n = seq[:n]
    diffs = [top_n[i] - top_n[i+1] for i in range(len(top_n)-1)]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    # Irrelevant computation (distractor)
    _ = [x ** 0.5 for x in diffs]
    return avg_diff

# Calculate entropy-like metric for distribution
def calc_diversity(arr):
    freq_map = {}
    for val in arr:
        freq_map[val] = freq_map.get(val, 0) + 1
    probabilities = [freq_map[k] / len(arr) for k in freq_map]
    entropy = -sum(p * log(p) for p in probabilities)
    return entropy

# Core scoring logic
def calculate_final_score(dataset):
    processed = preprocess_data(dataset)
    
    # Extract key metrics
    peak_trend = analyze_peaks(processed, 3)
    diversity_metric = calc_diversity(processed)
    
    # Secondary analysis with distractors
    window_sums = [sum(processed[i:i+3]) for i in range(0, len(processed)-2, 2)]
    spike_count = sum(1 for w in window_sums if w > 50)  # Not used later
    
    # Generate interaction features
    interactions = list(combinations([int(x) for x in processed[:4]], 2))
    interaction_sum = sum(a * b for a, b in interactions)  # Distractor
    
    # Key calculation path
    base_score = len(processed) * 10
    adjustment = int(peak_trend * 2) if peak_trend > 1.5 else 5
    penalty = int(diversity_metric * 3)
    
    # Final composition
    score_component_1 = base_score + adjustment
    score_component_2 = 100 - penalty
    final_score = (score_component_1 + score_component_2) // 2
    
    # Dead code path (distractor)
    if False:
        fallback = sum(interaction_sum for _ in range(2))
        final_score = fallback

    return final_score

# Main execution
data = [15, -5, 20, 18, 0, 22, 19, -3, 21]
final_score = calculate_final_score(data)
print(f"Target result: {final_score}")