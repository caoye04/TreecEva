from collections import defaultdict, Counter
from itertools import combinations

# Simulated system performance metrics
def collect_metrics():
    raw_data = [15, 23, 18, 42, 37, 29, 33]
    processed = defaultdict(float)
    temp_cache = []

    for i, val in enumerate(raw_data):
        if i % 2 == 0:
            processed['even_index_sum'] += val * 0.1
        else:
            processed['odd_index_sum'] += val * 0.1

        # Distractor: irrelevant transformation
        temp_cache.append((val ** 2 + 5) // 3)

    # Red herring: unused computation
    decoy_result = sum(temp_cache[i] for i in range(0, len(temp_cache), 3))

    processed['max_val'] = max(raw_data)
    processed['min_val'] = min(raw_data)
    return dict(processed)

# Weight configuration with misleading entries
def load_weights():
    weights = {
        'priority_boost': 1.5,
        'legacy_factor': 0.8,  # Not used in final calculation
        'decay_rate': 0.92,     # Unused
        'base_scale': 2.0      # Unused
    }

    # Decoy weight set
    alternate_weights = [0.1, 0.3, 0.4, 0.2]
    normalized = [w / sum(alternate_weights) for w in alternate_weights]

    # Inject correct weights indirectly
    weights.update({
        'w1': 0.4,
        'w2': 0.6
    })

    return weights

# Auxiliary function that appears important but has red herrings
def analyze_distribution(data):
    freq = Counter(data.values())
    mode_approx = freq.most_common(1)[0][1]

    # Complex but irrelevant combinatorics
    pairs = list(combinations(freq.keys(), 2))
    pair_count = len(pairs)

    # This looks like a correction factor but isn't used
    adjustment = (pair_count + mode_approx) / (len(data) + 1) if data else 0

    return mode_approx  # Actually unused downstream

# Core evaluation logic with hidden path
def evaluate_performance(metrics, weights):
    # Key variables
    base = metrics['even_index_sum']  # depends on indices 0,2,4,6
    bonus = metrics['odd_index_sum']   # indices 1,3,5
    peak = metrics['max_val']
    floor = metrics['min_val']

    # Distractor: complex unused formula
    phantom_score = (peak - floor) * weights['legacy_factor']
    decay_adjusted = 0
    for i in range(5):
        decay_adjusted += phantom_score * (weights['decay_rate'] ** i)

    # Real scoring uses only w1 and w2
    score_component_1 = base * weights['w1']  # (1.5 + 1.8 + 3.7 + 3.3) * 0.4
    score_component_2 = bonus * weights['w2'] # (2.3 + 4.2 + 2.9) * 0.6

    temp_result = score_component_1 + score_component_2

    # Conditional modification based on threshold
    if peak > 40:
        temp_result *= 1.25
    elif peak > 30:
        temp_result *= 1.15
    else:
        temp_result *= 1.05

    # Final adjustment using hidden rule
    final_modifier = 1.0
    if floor < 20:
        final_modifier = 1.2

    final_score = int(temp_result * final_modifier)

    # Dead code branch - never reached due to prior logic
    if final_score < 0:
        fallback = sum(weights[w] * peak for w in ['w1', 'w2'])
        final_score = int(fallback)

    return final_score

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect metrics
    metrics = collect_metrics()
    
    # Step 2: Load weight configuration
    weights = load_weights()
    
    # Step 3: Perform auxiliary analysis (result not used)
    _ = analyze_distribution(metrics)
    
    # Step 4: Evaluate final performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")