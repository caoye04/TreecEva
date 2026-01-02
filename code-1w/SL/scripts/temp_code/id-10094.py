from collections import defaultdict, Counter

# Simulated sensor network diagnostic system
def analyze_readings(readings):
    raw_stats = defaultdict(int)
    anomalies = []
    rolling_window = []
    temp_buffer = []
    baseline_threshold = 75
    volatility_index = 0
    correction_factor = 0.98
    mode_flags = {'STABLE': 0, 'FLUCTUATING': 1, 'ERRATIC': 2}

    for idx, reading in enumerate(readings):
        raw_stats['total_samples'] += 1
        if reading > baseline_threshold:
            raw_stats['above_threshold'] += 1
            if idx > 0 and readings[idx-1] > baseline_threshold:
                raw_stats['consecutive_high'] += 1
        else:
            anomalies.append(idx)
            temp_buffer.append(reading)

        rolling_window.append(reading)
        if len(rolling_window) > 3:
            rolling_window.pop(0)
        
        if len(rolling_window) == 3:
            window_std = (sum((x - sum(rolling_window)/3)**2 for x in rolling_window)/3)**0.5
            if window_std > 15:
                volatility_index += 1

    # Irrelevant signal processing branch (dead logic path)
    fft_buffer = [x * 0.5 for x in readings if x % 2 == 0]
    normalized = [min(max(x, 0), 100) for x in readings]
    if len(normalized) > 10:
        smoothed = sum(normalized[i:i+3])//3 for i in range(0, len(normalized)-2, 3)
    else:
        smoothed = normalized

    # Unused statistical measures
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    peak_to_avg = max(readings) / mean_val if mean_val else 0

    # Critical computation chain (obfuscated by surrounding noise)
    event_count = len(anomalies)
    consistency_ratio = (raw_stats['consecutive_high'] / raw_stats['total_samples']) if raw_stats['total_samples'] else 0
    
    # Decoy calculation with plausible but unused variables
    risk_score = event_count * volatility_index
    calibration_offset = sum(temp_buffer) if temp_buffer else 0

    # Key intermediate values
    aggregate_score = raw_stats['above_threshold'] - event_count
    mode_classification = mode_flags['FLUCTUATING'] if volatility_index > 2 else mode_flags['STABLE']
    
    # Red herring: complex bit manipulation with no impact
    decoy_state = 0
    for i in range(8):
        decoy_state ^= (mode_classification << i) | (i & volatility_index)
    decoy_state = (decoy_state >> 4) ^ (decoy_state & 0xFF)

    # Real adjustment logic buried in noise
    adjustment_factor = 0.1 * consistency_ratio
    if raw_stats['consecutive_high'] > 5:
        adjustment_factor += 0.05
    if event_count < 3:
        adjustment_factor += 0.03

    final_diagnostic = aggregate_score * (1 + adjustment_factor)

    # Final output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated IoT sensor data stream
data_stream = [88, 92, 76, 65, 81, 95, 89, 60, 55, 70, 91, 84, 50, 45, 87, 90, 68, 73]
analyze_readings(data_stream)