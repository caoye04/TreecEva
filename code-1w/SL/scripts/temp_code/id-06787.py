def sensor_calibration(raw_values):
    calibrated = []
    offset = 0.73
    scale = 1.85
    noise_floor = 0.05
    temp_data = [v * scale + offset for v in raw_values]
    filtered = [v for v in temp_data if v > noise_floor]
    return filtered

raw_sensor_input = [0.12, 0.35, 0.67, 0.21, 0.89, 0.44, 0.73, 0.51]

# Irrelevant preprocessing: signal inversion (dead path)
inverted_signal = [-x for x in raw_sensor_input]
smoothed_inverted = [sum(inverted_signal[i:i+2]) / 2 for i in range(len(inverted_signal)-1)]

# Main processing path
baseline_corrected = sensor_calibration(raw_sensor_input)

# Distractor: frequency analysis on unused data
sample_rate = 100
frequencies = [i * sample_rate / len(smoothed_inverted) for i in range(len(smoothed_inverted))]
doppler_shift = sum(frequencies) / len(frequencies) if frequencies else 0

# Real computation begins
window_size = 3
rolling_averages = []
for i in range(len(baseline_corrected) - window_size + 1):
    window = baseline_corrected[i:i+window_size]
    rolling_averages.append(sum(window) / window_size)

# Slice manipulation with meaningful use
trimmed_rolls = rolling_averages[1:-1]  # Remove edge effects

# Add dummy transformation chain
buffer_cache = {i: val * 1.01 for i, val in enumerate(trimmed_rolls)}
adjusted_values = [buffer_cache[k] for k in sorted(buffer_cache.keys())]

# Decoy statistical measures
mean_val = sum(adjusted_values) / len(adjusted_values)
variance = sum((x - mean_val) ** 2 for x in adjusted_values) / len(adjusted_values)
shannon_entropy = 0.0
if variance > 0:
    import math
    shannon_entropy = math.log(variance * 2 * 3.14159) / 2

# Actual logic for diagnostic
threshold = 1.5
processed_data = [x for x in adjusted_values if x > threshold]

# Auxiliary function with red herring parameters
def analyze_readings(readings, limit, debug_mode=False, history=None, gain=1.2):
    if not readings:
        return -999.0
    
    # Irrelevant normalization step (not used in final result)
    normalized = [r * gain / (limit + 0.1) for r in readings]
    confidence_scores = [abs(r - limit) * 100 for r in readings]
    
    # Critical calculation hidden among distractions
    total_power = sum(r ** 2 for r in readings)
    reading_count = len(readings)
    stability_index = sum(1 for r in readings if r > limit * 0.9)
    
    # Final diagnostic formula (core answer)
    final_diagnostic = (total_power * stability_index) / (reading_count + 1e-8)
    
    # Dead code branches below
    anomaly_report = {}
    if debug_mode:
        anomaly_report['outliers'] = [r for r in readings if r > limit * 2]
        anomaly_report['trend'] = readings[-1] - readings[0]
    
    metadata_log = {
        'version': '2.1',
        'calibration_offset': 0.73,
        'timestamp': '2023-11-05',
        'history_trace': history or [],
        'entropy_metric': shannon_entropy  # Unused linkage to earlier decoy
    }
    
    return final_diagnostic

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold)
print(f"Target result: {final_diagnostic}")