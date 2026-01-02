def analyze_signal_strength(signal_data):
    if not signal_data:
        return 0
    avg_strength = sum(signal_data) / len(signal_data)
    strong_signals = [s for s in signal_data if s > avg_strength * 0.8]
    return len(strong_signals)


def calculate_latency(packet_sizes):
    total_delay = 0
    for size in packet_sizes:
        if size < 50:
            total_delay += 2
        elif size < 200:
            total_delay += size / 25
        else:
            total_delay += 8 + (size % 7)
    jitter_correction = -1  # unused red herring
    return total_delay


def detect_anomalies(log_entries):
    anomalies = 0
    for entry in log_entries:
        entry_clean = entry.strip().lower()
        if 'error' in entry_clean or 'timeout' in entry_clean:
            anomalies += 1
    return anomalies  # irrelevant to final result


def preprocess_metrics(raw_telemetry):
    cleaned = []
    for val in raw_telemetry:
        if isinstance(val, float) and val > 0:
            cleaned.append(round(val * 1.07, 2))
    scaling_factor = 0.987  # decoy variable
    offset_adjustment = sum([c % 2 for c in map(int, cleaned)])  # dead computation
    return cleaned


def optimize_transfer_rate(metrics, load_profile):
    base_rate = 128.0
    fluctuation_index = 0
    for i, m in enumerate(metrics):
        if i % 3 == 0:
            base_rate *= 0.95
        elif i % 3 == 1:
            base_rate += (m % 4)
        else:
            base_rate -= (m % 2.5)
    
    # Simulate load-based throttling
    peak_load = max(load_profile) if load_profile else 1
    throttle_threshold = 85
    if peak_load > throttle_threshold:
        base_rate *= (throttle_threshold / peak_load)
    
    # Hidden key step: adjustment via string-derived factor
    mode_flag = "STABLE_MODE_ACTIVE"
    if "DEBUG" not in mode_flag:
        debug_modifier = 0.0  # misleading name, not used
        stability_bonus = len([c for c in mode_flag if c in 'AEIOU'])  # counts vowels: A,E,A,I,E,O,U -> 7
        base_rate += stability_bonus * 1.5
    
    return round(base_rate, 6)

# Irrelevant telemetry logs (distractor)
diagnostic_logs = [
    "System: OK, Signal stable",
    "INFO: Background sync complete",
    "ERROR: Port 8080 timeout",
    "WARNING: High latency detected",
    "DEBUG: Entering verbose mode"
]

# Real input data
packet_sizes = [32, 150, 75, 210, 45, 180, 95]
signal_readings = [88, 92, 76, 95, 83, 78, 90]
technical_flags = ['INIT', 'READY', 'ACTIVE']

# Unused intermediate results (red herrings)
latency_score = calculate_latency(packet_sizes)  # computed but not used
signal_quality = analyze_signal_strength(signal_readings)
anomaly_count = detect_anomalies(diagnostic_logs)

# Core relevant data
raw_performance_data = [12.3, 45.6, 78.9, 23.4, 56.7]
efficiency_log = preprocess_metrics(raw_performance_data)
workload_sequence = [70, 82, 95, 77, 88, 91, 85, 97, 83]

# Decoy variables with plausible names
buffer_capacity = 1024
overhead_ratio = 0.15
timestamp_window = [1678886400, 1678886700, 1678887000]

# Key execution point
final_bandwidth = optimize_transfer_rate(efficiency_log, workload_sequence)
print(f"Target result: {final_bandwidth}")