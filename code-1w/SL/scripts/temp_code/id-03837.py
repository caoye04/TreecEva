import itertools

# Simulated sensor fusion system for autonomous drone navigation
def analyze_sensor_data(raw_signals):
    filtered = [x * 0.9 + 1.1 for x in raw_signals if x > -5]
    return filtered[:len(filtered)//2]

# Irrelevant auxiliary function – dead code path
def deprecated_normalization(vec):
    magnitude = sum(x**2 for x in vec) ** 0.5
    return [v / magnitude for v in vec] if magnitude else vec

# Core metric processor with red herrings
def compute_derived_metrics(basic, flags):
    phase_shift = 0
    derived = []
    
    for i, val in enumerate(basic):
        if i % 3 == 0:
            phase_shift += val * (i + 1)
        temp = val ** 2 - i * 0.5
        derived.append(abs(temp))
    
    # Distractor: complex-looking but unused transformation
    zigzag = list(itertools.accumulate([derived[j] - derived[j-1] for j in range(len(derived)-1, 0, -1)] or [0]))
    scaling_factor = sum(zigzag) / (len(zigzag) or 1) if zigzag else 0
    adjusted = [d + scaling_factor for d in derived]

    # Real usage begins here
    if len(adjusted) >= 3:
        adjusted[2] += phase_shift * 0.1
    
    return adjusted

# Weighted evaluation with misleading branches
def apply_calibration(data, mode='standard'):
    result = []
    for d in data:
        if mode == 'legacy':
            result.append(d * 0.75)
        elif mode == 'turbo':
            result.append(d * 1.4)
        else:
            result.append(d * 1.05)  # actual path taken
    return result

# Main scoring logic buried in distractions
def evaluate_performance(metrics, weights):
    base = 100.0
    penalty = 0
    boost = 0

    # Complex conditional updates
    for idx, (m, w) in enumerate(zip(metrics, weights)):
        if idx % 2 == 0 and m > 20:
            boost += w * (m / 50)
        elif m < 5:
            penalty += w * 2
        
        if idx > 0 and metrics[idx-1] > m:
            penalty += 0.5 * w

    # Red herring: elaborate unused calculation
    entropy = 0
    for x in metrics:
        if x > 0:
            entropy -= x * __import__('math').log(x, 2)

    # Actual score computation
    adjustment = (boost - penalty) * 0.8
    final = base + adjustment

    # Secondary influence from pattern analysis
    trend_sum = 0
    for a, b in zip(metrics, metrics[1:]):
        if b > a:
            trend_sum += 1.2
        elif b < a:
            trend_sum -= 0.8

    final += trend_sum * 0.3

    return round(final, 6)

# --- Simulation setup with decoys ---
raw_telemetry = [-6, -3, 8, 12, 15, 22, 25, 30]
noise_profile = [0.1, -0.2, 0.3, -0.1]
system_flags = [True, False, True]

# Unused data structures – red herrings
historical_buffer = [[1,2],[3,4]]
calibration_lookup = {i: i*1.7 for i in range(5)}

# Real signal extraction
clean_data = analyze_sensor_data(raw_telemetry)

# Fake processing chain
shadow_copy = clean_data.copy()
for _ in range(2):
    shadow_copy = [x * 0.95 for x in shadow_copy]

# Critical data path
primary_metrics = compute_derived_metrics(clean_data, system_flags)

# Apply correct calibration
calibrated_metrics = apply_calibration(primary_metrics, mode='standard')  # not 'legacy' or 'turbo'

# Weights with non-uniform significance
metric_weights = [0.8, 1.2, 1.0, 0.5]

# Final evaluation point
final_score = evaluate_performance(calibrated_metrics, metric_weights)

# Output target result
print(f"Target result: {final_score}")