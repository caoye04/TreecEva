def monitor_system_performance():
    # Simulated system telemetry
    cpu_load = [0.78, 0.82, 0.91, 0.88, 0.76, 0.73, 0.85, 0.90]
    mem_usage = [0.64, 0.67, 0.71, 0.73, 0.69, 0.66, 0.68, 0.70]
    disk_io = [120, 135, 140, 130, 125, 118, 122, 131]
    network_latency = [45, 52, 48, 55, 60, 58, 50, 47]

    # Irrelevant metrics (distractors)
    ambient_temperature = [22.1, 22.3, 21.9, 22.5, 22.7, 23.0, 22.8, 22.6]
    fan_speed_rpm = [2400, 2500, 2600, 2550, 2480, 2420, 2510, 2580]
    power_draw_watts = [180, 185, 190, 188, 183, 181, 186, 189]

    # Misleading preprocessing
    normalized_temp = [round((t - 22) * 10) for t in ambient_temperature]
    avg_fan_speed = sum(fan_speed_rpm) / len(fan_speed_rpm)
    total_energy = sum(power_draw_watts)

    # Core diagnostic data structures
    health_logs = []
    for i, (cpu, mem) in enumerate(zip(cpu_load, mem_usage)):
        status_code = 1 if cpu > 0.85 or mem > 0.7 else 0
        health_logs.append({'index': i, 'cpu': cpu, 'mem': mem, 'status': status_code})

    # Dead code path (never executed due to hard return below)
    def deprecated_analysis(data):
        return sum(d['cpu'] for d in data) / len(data)  # Unused

    # Thresholds for failure detection
    thresholds = {
        'critical_cpu': 0.90,
        'high_mem': 0.70,
        'latency_warning': 50,
        'disk_bottleneck': 135
    }

    # Early exit red herring
    if sum(network_latency) < 400:
        return -999  # This condition is false, but distracts reasoning

    # Complex nested function with multiple logic paths
    def analyze_system_state(logs, config):
        anomaly_count = 0
        severity_score = 0.0
        recent_alerts = []

        # Bit manipulation decoy
        magic_key = 0
        for i in range(8):
            magic_key ^= i << 2

        # Spurious data transformation
        inverted_logs = [(idx, round(1.0 / entry['cpu'], 2)) for idx, entry in enumerate(logs)]
        avg_inverted = sum(inv for _, inv in inverted_logs) / len(inverted_logs)

        # Actual critical logic (buried)
        for idx, entry in enumerate(logs):
            if entry['status'] == 1:
                anomaly_count += 1
                severity_score += entry['cpu'] * 100
                if idx > 0 and logs[idx-1]['status'] == 1:
                    severity_score += 5  # back-to-back penalty

        # Red herring: unused min/max calculations
        peak_cpu = max(entry['cpu'] for entry in logs)
        min_memory = min(entry['mem'] for entry in logs)
        median_latency = sorted(network_latency)[len(network_latency)//2]

        # Distractor loop with no side effects
        temp_accum = 0
        for val in disk_io:
            if val > config['disk_bottleneck']:
                temp_accum += val % 10

        # Final decision logic
        base_score = severity_score + (anomaly_count * 10)
        adjustment_factor = 0.87

        # Real answer computation
        intermediate = base_score * adjustment_factor
        final_result = int(intermediate + 0.5)  # rounding

        # More noise: unused statistical calculation
        mean_disk = sum(disk_io) / len(disk_io)
        variance_disk = sum((x - mean_disk) ** 2 for x in disk_io) / len(disk_io)

        return final_result

    # Key execution point
    final_diagnostic = analyze_system_state(health_logs, thresholds)
    
    # Print required result
    print(f"Result: {final_diagnostic}")

    # Unused cleanup (dead code)
    def clear_cache():
        nonlocal health_logs, thresholds
        health_logs = []
        thresholds = {}

    return final_diagnostic

# Execute and capture output
monitor_system_performance()