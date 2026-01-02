import math

# Simulated sensor fusion system for environmental monitoring
base_readings = [0.87, 0.64, 0.91, 0.58, 0.73]

# Irrelevant calibration constants (distractors)
calib_a = 1.02
calib_b = 0.97
temp_offset = -0.05
voltage_gain = 2.1
reference_stability = 9876.5

# Real data processing begins
filtered = list(map(lambda x: round(x ** 2 + 0.1 * x, 4), base_readings))

# Misleading intermediate transformation (unused later)
legacy_compatibility_mode = True
deprecated_scale = [f * 0.91 for f in filtered]  # dead path

# Actual signal normalization
normalized = [round((f - min(filtered)) / (max(filtered) - min(filtered)), 6) for f in filtered]

# Noise threshold simulation (partially relevant but masked)
noise_floor = 0.1
amplified = [n * 1.5 if n > noise_floor else n * 0.5 for n in normalized]

# Spurious array with red herring values
phantom_signals = [0.02 * i for i in range(len(amplified))]
interference_mask = set(phantom_signals[1::2])  # distractor set usage

# Weight configuration for multi-sensor evaluation
metric_weights = {
    'sensitivity': 0.35,
    'stability': 0.25,
    'consistency': 0.15,
    'response': 0.15,
    'drift': 0.10
}

# Simulated raw metrics from different subsystems
raw_metrics = {
    'sensitivity': sum(amplified) / len(amplified),
    'stability': 1 - (max(amplified) - min(amplified)),
    'consistency': len([a for a in amplified if a > 0.5]) / len(amplified),
    'response': max(amplified),
    'drift': abs(amplified[-1] - amplified[0])
}

# Decoy function that is never called
def legacy_evaluation(data):
    return sum(d ** 1.5 for d in data) % 100

# Unused recursive helper (dead code)
def calculate_depth(value, depth=0):
    if value < 0.1:
        return depth
    return calculate_depth(value / 1.7, depth + 1)

# Secondary unused computation path
temporary_aggregate = 0
for i, val in enumerate(normalized):
    if i % 2 == 0:
        temporary_aggregate += val * (i + 1)

# Set-based filtering of phantom components (distractor operation)
cleaned_amplified = [a for i, a in enumerate(amplified) if i not in {1, 3}]

# Redundant slicing demonstration (irrelevant)
window_slice = cleaned_amplified[1:3]
overlap_chunk = window_slice[::-1]  # unused

# Core evaluation logic — this is where the answer comes from
def evaluate_performance(weights, metrics):
    score = 0.0
    for key in weights:
        if key == 'drift':
            # Invert drift since lower is better
            score += weights[key] * (1 - metrics[key])
        else:
            score += weights[key] * metrics[key]
    return round(score * 1000, 6)

# Final computation — the target execution point
final_score = evaluate_performance(metric_weights, raw_metrics)

# Output result as required
print(f"Target result: {final_score}")