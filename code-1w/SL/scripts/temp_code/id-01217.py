def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function analyzing efficiency (dead code path)."""
    if not data:
        return 0
    avg = sum(data) / len(data)
    return sum(1 for x in data if x > avg * threshold)


def transform_sequence(seq):
    """Misleading transformation that scrambles input but is never used."""
    transformed = [seq[i] ^ i for i in range(len(seq))]
    rotated = transformed[2:] + transformed[:2]
    return [x % 17 for x in rotated]

# Irrelevant global constants (distractors)
MAX_CAPACITY = 999
BASE_OFFSET = 37
DEFAULT_MODE = 'legacy'

# Real data used in computation
raw_metrics = [88, 54, 76, 92, 67]
metric_names = ['latency', 'throughput', 'accuracy', 'bandwidth', 'stability']
weights = {'latency': 0.3, 'throughput': 0.2, 'accuracy': 0.25, 'bandwidth': 0.15, 'stability': 0.1}

# Misleading intermediate calculations (red herrings)
decoy_sum = sum(x ** 0.5 for x in raw_metrics if x % 2 == 0)
temp_result = (decoy_sum * 1.618) % 100

# Dictionary construction with enumeration (relevant: dictionary and enumerate)
metrics = {name: raw_metrics[i] for i, name in enumerate(metric_names)}

# Spurious list creation and slicing (irrelevant slicing distractor)
shadow_copy = raw_metrics[1:4][::-1]
shadow_copy.append(999)  # Dead mutation

# Fake normalization function (never called)
def normalize_values(vals):
    m = min(vals)
    M = max(vals)
    return [(v - m) / (M - m) * 100 for v in vals]

# Core logic: recursive weight adjustment (recursion + dict operations)
def adjust_weights(w_dict, depth=3):
    if depth <= 0:
        return w_dict
    new_w = {}
    prev_val = None
    for key, val in w_dict.items():
        if prev_val is not None:
            new_w[key] = val + (prev_val * 0.1)
        else:
            new_w[key] = val
        prev_val = val
    return adjust_weights(new_w, depth - 1)

# Actual evaluation function
def evaluate_performance(met, w):
    # Adjust weights recursively (key relevant step)
    adjusted = adjust_weights(w)
    
    # Zip metrics with sorted order (zip + sorting)
    sorted_pairs = sorted(met.items(), key=lambda x: x[1], reverse=True)
    zipped_data = list(zip([p[1] for p in sorted_pairs], adjusted.values()))
    
    # Compute weighted score
    score = sum(value * weight for value, weight in zipped_data)
    
    # Irrelevant bitwise manipulation (distractor)
    magic_key = 0
    for i, (val, _) in enumerate(zipped_data):
        magic_key ^= int(val) & (i + 1) | 5
    
    # Dummy container (unused)
    audit_log = {f'step_{i}': v * 1.01 for i, v in enumerate(zipped_data)}
    
    # Real result calculation
    final = score * 0.95  # Final scaling
    return final

# Unused data structure (cross-reference red herring)
reference_grid = [[i + j for j in range(5)] for i in range(5)]
for row in reference_grid:
    row[:] = row[::-1]

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")