def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function analyzing efficiency (dead code path)."""
    return sum(1 for x in data if x > threshold) / len(data)


def compute_entropy(values):
    """Another decoy: computes entropy but never used in main logic."""
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    return -sum((count / total) * log2(count / total) for count in freq.values())

# Irrelevant global constants (distractors)
MAX_CAPACITY = 8192
BASELINE_OFFSET = 37
DEFAULT_TIMEOUT = 120

# Simulated sensor readings and calibration factors (mix of relevant and irrelevant)
sensor_data = [0.6, 0.8, 0.3, 0.9, 0.7, 0.5, 0.4]
calibration = [1.1, 0.9, 1.0, 1.2, 0.8, 1.0, 1.1]

# Misleading intermediate transformation
adjusted_readings = [round(d * c, 3) for d, c in zip(sensor_data, calibration)]

# Unused complex structure (red herring)
status_map = {
    'critical': [],
    'warning': [],
    'normal': []
}
for i, val in enumerate(adjusted_readings):
    if val > 0.85:
        status_map['critical'].append(i)
    elif val > 0.6:
        status_map['warning'].append(i)
    else:
        status_map['normal'].append(i)

# Actual relevant data structures
metrics = [
    {'name': 'latency', 'value': 0.45, 'weight': 0.3},
    {'name': 'throughput', 'value': 0.82, 'weight': 0.4},
    {'name': 'stability', 'value': 0.68, 'weight': 0.2},
    {'name': 'reliability', 'value': 0.91, 'weight': 0.1}
]

weights = [m['weight'] for m in metrics]
raw_values = [m['value'] for m in metrics]

# Bitwise manipulation on indices (irrelevant but looks important)
index_flags = 0
for i, val in enumerate(raw_values):
    if val > 0.7:
        index_flags |= (1 << i)  # Set bit i

# Decoy list comprehension with string operations
diagnostic_tags = [
    f"CHK_{i:02X}_{name.upper()[::-1]}" 
    for i, name in enumerate(['latency', 'throughput', 'stability', 'reliability'])
]

# Core evaluation logic hidden among noise
def normalize_score(val, min_val=0.0, max_val=1.0):
    return (val - min_val) / (max_val - min_val)

def weighted_average(values, weights):
    return sum(v * w for v, w in zip(values, weights))

def clamp(x, low, high):
    return max(low, min(high, x))

def evaluate_performance(metrics, weights):
    # Step 1: Extract and normalize values
    norm_values = [normalize_score(m['value']) for m in metrics]
    
    # Step 2: Apply weight adjustment using modular arithmetic on length
    adjusted_weights = [
        w * (len(metrics) % 3 + 1) if i % 2 == 0 else w 
        for i, w in enumerate(weights)
    ]
    
    # Step 3: Normalize adjusted weights
    total_weight = sum(adjusted_weights)
    normalized_weights = [w / total_weight for w in adjusted_weights]
    
    # Step 4: Compute base score
    base_score = weighted_average(norm_values, normalized_weights)
    
    # Step 5: Apply stability bonus if throughput > 0.8
    if metrics[1]['value'] > 0.8:
        base_score += 0.05
    
    # Step 6: Apply reliability penalty if any metric < 0.5
    if any(m['value'] < 0.5 for m in metrics):
        base_score -= 0.03
    
    # Step 7: Final clamping to valid range
    final = clamp(base_score, 0.0, 1.0)
    
    # Step 8: Scale to integer percentage and back to decimal
    scaled = round(final * 100) / 100
    
    return scaled

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")