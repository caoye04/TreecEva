import math

# Simulated sensor array diagnostics with interference data
def analyze_sensor_array(raw_readings):
    n = len(raw_readings)
    temp_cache = [0] * n
    for i in range(n):
        temp_cache[i] = raw_readings[i] + (i % 7) ** 2

    # Irrelevant frequency sweep analysis (dead path)
    def frequency_stability(signal):
        return sum(math.sin(x / 10.0) for x in signal[:5])

    stability_score = frequency_stability(temp_cache)  # unused

    processed = []
    for val in temp_cache:
        if val > 50:
            processed.append(val * 0.9)
        else:
            processed.append(val * 1.1)

    return processed


def compute_checksum(sequence):
    chk = 0
    for i, v in enumerate(sequence):
        chk ^= int(v) & 255
    return chk + 1000  # red herring value

# Real-time anomaly detection (partially relevant)
def detect_anomalies(data_stream):
    anomalies = []
    baseline = sum(data_stream) / len(data_stream)
    for idx, point in enumerate(data_stream):
        deviation = abs(point - baseline)
        if deviation > 0.2 * baseline:
            anomalies.append((idx, point))
    return anomalies

# Decoy function: power spectral density (not used in final result)
def psd_estimate(signal):
    fft_mag = [abs(complex(0, x * 0.01).real) for x in signal]
    return [math.log(m + 1) for m in fft_mag]

# Core metric aggregator (critical function)
def aggregate_metrics(diag, weight_map):
    total = 0.0
    keys = list(weight_map.keys())
    sorted_keys = sorted(keys, key=lambda k: weight_map[k], reverse=True)

    # Slice only the top 3 weighted components
    selected = sorted_keys[:3]

    for k in selected:
        if k in diag:
            total += diag[k] * weight_map[k]

    # Apply non-linear compression
    if total > 100:
        total = 100 + (total - 100) / math.log(total - 99)

    return round(total, 6)

# Main execution flow
if __name__ == "__main__":
    # Simulated raw diagnostic readings from hardware sensors
    raw_diagnostics = [45, 67, 23, 89, 12, 77, 34, 65]

    # Step 1: Preprocess sensor array
    cleaned_data = analyze_sensor_array(raw_diagnostics)

    # Step 2: Compute irrelevant checksum
    checksum_val = compute_checksum(cleaned_data)  # Not used later

    # Step 3: Detect anomalies (produces list, but only length matters)
    anomaly_list = detect_anomalies(cleaned_data)
    anomaly_count = len(anomaly_list)

    # Step 4: Construct diagnostic vector using slicing and transformations
    segment_a = cleaned_data[1:6]  # middle slice
    segment_b = cleaned_data[-3:]   # last three

    avg_a = sum(segment_a) / len(segment_a)
    avg_b = sum(segment_b) / len(segment_b)

    # Build diagnostics dictionary
    diagnostics = {
        'temporal_drift': avg_a * 0.85,
        'amplitude_spike': max(cleaned_data) * 0.1,
        'spectral_bias': avg_b * 0.75,
        'phase_wander': anomaly_count * 5.5,
        'baseline_shift': min(cleaned_data) * 0.2
    }

    # Weighting schema (simulates calibration matrix)
    weights = {
        'amplitude_spike': 3.1,
        'temporal_drift': 2.7,
        'spectral_bias': 1.9,
        'phase_wander': 0.8,
        'baseline_shift': 0.5
    }

    # Critical statement: aggregates final diagnostic score
    final_diagnostic = aggregate_metrics(diagnostics, weights)

    # Print target result
    print(f"Result: {final_diagnostic}")