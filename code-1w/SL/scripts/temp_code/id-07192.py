import math

def preprocess_readings(readings):
    normalized = []
    avg = sum(readings) / len(readings)
    variance_accum = 0
    for val in readings:
        diff = val - avg
        variance_accum += diff * diff
    std_dev = math.sqrt(variance_accum / len(readings))
    
    for val in readings:
        if std_dev != 0:
            z = (val - avg) / std_dev
            if z > 1.5:
                normalized.append(val * 0.9)
            else:
                normalized.append(val)
        else:
            normalized.append(val)
    return normalized

# Simulate sensor calibration drift correction
calibration_factor = 1.03
drift_adjustment = 0.98
temp_buffer = [102, 95, 110, 87, 93]
adjusted_temps = [t * calibration_factor for t in temp_buffer]

# Irrelevant transformation: spectral weighting (not used in final path)
spectral_weights = [0.88, 1.02, 0.91, 0.99, 1.05]
weighted_spectrum = [adjusted_temps[i] * spectral_weights[i] for i in range(len(adjusted_temps))]
mean_weighted = sum(weighted_spectrum) / len(weighted_spectrum)

# Main experimental data
experiment_data = [45, 67, 89, 54, 72]

# Secondary processing chain (partial distractor)
smoothed_data = []
for i in range(len(experiment_data)):
    neighbors = []
    for j in range(max(0, i-1), min(len(experiment_data), i+2)):
        neighbors.append(experiment_data[j])
    smoothed_val = sum(neighbors) / len(neighbors)
    smoothed_data.append(round(smoothed_val))

# Core logic with conditional expression and accumulation
baseline_shift = 5
activation_threshold = 60
significance_mask = [1 if x > activation_threshold else 0 for x in experiment_data]

amplification_factor = 1.75
boosted_signals = [
    x * amplification_factor if mask else x * 0.4
    for x, mask in zip(experiment_data, significance_mask)
]

# Accumulation with modular adjustment
cumulative_impact = 0
for idx, val in enumerate(boosted_signals):
    phase_mod = (idx + 1) % 4 or 4
    adjusted_val = val * (phase_mod / 3.5)
    cumulative_impact += adjusted_val

# Distractor block: entropy estimation (unused)
data_entropy = 0
if boosted_signals:
    total = sum(boosted_signals)
    if total > 0:
        probabilities = [s / total for s in boosted_signals]
        data_entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)

# Final processing function
def harvest_results(raw):
    processed = preprocess_readings(raw)
    
    # Conditional expression usage
    peak_response = max(processed) if len(processed) > 2 else 0
    response_factor = 2.1 if peak_response >= 80 else 1.6
    
    # Additional irrelevant computation: stability index
    stability_index = 0
    for i in range(1, len(processed)):
        stability_index += abs(processed[i] - processed[i-1])
    stability_index /= len(processed)
    
    # Actual yield calculation
    base_yield = sum(processed) * response_factor
    penalty_rate = 0.05 * sum(1 for x in processed if x < 40)
    net_yield = base_yield * (1 - penalty_rate)
    
    # Final nonlinear transformation
    final_output = int(net_yield + math.sqrt(abs(net_yield)) // 2)
    
    return final_output

# Execute main logic
final_yield = harvest_results(experiment_data)
print(f"Result: {final_yield}")