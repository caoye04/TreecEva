def analyze_phase_shift(signal, threshold=0.7):
    if len(signal) < 5:
        return 0
    shifted = [abs(signal[i] - signal[i-1]) for i in range(1, len(signal))]
    peaks = [v for v in shifted if v > threshold]
    return len(peaks) - sum(p > 1.2 for p in peaks)


def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    return variance < 0.5


def compute_entropy(data):
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)


def extract_features(stream):
    # Irrelevant feature extraction (distractor)
    features = []
    for i, val in enumerate(stream):
        if i % 3 == 0 and val > 0.5:
            features.append(val * 1.5)
    return features[:4]


def generate_key(signal):
    # Dead code path - never used in final computation
    key = 0
    for b in signal:
        key ^= int(b * 100) & 0xFF
    return key

# Simulated sensor inputs (real data and red herrings)
sensor_a = [0.8, 0.9, 0.85, 0.78, 0.82, 0.88]
sensor_b = [0.1, 0.15, 0.12, 0.18, 0.11]
sensor_c = [0.65, 0.71, 0.69, 0.73, 0.70, 0.68]

# Distractor: unused sensor fusion
decoy_fusion = [(a + c) / 2 for a, c in zip(sensor_a, sensor_c)]

# Critical diagnostic signature
health_signature = [
    analyze_phase_shift(sensor_a, 0.05),
    analyze_phase_shift(sensor_b, 0.08),
    analyze_phase_shift(sensor_c, 0.06)
]

# Irrelevant entropy analysis on rounded values
rounded_a = [round(x, 1) for x in sensor_a]
feature_entropy = compute_entropy(rounded_a)

# System load profile with slicing distraction
raw_load = [12, 15, 14, 18, 20, 22, 19, 16, 14, 13]
system_load = raw_load[2:8:2]  # Extracts [14, 20, 19]

# Fake normalization (unused)
normalized_load = [x / max(raw_load) for x in raw_load]

# Dummy assignment chain (red herring)
temp_status = 'nominal'
status_code = 200 if temp_status == 'critical' else 100
debug_flag = status_code != 100

# Multiple assignments (distraction)
x, y = 5, 7
y, x = x + 1, y - 1

# Conditional expression decoy
critical_alert = True if sum(system_load) > 60 else False

# Real processing function
def process_metrics(metrics, load_profile):
    # Complex logic with nesting and distractors
    base_score = 0
    adjustment = 0

    for i, m in enumerate(metrics):
        if i == 0:
            base_score += m * 10
        elif i == 1:
            # This branch is misleading - sensor_b has too few elements
            base_score += m * 2
        else:
            base_score += m * 5

    # Load-based correction (only part used)
    avg_load = sum(load_profile) / len(load_profile)
    if avg_load > 17.0:
        adjustment = 3
    elif avg_load > 15.0:
        adjustment = 1
    else:
        adjustment = -2

    # Hidden dependency: only the first metric is valid due to length check in analyze_phase_shift
    # sensor_b has only 5 elements -> analyze_phase_shift returns 0 regardless
    # So effective metrics are [result_of_sensor_a, 0, result_of_sensor_c]

    # Final computation
    result = base_score + adjustment

    # Decoy bit manipulation
    decoy_result = result ^ 0xFF
    decoy_result = (decoy_result << 2) & 0xFFFF

    return result

# Key execution point
final_diagnostic = process_metrics(health_signature, system_load)

# Print required output
print(f"Target result: {final_diagnostic}")