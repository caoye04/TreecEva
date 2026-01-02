def monitor_system_performance():
    # Simulated system health monitoring with diagnostic analysis
    raw_readings = [127, 255, 193, 64, 224, 96, 160, 31]
    weights = [0.1, 0.3, 0.15, 0.05, 0.2, 0.05, 0.08, 0.02]
    weighted_sum = sum(r * w for r, w in zip(raw_readings, weights))

    # Irrelevant transformation (distractor)
    normalized = [r / 255.0 for r in raw_readings]
    avg_normalized = sum(normalized) / len(normalized)

    # Bit manipulation for fault pattern detection (relevant)
    fault_signatures = []
    for reading in raw_readings:
        flipped = reading ^ 255  # Invert bits
        masked = flipped & 0x7F  # Keep lower 7 bits
        if masked > 50:
            fault_signatures.append(masked)

    # Decoy statistical analysis (dead path)
    variance = sum((x - sum(raw_readings)/len(raw_readings))**2 for x in raw_readings) / len(raw_readings)
    outlier_count = sum(1 for x in raw_readings if abs(x - 128) > 100)

    # Health log construction using enumerate (relevant)
    health_logs = {}
    for i, val in enumerate(raw_readings):
        key = f"sensor_{i+1}"
        status = 'critical' if val > 200 else 'stable' if val > 100 else 'low'
        health_logs[key] = {'value': val, 'status': status, 'index': i}

    # Threshold definitions (relevant)
    thresholds = {
        'warning': 100,
        'critical': 200,
        'decay_factor': 0.9
    }

    # Spurious machine learning imitation (distractor)
    predictions = []
    for i in range(len(raw_readings) - 1):
        pred = raw_readings[i] * 1.05 + 5
        predictions.append(int(pred))

    # Real diagnostic logic
    def analyze_system_state(logs, limits):
        critical_sensors = []
        total_value = 0
        decayed_sum = 0
        temporal_weights = [0.5 ** i for i in range(len(logs), 0, -1)]

        # Process logs with enumeration and weighting
        for idx, (sensor_id, data) in enumerate(sorted(logs.items(), key=lambda x: x[1]['index'])):
            value = data['value']
            total_value += value

            # Apply decay based on order
            decayed_value = value * thresholds['decay_factor'] ** idx
            decayed_sum += decayed_value

            if data['status'] == 'critical':
                critical_sensors.append(sensor_id)

        # Secondary check using bit signature length
        risk_factor = len(fault_signatures) * 10
        base_score = len(critical_sensors) * 100
        temporal_score = decayed_sum * 2

        # Final diagnostic calculation
        intermediate = base_score + temporal_score + risk_factor
        correction = 42 if len(critical_sensors) >= 2 else 0
        final_score = intermediate - correction

        # This print is irrelevant but adds distraction
        debug_info = {"count": len(predictions), "forecast": sum(predictions)}

        return int(final_score)

    # Execute main analysis
    final_diagnostic = analyze_system_state(health_logs, thresholds)
    
    # Dead assignment (red herring)
    system_verdict = 'unstable' if avg_normalized > 0.5 else 'stable'
    
    # Output the required result
    print(f"Result: {final_diagnostic}")

monitor_system_performance()