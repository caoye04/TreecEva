import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [i * math.sin(i / 10) + 2.5 for i in range(100)]
    offset_correction = sum([math.cos(i / 5) for i in range(10)])
    calibrated = [x + offset_correction / 10 for x in raw_readings]
    return calibrated

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x + 1e-5)
    return total

# Signal filtering based on adaptive threshold (relevant)
def dynamic_threshold(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return mean_val + 1.5 * std_dev

# Misleading normalization path (dead code path)
def legacy_normalize(signal):
    max_val = max(signal)
    min_val = min(signal)
    if max_val == min_val:
        return [0 for _ in signal]
    return [(x - min_val) / (max_val - min_val) for x in signal]

# Real filter: removes noise below statistical threshold
def filter_noise(signal, limit):
    return [x for x in signal if abs(x) > limit]

# Diagnostic engine with bit flags (mixed paradigm)
def analyze_signal(clean_data, cutoff):
    # Bit flag tracking: 1=stable, 2=spike, 4=drift, 8=oscillation
    flags = 0
    spike_count = 0
    drift_accumulator = 0

    for i in range(1, len(clean_data)):
        diff = clean_data[i] - clean_data[i-1]
        if abs(diff) > 3 * cutoff:
            spike_count += 1
            flags |= 2
        drift_accumulator += diff

    if abs(drift_accumulator) < 0.5:
        flags |= 1

    avg_spike = spike_count / len(clean_data) if clean_data else 0

    # Oscillation detection via zero-crossing (advanced logic)
    zero_crossings = 0
    for i in range(1, len(clean_data)):
        if clean_data[i-1] * clean_data[i] < 0:
            zero_crossings += 1

    if zero_crossings > len(clean_data) * 0.15:
        flags |= 8

    # Final diagnostic score: combination of metrics
    base_score = int(math.log(abs(drift_accumulator) + 1, 2))
    penalty = (flags & 2) * spike_count // 2
    bonus = (flags & 1) * 5
    oscillation_factor = (flags & 8) * (zero_crossings // 10)

    result = base_score - penalty + bonus + oscillation_factor

    # Dead computation - irrelevant to final result
    shadow_copy = [result * math.tan(0.1 * i) for i in range(5)]
    aggregate_shadow = sum(shadow_copy) / len(shadow_copy) if shadow_copy else 0

    return result  # Only 'result' feeds into final_diagnostic

# Unused predictive model (distractor)
def predict_failure_trend(history):
    n = len(history)
    if n < 2:
        return 0.0
    trend = sum(history[i+1] - history[i] for i in range(n-1)) / (n-1)
    return math.exp(-abs(trend))

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    sensor_stream = collect_sensor_readings()

    # Step 2: Compute irrelevant entropy metric (red herring)
    entropy_metric = compute_entropy(sensor_stream)

    # Step 3: Calculate dynamic threshold (relevant)
    threshold = dynamic_threshold(sensor_stream)

    # Step 4: Filter out low-amplitude noise (relevant)
    filtered_data = filter_noise(sensor_stream, threshold * 0.4)

    # Step 5: Apply legacy normalize? No — not used (misdirection)
    normalized_data = legacy_normalize(sensor_stream)  # Computed but unused

    # Step 6: Analyze signal characteristics (key step)
    final_diagnostic = analyze_signal(filtered_data, threshold)

    # Print final answer as required
    print(f"Result: {final_diagnostic}")