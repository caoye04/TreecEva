import math

# Simulated sensor data and calibration constants (some are decoys)
base_frequency = 50.0
phase_shift = 0.25
voltage_rms = 230.0
calibration_factor_x = 1.003
calibration_factor_y = 0.998  # Unused distractor
calibration_factor_z = 1.012  # Unused in computation

# Irrelevant environmental metadata
humidity = 67
ambient_temp = 22.5
elevation_m = 142

# Raw signal samples from three-phase input
raw_samples_a = [1.0, -0.5, 0.8, -0.2, 0.9, -0.7, 0.6, -0.3]
raw_samples_b = [0.7, -0.8, 0.4, -0.6, 1.1, -0.9, 0.2, -0.4]
raw_samples_c = [-0.3, 0.9, -0.7, 0.8, -0.2, 1.0, -0.5, 0.7]

# Misleading preprocessing path (dead end)
def legacy_filter(data):
    return [x * 0.95 for x in data]  # Never called

def apply_window(signal, window_type='hann'):
    n = len(signal)
    if window_type == 'hann':
        return [signal[i] * (0.5 - 0.5 * math.cos(2 * math.pi * i / (n - 1))) for i in range(n)]
    return signal

# Core processing pipeline
windowed_a = apply_window(raw_samples_a)
windowed_b = apply_window(raw_samples_b)
windowed_c = apply_window(raw_samples_c)

# Compute magnitude envelopes via RMS over segments
def compute_rms_segments(signal, segment_size=4):
    segments = []
    for i in range(0, len(signal), segment_size):
        segment = signal[i:i + segment_size]
        rms = math.sqrt(sum(x ** 2 for x in segment) / len(segment))
        segments.append(rms)
    return segments

rms_a = compute_rms_segments(windowed_a)
rms_b = compute_rms_segments(windowed_b)
rms_c = compute_rms_segments(windowed_c)

# Combine phases using vector sum approximation (key step)
combined_rms = [
    math.sqrt(a**2 + b**2 + c**2) for a, b, c in zip(rms_a, rms_b, rms_c)
]

# Apply correct calibration factor (only x is used)
adjusted_signal = [val * calibration_factor_x for val in combined_rms]

# Feature extraction: detect peaks above threshold
peak_threshold = 1.1
peaks_found = [x for x in adjusted_signal if x > peak_threshold]
peak_count = len(peaks_found)

# Secondary feature: average of non-peak values
non_peak_avg = sum(x for x in adjusted_signal if x <= peak_threshold) / (len(adjusted_signal) - peak_count) if peak_count < len(adjusted_signal) else 0.0

# Signal quality metric based on entropy approximation (distraction with unused lambda)
entropy_estimator = lambda vals: sum(-x * math.log(x) for x in vals if x > 0)  # Defined but not used

# Actual diagnostic logic
quality_score_raw = len(adjusted_signal) * 10 + peak_count * 5

# Decoy state machine (never executed)
class DiagnosticEngine:
    def __init__(self):
        self.mode = "standby"
    def run_diagnostics(self, data):
        return 0  # Dead code

diag_engine = DiagnosticEngine()  # Object created but unused

# Critical data transformation
processed_data = {
    'amplitudes': adjusted_signal,
    'peak_info': {
        'count': peak_count,
        'avg_non_peak': non_peak_avg
    },
    'metrics': {
        'quality_base': quality_score_raw,
        'entropy_proxy': 0.0  # Placeholder
    }
}

# Analysis function with early returns and conditional logic
def analyze_signal(data_dict):
    amps = data_dict['amplitudes']
    count = data_dict['peak_info']['count']
    base_quality = data_dict['metrics']['quality_base']
    
    if not amps:
        return -1
    
    max_amp = max(amps)
    if max_amp < 0.5:
        return base_quality // 2
    
    # Key branching logic
    if count >= 2:
        scaling_factor = 1.75
    elif count == 1:
        scaling_factor = 1.25
    else:
        scaling_factor = 0.85  # Default case taken
    
    # Apply scaling and add fixed offset
    intermediate = base_quality * scaling_factor
    final_value = int(intermediate + 12.6)  # Truncate to int after adding decimal
    
    # Early return guard (not triggered)
    if final_value > 10000:
        return 999
    
    return final_value

# Execute critical statement
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")