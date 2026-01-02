def analyze_system_health():
    # Real-time sensor data from multiple subsystems
    temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
    pressure_levels = [101.3, 102.1, 99.8, 103.4, 100.2, 101.8, 102.5]
    voltage_inputs = [5.01, 4.98, 5.05, 4.96, 5.03, 5.07, 4.99]

    # Irrelevant engineering constants (distractor)
    thermal_expansion_coeff = 12.4e-6
    resistivity_copper = 1.68e-8
    gravitational_constant = 9.81

    # Historical baselines (unused but plausible)
    historical_avg_temp = 24.0
    historical_avg_pressure = 101.5
    baseline_variance = 0.87

    # Simulated timestamps (partially used)
    timestamps = ['00:00', '00:01', '00:02', '00:03', '00:04', '00:05', '00:06']
    time_diffs = [j - i for i, j in zip(timestamps[:-1], timestamps[1:])]  # Dead code path

    # Data alignment via zip (relevant)
    sensor_fusion = list(zip(temperature_readings, pressure_levels, voltage_inputs))

    # Diagnostic flags with lambda (relevant)
    is_stable_temp = lambda t: 22.0 <= t <= 26.0
    is_critical_voltage = lambda v: v < 4.95 or v > 5.05
    temp_status = [is_stable_temp(t) for t in temperature_readings]
    voltage_alerts = [is_critical_voltage(v) for v in voltage_inputs]

    # Decoy function: looks important but unused
    def calculate_entropy(data):
        from math import log
        counts = {}
        for x in data:
            counts[x] = counts.get(x, 0) + 1
        total = len(data)
        entropy = 0
        for count in counts.values():
            p = count / total
            entropy -= p * log(p)
        return entropy

    # Bit manipulation red herring (irrelevant)
    status_word = 0b11010110
    masked_diagnostics = status_word & 0b00111100
    parity_check = bin(masked_diagnostics).count('1') % 2

    # Linear search in threshold violation (relevant)
    def first_out_of_bounds(data, lower, upper):
        for i, val in enumerate(data):
            if val < lower or val > upper:
                return i
        return -1

    # Threshold definitions (critical)
    system_thresholds = {
        'temp': (22.5, 25.5),
        'pressure': (100.0, 103.0),
        'voltage': (4.95, 5.05)
    }

    # Unused transformation (distractor)
    normalized_temps = [round((t - min(temperature_readings)) / 
                            (max(temperature_readings) - min(temperature_readings)), 3) 
                       for t in temperature_readings]

    # Core processing logic
    def evaluate_anomaly_score(readings, bounds):
        low, high = bounds
        deviations = [abs(val - ((low + high) / 2)) for val in readings]
        return sum(deviations) / len(deviations)

    def process_metrics(fused_data, thresholds):
        # Extract components using slicing (relevant)
        temps = [row[0] for row in fused_data]
        pressures = [row[1] for row in fused_data]
        voltages = [row[2] for row in fused_data]

        # Compute anomaly scores
        temp_score = evaluate_anomaly_score(temps, thresholds['temp'])
        pressure_score = evaluate_anomaly_score(pressures, thresholds['pressure'])
        voltage_score = evaluate_anomaly_score(voltages, thresholds['voltage'])

        # Combine scores with weighted fusion (key computation)
        composite_score = (temp_score * 0.5) + (pressure_score * 0.3) + (voltage_score * 0.2)

        # Non-linear activation (simulates diagnostic curve)
        if composite_score < 0.5:
            level = 1
        elif composite_score < 1.0:
            level = 2
        else:
            level = 3

        # Additional decoy logic (never executed due to return above)
        health_map = {1: 'OPTIMAL', 2: 'MONITOR', 3: 'CRITICAL'}
        debug_trace = [f"{t:.2f}" for t in temps if t > 25.0]
        checksum = sum(ord(c) for c in ''.join(debug_trace)) % 100

        return int(composite_score * 1000) + level  # Final diagnostic code

    # Unused set operations (distractor)
    unique_pressures = set(round(p, 1) for p in pressure_levels)
    fluctuation_set = set(abs(p1 - p2) for p1, p2 in zip(pressure_levels, pressure_levels[1:]))
    significant_drops = {f for f in fluctuation_set if f > 1.0}

    # Critical execution point
    final_diagnostic = process_metrics(sensor_fusion, system_thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")

analyze_system_health()