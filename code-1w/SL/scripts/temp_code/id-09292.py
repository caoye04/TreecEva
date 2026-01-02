from itertools import combinations
import math

# Simulate sensor readings from a thermal regulation system
raw_readings = [23.4, 25.1, 22.8, 26.5, 24.3, 23.9, 27.1, 25.6]

# Misleading preprocessing: irrelevant transformation
offset_adjusted = [round(r + 0.6 - 0.3 * 2, 2) for r in raw_readings]  # net +0.0, no effect
temp_buckets = {i: [] for i in range(3)}

# Distribute into arbitrary buckets (only used for distraction)
for idx, val in enumerate(offset_adjusted):
    temp_buckets[idx % 3].append(val)

# Actual relevant processing
filtered_readings = [r for r in raw_readings if 23 <= r <= 26]  # exclude outliers
smoothed = [round((filtered_readings[i] + filtered_readings[i+1]) / 2, 2) 
             for i in range(len(filtered_readings) - 1)]
delta_changes = [abs(smoothed[i+1] - smoothed[i]) for i in range(len(smoothed) - 1)]

# Compute stability metric (average fluctuation)
stability_index = sum(delta_changes) / len(delta_changes) if delta_changes else 0.0

# Simulate process phases with dummy state tracking
phases = ['init', 'warmup', 'stable', 'cooling']
phase_durations = {'init': 12, 'warmup': 25, 'stable': 40, 'cooling': 18}
total_runtime = sum(phase_durations.values())

# Irrelevant combinatorial analysis on small subsets
pairwise_combs = list(combinations(raw_readings[:4], 2))
mean_product_entropy = sum(math.log(abs(a * b)) for a, b in pairwise_combs if a * b > 0) / len(pairwise_combs)

# Hidden correction factor derived from stability
adjustment_factor = round(1 - (stability_index / 10), 2)

# Lambda-based dynamic threshold
threshold_fn = lambda x: 0.85 if x > 0.5 else 0.65
confidence_weight = threshold_fn(stability_index)

# Data aggregation into final processed structure
processed_data = {
    'base_count': len(filtered_readings),
    'peak_stability': max(0.1, 1 - stability_index),
    'runtime_factor': phase_durations['stable'] / total_runtime,
    'adjustment': adjustment_factor,
    'weight': confidence_weight
}

# Extraneous dictionary operations for distraction
processed_data['derived_keys'] = [
    k.upper() + '_NORM' for k in processed_data.keys() if isinstance(processed_data[k], (int, float))
]
processed_data['dummy_metric'] = sum(
    len(k) * v for k, v in processed_data.items() if isinstance(v, (int, float))
)

# Core calculation function (appears complex due to layout)
def calculate_efficiency(data):
    count = data['base_count']
    stability = data['peak_stability']
    runtime_ratio = data['runtime_factor']
    adj = data['adjustment']
    w = data['weight']
    
    # Real computation chain
    base_eff = count * 3.5
    stability_bonus = base_eff * stability
    adjusted_eff = stability_bonus * runtime_ratio * adj
    final_eff = adjusted_eff * w
    
    # Distractor: unused internal metrics
    ceiling_potential = base_eff * 1.8
    efficiency_gap = ceiling_potential - final_eff
    
    return int(round(final_eff))

# Key execution point
efficiency_score = calculate_efficiency(processed_data)

# Additional red herring: unused function
def predict_failure_modes(data):
    return [k for k, v in data.items() if str(v).startswith('0.')]

Result: efficiency_score