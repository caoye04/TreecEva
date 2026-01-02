def monitor_system_performance():
    # Core system metrics
    cpu_temp = 67.3
    memory_usage = 8245
    disk_latency_ms = 14
    network_packets = [120, 155, 98, 201, 176]
    uptime_hours = 342

    # Irrelevant telemetry (distraction)
    ambient_temperature = 22.1
    user_sessions = ['admin', 'guest']
    last_backup_timestamp = '2023-11-05T03:45:00Z'
    encryption_key_size = 256

    # Health indicators with mixed types (tuples and dicts)
    health_metrics = {
        'temp': (cpu_temp, 'C'),
        'mem': (memory_usage, 'MB'),
        'latency': (disk_latency_ms, 'ms'),
        'packets': (sum(network_packets), 'count'),
        'uptime': (uptime_hours, 'hours')
    }

    # System load profile (used in computation)
    system_load = {
        'peak_load': 945,
        'base_load': 320,
        'spike_count': 3,
        'recovery_time': 12
    }

    # Distractor: unused function (dead code path)
    def calculate_compression_ratio(data_in, data_out):
        return data_out / data_in if data_in > 0 else 0

    # Distractor: misleading intermediate calculation
    predicted_failure_window = (cpu_temp * 2) + (disk_latency_ms * 5)  # Not used later

    # Red herring: complex string analysis with no impact
    log_summary = "System stable: OK | Load: NOMINAL | Temp: GREEN"
    status_flag = 'CRITICAL' if 'CRITICAL' in log_summary else 'STABLE'
    normalized_status = status_flag.lower().strip()  # Unused

    # Conditional expression with fallback (used)
    load_ratio = (system_load['peak_load'] / system_load['base_load']) if system_load['base_load'] != 0 else 1.0

    # Bit manipulation decoy (irrelevant)
    encoded_signal = (memory_usage ^ 0xABCD) & 0xFFFF
    signal_integrity = bin(encoded_signal).count('1')

    # Real logic begins: recursive depth-limited analysis
    def evaluate_stress_level(level, depth=0):
        if depth >= 3:
            return level * 0.75
        adjusted = level * (0.9 if level > 800 else 1.1)
        return evaluate_stress_level(adjusted, depth + 1)

    # Trigger recursion
    stress_eval = evaluate_stress_level(system_load['peak_load'])

    # Destructuring assignment (tuple unpacking)
    total_packets, _ = health_metrics['packets']

    # Comparison and logical operations chain
    is_overloaded = stress_eval > 700
    has_high_latency = health_metrics['latency'][0] > 10
    critical_condition = is_overloaded and has_high_latency and (cpu_temp >= 65)

    # Sorting distraction: irrelevant ordered list
    sorted_packets = sorted(network_packets, reverse=True)
    median_packet_size = sorted_packets[len(sorted_packets)//2]  # Not used

    # Main analysis function embedded to increase nesting
    def analyze_system_state(metrics, load_profile):
        # Extract relevant values using dictionary access
        temp_val = metrics['temp'][0]
        mem_val = metrics['mem'][0]
        latency_val = metrics['latency'][0]

        # Compute derived diagnostic score
        base_score = temp_val * 2.1 + mem_val * 0.05 + latency_val * 7.3

        # Additional factor from load analysis
        spike_penalty = load_profile['spike_count'] * 18.2

        # Conditional adjustment using ternary
        recovery_bonus = 45.0 if load_profile['recovery_time'] < 15 else 0.0

        # Final composite calculation
        raw_diagnostic = base_score + spike_penalty - recovery_bonus

        # Apply recursive stress weighting
        final_weight = stress_eval / 1000.0
        adjusted_diagnostic = raw_diagnostic * (1 + final_weight)

        # Clamp result to simulate system bounds
        clamped = max(100, min(adjusted_diagnostic, 9999))

        # Key variable assignment - this is the answer
        final_diagnostic = int(round(clamped))

        return final_diagnostic

    # Execute main analysis
    final_diagnostic = analyze_system_state(health_metrics, system_load)

    # Print result for verification
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Run simulation
monitor_system_performance()