def monitor_system_health(telemetry_stream, calibration_data):
    baseline = sum(calibration_data) / len(calibration_data)
    deviations = [abs(val - baseline) for val in telemetry_stream]
    high_deviation_peaks = [i for i, d in enumerate(deviations) if d > 2.5]
    return high_deviation_peaks


def compute_signal_envelope(input_waveform, noise_floor=0.15):
    envelope = []
    for i in range(1, len(input_waveform) - 1):
        center = abs(input_waveform[i])
        neighbor_avg = (abs(input_waveform[i-1]) + abs(input_waveform[i+1])) / 2
        if center > neighbor_avg + noise_floor:
            envelope.append(center * 0.85)
    return envelope if envelope else [0.0]


def detect_phase_shift(timing_log, reference_cycle):
    phase_deltas = []
    for i in range(len(timing_log)):
        delta = (timing_log[i] - reference_cycle[i % len(reference_cycle)]) * 1000
        phase_deltas.append(int(delta))
    shifted_indices = {i for i, d in enumerate(phase_deltas) if abs(d) > 500}
    return shifted_indices


def analyze_fault_sequence(event_log, threshold_config):
    # Irrelevant preprocessing
    temp_buffer = [x * 1.05 for x in event_log if x > 0]
    temp_buffer = [t for t in temp_buffer if t < 95]

    # Distractor: unused signal analysis
    moving_avg = []
    window_size = 3
    for i in range(len(temp_buffer) - window_size + 1):
        moving_avg.append(sum(temp_buffer[i:i+window_size]) / window_size)
    spike_count = sum(1 for v in temp_buffer if v > 80)

    # Real logic begins here
    severity_weights = {"critical": 5, "high": 3, "medium": 2, "low": 1}
    base_score = 0
    for entry in event_log:
        if entry > threshold_config['critical']:
            base_score += severity_weights["critical"]
        elif entry > threshold_config['high']:
            base_score += severity_weights["high"]
        elif entry > threshold_config['medium']:
            base_score += severity_weights["medium"]
        else:
            base_score += severity_weights["low"]

    # Secondary processing with set operations (required)
    anomaly_set_a = {i for i, x in enumerate(event_log) if x > threshold_config['critical']}
    anomaly_set_b = {i for i, x in enumerate(event_log) if x < threshold_config['baseline']}
    cross_anomalies = anomaly_set_a.intersection(anomaly_set_b)
    anomaly_penalty = len(cross_anomalies) * 4

    # Tertiary adjustment based on distribution
    upper_quartile = sorted(event_log)[int(0.75 * len(event_log))]
    stability_factor = 1.0
    if upper_quartile > 88:
        stability_factor = 0.88
    elif upper_quartile < 60:
        stability_factor = 1.12

    # Final computation path
    raw_diagnostic = base_score - anomaly_penalty
    adjusted_diagnostic = int(raw_diagnostic * stability_factor)

    # Dead code branch (distractor)
    if adjusted_diagnostic < 0:
        fallback_recovery = [x for x in event_log if x % 2 == 0]
        adjusted_diagnostic = len(fallback_recovery)

    # Key assignment
    final_diagnostic = adjusted_diagnostic + 100

    # More red herrings
    debug_snapshot = {
        'checksum': sum([final_diagnostic, len(event_log), 777]) % 1000,
        'status_flag': 'OK' if final_diagnostic > 50 else 'FAIL',
        'aux_data': [0] * 5
    }

    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Simulated sensor inputs
    operational_log = [76, 82, 89, 93, 77, 65, 54, 91, 95, 87, 73, 68, 59, 94]
    fault_thresholds = {
        'baseline': 60,
        'medium': 70,
        'high': 85,
        'critical': 90
    }

    # Irrelevant auxiliary data
    waveform_sample = [-0.2, 0.3, 0.7, 1.1, 0.6, -0.1, 0.4, 0.9, 1.3, 0.8]
    timing_reference = [0.012, 0.013, 0.011, 0.014]
    system_telemetry = [88, 85, 76, 92, 83]
    calibration_params = [70, 72, 68, 74, 71]

    # Distractor function calls
    unexpected_peaks = monitor_system_health(system_telemetry, calibration_params)
    signal_env = compute_signal_envelope(waveform_sample)
    phase_issues = detect_phase_shift([0.015, 0.010, 0.016, 0.012, 0.018], timing_reference)

    # Critical statement
    final_diagnostic = analyze_fault_sequence(operational_log, fault_thresholds)

    print(f"Result: {final_diagnostic}")