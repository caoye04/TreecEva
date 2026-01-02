from collections import defaultdict, Counter

# Simulated sensor data processing system with diagnostic flags
def process_sensor_stream(raw_readings, thresholds):
    timing_log = []
    fault_flags = []
    temp_cache = []
    cumulative_shift = 0
    baseline_reference = sum(thresholds) / len(thresholds)

    for idx, (reading, threshold) in enumerate(zip(raw_readings, thresholds)):
        adjusted = reading * (1.0 + 0.01 * idx) - baseline_reference
        shifted = int(adjusted * 10) & 0xFF
        timing_log.append(shifted)

        # Irrelevant transformation branch (dead logic path)
        if shifted > 200:
            temp_cache.append(shifted ** 2)
        elif shifted < 50:
            temp_cache.append(-shifted)
        else:
            pass  # Dead code: no effect

        # Real fault detection logic
        if abs(reading) > threshold * 1.5:
            flag_code = 1 << (idx % 4)
            fault_flags.append(flag_code)
            cumulative_shift ^= flag_code

        # Misleading intermediate calculation (unused)
        debug_residual = (adjusted % 7) * idx
        _ = debug_residual  # Distractor: looks important but unused

    # Secondary irrelevant structure (decoy analysis)
    stats_summary = defaultdict(int)
    for val in timing_log:
        if val > 100:
            stats_summary['high'] += 1
        elif val > 50:
            stats_summary['medium'] += 1
        else:
            stats_summary['low'] += 1

    # Unused complex transformation
    weighted_fft = [timing_log[i] * (i+1) for i in range(len(timing_log))]
    normalized_fft = [w / max(weighted_fft) for w in weighted_fft] if weighted_fft else [0]

    # Another decoy function embedded
    def analyze_pattern(seq):
        count = Counter(seq)
        return max(count.values()) if count else 0
    
    pattern_score = analyze_pattern([x & 15 for x in timing_log])  # Unused result

    return timing_log, fault_flags

# Aggregation logic that computes final diagnostic value
def aggregate_metrics(log, flags):
    base_score = sum(log)
    penalty = 0
    
    for i, flag in enumerate(flags):
        if flag & 1:
            penalty += i * 10
        elif flag & 2:
            penalty -= i
        else:
            penalty += 5
    
    # Complex conditional expression involving bitwise and arithmetic
    adjustment = (len(flags) > 0 and ((base_score >> 3) ^ flags[-1])) or (base_score % 100)
    
    # Final computation
    final_value = (base_score - penalty) + adjustment
    
    # Irrelevant floating point accumulation (distractor)
    avg_magnitude = sum(abs(x) for x in log) / len(log) if log else 0
    drift_estimate = avg_magnitude * 0.01 * len(log)

    return int(final_value)

# Main execution
if __name__ == '__main__':
    sensor_data = [89, 102, 45, 210, 77, 150, 33, 190]
    safety_limits = [100, 95, 60, 200, 80, 140, 40, 180]

    # Unused auxiliary data structures (red herring)
    calibration_matrix = [[i*j for j in range(4)] for i in range(4)]
    metadata_trace = {'version': '2.1', 'nodes': 8, 'mode': 'diagnostic'}
    
    # Unused statistical transform
    squared_devs = [(x - sum(sensor_data)//len(sensor_data))**2 for x in sensor_data]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    readings_log, errors = process_sensor_stream(sensor_data, safety_limits)
    final_diagnostic = aggregate_metrics(readings_log, errors)
    
    # Critical output
    print(f"Result: {final_diagnostic}")