import math

# Simulated system telemetry data
timestamps = [1623456000 + i*60 for i in range(100)]
base_load = [abs(50 + 30 * math.sin(t / 10000)) for t in timestamps]
noise = [math.cos(t / 5000) * math.sin(t / 7000) for t in timestamps]
raw_sensor_data = [base_load[i] + noise[i] for i in range(len(base_load))]

# Irrelevant signal processing (distractor)
def apply_fourier_smoothing(data, passes=3):
    smoothed = data.copy()
    for _ in range(passes):
        for i in range(1, len(smoothed) - 1):
            smoothed[i] = (smoothed[i-1] + smoothed[i] + smoothed[i+1]) / 3
    return smoothed

filtered_data = apply_fourier_smoothing(raw_sensor_data)  # Dead path: not used later

# System health indicators (some relevant, some misleading)
cpu_temp_spike = sum(1 for x in raw_sensor_data if x > 75)
memory_leak_warning = any(x < 2 for x in raw_sensor_data)  # Always false

# Real-time anomaly detection flags
anomaly_threshold = 80
exceedance_count = sum(1 for x in raw_sensor_data if x > anomaly_threshold)
recent_exceedances = [i for i, x in enumerate(raw_sensor_data[-20:]) if x > anomaly_threshold]

# Auxiliary calculations with plausible but unused metrics
def compute_entropy(data):
    from collections import Counter
    counts = Counter([round(x) for x in data])
    total = sum(counts.values())
    return -sum((freq/total) * math.log2(freq/total) for freq in counts.values())

entropy_score = compute_entropy(raw_sensor_data)  # Distractor: looks important

# Data windowing and segmentation
window_size = 25
segmented_logs = [raw_sensor_data[i:i+window_size] for i in range(0, len(raw_sensor_data), window_size)]
overlapping_windows = [raw_sensor_data[i:i+window_size] for i in range(0, len(raw_sensor_data)-window_size//2, window_size//2)]  # Unused

# Flag generation logic
system_flags = {
    'high_activity': len([x for x in raw_sensor_data if x > 60]) > 40,
    'critical_spikes': exceedance_count > 5,
    'stability_issue': sum(1 for i in range(1, len(raw_sensor_data)) if abs(raw_sensor_data[i] - raw_sensor_data[i-1]) > 10) > 8,
    'oscillation_pattern': any(abs(noise[i] - noise[i-1]) > 1.5 for i in range(1, len(noise)))
}

# Log entry structure with metadata
log_entries = [
    {
        'timestamp': ts,
        'load': round(raw_sensor_data[i], 2),
        'normalized': (raw_sensor_data[i] - 50) / 50,
        'severity': max(0, raw_sensor_data[i] - 70) / 10,
        'is_peak': raw_sensor_data[i] > 75
    }
    for i, ts in enumerate(timestamps)
]

# Red herring function: computes complex but unused metric
def calculate_system_resilience(entries):
    peaks = [e['load'] for e in entries if e['is_peak']]
    if not peaks:
        return 0.0
    variance = sum((p - sum(peaks)/len(peaks))**2 for p in peaks) / len(peaks)
    return round(math.exp(-variance/100), 4)

resilience_index = calculate_system_resilience(log_entries)  # Not used

# Core diagnostic aggregation function
def aggregate_metrics(logs, flags):
    # Extract severity values only for high-severity windows
    critical_windows = []
    for i in range(0, len(logs), 10):
        window = logs[i:i+10]
        if sum(1 for entry in window if entry['load'] > 65) >= 3:
            avg_severity = sum(e['severity'] for e in window) / len(window)
            critical_windows.append(avg_severity)
    
    # Apply conditional weighting based on system flags
    base_metric = sum(critical_windows)
    
    if flags['high_activity']:
        base_metric *= 1.25
    if flags['critical_spikes']:
        base_metric += 10
    if flags['stability_issue']:
        base_metric = abs(base_metric - 5)  # Counterintuitive adjustment
    
    # Final transformation
    transformed = math.floor(base_metric * 100) / 100  # Round down to 2 decimal places
    
    # Incorporate oscillation impact only if other conditions met
    if flags['oscillation_pattern'] and base_metric > 15:
        transformed -= 3.5
    
    return transformed

# Execution point of interest
final_diagnostic = aggregate_metrics(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")