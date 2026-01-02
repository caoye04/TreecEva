import math

# Simulated sensor data processing with performance scoring
raw_readings = [127, 255, 64, 192, 32, 180, 95, 160]

# Irrelevant transformation: color space conversion (distractor)
def rgb_to_hsv(r, g, b):
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val
    if delta == 0:
        h = 0
    elif max_val == r:
        h = 60 * (((g - b) / delta) % 6)
    elif max_val == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)
    return (h, 0, 0)

# Dead function: never called (red herring)
def legacy_calibrate(x):
    return [val * 0.95 for val in x if val > 100]

# Misleading intermediate calculation: checksum (not used in final result)
checksum = sum((x << 2) ^ 0xA3 for x in raw_readings) % 256

# Signal conditioning
filtered = [x for x in raw_readings if x % 2 == 0]  # Only even readings
normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) if max(filtered) != min(filtered) else 0 for x in filtered]

# Derived features (some useful, some not)
peak_magnitude = max(normalized)
signal_entropy = -sum(p * math.log(p) for p in normalized if p > 0)
drift_rate = abs(normalized[-1] - normalized[0])

# Unused feature transformations (distractors)
transformed_fft = list(map(lambda x: round(x * 100) % 7, normalized))[::2]
decimated = normalized[::-1][1::3]  # Reversed and sliced

# Weight initialization with red herrings
weights = {
    'magnitude': 0.4,
    'entropy': 0.3,
    'drift': 0.2,
    'ghost_metric': 0.1  # This weight corresponds to no actual metric
}

# Additional fake metrics that look plausible but aren't fully used
auxiliary_metrics = {
    'jitter': sum(abs(normalized[i] - normalized[i+1]) for i in range(len(normalized)-1)),
    'stability': 1 / (drift_rate + 0.1),
    'harmonics': len([x for x in transformed_fft if x > 3])
}

# Real metrics used in evaluation
metrics = {
    'magnitude': peak_magnitude,
    'entropy': signal_entropy,
    'drift': drift_rate
}

# Fake normalization chain (distraction)
temp_scores = []
for key in ['magnitude', 'entropy', 'drift']:
    raw_val = metrics[key]
    adjusted = (raw_val - 0.1) * 1.5 if raw_val > 0.2 else raw_val * 0.8
nonsense_agg = sum(transformed_fft) * drift_rate

# Core evaluation logic (buried among distractions)
def evaluate_performance(metrs, wts):
    score = 0.0
    for k in wts:
        if k in metrs:
            score += wts[k] * metrs[k]
    # Final nonlinear calibration
    calibrated = math.tanh(score * 2.5)
    return round(calibrated * 1000) / 1000

# Key statement
final_score = evaluate_performance(metrics, weights)

# Output the target result
print(f"Target result: {final_score}")