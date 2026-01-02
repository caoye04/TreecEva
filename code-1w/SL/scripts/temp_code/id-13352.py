from itertools import combinations

def analyze_peaks(values):
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peaks.append(i)
    return peaks

# Simulate sensor readings with noise filtering
def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

# Core logic for ranking aggregation
def compute_rank_overlap(rank_a, rank_b):
    set_a = set(rank_a)
    set_b = set(rank_b)
    return len(set_a & set_b)

# Weighted score calculation with normalization
def normalize_weights(ws):
    total = sum(ws)
    return [w / total for w in ws] if total else [1/len(ws)] * len(ws)

def compute_final_score(rankings, weights):
    # Irrelevant precomputation (distractor)
    n = len(rankings)
    all_pairs = list(combinations(range(n), 2))
    pair_similarities = []
    
    for i, j in all_pairs:
        overlap = compute_rank_overlap(rankings[i], rankings[j])
        pair_similarities.append(overlap)
    
    avg_similarity = sum(pair_similarities) / len(pair_similarities) if pair_similarities else 0
    
    # Real computation begins
    base_scores = []
    for rank_list in rankings:
        score = 0
        for idx, val in enumerate(rank_list):
            score += val * (len(rank_list) - idx)  # Higher weight for earlier elements
        base_scores.append(score)
    
    # Normalize weights
    norm_weights = normalize_weights(weights)
    
    # Apply weights to scores
    weighted_sum = sum(base_scores[i] * norm_weights[i] for i in range(len(base_scores)))
    
    # Dummy tracking state (irrelevant)
    history_log = []
    for i, s in enumerate(base_scores):
        history_log.append(f'Round {i}: {s}')
    
    # Final transformation
    adjustment_factor = len(rankings[0]) / (1 + avg_similarity)
    final_score = weighted_sum / adjustment_factor
    
    # Dead code path (misleading)
    if False:
        fallback = sum(len(r) for r in rankings) // n
        final_score = max(final_score, fallback)
    
    return final_score

# Setup experiment data
rankings = [
    [3, 1, 4, 2],
    [1, 4, 3, 2],
    [4, 2, 1, 3]
]

weights = [0.5, 0.3, 0.2]

# Preprocess: simulate raw signal input
raw_signals = [
    [3.1, 0.9, 4.2, 1.8, 5.1, 0.7],
    [1.2, 4.3, 2.9, 2.1],
    [4.4, 1.7, 3.3]
]

filtered_signals = [filter_outliers(signal) for signal in raw_signals]
peaks_detected = [analyze_peaks(signal) for signal in filtered_signals]

# Key execution point
final_score = compute_final_score(rankings, weights)

# Output result
print(f"Result: {final_score}")