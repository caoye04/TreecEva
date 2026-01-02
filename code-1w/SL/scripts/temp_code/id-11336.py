def analyze_trends(data, threshold=0.5):
    """Irrelevant trend analysis function with misleading computations."""
    moving_avg = sum(data) / len(data)
    volatility = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    signal_strength = moving_avg * volatility
    normalized = [x / max(data) for x in data]
    return [x for x in normalized if x > threshold]

# Irrelevant constants and decoy variables
decoys = [2.71, 3.14, 1.41, 0.577, 1.618]
offset_map = {'a': 1, 'b': 2, 'c': 3}
scaling_factor = 1.23

# Real input data (simulated sensor readings)
raw_readings = [0.8, 0.9, 0.75, 0.85, 0.92, 0.78, 0.88]

# Misleading transformation chain
temp_filtered = [x for x in raw_readings if x > 0.7]
smoothed = [sum(temp_filtered[i:i+2]) / 2 for i in range(len(temp_filtered)-1)]
adjusted = [x * scaling_factor for x in smoothed if x < 0.9]

# Decoy function that looks important but is unused
def compute_entropy(values):
    from math import log
    total = sum(values)
    probs = [v/total for v in values]
    return -sum(p * log(p) for p in probs if p > 0)

# Core logic disguised among distractions
baseline = (0.8 + 0.85 + 0.78) / 3
metric_data = [
    ('precision', raw_readings[0] * 100),
    ('recall', raw_readings[2] * 95),
    ('f1', raw_readings[4] * 88),
    ('support', 120)
]

# Distractor: complex-looking but unused list comprehension
reweighted_metrics = [
    (name.upper(), val * (1.1 if name in ['precision','recall'] else 1.0))
    for name, val in metric_data[:-1]
]

# Conditional branches with red herrings
if len(raw_readings) > 5:
    adjustment = 0.95
    if baseline > 0.82:
        adjustment *= 0.98
    else:
        adjustment *= 1.02
else:
    adjustment = 1.05

# Tuple unpacking distraction
categories = ['A', 'B', 'C']
weights = [0.5, 0.3, 0.2]
combo = list(zip(categories, weights))

# Key computation buried in distractions
effective_values = []
for _, val in metric_data[:3]:
    if val > 80:
        effective_values.append(val * 0.9)
    else:
        effective_values.append(val * 1.1)

aggregated = sum(effective_values) / len(effective_values)

# Another decoy operation
checksum = sum(int(x*10) for x in decoys) % 7

# Critical assignment obscured by context
def evaluate_performance(metrics, base):
    score = 0
    for i, (_, val) in enumerate(metrics[:3]):
        diff = val - (base * (85 + i*5))
        if diff >= 0:
            score += 10 + diff
        else:
            score += 5 + diff/2
    return int(score * adjustment)

# Unused but plausible-looking function call
dummy_call = analyze_trends(smoothed, 0.8)

# The actual key statement
final_score = evaluate_performance(metric_data, baseline)

print(f"Target result: {final_score}")