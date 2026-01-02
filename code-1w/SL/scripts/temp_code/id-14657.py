import math

# Simulated sensor data processing with diagnostic flags
def collect_sensor_data():
    raw_samples = [i * 0.5 + (i % 7) for i in range(30)]
    timestamps = [t * 100 + 5 for t in range(30)]
    return list(zip(timestamps, raw_samples))

# Irrelevant auxiliary function - dead path
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return entropy

# Signal conditioning with multiple distractions
def filter_noise(signal_pairs, threshold=6.0):
    cleaned = []
    amplitudes = []
    phase_shift = 0.0
    temp_buffer = []

    for ts, val in signal_pairs:
        adjusted = abs(val) ** 0.5 * (1 + math.sin(phase_shift))
        if adjusted > threshold / 2:
            cleaned.append((ts, val))
            amplitudes.append(adjusted)
        else:
            temp_buffer.append(val * 0.1)  # Distractor buffer
        phase_shift += 0.3

    # Decoy transformation
    normalized_amps = [a / (max(amplitudes) + 1e-9) for a in amplitudes]
    return cleaned, normalized_amps

# Misleading feature extraction
def extract_features(data_list):
    features = []
    for i, item in enumerate(data_list):
        if i % 3 == 0:
            features.append(item[1] * 1.5)
        elif i % 4 == 0:
            features.append(item[1] * 0.7)
    return features or [0.0]  # Avoid empty

# Core logic buried among distractors
def reconstruct_phase(signal_parts, amps):
    total_weight = 0.0
    phase_sum = 0.0
    dummy_counter = 0

    for idx, (ts, val) in enumerate(signal_parts):
        weight = amps[idx] if idx < len(amps) else 0.5
        contribution = math.atan(val / (weight + 1e-5))
        if idx % 2 == 0 and val > 4.0:
            phase_sum += contribution * weight
            total_weight += weight
        dummy_counter += 1

    return phase_sum / (total_weight + 1e-5) if total_weight > 0 else 0.0

# Red herring: unused complex structure
class DiagnosticCache:
    def __init__(self):
        self.entries = {}
        self.hit_count = 0

    def add_entry(self, key, value):
        self.entries[key] = value

    def get_diagnostic(self, key):
        return self.entries.get(key, 0)

# Secondary distraction: power analysis (not used in final result)
def estimate_power_usage(duration_ms, load_factor=1.2):
    base = 0.8 * duration_ms
    peak = base * load_factor
    return (base + peak) / 2

# Primary processing chain
def process_frames(raw_data):
    filtered_pairs, norms = filter_noise(raw_data, threshold=5.8)
    feature_vector = extract_features(filtered_pairs)  # Unused but looks important

    # Dummy accumulation
    cumulative_offset = 0.0
    for f in feature_vector:
        cumulative_offset += math.cos(f) * 0.1

    # Actual relevant computation
    phase_recon = reconstruct_phase(filtered_pairs, norms)
    frame_count = len(filtered_pairs)

    # Destructuring that seems critical
    first_ts, _ = filtered_pairs[0] if filtered_pairs else (0, 0)
    last_ts, _ = filtered_pairs[-1] if filtered_pairs else (0, 0)
    duration = (last_ts - first_ts) / 1000.0 if last_ts > first_ts else 0.001

    # Complex-looking but partially irrelevant formula
    scaling_factor = math.log(duration + 2) * (1 + cumulative_offset ** 2)

    # Key calculation disguised as one among many
    signal_metric = (phase_recon * frame_count) / (scaling_factor + 0.5)

    # Multiple assignments to obscure focus
    debug_flag = True
    validation_score = 0.0
    processed = {
        'metric': signal_metric,
        'count': frame_count,
        'duration': duration,
        'debug': debug_flag
    }
    return processed

# Final analysis with conditional expression
def analyze_signal(frames_dict):
    metric = frames_dict['metric']
    count = frames_dict['count']
    duration = frames_dict['duration']

    # Critical branching with distractors
    baseline = 12.5 if count > 10 else 8.2
    penalty = 0.0

    if duration < 0.1:
        penalty += 2.5
    elif duration > 0.5:
        penalty -= 1.0

    # Core answer generation buried here
    intermediate = (metric + baseline) * (1 - penalty / 10)

    # Seemingly important but irrelevant check
    if frames_dict['debug']:
        validation_refs = [intermediate * 0.95, intermediate * 1.05]
        outlier_check = any(abs(v - baseline) > 5 for v in validation_refs)

    # Final result using conditional expression
    final_value = intermediate if not locals().get('outlier_check', False) else baseline

    # Dead code - never executed due to default False
    extra_adjustment = math.tanh(final_value) if 'CALIBRATE' in globals() else 0.0

    return final_value + extra_adjustment

# --- Execution Flow ---
sensor_log = collect_sensor_data()
processed_frames = process_frames(sensor_log)
final_diagnostic = analyze_signal(processed_frames)

# Print result as required
print(f"Target result: {final_diagnostic}")