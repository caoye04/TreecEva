import math

# Simulated sensor data processing pipeline with diagnostic checks
def collect_sensor_data():
    raw = [math.sin(x * 0.5) + 0.5 * math.cos(x * 1.3) for x in range(100)]
    return raw

def apply_noise_filter(data):
    # Irrelevant smoothing (distractor)
    smoothed = [(data[i-1] + data[i] + data[i+1]) / 3 for i in range(1, len(data)-1)]
    extended = [data[0]] + smoothed + [data[-1]]
    normalized = [max(min(x, 1.0), -1.0) for x in extended]
    return normalized

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append((i, signal[i]))
    return peaks

def compute_entropy(values):
    # Dead-end statistical analysis (decoy function)
    freq_map = {}
    for v in values:
        bucket = int(v * 10)
        freq_map[bucket] = freq_map.get(bucket, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def validate_calibration(peaks):
    # Misleading calibration check
    if len(peaks) == 0:
        return False
    indices = [p[0] for p in peaks]
    mean_spacing = sum(indices[i+1] - indices[i] for i in range(len(indices)-1)) / (len(indices)-1) if len(indices) > 1 else 0
    return 15 < mean_spacing < 25

def derive_phase_offset(peaks):
    # Complex but irrelevant phase logic (red herring)
    if not peaks:
        return 0.0
    weighted_sum = sum(i * val for i, val in peaks)
    total_weight = sum(val for _, val in peaks)
    return weighted_sum / total_weight if total_weight != 0 else 0

def analyze_signal(data):
    # Core computation path
    magnitude = sum(abs(x) for x in data[:50])  # Only first half matters
    threshold = 0.7
    above_count = sum(1 for x in data[:50] if abs(x) > threshold)
    stability_factor = len(data) // len(set(f'{x:.2f}' for x in data))
    # Key formula: combines magnitude, filtered count, and artificial penalty
    score = magnitude * above_count - (stability_factor ** 2)
    # Final transformation
    result = int(score + 500)  # Shifted to avoid negative assumptions
    return result

# --- Main execution with distractions ---
sensor_log = []
timestamps = [t for t in range(100)]

# Simulate data acquisition
collected = collect_sensor_data()

# Apply multiple layers of irrelevant processing
filtered_data = apply_noise_filter(collected)

# Extract features that won't be used
peak_list = extract_peaks(filtered_data)
entropy_value = compute_entropy(filtered_data)
phase_offset = derive_phase_offset(peak_list)

calibration_ok = validate_calibration(peak_list)
if calibration_ok:
    adjustment = math.tanh(phase_offset / 10)
else:
    adjustment = -0.1

# Secondary distraction: mock system diagnostics
diag_metrics = {}
diag_metrics['buffer_size'] = len(collected) * 2
diag_metrics['compression_ratio'] = 0.87
diag_metrics['checksum'] = sum(hash(str(x)) % 10000 for x in collected[:10])

diag_summary = ""
for k, v in diag_metrics.items():
    diag_summary += f"{k}:{v}|"
diag_summary = diag_summary.rstrip('|')

diag_length = len(diag_summary)

# Critical statement
final_diagnostic = analyze_signal(filtered_data)

# Print final result as required
print(f"Result: {final_diagnostic}")