def analyze_sensor_network():
    # Simulated IoT sensor grid data (temperature, pressure, humidity)
    sensor_ids = [f'SNR-{i:03d}' for i in range(1, 17)]
    base_temps = [22.1, 23.5, 19.8, 24.0, 20.3, 25.7, 21.9, 26.2,
                  18.6, 27.4, 22.8, 19.3, 24.9, 20.7, 23.2, 25.1]
    pressures = [101.3, 102.1, 99.8, 103.4, 100.2, 104.7, 101.8, 105.2,
                 98.6, 106.3, 102.4, 99.1, 103.9, 100.7, 102.9, 104.1]
    humidities = [45, 52, 38, 58, 41, 63, 49, 67, 35, 71, 54, 40, 60, 44, 56, 62]

    # Irrelevant calibration coefficients (distractor)
    calib_a = [0.98, 1.02, 0.97, 1.01, 0.99, 1.03, 0.96, 1.04]
    calib_b = [0.05, 0.03, 0.07, 0.02, 0.04, 0.01, 0.06, 0.00]
    adjusted_calib = [a * b for a, b in zip(calib_a, calib_b) if b > 0.02]

    # Threshold configurations (only temp_threshold and hum_thresh are used)
    thresholds = {
        'temp_threshold': 24.5,
        'pressure_anomaly': 105.0,
        'hum_thresh': 60,
        'vibration_limit': 0.8,
        'co2_ceiling': 450
    }

    # Misleading preprocessing - dead code path (not actually used)
    def legacy_normalize(data):
        min_val, max_val = min(data), max(data)
        return [(x - min_val) / (max_val - min_val) for x in data]

    normalized_temps = legacy_normalize(base_temps)  # Distractor computation

    # Real processing begins: identify sensors exceeding thresholds
    high_temp_sensors = []
    for idx, temp in enumerate(base_temps):
        if temp > thresholds['temp_threshold']:
            high_temp_sensors.append(idx)

    high_humidity_zones = [i for i, h in enumerate(humidities) if h > thresholds['hum_thresh']]

    # Cross-reference anomalies using bitwise logic (relevant)
    critical_mask = 0
    for i in high_temp_sensors:
        if i in high_humidity_zones:
            critical_mask |= (1 << i)

    # Simulated packet loss simulation (irrelevant)
    packet_sequence = []
    for i in range(16):
        seq = (i * 29 + 7) % 97
        ack_status = seq % 2 == 0
        packet_sequence.append((seq, ack_status))

    # Actual data filtering based on combined conditions
    filtered_data = []
    for i, (sid, temp, press, hum) in enumerate(zip(sensor_ids, base_temps, pressures, humidities)):
        is_high_temp = temp > thresholds['temp_threshold']
        is_high_pressure = press > thresholds['pressure_anomaly']
        is_critical = is_high_temp and hum > thresholds['hum_thresh']
        score = (temp * 2) + hum  # Composite metric, only used in filter condition
        
        # Conditional expression with meaningful logic
        status_flag = 'CRITICAL' if is_critical else ('WARNING' if is_high_temp or hum > thresholds['hum_thresh'] else 'NORMAL')
        
        if status_flag != 'NORMAL':  # Only include non-normal sensors
            filtered_data.append({
                'id': sid,
                't': temp,
                'p': press,
                'h': hum,
                'flag': status_flag,
                'index': i
            })

    # Red herring: unused sorting operation
    sorted_by_id = sorted(filtered_data, key=lambda x: x['id'])
    sorted_by_temp = sorted(filtered_data, key=lambda x: x['t'], reverse=True)
    sorted_by_score = sorted(filtered_data, key=lambda x: (x['t']*2 + x['h']), reverse=True)  # Not used

    # Decoy function that's defined but not called
    def compute_variance(data, key='t'):
        n = len(data)
        mean = sum(d[key] for d in data) / n
        return sum((d[key] - mean)**2 for d in data) / n

    # Threshold map construction - actually used
    threshold_map = {
        'T_MAX': thresholds['temp_threshold'],
        'H_MAX': thresholds['hum_thresh'],
        'WEIGHT_T': 2.0,
        'WEIGHT_H': 1.0
    }

    # Core processing function (defined inside to increase nesting)
    def process_readings(readings, config):
        total_risk = 0.0
        anomaly_count = 0
        
        for entry in readings:
            temp_score = (entry['t'] - 20) * config['WEIGHT_T']
            hum_score = max(0, entry['h'] - 50) * config['WEIGHT_H']
            combined_risk = temp_score + hum_score
            
            # Conditional risk multiplier
            multiplier = 1.5 if entry['flag'] == 'CRITICAL' else 1.0
            total_risk += combined_risk * multiplier
            
            if entry['flag'] == 'CRITICAL':
                anomaly_count += 1

        # Final diagnostic uses modular arithmetic on bit mask
        base_diagnostic = int(total_risk * 100)
        mod_component = critical_mask % 17  # Depends on outer scope variable
        adjustment = (anomaly_count * 1000) if anomaly_count > 0 else 0
        final_value = base_diagnostic + mod_component + adjustment
        
        # Dead code: unreachable branch (misleading)
        if False:
            final_value = sum(pressures) / len(pressures)
        
        return final_value

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")

analyze_sensor_network()