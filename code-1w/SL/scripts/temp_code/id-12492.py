from itertools import compress, cycle

def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val + 1e-8) for x in data]

def apply_weighting(values, weights):
    # Misleading: weights are cycled but only first few used
    weighted = [v * w for v, w in zip(values, cycle(weights))]
    return [w / sum(weighted) for w in weighted]  # Normalization distraction

def compute_aggregate(values, limits):
    # Core logic hidden among red herrings
    clipped = [min(max(v, low), high) for v, (low, high) in zip(values, limits)]
    
    # Distractor: complex filtering with no impact
    mask = [v > 0.5 for v in clipped]
    filtered = list(compress(clipped, mask))
    fallback_sum = sum(filtered) if filtered else sum(clipped)
    
    # Actual contribution
    adjustment_factor = len([c for c in clipped if c > 0.7]) // 2
    base_score = sum(clipped) * 100
    
    # Dead computation: uses irrelevant math
    temp_debug = [abs(x - 0.5)**2 for x in values][:10]
    debug_total = sum(temp_debug)  # Unused
    
    return int(base_score - adjustment_factor * 10)

# Main execution
raw_data = [35, 89, 42, 76, 23, 91, 64]
config_weights = [0.8, 1.2, 0.9, 1.1]
thresholds = [(0.1, 0.8), (0.2, 0.9), (0.1, 0.7), (0.3, 0.85), (0.05, 0.6), (0.15, 0.95), (0.25, 0.8)]

# Irrelevant preprocessing chain
processed = [x for x in raw_data if x >= 20]
sorted_data = sorted(processed, reverse=True)
delta_diffs = [a - b for a, b in zip(sorted_data, sorted_data[1:])]  # Unused

normalized = normalize(sorted_data)
scaled_values = [val * 0.95 for val in normalized]  # Final input to function

# Dummy state tracking
state_log = []
for i, val in enumerate(scaled_values):
    if val > 0.7:
        state_log.append((i, 'high'))
    elif val > 0.4:
        state_log.append((i, 'medium'))
    else:
        state_log.append((i, 'low'))

# Key computation
final_score = compute_aggregate(scaled_values, thresholds)
print(f"Result: {final_score}")