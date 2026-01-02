def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing block (dead path)
    temp_offsets = [0.1 * i for i in range(len(raw_readings))]
    adjusted_offsets = [x * 0.9 for x in temp_offsets]

    # Distractor: complex but unused transformation
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 3 == 0:
            transformed.append(val ** 0.5 + calibration_factor)
        elif i % 3 == 1:
            transformed.append(val // 2 - calibration_factor)
        else:
            transformed.append(abs(val - calibration_factor) * 2)

    # Real processing begins: filter valid channels
    valid_indices = [i for i, x in enumerate(raw_readings) if x > 50 and i % 2 == 0]
    filtered_data = [raw_readings[i] for i in valid_indices]

    # Decoy function call with misleading name
    def compute_health_score(data):
        return sum(d ** 0.3 for d in data) // len(data) if data else 0

    health_status = compute_health_score(filtered_data)  # Unused

    # Set operations to exclude redundant sensor groups
    primary_sensors = {i for i in range(0, len(raw_readings), 3)}
    secondary_sensors = {i for i in range(1, len(raw_readings), 3)}
    excluded_interference = primary_sensors & secondary_sensors  # Always empty

    # Conditional mapping using slicing and zip
    categories = ['low', 'medium', 'high']
    bounds = [100, 200]
    threshold_map = {}
    for cat, (lower, upper) in zip(categories, [(0, 100), (100, 200), (200, float('inf'))]):
        threshold_map[cat] = (lower, upper)

    # Bit manipulation red herring
    checksum = 0
    for val in raw_readings:
        checksum ^= int(val) & 0xFF
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF

    # Actual key logic hidden among distractions
    def process_readings(data, thresholds):
        total = 0
        for d in data:
            if thresholds['low'][0] <= d < thresholds['low'][1]:
                total += d // 10
            elif thresholds['medium'][0] <= d < thresholds['medium'][1]:
                total += d // 5
            elif thresholds['high'][0] <= d:
                total += int(d * 0.75)
        # Additional conditional expression
        scale = 2 if sum(data) > 300 else 1
        return total * scale

    # Misleading intermediate result
    anomaly_count = sum(1 for x in raw_readings if x < 0 or x > 350)

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Print required output
    print(f"Result: {final_diagnostic}")

# Input setup
sensor_readings = [45, 108, 52, 215, 67, 93, 118, 88, 250, 73]
calibration = 12.5

# Execute main logic
analyze_sensor_array(sensor_readings, calibration)