import math

# Simulated telemetry data from a distributed sensor array
def collect_sensor_readings():
    raw_signals = [127, 255, 193, 64, 88, 201]
    calibrated = [x * 0.78 for x in raw_signals]
    return calibrated

# Legacy checksum function (unused but looks relevant)
def compute_legacy_hash(data):
    acc = 0
    for d in data:
        acc = (acc * 31 + int(d)) % 65537
    return acc

# Signal smoothing using moving average
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        window_vals = signal[start:end]
        avg = sum(window_vals) / len(window_vals)
        smoothed.append(avg)
    return smoothed

# Frequency domain transformation (distraction)
def time_to_frequency(times):
    freqs = []
    for t in times:
        if t != 0:
            freqs.append(round(1/t, 4))
    return freqs

# Core diagnostic engine
def analyze_phase_shift(readings):
    phase_data = []
    for val in readings:
        shifted = val * math.sin(math.pi / 4)
        normalized = abs(shifted) % 100
        phase_data.append(normalized)
    return phase_data

# Flag problematic sensors based on thresholds
def detect_anomalies(phases):
    flags = []
    for p in phases:
        if p > 75:
            flags.append(3)  # Critical anomaly
        elif p > 50:
            flags.append(2)  # Warning
        elif p > 25:
            flags.append(1)  # Notice
        else:
            flags.append(0)  # Normal
    return flags

# Accumulate timing statistics (actually used)
def generate_timing_profile(anomaly_flags):
    log_entries = []
    accumulator = 0.0
    for i, flag in enumerate(anomaly_flags):
        if flag == 3:
            delta = 0.15 * (i + 1)
        elif flag == 2:
            delta = 0.08 * (i + 1)
        else:
            delta = 0.03 * (i + 1)
        accumulator += delta
        log_entries.append(round(accumulator, 4))
    return log_entries

# Main aggregation logic (key function)
def aggregate_metrics(timing_log, system_flags):
    base_score = sum(timing_log) * 100
    penalty = 0
    for f in system_flags:
        if f == 3:
            penalty += 120
        elif f == 2:
            penalty += 45
    adjustment = len(system_flags) * 7
    result = base_score - penalty + adjustment
    return int(result)

# Irrelevant string processing (distractor)
def parse_sensor_ids(id_list):
    parsed = []
    for sid in id_list:
        clean = sid.strip().upper()
        if clean.startswith("S"):
            parsed.append(clean[1:])
    return parsed

# Unused recursive function to mislead reasoning
def calculate_depth_factor(n):
    if n <= 1:
        return 1
    return n * calculate_depth_factor(n - 1)

# Entry point simulation
def main():
    # Step 1: Collect raw data
    readings = collect_sensor_readings()  # [99.06, 198.9, 150.54, 49.92, 68.64, 156.78]
    
    # Step 2: Smooth the signal (used)
    filtered = smooth_signal(readings)
    
    # Step 3: Transform into phase space
    phase_output = analyze_phase_shift(filtered)
    
    # Step 4: Detect anomalies in phase data
    system_flags = detect_anomalies(phase_output)  # [2, 3, 3, 1, 2, 3]
    
    # Step 5: Generate timing behavior profile
    timing_log = generate_timing_profile(system_flags)  # cumulative deltas
    
    # Step 6: Parse dummy IDs (irrelevant)
    sensor_names = [" S01 ", "S02", "S03", "S04", "S05", "S06"]
    ids = parse_sensor_ids(sensor_names)  # ['01', '02', '03', '04', '05', '06']
    
    # Step 7: Compute legacy hash (unused distractor)
    legacy_checksum = compute_legacy_hash([ord(c) for c in ''.join(ids)])
    
    # Step 8: Calculate depth (dead code)
    depth_metric = calculate_depth_factor(4)  # 24, never used
    
    # Step 9: Aggregate final metrics (KEY STEP)
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()