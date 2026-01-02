from collections import defaultdict, Counter
import math

# Irrelevant utility function (decoy)
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

def calculate_entropy(values):
    """Misleading intermediate calculation"""
    freqs = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Unused but plausible function
def adjust_for_bias(arr, factor=1.0):
    return [x + factor * (1 - x) for x in arr]

# Core logic disguised among distractions
bias_mode = True
scaling_factor = 0.87

# Simulated telemetry data (some irrelevant)
telemetry_logs = [
    {'event': 'start', 'timestamp': 1001, 'payload': [1,1,0]},
    {'event': 'compute', 'timestamp': 1003, 'payload': [1,0,1]},
    {'event': 'end', 'timestamp': 1008, 'payload': [0,1,1]}
]

# Distractor: complex-looking but unused transformation
telemetry_stats = defaultdict(int)
for log in telemetry_logs:
    telemetry_stats[log['event']] += 1
    telemetry_stats['total_duration'] = log['timestamp'] - telemetry_logs[0]['timestamp']

# Real input data buried in noise
raw_metrics = [0.78, 0.82, 0.65, 0.91, 0.54]

# Weighting system with red herring branch
use_dynamic_weights = False
static_weights = [0.1, 0.2, 0.3, 0.25, 0.15]
dynamic_weights = [round(abs(math.sin(i)), 2) for i in range(5)]

# Dead code path (never taken)
if len(raw_metrics) > 10:
    weights = dynamic_weights
else:
    weights = static_weights  # This actually runs, but looks suspicious

# More misdirection
shadow_copy = raw_metrics.copy()
adjustment_map = lambda x: x * 1.1 if x < 0.7 else x * 0.95
adjusted_metrics = list(map(adjustment_map, shadow_copy))

# Actual relevant computation starts here
filtered_metrics = [m for m in raw_metrics if m >= 0.6]  # filters 0.54

# Secondary filter based on index parity (plausible but non-obvious)
indexed_data = [(i, m) for i, m in enumerate(filtered_metrics)]
parity_filtered = [m for i, m in indexed_data if i % 2 == 0]  # takes index 0,2 -> 0.78, 0.65

# Aggregation via weighted sum using original indexing alignment
aligned_weights = [weights[i] for i in range(len(raw_metrics))]  # uses full weight vector
trimmed_weights = [w for i, w in enumerate(aligned_weights) if raw_metrics[i] >= 0.6 and i % 2 == 0]

# Normalize weights for trimmed set
weight_sum = sum(trimmed_weights)
normalized_contribution = sum(
    parity_filtered[i] * (trimmed_weights[i] / weight_sum)
    for i in range(len(parity_filtered))
)

# Final nonlinear transformation
transformed_value = math.tanh(normalized_contribution * 2)

# Evaluate performance - key statement
final_score = int(round(transformed_value * 1000))

# Distractor print (not affecting result)
entropy_debug = calculate_entropy([1,2,2,3,3,3])

# Unused lambda
data_enhancer = lambda x, y: x + y * scaling_factor

# Critical output
Result: final_score