def analyze_trend(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        smoothed.append(sum(data[i:i+window]) / window)
    return smoothed

# Simulated sensor readings over time
temperature_readings = [20, 22, 25, 24, 23, 26, 28, 27, 25, 24]

# Apply smoothing to reduce noise (irrelevant for final result but adds cognitive load)
smoothed_temps = analyze_trend(temperature_readings, window=2)

# Auxiliary calculations with misleading variables
cumulative_drift = 0
for reading in temperature_readings:
    cumulative_drift += (reading - 24) ** 0.5 if reading > 24 else 0

# Weight adjustment factors (some are red herrings)
factor_a = len(smoothed_temps) / 2
factor_b = cumulative_drift * 0.75
offset_correction = factor_a - 1.5  # Unused distraction

# Real metrics used in evaluation
metrics = {
    'stability': sum(1 for i in range(1, len(temperature_readings)) if abs(temperature_readings[i] - temperature_readings[i-1]) <= 2),
    'peaks': sum(1 for x in temperature_readings if x >= 25),
    'consistency': len(temperature_readings) - len(smoothed_temps)
}

# Weights for scoring (only these matter)
weights = {
    'stability': 1.2,
    'peaks': 0.8,
    'consistency': 0.5
}

# Misleading secondary metric calculation (dead code path)
def calculate_efficiency(x):
    return x * 0.9 if x > 20 else x * 1.1

hypothetical_efficiency = calculate_efficiency(metrics['stability'])

# Core logic: weighted score computation
final_score = 0
for key in metrics:
    if key in weights:
        final_score += metrics[key] * weights[key]

# Additional irrelevant transformation
adjusted_score = final_score * (1 + offset_correction / 10)  # Not used

# Print final answer as required
print(f"Result: {final_score}")