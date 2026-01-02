import math

# Simulated sensor array data from distributed IoT devices
def collect_sensor_readings():
    raw_readings = [
        [14, 17, 23, 42, 19],
        [8, 21, 16, 27, 33],
        [11, 13, 18, 25, 30],
        [9, 15, 20, 24, 29]
    ]
    return raw_readings

# Legacy function — unused but looks relevant
def calculate_legacy_score(data):
    score = 0
    for row in data:
        for val in row:
            score += (val % 7) ** 2
    return score  # Never actually used

# Signal normalization using z-score with dynamic mean estimation
def normalize_signal(signal_stream):
    flat = [item for sublist in signal_stream for item in sublist]
    mean_val = sum(flat) / len(flat)
    variance = sum((x - mean_val) ** 2 for x in flat) / len(flat)
    std_dev = math.sqrt(variance) if variance > 0 else 1
    normalized = [(x - mean_val) / std_dev for x in flat]
    return normalized

# Frequency domain analysis stub (red herring)
def analyze_frequency_components(signal):
    freq_peaks = []
    for i in range(len(signal)):
        if i % 10 == 0 and i > 0:
            freq_peaks.append(math.sin(i * 0.5))
    return freq_peaks  # Not used in final result

# Core health metric computation based on weighted cluster analysis
def compute_cluster_health(data_matrix):
    clusters = []
    for idx, row in enumerate(data_matrix):
        activation = sum(x ** 0.5 for x in row if x > 10)
        decay_factor = math.exp(-idx * 0.1)
        clusters.append(activation * decay_factor)
    return clusters

# Weight assignment using bitwise patterns (distraction)
def generate_bitwise_weights(n):
    weights = []
    for i in range(n):
        w = (i ^ 2) & 5  # XOR and AND manipulation
        weights.append(w if w != 0 else 0.5)
    return weights

# Real weight generator — subtle distinction
def generate_cluster_weights(n):
    base = [1.1, 0.9, 1.2, 0.8][:n]
    adjusted = [w * (1 + i * 0.05) for i, w in enumerate(base)]
    return adjusted

# Main aggregation logic with red herrings and decoys
def aggregate_health_metric(weights, signals):
    # Irrelevant slicing distraction
    critical_slice = signals[::3][:5]
    temp_accum = 0
    for s in critical_slice:
        temp_accum += abs(s) * 1.1
    
    # Actual computation path
    signal_chunks = [signals[i:i+5] for i in range(0, len(signals), 5)]
    chunk_averages = [sum(chunk)/len(chunk) for chunk in signal_chunks]
    
    # Misleading intermediate: looks important but unused
    outlier_flags = [abs(avg) > 1.5 for avg in chunk_averages]
    
    # Correct path: cross-reference with cluster weights
    final_values = []
    for i, avg in enumerate(chunk_averages):
        if i < len(weights):
            # Apply weight and dampen by exponential factor
            contribution = avg * weights[i] * math.cos(i * 0.2)
            final_values.append(contribution)
    
    aggregate = sum(final_values)
    
    # Decoy operation — modifies a copy
    _ = [x * 1.5 for x in final_values]
    
    return aggregate

# Orchestration function with multiple entry points (only one used)
def system_diagnostics(mode="comprehensive"):
    readings = collect_sensor_readings()
    
    # Dead code path — looks like it does something
    if mode == "legacy":
        legacy_score = calculate_legacy_score(readings)
        return legacy_score
    
    # Frequency analysis — computed but not used
    flattened = [item for row in readings for item in row]
    normalized_signals = normalize_signal(readings)
    freq_analysis = analyze_frequency_components(flattened)  # Unused
    
    # Cluster processing
    cluster_metrics = compute_cluster_health(readings)
    cluster_weights = generate_cluster_weights(len(cluster_metrics))
    
    # Key statement
    final_diagnostic = aggregate_health_metric(cluster_weights, normalized_signals)
    
    # Print required at end
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execution entry point
if __name__ == "__main__":
    system_diagnostics("comprehensive")