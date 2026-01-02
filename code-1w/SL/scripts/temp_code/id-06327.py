import math

# Simulated sensor data processing with performance evaluation
raw_readings = [0.88, 0.92, 0.76, 0.94, 0.85, 0.81, 0.91, 0.89]
noise_floor = 0.1
amplification_factor = 2.5
calibration_offset = -0.05

# Irrelevant auxiliary variables (distractors)
temp_buffer = [x * 1.05 for x in raw_readings if x > 0.8]
baseline_correction = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0.0
snapshot_log = {'timestamp': 1234567890, 'status': 'calibrated'}

# Signal conditioning chain (some steps are red herrings)
filtered_signal = [max(0, reading - noise_floor) for reading in raw_readings]
scaled_output = [x * amplification_factor for x in filtered_signal]
adjusted_signal = [x + calibration_offset for x in scaled_output]
clipped_signal = [min(1.0, max(0, x)) for x in adjusted_signal]  # Normalize to [0,1]

# Decoy transformation: complex but unused later
transformed_magnitude = [math.sin(x * math.pi / 2) ** 2 for x in clipped_signal]
decoherence_index = sum((i + 1) * val for i, val in enumerate(transformed_magnitude)) / sum(transformed_magnitude) if sum(transformed_magnitude) != 0 else 0

# Primary metric computation path
activation_mask = [1 if x >= 0.8 else 0 for x in clipped_signal]
burst_segments = []
current_burst = 0
for val in activation_mask:
    if val == 1:
        current_burst += 1
    else:
        if current_burst > 0:
            burst_segments.append(current_burst)
            current_burst = 0
if current_burst > 0:
    burst_segments.append(current_burst)

# Secondary decoy logic (dead code path - never executed due to condition)
if len(burst_segments) > 100:
    smoothed_bursts = [b * 0.9 for b in burst_segments]
    normalized_energy = sum(smoothed_bursts) / len(smoothed_bursts)
elif len(burst_segments) == 0:
    normalized_energy = 0.0
else:
    normalized_energy = sum(b ** 1.5 for b in burst_segments) / len(burst_segments)  # Unused!

# Real metric derivation begins here
metric_data = [x ** 2 for x in clipped_signal if x >= 0.7]
base_threshold = 0.65

# Evaluate performance using non-obvious aggregation
def evaluate_performance(metrics, threshold):
    if not metrics:
        return 0.0
    
    # Red herring local computation
    peak_response = max(metrics)
    response_ratio = peak_response / (sum(metrics) / len(metrics))
    efficiency_penalty = 0.0
    if response_ratio > 1.2:
        efficiency_penalty = (response_ratio - 1.2) * 5
    
    # Actual decision logic buried in distractions
    significant_contributions = [m for m in metrics if m >= threshold]
    contribution_weight = len(significant_contributions) / len(metrics)
    
    # Hidden accumulation pattern
    cumulative_impact = 0.0
    decay = 0.85
    for i, val in enumerate(significant_contributions):
        cumulative_impact += val * (decay ** i)
    
    # Final score combines multiple subtle effects
    stability_bonus = 1.0
    if len(burst_segments) > 0 and all(b <= 2 for b in burst_segments):
        stability_bonus = 1.25
    
    # Critical line: what is the value of final_score after this statement?
    final_score = (cumulative_impact * contribution_weight + 10) * stability_bonus - efficiency_penalty
    
    return final_score

# Execute main evaluation
eval_result = sum(transformed_magnitude) / len(raw_readings)  # Misleading intermediate
reference_anchor = math.log(baseline_correction + 1) if baseline_correction > 0 else 0  # Unused

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")