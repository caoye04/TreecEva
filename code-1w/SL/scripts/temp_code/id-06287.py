def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x for x in data if x > threshold]

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
temp_offset = 42

# Simulated sensor metrics (some relevant, some misleading)
metrics = [0.82, 0.91, 0.67, 0.74, 0.95]
weights = [3, 4, 2, 3, 5]

# Decoy variables with plausible but unused computations
raw_aggregate = sum([m * w for m, w in zip(metrics, weights)])
baseline_adjustment = (metrics[0] + metrics[-1]) / 2
scaling_factor = 1.0 + (0.1 * len(metrics))

# Unused transformation path (dead code)
def transform readings(reading_list):
    return [round(r ** 0.5, 3) for r in reading_list]

# Misleading intermediate calculation
weighted_sum = 0
for i in range(len(metrics)):
    if i % 2 == 0:
        weighted_sum += metrics[i] * weights[i] * 0.9  # Partial use with distortion
    else:
        weighted_sum += metrics[i] * weights[i] * 1.1

# Conditional expression used idiomatically
adjustment = 0.95 if sum(weights) > 15 else 1.05

# Core logic embedded within distractions
def process_performance(mets, wts):
    total_weight = sum(wts)
    normalized = [w / total_weight for w in wts]
    
    # Use enumerate and conditional expression (required features)
    adjusted_metrics = [
        m * (1.1 if i % 2 == 0 else 0.9) 
        for i, m in enumerate(mets)
    ]
    
    # Real computation buried among noise
    performance_product = 1.0
    for val in adjusted_metrics:
        performance_product *= val
    
    # Key aggregation
    base_score = sum(m * n for m, n in zip(adjusted_metrics, normalized))
    
    # Final adjustment using product as non-linear factor
    final_component = base_score * (performance_product ** 0.1)
    
    # This is the actual answer path
    return round(final_component * 1000)

# Unused alternative method (red herring)
def calculate_stability(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs)

# Execution point of interest
final_score = process_performance(metrics, weights)

# Print required result format
print(f"Result: {final_score}")