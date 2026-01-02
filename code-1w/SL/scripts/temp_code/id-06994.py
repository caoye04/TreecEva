def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    gaps = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return all(g == gaps[0] for g in gaps)

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

# Unused transformation path (dead code)
def transform_data(raw):
    processed = []
    for x in raw:
        if x % 2 == 0:
            processed.append(x // 2)
        else:
            processed.append(x * 3 + 1)
    return processed

# Misleading statistical function with no impact
def get_summary_stats(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    peak = max(values)
    trough = min(values)
    return {'mean': mean_val, 'variance': variance, 'peak': peak, 'trough': trough}

# Core logic disguised among distractions
def generate_baseline(n):
    base = [1]
    for i in range(1, n):
        base.append(base[-1] * 2 + (i % 3))
    return set(base)

def filter_candidates(pool, threshold=50):
    # Linear search with filtering (irrelevant to final result)
    valid = []
    for item in pool:
        if isinstance(item, int) and item > 0 and (item & (item - 1)) == 0:  # power of two
            valid.append(item)
    return valid

def evaluate_performance(metrics, reference):
    intersection = metrics & reference
    union = metrics | reference
    jaccard_index = len(intersection) / len(union) if union else 0
    
    # Secondary scoring based on pattern analysis
    sorted_vals = sorted(list(metrics))
    has_arithmetic = analyze_pattern(sorted_vals[:min(4, len(sorted_vals))])
    
    # Main calculation hidden in composite logic
    base_score = len(intersection) * 17
    penalty = 0
    if len(metrics) > len(reference) * 1.5:
        penalty = (len(metrics) - len(reference)) * 5
    adjustment = 1 if has_arithmetic else 0.9
    
    # Decoy computation that looks important but isn't used directly
    _redundant_metric = (len(metrics) + len(reference)) / (len(union) + 1e-8)
    _hidden_check = len(intersection) >= 0.7 * len(reference)
    
    final_raw = (base_score - penalty) * adjustment
    return int(round(final_raw))

# Irrelevant global variables
MAX_ITER = 1000
DEBUG_MODE = False
VERSION_TAG = 'v2.1-alpha'
TEMP_BUFFER = [0] * 256

# Setup data with meaningful names
primary_sequence = [1, 3, 7, 15, 31, 63]
secondary_data = [2, 4, 8, 16, 32, 64, 128]
metadata_flags = {1, 2, 4, 8, 16}  # powers of two

# Transformations that feed into final logic
processed_primary = set(x + 1 for x in primary_sequence if x < 50)
expanded_secondary = set(y * 2 for y in secondary_data)

# Generate true baseline (critical path)
baseline = generate_baseline(6)

# Construct metric set through multiple steps
intermediate_merge = processed_primary | expanded_secondary
filtered_metrics = {val for val in intermediate_merge if val % 3 != 0}  # remove multiples of 3
metric_set = filter_candidates(list(filtered_metrics))  # apply irrelevant filter
metric_set = set(metric_set)  # reconvert to set

# Add red herring operations
_ignored_result = compute_entropy([1,1,2,3,5,8])
dummy_analysis = get_summary_stats(secondary_data)

# Key statement - target of evaluation
final_score = evaluate_performance(metric_set, baseline)

# Print result as required
print(f"Target result: {final_score}")