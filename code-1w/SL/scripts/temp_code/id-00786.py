import math

# Simulated sensor data log with timestamps and readings
data_log = [
    {'time': 100, 'temp': 23.5, 'pressure': 101.3, 'status': 'active'},
    {'time': 105, 'temp': 24.1, 'pressure': 101.5, 'status': 'active'},
    {'time': 110, 'temp': 22.8, 'pressure': 100.9, 'status': 'idle'},
    {'time': 115, 'temp': 25.3, 'pressure': 102.1, 'status': 'active'},
    {'time': 120, 'temp': 24.7, 'pressure': 101.8, 'status': 'active'}
]

# Auxiliary transformation: normalize pressure values
def normalize(values):
    mean_val = sum(values) / len(values)
    return [(v - mean_val) / mean_val for v in values]

# Misleading function - appears useful but not used in final calculation
def analyze_trend(seq):
    trend_score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            trend_score += 1
        elif seq[i] < seq[i-1]:
            trend_score -= 1
    return abs(trend_score)

# Higher-order function that looks important but only partially contributes
apply_correction = lambda f, x: f(x) if x > 0 else 0

# Core processing pipeline
def process_metrics(log):
    temperatures = [entry['temp'] for entry in log]
    pressures = [entry['pressure'] for entry in log]
    active_count = len([e for e in log if e['status'] == 'active'])

    # Irrelevant normalization (distractor)
    norm_pressures = normalize(pressures)

    # Compute base metrics
    avg_temp = sum(temperatures) / len(temperatures)
    temp_variance = sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)
    
    # Hidden key computation: count how many temps are above average + 0.5
    threshold = avg_temp + 0.5
    above_threshold = sum(1 for t in temperatures if t > threshold)

    # Dummy state tracking (not used later)
    state_history = []
    cumulative_drift = 0.0
    for p in pressures:
        drift = apply_correction(math.log, abs(p - 101.3))
        cumulative_drift += drift
n        state_history.append('drift_applied')

    # Secondary metric with red herring variables
    stability_index = 0
    for i in range(1, len(pressures)):
        diff = abs(pressures[i] - pressures[i-1])
        if diff < 0.7:
            stability_index += 1

    # Efficiency score depends only on: active_count * above_threshold
    # All prior computations create cognitive load but only these two matter
    efficiency_score = active_count * above_threshold

    # Dead code branch (never executed, adds distraction)
    if False:
        efficiency_score = int(efficiency_score * stability_index / (temp_variance + 1))

    final_output = efficiency_score
    return final_output

# Execute
result_value = process_metrics(data_log)
print(f"Result: {result_value}")