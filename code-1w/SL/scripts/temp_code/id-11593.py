import itertools

# Simulated sensor data processing system for environmental monitoring
base_readings = [0.45, 0.78, 0.33, 0.91, 0.67]
offsets = [0.01, -0.02, 0.005, 0.03, -0.015]

# Irrelevant auxiliary arrays (distractor)
aux_data = [x ** 2 for x in base_readings if x > 0.5]
dummy_pairs = list(itertools.combinations(base_readings, 2))

# Apply corrections to raw data
calibrated = [a + b for a, b in zip(base_readings, offsets)]

# Noise filter simulation (only affects values above threshold)
filtered = []
for val in calibrated:
    if val > 0.8:
        val = val * 0.95
    elif val < 0.35:
        val = val * 1.1
    filtered.append(round(val, 4))

# Derived metrics (some are decoys)
mean_val = sum(filtered) / len(filtered)
variance = sum((x - mean_val) ** 2 for x in filtered) / len(filtered)
peak_to_avg = max(filtered) / mean_val

# Decoy metric calculations using itertools (distractor)
pairwise_deltas = [abs(a - b) for a, b in itertools.permutations(filtered, 2)]
longest_run = max([len(list(g)) for k, g in itertools.groupby([x > mean_val for x in filtered])])

# Weighted importance factors for real evaluation
weights = {
    'stability': 0.4,
    'consistency': 0.35,
    'responsiveness': 0.25
}

# Simulated reference benchmark (irrelevant but looks important)
baseline_profile = {k: v * 0.98 for k, v in weights.items()}

# Core logic disguised among distractions
def calculate_stability(series):
    diffs = [abs(series[i] - series[i+1]) for i in range(len(series)-1)]
    return 1 - (sum(diffs) / (len(diffs) * 0.5))

def assess_consistency(series):
    q1 = sorted(series)[len(series)//4]
    q3 = sorted(series)[3*len(series)//4]
    iqr = q3 - q1
    return 1 / (1 + iqr)

def measure_responsiveness(series, baseline=0.5):
    deviations = [abs(x - baseline) for x in series]
    return sum(1 for d in deviations if d > 0.1) / len(deviations)

# Decoy functions (never called - dead code path)
def deprecated_normalization(data):  # Unused
    m = min(data)
    M = max(data)
    return [(x - m) / (M - m) for x in data]

def legacy_metric_engine(seq):  # Unused
    return sum(x * (i+1) for i, x in enumerate(seq)) / sum(range(1, len(seq)+1))

# Lambda-based transformation chain (relevant)
transform_chain = [
    lambda x: round(x, 3),
    lambda x: x + 0.01 if x < 0.3 else x,
    lambda x: 0.99 if x > 0.9 else x
]

processed = filtered
for func in transform_chain:
    processed = [func(x) for x in processed]

# Build metric set with both real and misleading components
metric_set = {
    'raw_count': len(base_readings),  # Distractor
    'stability': calculate_stability(processed),
    'consistency': assess_consistency(processed),
    'responsiveness': measure_responsiveness(processed),
    'entropy': sum(-x * __import__('math').log2(x) for x in processed if x > 0),  # Looks complex but unused in final score
    'trend_strength': abs(sum(processed[i+1] - processed[i] for i in range(len(processed)-1)))  # Red herring
}

# Final evaluation (key statement)
final_score = evaluate_performance(metric_set, weights)

# Critical function buried after distractions
def evaluate_performance(metrics, weight_map):
    # Only three weights are used in calculation despite more metrics existing
    s = metrics['stability'] * weight_map['stability']
    c = metrics['consistency'] * weight_map['consistency']
    r = metrics['responsiveness'] * weight_map['responsiveness']
    return round(s + c + r, 6)  # Deterministic scalar output

# Print result as required
print(f"Result: {final_score}")