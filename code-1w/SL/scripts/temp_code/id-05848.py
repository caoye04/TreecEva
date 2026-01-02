def analyze_system_load(usage_stream, threshold_config):
    cumulative_load = 0
    peak_moment = -1
    temp_buffer = []
    debug_snapshot = [0] * len(usage_stream)
    normalization_factor = sum(u ** 0.5 for u in usage_stream if u > 5) or 1

    for i, load in enumerate(usage_stream):
        if load > threshold_config['critical']:
            temp_buffer.append((i, load * 0.8))
        elif load > threshold_config['warning']:
            temp_buffer.append((i, load * 0.9))
        else:
            temp_buffer.append((i, load))

    adjusted_values = [tb[1] for tb in temp_buffer]
    smoothed = [sum(adjusted_values[max(0, j-2):j+1]) / (j+1) for j in range(len(adjusted_values))]

    outlier_mask = [1 if abs(smoothed[k] - sum(smoothed)/len(smoothed)) > 2 else 0 for k in range(len(smoothed))]
    filtered_stream = [smoothed[m] for m in range(len(smoothed)) if not outlier_mask[m]]

    if len(filtered_stream) < 3:
        return sum(adjusted_values)

    trend_score = 0
    for n in range(1, len(filtered_stream)):
        trend_score += (filtered_stream[n] - filtered_stream[n-1]) * (0.9 ** n)

    diagnostic_weight = 1.75 if trend_score > 0 else 0.85
    return int(trend_score * diagnostic_weight)


def encode_signal_pattern(raw_sequence, key_shift):
    encoded = []
    shift_cycle = [key_shift % 3, (key_shift + 1) % 3, (key_shift + 2) % 3]
    for idx, val in enumerate(raw_sequence):
        shifted = val ^ (shift_cycle[idx % 3])
        encoded.append(shifted)
    return encoded


def evaluate_response_time(timestamps):
    intervals = [timestamps[j] - timestamps[j-1] for j in range(1, len(timestamps))]
    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    variance = sum((t - avg_interval)**2 for t in intervals) / len(intervals) if intervals else 0
    return avg_interval, variance

# Irrelevant helper function (dead code path)
def deprecated_normalization(data):
    return [x / max(data) if max(data) != 0 else 0 for x in data]

# Misleading metric calculation
baseline_reference = [12, 15, 14, 18, 21, 19, 22]
shadow_copy = baseline_reference[:]
bogus_correction = sum(b ** 2 for b in shadow_copy if b % 2 == 0) // 7

# Simulated telemetry input
telemetry_stream = [8, 12, 14, 19, 23, 25, 20, 18, 22, 26, 24, 28]
config_params = {
    'warning': 15,
    'critical': 22
}

# Unused transformation path
transformed_telemetry = [t * 1.05 for t in telemetry_stream]
scaled_for_debug = transformed_telemetry[::-1]  # Reversed, unused later

# Signal encoding side computation (distractor)
pattern_sequence = [7, 11, 13, 17, 19]
encoded_signal = encode_signal_pattern(pattern_sequence, 5)

# Timestamp analysis distraction
timing_log = [100, 104, 109, 115, 122]
mean_response, response_var = evaluate_response_time(timing_log)

# Core processing chain
log_data = [x + 1 for x in telemetry_stream if x > 10]

# Red herring list manipulation
dummy_flags = [True if i % 3 == 0 else False for i in range(len(log_data))]
flag_summary = {i: dummy_flags[i] for i in range(len(dummy_flags))}

# Actual threshold logic with embedded slicing and conditional expression
system_threshold = {
    'critical': 22,
    'window': 3
}

interim_result = 0
for index, reading in enumerate(log_data):
    window_slice = log_data[max(0, index - system_threshold['window']):index]
    local_avg = sum(window_slice) / len(window_slice) if window_slice else 0
    adjustment = reading * 0.9 if local_avg > 20 else reading * 1.1
    interim_result += int(adjustment)

# Secondary correction using zip and enumerate (meaningful but partially obscured)
corrected_readings = [r * 0.95 for r in log_data]
indices = list(range(len(corrected_readings)))
combined_pairs = list(zip(indices, corrected_readings))

weighted_sum = 0
for pos, value in combined_pairs:
    weight = 1.2 if value > 20 else 0.8
    weighted_sum += value * weight

# Final diagnostic depends on prior state and external function call
def process_metrics(data, config):
    base_score = analyze_system_load(data, config)
    surge_penalty = sum(1 for d in data if d > config['critical']) * 10
    return base_score - surge_penalty

final_diagnostic = process_metrics(log_data, system_threshold)
print(f"Target result: {final_diagnostic}")