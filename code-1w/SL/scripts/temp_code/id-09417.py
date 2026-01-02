def process_environmental_data(readings, thresholds, tags):
    # Irrelevant preprocessing block (dead path)
    temp_log = []
    for val in readings:
        if val > 100:
            temp_log.append(val * 0.1)

    # Distractor: complex but unused transformation
    normalized = [round((x - min(readings)) / (max(readings) - min(readings)) * 10, 3) for x in readings]
    classification = {i: 'HIGH' if x > thresholds[0] else 'LOW' for i, x in enumerate(readings)}

    # Actual filtering logic (used)
    filtered_data = [readings[i] for i in range(len(readings)) if readings[i] >= thresholds[1] and tags[i] != 'OBSOLETE']

    # Decoy function call with misleading name
    def compute_thermal_index(data):
        return sum(x ** 0.5 for x in data if x > 50) // len(data)

    dummy_index = compute_thermal_index(readings)  # Unused result

    # Bit manipulation red herring (no effect on output)
    bit_fingerprint = 0
    for x in readings[:3]:
        bit_fingerprint ^= (x << 2) | (x >> 3)
    bit_fingerprint = bit_fingerprint & 0xFFFF

    # Real impact map construction
    impact_map = {}
    for i, tag in enumerate(tags):
        if tag in ['CRITICAL', 'PRIORITY']:
            impact_map[i] = readings[i] * 2.1 if readings[i] > 0 else 0.0

    # Unused recursive helper (decoy)
    def traverse_map(dct, depth=0):
        if depth > 3 or not dct:
            return 0
        total = 0
        for k in dct:
            total += traverse_map({k-1: None} if k > 0 else {}, depth + 1)
        return total + depth

    structure_depth = traverse_map(impact_map)  # Dead end

    # Core aggregation logic
    def aggregate_metrics(data, impacts):
        base_sum = sum(data)
        impact_bonus = sum(v for k, v in impacts.items() if k < len(data))
        penalty = len([x for x in data if x % 7 == 0]) * 3.5
        return round(base_sum + impact_bonus - penalty, 4)

    # Key assignment point
    filtration_score = aggregate_metrics(filtered_data, impact_map)
    
    # Final red herring: irrelevant container operation
    stats_summary = {
        'count': len(filtered_data),
        'modes': [item for item, count in dict((x, filtered_data.count(x)) for x in set(filtered_data)).items() if count > 1],
        'checksum': sum(filtered_data[i] * (i+1) for i in range(len(filtered_data)))
    }

    # Output the required variable
    print(f"Target result: {filtration_score}")
    return filtration_score

# Input data
sensor_readings = [12, 45, 67, 89, 105, 72, 0, 56, 77, 81]
threshold_values = [50, 60]  # Only second threshold used
tag_labels = ['NORMAL', 'NORMAL', 'PRIORITY', 'CRITICAL', 'OBSOLETE', 'PRIORITY', 'NORMAL', 'NORMAL', 'PRIORITY', 'CRITICAL']

result = process_environmental_data(sensor_readings, threshold_values, tag_labels)