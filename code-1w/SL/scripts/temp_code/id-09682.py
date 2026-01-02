def analyze_system_logs():
    # Simulated system log entry: (timestamp, cpu_load, memory_usage, disk_io, error_flag)
    raw_data = [
        (100, 78, 85, 30, False), (101, 85, 90, 35, True), (102, 80, 88, 40, False),
        (103, 92, 94, 55, True), (104, 88, 91, 50, False), (105, 76, 83, 45, False),
        (106, 95, 96, 60, True), (107, 89, 87, 48, False), (108, 93, 95, 62, True)
    ]

    # Filter critical logs (high CPU or errors)
    critical_events = [entry for entry in raw_data if entry[1] > 90 or entry[4]]

    # Extract performance metrics from all logs
    cpu_loads = [entry[1] for entry in raw_data]
    memory_uses = [entry[2] for entry in raw_data]
    disk_ios = [entry[3] for entry in raw_data]

    # Calculate baseline thresholds (75th percentile approx)
    sorted_cpu = sorted(cpu_loads)
    sorted_mem = sorted(memory_uses)
    sorted_disk = sorted(disk_ios)
    cpu_threshold = sorted_cpu[-len(sorted_cpu)//4]  # Top 25%
    mem_threshold = sorted_mem[-len(sorted_mem)//4]
    disk_threshold = sorted_disk[-len(sorted_disk)//4]

    # Thresholds for anomaly detection
    thresholds = {
        'cpu': cpu_threshold,
        'memory': mem_threshold,
        'disk': disk_threshold
    }

    # Misleading distraction: calculate average temp (not real data)
    temp_readings = [22.1, 23.5, 24.0, 22.8, 25.1, 23.9, 24.4, 22.6, 23.0]
    avg_temp = sum(temp_readings) / len(temp_readings)
    temp_alert_count = len([t for t in temp_readings if t > 24.0])

    # Another red herring: network pings (unrelated to final score)
    ping_times_ms = [45, 120, 80, 300, 95, 110, 250, 70, 100]
    high_latency_count = len([p for p in ping_times_ms if p > 200])
    avg_ping = sum(ping_times_ms) / len(ping_times_ms)

    # Log entries with derived risk level
    log_entries = []
    for ts, cpu, mem, disk, err in raw_data:
        risk = 0
        if cpu > thresholds['cpu']: risk += 2
        if mem > thresholds['memory']: risk += 2
        if disk > thresholds['disk']: risk += 1
        if err: risk += 3
        
        # Apply arbitrary decay based on timestamp proximity to latest
        age_factor = (108 - ts) / 10.0
        adjusted_risk = max(risk - age_factor, 0)
        
        log_entries.append((ts, cpu, mem, disk, err, adjusted_risk))

    # Helper function to compute weighted reliability score
    def compute_reliability_score(entries):
        total_risk = sum(entry[5] for entry in entries)
        event_count = len(entries)
        recent_high_risk = len([e for e in entries if e[1] > 90 and e[5] > 2.5])
        penalty = recent_high_risk * 1.5
        return 100 - total_risk * 2 - penalty

    # Aggregate performance score
    def aggregate_performance(entries, thresh):
        base_score = compute_reliability_score(entries)
        
        # Extra distraction: unused transformation
        normalized = [(e[1]/100, e[2]/100, e[3]/100) for e in entries]
        stability_factor = sum(1 for n in normalized if n[0] < 0.85) * 0.5
        
        # Real adjustment: bonus for non-error recovery
        recovery_opportunities = 0
        for i in range(1, len(entries)):
            prev_err = entries[i-1][4]
            curr_cpu = entries[i][1]
            if prev_err and curr_cpu < thresh['cpu']:
                recovery_opportunities += 1
        
        recovery_bonus = recovery_opportunities * 3
        final = base_score + recovery_bonus + stability_factor
        
        # Dead code branch (never executed due to data)
        emergency_override = False
        if any(e[1] > 99 for e in entries):
            final = max(final - 50, 0)
            emergency_override = True
        
        return int(round(final))

    final_score = aggregate_performance(log_entries, thresholds)
    print(f"Result: {final_score}")

analyze_system_logs()