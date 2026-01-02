from collections import defaultdict, Counter

def main():
    # Sensor data simulation (real values)
    raw_readings = [
        (101, 'temp', 23.5), (102, 'pressure', 1013.25), (103, 'temp', 24.1),
        (104, 'humidity', 45.0), (105, 'temp', 19.8), (106, 'pressure', 1009.5),
        (107, 'humidity', 52.3), (108, 'temp', 26.7), (109, 'pressure', 1015.0)
    ]

    # Irrelevant mapping (distractor)
    device_names = {101: 'sensor_a', 102: 'sensor_b', 103: 'sensor_c',
                   104: 'sensor_d', 105: 'sensor_e', 106: 'sensor_f',
                   107: 'sensor_g', 108: 'sensor_h', 109: 'sensor_i'}

    # Threshold configuration for valid ranges (used later)
    threshold_map = {
        'temp': (20.0, 25.0),
        'pressure': (1000.0, 1020.0),
        'humidity': (30.0, 60.0)
    }

    # Misleading preprocessing: normalize readings (unused path)
    normalized = []
    for rid, typ, val in raw_readings:
        if typ == 'temp':
            norm_val = (val - 20) / 5
        elif typ == 'pressure':
            norm_val = (val - 1000) / 20
        elif typ == 'humidity':
            norm_val = val / 100
        normalized.append((rid, typ, norm_val))

    # Actual filtering logic: extract only temperature readings above threshold lower bound
    filtered_data = []
    temp_count = 0
    pressure_sum = 0.0
    humidity_set = set()

    for record in raw_readings:
        r_id, r_type, r_value = record

        # Only collect temperature readings within valid operational range
        if r_type == 'temp':
            min_t, max_t = threshold_map['temp']
            if min_t <= r_value <= max_t:
                filtered_data.append(r_value)
                temp_count += 1

        # Dead code branch: collects pressure but never used in final analysis
        if r_type == 'pressure':
            pressure_sum += r_value
            if r_value > 1010:
                pass  # Placeholder logic (irrelevant)

        # Another distractor: build humidity set but unused
        if r_type == 'humidity':
            humidity_set.add(round(r_value))

    # Decoy function call (never executed)
    def calculate_stability_index(data):
        return sum(data) / len(data) if data else 0.0

    # Real analysis function
    def analyze_readings(readings, thresholds):
        # Compute deviation from ideal (22.5°C)
        ideal = 22.5
        deviations = [abs(val - ideal) for val in readings]

        # Use Counter to count deviation categories (idiosyncratic but required)
        dev_counter = Counter()
        for d in deviations:
            if d < 1.0:
                dev_counter['low'] += 1
            elif d < 2.0:
                dev_counter['medium'] += 1
            else:
                dev_counter['high'] += 1

        # Aggregate score based on weighted deviation
        total_score = 0.0
        for d in deviations:
            if d <= 1.0:
                total_score += 10
            elif d <= 2.0:
                total_score += 5
            else:
                total_score += 1

        # Additional logic: apply penalty if too few valid readings
        if len(readings) < 3:
            total_score *= 0.5

        # Incorporate unused pressure average as red herring (but don't use it)
        pressure_avg = pressure_sum / len([r for r in raw_readings if r[1] == 'pressure'])

        # Final diagnostic is integer-rounded total_score
        result = int(total_score)

        # Unrelated bit manipulation (distractor)
        mask = 0b101010
        encoded = result ^ mask & 0xFF

        # But we return the unencoded score
        return result

    # Execute analysis
    final_diagnostic = analyze_readings(filtered_data, threshold_map)

    # Print result for verification
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()