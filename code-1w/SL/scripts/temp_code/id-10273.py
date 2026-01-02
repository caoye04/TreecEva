import math

# Simulated sensor array diagnostics with noise filtering
def analyze_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if 0.1 <= abs(x) <= 100.0]
    return [val * 1.07 for val in filtered if val > 0]  # Amplify positive signals

# Signal phase alignment
def align_phase(signal, shift):
    return signal[-shift:] + signal[:-shift]

# Baseline normalization (irrelevant to final result but looks important)
def normalize_baseline(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]

# Red herring function: appears critical but unused
def compute_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = -sum((freq/total) * math.log2(freq/total) for freq in counts.values())
    return entropy

# Core metric aggregator - actually used
def aggregate_metrics(trends, base):
    trend_sum = sum(trends)
    base_factor = abs(base)
    adjustment = 0
    for i, t in enumerate(trends):
        if i % 3 == 0:
            adjustment += math.sin(t)
        elif i % 5 == 0:
            adjustment += math.cos(t)
    return int(trend_sum * base_factor + adjustment)

# Simulate hardware calibration (dead code path)
def calibrate_sensors(logs):
    checksum = 0
    for entry in logs:
        if isinstance(entry, str):
            checksum ^= hash(entry) % 1000
    return checksum

# Main execution block
if __name__ == '__main__':
    # Raw diagnostic data from sensors (simulated)
    raw_diagnostics = [-5.2, 12.8, 0.0, 45.1, 98.3, -105.0, 23.4, 67.2, 3.1, 88.9, 1000.0]

    # Irrelevant preprocessing step (only distraction)
    processed_logs = ['event_1', 'alert_2', 'event_3']
    log_hash = calibrate_sensors(processed_logs)

    # Real signal processing begins
    cleaned_signal = analyze_sensor_readings(raw_diagnostics)
    rotated_signal = align_phase(cleaned_signal, 2)
    
    # Inject more distractions
    normalized_context = normalize_baseline(rotated_signal)
    signal_energy = sum([x**2 for x in rotated_signal]) / len(rotated_signal)
    peak_noise_ratio = max(rotated_signal) / (1 + min(rotated_signal))

    # Define baseline for aggregation (this is used)
    baseline = len(rotated_signal) - 7  # evaluates to 4

    # Apply non-linear transformation on every third element
    trend_data = []
    for idx, val in enumerate(rotated_signal):
        if idx % 3 == 0:
            trend_data.append(int(math.log(val + 1) ** 2))
        else:
            trend_data.append(int(val // 2.5))

    # Decoy statistical analysis
    mode_approx = max(set([int(x) for x in trend_data]), key=[int(x) for x in trend_data].count)
    spread_metric = max(trend_data) - min(trend_data)

    # Critical assignment point
    corrective_offset = len(normalized_context)  # This equals 9, but name suggests relevance
    final_diagnostic = aggregate_metrics(trend_data, baseline) + corrective_offset

    print(f"Result: {final_diagnostic}")