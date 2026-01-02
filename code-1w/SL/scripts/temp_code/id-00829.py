def analyze_sensor_data(raw_readings, threshold=0.75):
    # Irrelevant preprocessing: Normalize timestamps (unused later)
    normalized_times = [(t - raw_readings[0][0]) / 1000 for t, _ in raw_readings]
    
    # Extract values and apply moving average filter (partially relevant)
    sensor_values = [v for _, v in raw_readings]
    smoothed = []
    window_size = 3
    for i in range(len(sensor_values)):
        if i < window_size - 1:
            smoothed.append(sensor_values[i])
        else:
            window_avg = sum(sensor_values[i - window_size + 1:i+1]) / window_size
            smoothed.append(round(window_avg, 4))
    
    # Compute rolling variance (distractor - not used in final logic)
    variances = []
    for i in range(2, len(smoothed)):
        mean_win = sum(smoothed[i-2:i+1]) / 3
        variance = sum((x - mean_win) ** 2 for x in smoothed[i-2:i+1]) / 3
        variances.append(round(variance, 6))
    
    # Identify spikes above threshold (core logic begins)
    spike_indices = []
    for idx, val in enumerate(smoothed):
        if val > threshold and (idx == 0 or smoothed[idx - 1] < threshold):
            spike_indices.append(idx)
    
    # Simulate false positives filter (mixed relevance)
    filtered_spikes = []
    for i in spike_indices:
        context_sum = 0
        for j in range(max(0, i - 2), min(len(smoothed), i + 3)):
            context_sum += smoothed[j]
        if context_sum > threshold * 5:
            filtered_spikes.append(i)
    
    # Generate synthetic diagnostic codes (mostly irrelevant)
    diagnostics = []
    for k in range(len(filtered_spikes)):
        code = (k * 17 + 42) % 1000
        diagnostics.append(code)
    
    # Unused recursive helper (dead code path)
    def calc_recursive(n):
        if n <= 1:
            return 1
        return n * calc_recursive(n - 2) + (n % 5)
    
    # Anomaly scoring based on spike clustering (critical section)
    clusters = []
    current_cluster = []
    for pos in filtered_spikes:
        if not current_cluster or pos - current_cluster[-1] <= 3:
            current_cluster.append(pos)
        else:
            if len(current_cluster) >= 2:
                clusters.append(current_cluster)
            current_cluster = [pos]
    if current_cluster and len(current_cluster) >= 2:
        clusters.append(current_cluster)
    
    # Secondary clustering metric (misleading intermediate)
    cluster_densities = []
    for cl in clusters:
        span = cl[-1] - cl[0] + 1
        density = len(cl) / span if span > 0 else 0
        cluster_densities.append(round(density, 4))
    
    # Core metrics calculation (key logic)
    base_impact = len(clusters) * 100
    duration_score = sum(len(c) for c in clusters) * 10
    aggregate_metrics = [base_impact, duration_score, base_impact + duration_score]
    
    # Bit manipulation decoy (irrelevant XOR chain)
    magic_key = 0
    for x in [123, 45, 67, 89]:
        magic_key ^= (x << 2) | (x >> 1)
    magic_key &= 0xFF
    
    # String-based validation (distractor using string methods)
    status_flags = ['OK', 'PENDING', 'ALERT', 'RESOLVED']
    flag_summary = ''.join(s[0] for s in status_flags if len(s) > 3)
    validation_hash = sum(ord(c) for c in flag_summary.lower())
    
    # Splice operation (irrelevant slicing)
    temp_slice = sensor_values[::2][:5]
    processed_length = len(temp_slice)
    
    # Final anomaly score depends only on number of clusters (hidden signal)
    anomaly_score = len(clusters) ** 3 if clusters else 0
    scaling_factor = 16.25
    
    # Key assignment statement
    final_diagnostic = aggregate_metrics[-1] + anomaly_score * scaling_factor
    
    # Red herring: unused zip and enumerate
    indexed_diagnostics = list(enumerate(zip(smoothed, variances[:len(smoothed)])))
    
    # Output result
    print(f'Result: {final_diagnostic}')

# Execute with sample data
data_stream = [
    (1678886400, 0.3), (1678886410, 0.4), (1678886420, 0.82),
    (1678886430, 0.85), (1678886440, 0.3), (1678886450, 0.78),
    (1678886460, 0.81), (1678886470, 0.83), (1678886480, 0.2),
    (1678886490, 0.79), (1678886500, 0.84)
]

analyze_sensor_data(data_stream)