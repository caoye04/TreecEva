from itertools import compress

def analyze_efficiency(values):
    """Calculate efficiency ratio with sliding window."""
    if len(values) < 3:
        return 0.0
    ratios = []
    for i in range(len(values) - 2):
        window = values[i:i+3]
        avg = sum(window) / 3
        peak = max(window)
        ratios.append(avg / peak if peak != 0 else 0)
    return sum(ratios) / len(ratios) if ratios else 0.0

# Simulated sensor readings over time
temperature_data = [22, 24, 19, 25, 27, 23, 20, 26]
humidity_data = [45, 50, 60, 55, 40, 65, 70, 58]
pressure_data = [1013, 1015, 1010, 1018, 1020, 1012, 1008, 1016]

# Misleading preprocessing (some irrelevant)
deviations = [abs(t - 22) for t in temperature_data]
adjusted_humidity = [h + 5 for h in humidity_data if h < 60]  # partial list
pressure_changes = [pressure_data[i+1] - pressure_data[i] for i in range(len(pressure_data)-1)]

# Core metrics for system evaluation
efficiency_metric = analyze_efficiency(temperature_data)
stability_metric = sum([abs(pressure_changes[i]) for i in range(0, len(pressure_changes), 2)])
humidity_focus = len(list(compress(humidity_data, [h > 55 for h in humidity_data])))

# Weight factors (normalized)
weights = [0.4, 0.35, 0.25]

# Distractor: unused function
def calculate_entropy(data):
    from math import log
    freq = {}
    for d in set(data):
        freq[d] = data.count(d)
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Another distractor variable
redundant_calc = ''.join([str(int(h/10)) for h in humidity_data])

# Key metric derived via slicing and conditional logic
recent_trends = temperature_data[-4:]
recent_avg = sum(recent_trends) / len(recent_trends)
trend_boost = 1.1 if recent_avg > 23 else 1.0

# Conditional expression affecting final weight
adaptive_weights = [w * trend_boost if i == 0 else w for i, w in enumerate(weights)]

metrics = [
    efficiency_metric * 100,  # scaled
    100 - stability_metric,      # inverted penalty
    humidity_focus * 10         # amplified count
]

# Final performance evaluation with distraction
baseline_offset = 5.0
noise_floor = sum([d % 2 for d in deviations]) * 0.1  # negligible effect

final_score = evaluate_performance(metrics, adaptive_weights) if 'trend_boost' in locals() else 0

# Define function after usage (still valid in script context)
def evaluate_performance(mets, wts):
    """Weighted sum of performance metrics."""
    return sum(m * w for m, w in zip(mets, wts)) + noise_floor

# Recompute final score properly
final_score = evaluate_performance(metrics, adaptive_weights)

print(f"Result: {final_score}")