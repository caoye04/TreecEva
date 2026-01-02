def analyze_sensor_data():
    # Simulated sensor readings from environmental monitoring stations
    temperature_readings = [23.5, 24.1, 19.8, 22.7, 25.3, 20.4, 21.9, 26.0]
    humidity_readings = [45, 50, 52, 47, 55, 48, 51, 53]
    pressure_readings = [1013, 1015, 1012, 1010, 1016, 1014, 1011, 1009]

    # Irrelevant transformation: unused transformed list
    scaled_temps = [round(t * 1.02, 2) for t in temperature_readings if t > 20]

    # Distractor: complex-looking but unused bitwise flag system
    SYSTEM_FLAGS = 0b10101010
    DEBUG_MODE = SYSTEM_FLAGS & 0b00000001
    LOGGING_ACTIVE = (SYSTEM_FLAGS >> 1) & 1
    ANOMALY_MASK = (SYSTEM_FLAGS >> 2) & 0b1111

    # Unused recursive function (dead code path)
    def calculate_depth(index):
        if index <= 0:
            return 0
        return index + calculate_depth(index - 2)

    # Real processing begins: normalize data
    normalized_temp = [t - 20 for t in temperature_readings]  # baseline shift
    temp_sum = sum(normalized_temp)
    temp_count = len(normalized_temp)

    # Compute moving average (unused distractor)
    moving_avg = []
    for i in range(2, len(temperature_readings)):
        avg = sum(temperature_readings[i-2:i+1]) / 3
        moving_avg.append(round(avg, 2))

    # Boolean logic and comparisons to detect anomalies
    high_humidity_zones = [h > 50 for h in humidity_readings]
    critical_zone_flags = [temp > 24 and humid > 50 for temp, humid in zip(temperature_readings, humidity_readings)]

    # Set operations: identify overlapping risk conditions
    high_temp_set = {i for i, t in enumerate(temperature_readings) if t > 24}
    high_humid_set = {i for i, h in enumerate(humidity_readings) if h > 50}
    critical_indices = high_temp_set & high_humid_set  # intersection

    # Distractor: elaborate but unused data structure
    diagnostic_log = {}
    for idx, (t, h) in enumerate(zip(temperature_readings, humidity_readings)):
        status_code = (t << 2) ^ h  # Bit manipulation red herring
        diagnostic_log[idx] = {
            'raw_status': status_code,
            'phase': 'monitoring' if idx % 2 == 0 else 'standby',
            'checksum': (idx + status_code) % 7
        }

    # Linear search for first critical point (used later)
    first_critical_index = -1
    for i in range(len(critical_zone_flags)):
        if critical_zone_flags[i]:
            first_critical_index = i
            break

    # Complex conditional with short-circuit evaluation
    base_threshold = 150
    adjustment_factor = 0
    if len(critical_indices) > 1 and first_critical_index > 2:
        adjustment_factor = 12
    elif len(critical_indices) == 1 and first_critical_index == 4:
        adjustment_factor = 8
    else:
        adjustment_factor = 5

    # Multiple assignment and tuple unpacking (real usage)
    avg_temp_offset, avg_humidity = sum(normalized_temp) / temp_count, sum(humidity_readings) / len(humidity_readings)

    # Composite calculation chain
    signal_strength = 0
    for i, p in enumerate(pressure_readings):
        signal_strength += (p % 10) * (i + 1)

    # Primary score computation
    aggregate_score = int(avg_temp_offset * 10) + int(avg_humidity)

    # Anomaly detection using bit counting and logical ops
    anomaly_seed = len(critical_indices) * 17
    anomaly_mask = 0
    for i in range(8):
        if (anomaly_seed >> i) & 1:
            anomaly_mask ^= (1 << (7 - i))
    anomaly_detector = bin(anomaly_mask).count('1') * 23

    # UNUSED: another dead-end function
    def generate_report(data):
        return sorted(data, reverse=True)[:3]

    # Key statement — target execution point
    final_diagnostic = aggregate_score + anomaly_detector

    # Print result as required
    print(f"Result: {final_diagnostic}")

analyze_sensor_data()