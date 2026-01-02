from collections import defaultdict, Counter
import math

# Simulated sensor array data (real values)
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
raw_readings = [
    {'S1': [1.2, 1.5, 1.3], 'S2': [0.9, 1.0, 1.1], 'S3': [2.1, 2.0, 2.2], 'S4': [0.8, 0.7, 0.9], 'S5': [3.0, 3.1, 2.9]},
    {'S1': [1.4, 1.6, 1.5], 'S2': [1.2, 1.3, 1.1], 'S3': [2.3, 2.4, 2.2], 'S4': [0.6, 0.8, 0.7], 'S5': [3.2, 3.3, 3.1]},
    {'S1': [1.7, 1.8, 1.6], 'S2': [1.4, 1.5, 1.6], 'S3': [2.5, 2.6, 2.4], 'S4': [0.9, 1.0, 0.8], 'S5': [3.4, 3.5, 3.6]}
]

# Irrelevant baseline calibration map (distractor)
calibration_map = {
    'S1': 0.05, 'S2': 0.03, 'S3': 0.07, 'S4': 0.02, 'S5': 0.08
}

# Misleading auxiliary function (dead code path)
def deprecated_normalization(x):
    return [val * 0.95 for val in x]  # Never used

# Heavily distracting statistical tracker (partially unused)
stats_tracker = defaultdict(lambda: defaultdict(int))
total_observations = 0
for i, reading_set in enumerate(raw_readings):
    for sid in sensor_ids:
        readings = reading_set[sid]
        stats_tracker[sid]['count'] += len(readings)
        stats_tracker[sid]['sum'] += sum(readings)
        total_observations += len(readings)

# Compute averages (only some are actually used later)
average_readings = {}
for sid in sensor_ids:
    avg = stats_tracker[sid]['sum'] / stats_tracker[sid]['count']
    average_readings[sid] = round(avg, 3)

# Decoy transformation using bitwise and trigonometric red herring
bit_flags = 0b1010
masked_values = {}
for k, v in average_readings.items():
    masked = int((v * 100) & bit_flags)  # Distraction
    masked_values[k] = math.sin(masked) if masked > 0 else 0.0  # Unused

# Actual signal processing begins here
processed_signals = []
for reading_batch in raw_readings:
    batch_signals = []
    for s_id, vals in reading_batch.items():
        # Core logic: apply dynamic threshold filtering
        mean_val = sum(vals) / len(vals)
        deviation = [(x - mean_val)**2 for x in vals]
        variance = sum(deviation) / len(deviation)
        std_dev = math.sqrt(variance)
        
        # Filter outliers beyond 1.5σ (actual relevant logic)
        filtered = [x for x in vals if abs(x - mean_val) <= 1.5 * std_dev]
        batch_signals.extend(filtered)
    
    # Aggregate per batch (used later)
    processed_signals.append(sum(batch_signals))

# Secondary distraction: frequency analysis on sensor IDs (irrelevant)
frequency_counter = Counter(''.join(sensor_ids))
total_chars = sum(frequency_counter.values())
char_entropy = -sum((count/total_chars) * math.log2(count/total_chars) 
                   for count in frequency_counter.values())

# Another decoy structure (never accessed)
intermediate_diagnostics = {
    'entropy': char_entropy,
    'flags': bit_flags,
    'calibration_drift': sum(calibration_map.values())
}

# Critical function with embedded logic chain
logarithmic_weights = []
for i, signal_sum in enumerate(processed_signals):
    # Weight by log(index + 2) to avoid log(0)
    weight = math.log(i + 2)
    adjusted = signal_sum * weight
    logarithmic_weights.append(adjusted)

# Accumulate weighted signals
weighted_total = sum(logarithmic_weights)

# Control flow with misleading branching
threshold_regime = 'high' if weighted_total > 15 else 'low'

if threshold_regime == 'high':
    adjustment_factor = 0.85
    # Dead branch: complex correction never taken
    corrections = []
    for x in logarithmic_weights:
        corr = x * (1 + math.cos(math.pi / 4))
        corrections.append(corr)  # Computed but unused
else:
    adjustment_factor = 1.0  # Not taken

# Final diagnostic computation (answer point)
final_diagnostic = weighted_total * adjustment_factor

# Print result as required
print(f"Result: {final_diagnostic}")