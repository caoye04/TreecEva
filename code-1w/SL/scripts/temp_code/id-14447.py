from collections import defaultdict, Counter
import math

# Simulate multi-sensor data acquisition
def acquire_sensor_data():
    raw_signals = {
        'sensor_a': [1.2, 3.5, 2.1, 4.7, 3.3],
        'sensor_b': [0.9, 2.3, 1.8, 5.1, 2.9],
        'sensor_c': [1.1, 4.4, 2.2, 3.6, 4.0]
    }
    calibration_offset = {'a': 0.1, 'b': -0.2, 'c': 0.3}
    return raw_signals, calibration_offset

# Irrelevant helper (distractor)
def compute_entropy(data_list):
    freq = Counter(data_list)
    total = len(data_list)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Preprocess signal with normalization and noise filtering
def preprocess_signal(raw_data, offset_map):
    processed = defaultdict(list)
    noise_floor = 0.5
    gain_factor = 1.05

    for key, values in raw_data.items():
        sensor_id = key.split('_')[1]
        calibrated = [v + offset_map.get(sensor_id, 0) for v in values]
        filtered = [g * (x if abs(x) > noise_floor else 0) for x in calibrated]
        normalized = [round(x / max(filtered + [1]), 3) for x in filtered]
        processed[key] = normalized

    # Dead code path (distractor)
    if len(processed) > 10:
        return None
    
    # Unused transformation
    temp_snapshot = {k: v[:] for k, v in processed.items()}
    scaling_log = []
    for k, v_list in temp_snapshot.items():
        scaling_log.append(f"{k}: scaled to {len(v_list)} entries")

    return processed

# Misleading analysis function (decoy)
def evaluate_stability(metrics):
    if not metrics:
        return False
    avg_metric = sum(sum(v) for v in metrics.values()) / sum(len(v) for v in metrics.values())
    return avg_metric > 0.6

# Core diagnostic logic
def generate_threshold_map(signal_dict):
    base_thresholds = defaultdict(float)
    aggregate_stats = []

    for sensor, readings in signal_dict.items():
        valid_readings = [r for r in readings if r > 0]
        if valid_readings:
            mean_val = sum(valid_readings) / len(valid_readings)
            peak = max(valid_readings)
            base_thresholds[sensor] = (mean_val * 0.7 + peak * 0.3)
            aggregate_stats.extend(valid_readings)

    # Extra irrelevant computation
    global_mean = sum(aggregate_stats) / len(aggregate_stats) if aggregate_stats else 0
    outlier_count = sum(1 for x in aggregate_stats if x > global_mean * 2)

    # Actual useful output
    return dict(base_thresholds)

# Signal anomaly classification (unused but plausible)
def classify_pattern(sequence):
    if len(sequence) < 3:
        return 'indeterminate'
    trend = 'rising' if sequence[-1] > sequence[0] else 'falling'
    volatility = 'high' if max(sequence) - min(sequence) > 0.5 else 'low'
    return f"{trend}_{volatility}"

# Main analysis engine
def analyze_signal(data_block, thresholds):
    diagnostics = []
    cumulative_score = 0
    event_count = 0

    for sensor_name, samples in data_block.items():
        thresh = thresholds.get(sensor_name, 0.5)
        high_activity = [s for s in samples if s > thresh]
        
        if len(high_activity) >= 2:
            severity = sum(h for h in high_activity) * 100
            diagnostics.append(severity)
            cumulative_score += severity
            event_count += 1

        # Red herring computation
        coherence_ratio = len(high_activity) / len(samples) if samples else 0
        if coherence_ratio > 1.0:
            cumulative_score -= 10  # Impossible branch (never reached)

    # Secondary processing on diagnostics
    filtered_diagnostics = [d for d in diagnostics if d > 50]
    adjustment_factor = 0.9 if event_count > 1 else 1.1
    
    intermediate_result = sum(filtered_diagnostics) * adjustment_factor
    
    # Final computation chain
    penalty = 0
    if event_count == 0:
        penalty = -100
    elif event_count == 3:
        bonus = 50
        intermediate_result += bonus  # Only one sensor triggers

    final_diagnostic = int(round(intermediate_result + penalty))

    # Distractor: unused complex structure
    summary_report = {
        'timestamp': '2023-11-05T10:30:00Z',
        'readings_processed': sum(len(v) for v in data_block.values()),
        'threshold_reference': dict(thresholds),
        'raw_diagnostics': diagnostics,
        'event_meta': {'count': event_count, 'bonus_applied': 'bonus' in locals()}
    }

    return final_diagnostic

# Orchestration
if __name__ == '__main__':
    # Step 1: Acquire data
    raw_data, offsets = acquire_sensor_data()
    
    # Step 2: Preprocess
    processed_data = preprocess_signal(raw_data, offsets)
    
    # Step 3: Generate thresholds
    threshold_map = generate_threshold_map(processed_data)
    
    # Step 4: Analyze signal
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")