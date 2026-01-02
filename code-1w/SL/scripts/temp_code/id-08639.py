import itertools

# System stability monitoring with red herrings and complex logic
base_signals = [0.8, 1.2, -0.5, 3.1, -2.0, 1.7]
noise_floor = 0.3

def generate_harmonics(signal):
    return [signal * 2, signal * 0.5] if signal > 0 else [signal + 1, signal - 1]

def filter_outliers(data, limit=2.5):
    return [x for x in data if abs(x) < limit]

def calculate_entropy(values):
    # Irrelevant entropy calculation (decoy)
    from math import log
    total = sum(abs(v) for v in values)
    if total == 0: return 0.0
    probs = [abs(v)/total for v in values]
    return -sum(p * log(p) for p in probs if p > 0)

def apply_calibration(signal_batch):
    calibrated = []
    for s in signal_batch:
        if s > 1:
            calibrated.append(s * 0.9)
        elif s < -1:
            calibrated.append(s * 1.1)
        else:
            calibrated.append(s)
    return [round(c, 3) for c in calibrated]

def compute_derivatives(sequence):
    # Dead function - not used in final path
    return [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

def detect_patterns(values):
    # Misleading pattern detector
    patterns = 0
    for a, b, c in itertools.pairwise(values) + [(None, None, None)]:
        if a is not None and a < b > c:
            patterns += 1
    return patterns

def transform_weights(raw_weights):
    # Key transformation with distractors
    temp = [w ** 2 for w in raw_weights]
    adjusted = [t + noise_floor for t in temp]
    normalized = [a / (sum(adjusted)) for a in adjusted]
    return [round(n, 4) for n in normalized]

def evaluate_stability_index(weights):
    score = 0.0
    for w in weights:
        if w > 0.1:
            score += w * 100
        else:
            score -= 50
    return int(score)  # Final deterministic integer result

# Irrelevant data structures
historical_logs = {
    'version': '2.1',
    'records': [
        {'time': 100, 'value': 0.1},
        {'time': 200, 'value': 0.5}
    ],
    'checksum': 'ignored'
}

# Unused helper
def validate_integrity(data):
    return sum(abs(d) for d in data) % 1 == 0

# Generate multiple signal harmonics (some irrelevant)
all_harmonics = []
for sig in base_signals:
    all_harmonics.extend(generate_harmonics(sig))

# Filter and calibrate (partially relevant)
filtered_signals = filter_outliers(all_harmonics, limit=2.5)
calibrated_signals = apply_calibration(filtered_signals)

# Transform to final weights (key step)
final_weights = transform_weights(calibrated_signals)

# DEAD CODE PATHS BELOW (red herrings)
entropy_metric = calculate_entropy(calibrated_signals)
detected_pattern_count = detect_patterns(calibrated_signals)
derivative_sequence = compute_derivatives(calibrated_signals)  # Unused

# CRITICAL EXECUTION POINT
threshold_score = evaluate_stability_index(final_weights)

# Print result as required
print(f"Result: {threshold_score}")