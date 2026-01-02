import math

# Simulated sensor array data (irrelevant for final result)
sensor_readings = [0.1, 0.4, 0.7, 0.9, 0.2]
noise_floor = 0.05
filtered_data = [x for x in sensor_readings if x > noise_floor]

def analyze_signal(data):
    return sum([math.sin(x) * math.exp(-x) for x in data])

# Unused signal analysis (distractor)
signal_strength = analyze_signal(filtered_data)

# Core evaluation parameters
base_metrics = {
    'accuracy': 87.5,
    'latency': 120,
    'throughput': 450,
    'energy_efficiency': 88.3
}

# Irrelevant transformation (dead path)
transformed = {k: v ** 0.5 for k, v in base_metrics.items() if 'y' in k}

# Weight configuration (only this matters)
weights = [0.3, 0.2, 0.4, 0.1]

# Derived metrics with red herring calculations
computed = {}
for k, v in base_metrics.items():
    if k == 'latency':
        computed[k] = 100 - (v / 2)  # Inverted: lower latency = higher score
    elif k == 'throughput':
        computed[k] = min(v / 5, 100)
    else:
        computed[k] = v  # accuracy and energy_efficiency used directly

# Spurious intermediate normalization (misleading)
normalized = {k: (v - 50) / 50 for k, v in computed.items()}

# Fake optimization pass (decoy function call)
def optimize_system(config):
    return {key: val * 0.95 for key, val in config.items()}

optimized_metrics = optimize_system(computed)  # Result unused

# Critical metric adjustment based on conditional logic
adjusted_metrics = []
for i, (k, v) in enumerate(computed.items()):
    adjustment_factor = 1.0
    if v > 90:
        adjustment_factor = 0.95
    elif v < 60:
        adjustment_factor = 1.1
    
    # Only this line chain leads to correct answer
    adjusted_value = v * adjustment_factor
    adjusted_metrics.append(adjusted_value)

# Decoy list comprehension with side-effect-free operation
_ = [x * 1.05 for x in adjusted_metrics if x > 100]

# Final weighted scoring logic (answer depends only on this)
def evaluate_performance(metrics_list, weight_vector):
    sorted_vals = sorted(metrics_list)  # Red herring sort (not needed)
    total = 0.0
    for idx in range(len(weight_vector)):
        # Actual computation uses original order, not sorted
        contribution = list(metrics_list)[idx] * weight_vector[idx]
        total += contribution
    return round(total, 4)

# Execution point of interest
final_score = evaluate_performance(adjusted_metrics, weights)

# Print result as required
print(f"Result: {final_score}")