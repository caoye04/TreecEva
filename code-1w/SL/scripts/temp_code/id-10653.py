def analyze_component(reading):
    if len(reading) < 3:
        return 0
    base = sum([ord(c) - 96 for c in reading[:3].lower()])
    adjustment = len(reading) * 2 - sum([1 for c in reading if c.isupper()])
    return base + adjustment // 2

# Irrelevant helper function (decoy)
def validate_entry(code):
    return code.startswith('X') and len(code) == 8 and code[-1].isdigit()

# Another decoy function with misleading purpose
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Unused but plausible-looking transformation
temp_registry = ['A12', 'B34', 'C56', 'D78']
processed = list(map(lambda x: x[::-1].lower(), temp_registry))
filtered = [p for p in processed if p.startswith('2')]

# Real data processing begins
raw_inputs = ['SignalAlpha', 'BetaSync', 'GammaWave', 'DeltaFlux']

# Distractor: complex-looking but unused list comprehension with string operations
_ = [x.upper()[::-1].replace('A', '@') for x in raw_inputs if len(x) > 7]

# Actual component analysis
component_values = [analyze_component(inp) for inp in raw_inputs]

# Simulated metric collection with dictionary operations
diagnostic_metrics = {
    'stability': component_values[0] * 0.8,
    'coherence': component_values[1] + component_values[2],
    'bandwidth': max(component_values),
    'latency': min(component_values) * 1.2,
    'harmonic': (component_values[2] - component_values[1]) * 0.5
}

# Distractor: irrelevant string splitting/joining
log_string = "|".join(raw_inputs)
split_parts = log_string.split('|')
rejoined = "-".join([part[:5] for part in split_parts if 'a' in part.lower()])

# Weight configuration (some weights are misleadingly set to zero)
weights = {
    'stability': 0.3,
    'coherence': 0.4,
    'bandwidth': 0.2,
    'latency': 0.0,  # This weight intentionally set to zero (red herring)
    'phase_noise': 0.1,  # Not present in metrics (distractor key)
    'harmonic': 0.1
}

# Dead code path: never executed but looks relevant
if diagnostic_metrics.get('efficiency', 0) > 50:
    weights['coherence'] *= 1.1

# Core aggregation logic
valid_keys = set(diagnostic_metrics.keys()) & set(weights.keys())
active_weights = {k: weights[k] for k in valid_keys if weights[k] > 0}

# Normalize weights to sum to 1.0
weight_sum = sum(active_weights.values())
normalized_weights = {k: v / weight_sum for k, v in active_weights.items()}

# Aggregate performance using only valid, non-zero weighted metrics
weighted_sum = sum(diagnostic_metrics[k] * normalized_weights[k] for k in normalized_weights)

# Final scaling based on system calibration (key step)
calibration_factor = len(raw_inputs) / 4.0  # Always 1.0 given input size
final_score = int(weighted_sum * calibration_factor)

# Output result as required
print(f"Result: {final_score}")