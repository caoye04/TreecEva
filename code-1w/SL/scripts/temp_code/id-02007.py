import math

def preprocess_signals(raw_readings):
    filtered = []
    noise_floor = 0.041
    for i, val in enumerate(raw_readings):
        if abs(val) < noise_floor:
            corrected = 0.0
        else:
            corrected = val * (1 + math.sin(i % 4))
        filtered.append(corrected)
    return [x for x in filtered if x != 0]


def compute_coherence(peak_locations, sample_rate):
    coherence_score = 0.0
    for i in range(1, len(peak_locations)):
        interval = (peak_locations[i] - peak_locations[i-1]) / sample_rate
        coherence_score += math.cos(interval * math.pi)
    return coherence_score if coherence_score > 0 else 0.135


def generate_synthetic_pattern(n):
    pattern = [0.5]
    for i in range(1, n):
        pattern.append((pattern[-1] * 1.87) % 1.0)
    return pattern  # Unused in main logic - red herring


def extract_timing_features(signal_chunk):
    peaks = []
    for i in range(1, len(signal_chunk)-1):
        if signal_chunk[i] > signal_chunk[i-1] and signal_chunk[i] > signal_chunk[i+1]:
            peaks.append(i)
    return peaks if len(peaks) > 2 else [1, 2, 3]  # Ensure non-empty


def validate_phase_alignment(peaks, ref_cycle):
    total_offset = 0
    for idx, peak in enumerate(peaks):
        total_offset += (peak - (idx + 1) * ref_cycle) ** 2
    rms_error = math.sqrt(total_offset / len(peaks))
    return rms_error < 5.0


def calculate_entropy(data_sequence):
    from collections import Counter
    counts = Counter([round(x, 2) for x in data_sequence])
    total = len(data_sequence)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy  # Not used in final computation - distractor


def aggregate_metrics(timing_log, calib_map):
    base_score = 0
    for cycle_idx, timestamps in enumerate(timing_log):
        if cycle_idx % 2 == 0:
            base_score += len(timestamps) * calib_map.get('gain', 1.2)
        else:
            adjustment = calib_map.get('offset', 0.8)
            base_score -= sum(timestamps) * adjustment * 0.01
    return int(base_score + calib_map.get('bias', 5))

# Main execution with extensive irrelevant setup
raw_sensor_data = [0.05, -0.03, 0.12, 0.08, 0.01, -0.02, 0.15, 0.11, 0.07, 0.09]
denoised_signal = preprocess_signals(raw_sensor_data)
signal_peaks = extract_timing_features(denoised_signal)

# Irrelevant synthetic data generation (dead path)
synthetic_test_pattern = generate_synthetic_pattern(50)
entropy_diagnostic = calculate_entropy(synthetic_test_pattern)

# Timing analysis branch (partially relevant)
timing_data = []
for rep in range(3):
    shifted_peaks = [p + rep * 2 for p in signal_peaks]
    timing_data.append(shifted_peaks)

# Calibration structure with decoy keys
calibration_matrix = {
    'gain': 1.5,
    'offset': 0.6,
    'bias': 7,
    'noise_threshold': 0.05,  # unused
    'sample_freq': 100,         # unused
    'version': '2.1a'           # unused metadata
}

# Validation side-path (no impact on result)
reference_cycle_length = 4.0
alignment_status = validate_phase_alignment(signal_peaks, reference_cycle_length)
coherence_metric = compute_coherence(signal_peaks, 50)

# Critical computation point
final_diagnostic = aggregate_metrics(timing_data, calibration_matrix)

# Extraneous transformation (distractor)
if alignment_status:
    transformed_diag = math.tanh(final_diagnostic / 100)
    final_diagnostic += int(transformed_diag * 10)

print(f"Result: {final_diagnostic}")