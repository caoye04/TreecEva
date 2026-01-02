from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def collect_diagnostics():
    raw_signals = [127, 255, 192, 64, 32, 16, 8, 4, 2, 1]
    timing_log = []
    system_flags = []
    
    # Irrelevant preprocessing: signal mirroring (distractor)
    mirrored = [x ^ 255 for x in raw_signals]
    normalized = [x / 255.0 for x in raw_signals]
    
    # Real processing path begins
    for i, val in enumerate(raw_signals):
        if val & (val - 1) == 0 and val > 1:  # Power of two check
            shift_count = 0
            temp = val
            while temp > 1:
                temp >>= 1
                shift_count += 1
            timing_log.append((i, shift_count))

    # Dead code path - never executed due to condition (red herring)
    if sum(mirrored) < 0:
        debug_trace = [bin(x) for x in mirrored]
        system_flags.append('DEBUG_MODE')

    # Actual flag generation logic
    for idx, (pos, shift) in enumerate(timing_log):
        if shift % 2 == 0:
            system_flags.append(f'ALIGN_{shift}')
        else:
            system_flags.append(f'OFFSET_{shift}')

    # Decoy function call (never used)
    def analyze_phase_noise(data):
        return sum(x ** 0.5 for x in data) / len(data)
    
    # Unused intermediate calculation (misleading)
    baseline_rms = sum(n ** 2 for n in normalized) ** 0.5
    peak_signal = max(raw_signals)
    
    # Real aggregation logic hidden among distractions
    return timing_log, system_flags

# Secondary transformation with distractors
def filter_anomalies(log_data):
    anomalies = []
    for index, shift_val in log_data:
        if shift_val in [1, 3, 5]:
            anomalies.append(index * 2)
    # This function is called but result not directly used (distraction)
    return anomalies

# Core metric computation - critical path
def aggregate_metrics(log, flags):
    metric_map = defaultdict(int)
    
    # Process timing log into frequency counts
    for pos, shift in log:
        metric_map['total_shifts'] += 1
        metric_map[f'shift_{shift}'] += 1
    
    # Parse system flags for pattern counting
    flag_counter = Counter(flags)
    for key, count in flag_counter.items():
        if 'ALIGN' in key:
            metric_map['alignment_events'] += count
        elif 'OFFSET' in key:
            metric_map['offset_events'] += count
    
    # Compute diagnostic score using only specific components
    base_score = metric_map['total_shifts'] * 100
    alignment_bonus = metric_map['alignment_events'] * 10
    offset_penalty = metric_map['offset_events'] * 5
    
    # Red herring: unused complex calculation
    spectral_entropy = sum(
        - (count / len(flags)) * ((count / len(flags)) ** 0.5)
        for count in flag_counter.values()
    )
    
    # Final diagnostic formula (only this matters)
    final_diagnostic = base_score + alignment_bonus - offset_penalty
    
    # Additional decoy variables
    derived_index = spectral_entropy * 1000
    calibration_offset = len(log) - len(flags)
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Collect primary data
    timing_log, system_flags = collect_diagnostics()
    
    # Call irrelevant analysis function (distraction)
    _ = filter_anomalies(timing_log)
    
    # Critical computation
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")