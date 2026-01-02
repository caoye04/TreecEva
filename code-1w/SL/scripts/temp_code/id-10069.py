def analyze_vital(row, baseline):
    # Irrelevant transformation
    offset = sum([x ** 0.5 for x in baseline])
    adjusted = [val - baseline[i] + offset for i, val in enumerate(row)]
    return [a * 1.05 for a in adjusted]

# Distractor function – never called
def compute_stress_index(data):
    stress = 0
    for d in data:
        if d > 80:
            stress += d * 0.3
    return max(stress, 1e-6)

# Another decoy: complex but unused
transform_matrix = [[i * j + 2 for j in range(4)] for i in range(4)]

# Real data processing begins
baselines = [72, 120, 80, 95]
critical_flags = []
temporary_scores = {}

# Simulated sensor readings over time
health_data = [
    [70, 118, 82, 96],
    [74, 122, 78, 94],
    [76, 124, 85, 98],
    [68, 116, 70, 92]
]

# Unused but plausible structure
diagnostic_log = {f'entry_{i}': {f'param_{j}': 0 for j in range(4)} for i in range(4)}

# Thresholds for anomaly detection (used later)
thresholds = {
    'hr': (60, 100),
    'sys': (110, 140),
    'dias': (70, 90),
    'temp': (95, 100)
}

# Distractor: intermediate normalization (partially used, mostly noise)
normalized_shifts = []
for idx, row in enumerate(health_data):
    shift = [abs(row[i] - baselines[i]) / baselines[i] for i in range(len(row))]
    normalized_shifts.append(shift)

# Dead code path: looks important but unused
aggregate_risk = 0
for ns in normalized_shifts:
    if sum(ns) > 0.5:
        aggregate_risk += sum(ns) * 10

# Key function: actually contributes to final result
def evaluate_stability(metrics, limits):
    scores = []
    for i, series in enumerate(zip(*metrics)):
        low, high = list(limits.values())[i]
        stable = all(low <= x <= high for x in series)
        # Complex but meaningful calculation
        deviation = sum(abs(x - (low + high) / 2) for x in series) / len(series)
        score = 100 - deviation if stable else 50 - deviation
        scores.append(score)
    return scores

# Another red herring: entropy-like computation
import math
def shannon_like(seq):
    total = sum(seq)
    if total == 0:
        return 0
    probs = [v / total for v in seq if v > 0]
    return -sum(p * math.log(p) for p in probs)

entropy_values = [shannon_like(row) for row in health_data]

# Core logic buried among distractions
interim_results = []
for reading in health_data:
    analysis = analyze_vital(reading, baselines)
    # Only one component used downstream
    extracted_metric = analysis[2]  # diastolic-derived
    interim_results.append(extracted_metric * 0.8)

# This part seems like post-processing but is actually critical
evaluation_snippets = []
for i, val in enumerate(interim_results):
    # Conditional obfuscation
    if i % 2 == 0:
        evaluation_snippets.append(val + 5)
    else:
        evaluation_snippets.append(val - 3)

# Central aggregation function
def aggregate_metrics(dataset, bounds):
    # Heavily distracted logic
    temp_store = []
    for r in dataset:
        temp_store.append(r[3])  # collect temperature-like values
    
    # Actual key computation
    avg_temp = sum(temp_store) / len(temp_store)
    
    # Use evaluate_stability which depends on global thresholds and transposed data
    stability_profile = evaluate_stability(dataset, bounds)
    
    # Hidden dependency: only third element matters
    base_component = stability_profile[2]  # dias-related
    
    # Misleading combination
    phantom_weight = shannon_like(stability_profile) * 10
    
    # Final integration: subtle arithmetic
    result = base_component * 1.5 + avg_temp - sum(evaluation_snippets[:3]) * 0.5
    
    # Red herring return alternative
    if result < 0:
        return -result
    return abs(result)  # deterministic

# Critical execution point
final_diagnostic = aggregate_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")