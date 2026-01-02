def analyze_sensor_data():
    # Simulated sensor readings (temperature, pressure, humidity)
    raw_readings = [
        [23.4, 101.3, 45.0],
        [24.1, 100.9, 47.2],
        [22.8, 101.5, 44.1],
        [25.6, 102.1, 50.3],
        [19.9, 100.7, 42.9],
        [26.3, 103.4, 53.1],
        [20.1, 99.8, 41.0]
    ]

    # Thresholds for anomalies
    TEMP_HIGH = 25.0
    TEMP_LOW = 21.0
    PRESSURE_DRIFT = 2.0
    HUMIDITY_RISE_RATE = 5.0

    # Derived metrics
    temperature_trend = [row[0] for row in raw_readings]
    pressure_baseline = sum(row[1] for row in raw_readings) / len(raw_readings)
    humidity_sequence = [row[2] for row in raw_readings]

    # Irrelevant transformation: normalize humidity to 0-1 scale (not used later)
    normalized_humidity = [h / 100.0 for h in humidity_sequence]

    # Track high-temp events
    high_temp_events = []
    for i, temp in enumerate(temperature_trend):
        if temp > TEMP_HIGH:
            high_temp_events.append(i)

    # Compute rolling average pressure (distractor - not used in final logic)
    window_size = 3
    rolling_pressures = []
    for i in range(len(raw_readings) - window_size + 1):
        avg_p = sum(raw_readings[i+j][1] for j in range(window_size)) / window_size
        rolling_pressures.append(avg_p)

    # Identify sudden humidity jumps (unused path)
    humidity_increases = []
    for i in range(1, len(humidity_sequence)):
        if humidity_sequence[i] - humidity_sequence[i-1] > HUMIDITY_RISE_RATE:
            humidity_increases.append(i)

    # Core diagnostic logic
    temp_anomalies = 0
    for temp in temperature_trend:
        if temp > TEMP_HIGH or temp < TEMP_LOW:
            temp_anomalies += 1

    # Pressure variance check
    pressure_variance = max(row[1] for row in raw_readings) - min(row[1] for row in raw_readings)
    pressure_alert = 1 if pressure_variance > PRESSURE_DRIFT else 0

    # Unused: simulate fault injection test (dead code path)
    def simulate_failure_mode():
        return False  # Never called

    # Destructuring assignment (relevant)
    first_temp, *middle_temps, last_temp = temperature_trend

    # Compute stability metric using slicing and enumerate
    stable_period_count = 0
    for idx, temp in enumerate(middle_temps):
        if TEMP_LOW <= temp <= TEMP_HIGH:
            stable_period_count += 1

    # Anomaly-based scoring
    base_risk_score = temp_anomalies * 10
    aggregate_score = base_risk_score + pressure_alert * 25

    # Decoy calculation with set operations (irrelevant)
    unique_humidity_set = set(round(h, 1) for h in humidity_sequence)
    expected_readings = {42.9, 44.1, 45.0, 47.2}
    missing_readings = expected_readings - unique_humidity_set
    unexpected_readings = unique_humidity_set - expected_readings

    # Another decoy: zipped iteration over unrelated data
    synthetic_flags = [0, 1, 1, 0, 1]
    for h, f in zip(humidity_sequence, synthetic_flags):
        if h > 50 and f:
            pass  # No effect

    # Critical flag determination
    sustained_high_temp = len(high_temp_events) >= 2 and last_temp > TEMP_HIGH
    anomaly_flag = 1 if sustained_high_temp else 0

    # Correction factor based on initial conditions
    correction_factor = 0
    if first_temp < TEMP_LOW:
        correction_factor += 15
    if raw_readings[0][1] < pressure_baseline:
        correction_factor += 10

    # Key execution point
    final_diagnostic = aggregate_score + anomaly_flag * correction_factor

    # Print required result
    print(f"Result: {final_diagnostic}")

analyze_sensor_data()