def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant transformation (dead code path)
    normalized = [x * 0.98 for x in raw_readings if x > -50]
    
    # Distractor: complex but unused computation
    stats = {
        'mean': sum(raw_readings) / len(raw_readings),
        'peak': max(raw_readings),
        'baseline': sum(1 for x in raw_readings if x < 10)
    }

    # Real processing begins: filter out invalid readings
    valid_indices = []
    for i, val in enumerate(raw_readings):
        if val >= 0 and val % 2 == 1:  # Only positive odd values
            valid_indices.append(i)

    # Distractor: unused zip operation with irrelevant data
    timestamps = list(range(1000, 1000 + len(raw_readings)))
    paired_data = list(zip(timestamps, raw_readings))
    recent_events = [t for t, v in paired_data if v > 40]

    # Actual signal extraction (relevant)
    extracted_signals = [raw_readings[i] for i in valid_indices]
    amplified = [int(x * calibration_factor) for x in extracted_signals]

    # Another red herring: recursive function that's called but doesn't affect output
    def noise_filter(data, level=0):
        if level >= 3 or len(data) < 2:
            return data
        return noise_filter([data[i] for i in range(1, len(data), 2)], level + 1)
    
    filtered_noise = noise_filter(amplified)  # Not used later

    # Core logic disguised among distractions
    threshold_map = {}
    for idx, val in enumerate(amplified):
        if idx % 3 == 0:
            threshold_map[idx] = val // 3
        elif idx % 3 == 1:
            threshold_map[idx] = val // 4
        else:
            threshold_map[idx] = val // 5

    # Conditional branching with misleading branches
    adjustment = 0
    if sum(amplified) > 500:
        adjustment = 5
    elif sum(amplified) > 300:
        adjustment = 3
    else:
        adjustment = 1  # This will actually trigger

    # Linear search through amplified values for specific pattern
    target_found = False
    for i in range(len(amplified) - 2):
        if amplified[i] == 7 and amplified[i+1] == 7 and amplified[i+2] == 7:
            target_found = True
            break

    # Distractor: dead assignment
    diagnostic_flag = 'CRITICAL' if target_found else 'NORMAL'

    # Key data structure transformation (relevant)
    filtered_data = []
    for i, val in enumerate(amplified):
        if val > (threshold_map.get(i, 10) + adjustment):
            filtered_data.append(val - threshold_map.get(i, 10))

    # Decoy function that looks important
    def integrate_system_health(data):
        if not data:
            return -999
        return sum(x ** 0.5 for x in data if x > 5) // len(data)

    system_health = integrate_system_health(filtered_data)  # Unused

    # Critical function buried in noise
    def process_readings(data, thresholds):
        base = 100
        for i, val in enumerate(data):
            if i in thresholds:
                base += val % 7
            else:
                base -= val % 3
        return int(base * 1.5)  # Final transformation

    final_diagnostic = process_readings(filtered_data, threshold_map)
    print(f"Result: {final_diagnostic}")