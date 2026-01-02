import math

# Simulated sensor data processing with noise filtering and diagnostic traces
def process_sensor_readings(raw_readings, threshold=100, window_size=5):
    # Irrelevant diagnostic counters (distractors)
    diagnostic_passes = 0
    checksum_errors = 0
    recalibration_count = 0

    # Initialize buffers
    cleaned_data = []
    moving_averages = [0] * len(raw_readings)
    spike_log = []

    # Data cleaning: remove outliers
    for i, value in enumerate(raw_readings):
        if abs(value) > threshold:
            cleaned_value = threshold if value > 0 else -threshold
            spike_log.append((i, value))
        else:
            cleaned_value = value
        cleaned_data.append(cleaned_value)

    # Compute moving average (unused in final result - red herring)
    for i in range(len(raw_readings)):
        start = max(0, i - window_size + 1)
        moving_averages[i] = sum(cleaned_data[start:i+1]) / (i - start + 1)

    # Apply exponential smoothing (dead code path - not used)
    smoothed_data = [cleaned_data[0]]
    alpha = 0.3
    for j in range(1, len(cleaned_data)):
        smoothed_val = alpha * cleaned_data[j] + (1 - alpha) * smoothed_data[-1]
        smoothed_data.append(smoothed_val)

    # Focus on central window for signal integrity (relevant path)
    mid_point = len(cleaned_data) // 2
    analysis_window = cleaned_data[mid_point - window_size//2 : mid_point + window_size//2 + 1]

    # Compute entropy for randomness assessment (irrelevant computation)
    entropy = 0.0
    freq_map = {}
    for x in analysis_window:
        freq_map[x] = freq_map.get(x, 0) + 1
    for freq in freq_map.values():
        p = freq / len(analysis_window)
        entropy -= p * math.log2(p) if p > 0 else 0

    # Signal correction logic
    base_reference = sum(analysis_window) / len(analysis_window)
    deviation = abs(base_reference - 50)  # Assumed nominal baseline
    correction_factor = 1.0 + (deviation / 200)

    # Filtered data using slice reversal transformation (key relevant operation)
    reversed_center = analysis_window[::-1]
    filtered_data = [abs(reversed_center[k] - reversed_center[0]) + 1 for k in range(len(reversed_center))]

    # Conditional logic with slicing and conditional expression (required Python feature)
    use_correction = len(spike_log) > 0 and len(raw_readings) % 2 == 1
    signal_strength = filtered_data[window_size] * correction_factor if use_correction else filtered_data[window_size - 1]

    # Dead-end branch with decoy assignment (misleading intermediate)
    if len(analysis_window) > 10:
        signal_strength *= 0.9  # Never executes

    # Final output
    print(f"Result: {signal_strength}")
    return signal_strength

# Input data generation (deterministic seed)
raw_input = [105, -45, 150, 73, 88, 52, 203, -67, 91, 110, 44]

# Execute
result = process_sensor_readings(raw_input)