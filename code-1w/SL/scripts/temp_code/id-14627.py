import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    base_signals = [i * 0.5 for i in range(20)]
    noise_floor = 0.23
    return [signal + noise_floor for signal in base_signals]

# Legacy checksum calculator (distractor - not used in final result)
def legacy_checksum(data):
    checksum = 0
    for val in data:
        checksum ^= int(val * 100) % 256
    return checksum

# Signal normalization using outdated method (red herring)
def normalize_legacy(signal_list):
    max_val = max(signal_list)
    return [val / max_val for val in signal_list] if max_val > 0 else signal_list

# Core processing functions
def extract_peaks(signal_data, threshold=0.75):
    peaks = []
    for i in range(1, len(signal_data) - 1):
        if signal_data[i] > threshold and signal_data[i] > signal_data[i-1] and signal_data[i] > signal_data[i+1]:
            peaks.append((i, signal_data[i]))
    return peaks

# Frequency domain approximation (irrelevant computation)
def estimate_dominant_frequency(signal_data):
    period_sum = 0
    count = 0
    for i in range(1, len(signal_data)):
        if signal_data[i] > signal_data[i-1] and count < 5:
            period_sum += 1
            count += 1
    return round(1.0 / (period_sum / 5) if period_sum > 0 else 0, 4)

# Advanced diagnostic engine
def analyze_pattern_consistency(peaks):
    if len(peaks) < 2:
        return 0.0
    intervals = [peaks[i+1][0] - peaks[i][0] for i in range(len(peaks)-1)]
    mean_interval = sum(intervals) / len(intervals)
    variance = sum((x - mean_interval) ** 2 for x in intervals) / len(intervals)
    return round(math.exp(-variance / 10.0), 6)

# Data structure transformation layer
def build_event_map(peaks):
    event_dict = {}
    for index, value in peaks:
        key = f"event_{index}"
        event_dict[key] = {
            'magnitude': round(value, 4),
            'category': 'critical' if value > 8.0 else 'warning' if value > 5.0 else 'info',
            'timestamp': index * 100
        }
    return event_dict

# Secondary validation chain (partially dead code path)
def validate_event_chain(event_map):
    critical_count = 0
    for event in event_map.values():
        if event['category'] == 'critical':
            critical_count += 1
    # This function is called but its return is unused
    return critical_count > 2

# Main metrics processor
def process_health_score(events):
    score = 100.0
    for event in events.values():
        if event['category'] == 'critical':
            score -= 15.0
        elif event['category'] == 'warning':
            score -= 5.0
    return max(score, 0)

# Decoy function that appears important but is irrelevant
def calculate_system_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 4)

# Real-time monitoring configuration (misleading parameters)
system_config = {
    'sampling_rate': 100,
    'buffer_size': 1024,
    'threshold_primary': 0.75,
    'threshold_secondary': 1.2,
    'activation_delay': 5,
    'legacy_mode': False
}

# Actual thresholds used in processing (hidden in plain sight)
system_thresholds = {
    'peak_detection': 7.2,
    'consistency_penalty': 3.5,
    'minimum_events': 2
}

# Simulated log entries with embedded signals
log_entries = [
    {'time': t, 'value': val, 'type': 'sensor'} 
    for t, val in enumerate(generate_telemetry())
]

# Extraneous data transformation (unused branch)
transformed_logs = []
for entry in log_entries:
    transformed = entry.copy()
    transformed['normalized'] = entry['value'] * 0.98
    transformed['flagged'] = False
    if transformed['normalized'] > 9.0:
        transformed['flagged'] = True
    transformed_logs.append(transformed)

# Key processing pipeline
raw_signal = [entry['value'] for entry in log_entries]

# Irrelevant pre-processing chain
filtered_signal = []
for val in raw_signal:
    if val > 0.5:
        filtered_signal.append(val * 1.02)
    else:
        filtered_signal.append(val)

# Primary peak detection (actual relevant step)
detected_peaks = extract_peaks(raw_signal, system_thresholds['peak_detection'])

# Build event mapping structure
event_lookup = build_event_map(detected_peaks)

# Validate chain (distractor call - return value unused)
validate_event_chain(event_lookup)

# Calculate auxiliary metrics (some used, some not)
pattern_score = analyze_pattern_consistency(detected_peaks)
health_metric = process_health_score(event_lookup)
frequency_estimate = estimate_dominant_frequency(raw_signal)  # Unused
entropy_measure = calculate_system_entropy(raw_signal)      # Unused

# Final diagnostic synthesis using lambda for dynamic weighting
diagnostic_weight_fn = lambda p, h: round((p * 0.6) + (h / 100 * 0.4), 6)

# Critical statement containing the answer
calibration_offset = 1.86
final_diagnostic = round(
    diagnostic_weight_fn(pattern_score, health_metric) * 100 + calibration_offset, 4
)

# Print final result as required
print(f"Result: {final_diagnostic}")