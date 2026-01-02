def analyze_readings(readings):
    # Irrelevant signal processing (distractor)
    filtered = [x * 0.9 for x in readings if x > 0]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    peak = max(smoothed) if smoothed else 0

    # Relevant computation: count anomalies above threshold
    anomaly_count = sum(1 for x in readings if x > 75 and x % 5 == 0)

    # Dead code path (misleading)
    if len(readings) > 100:
        return -1  # Never reached

    return anomaly_count


def extract_segments(data_str):
    # String slicing and method usage (required feature)
    segments = data_str.split('|')
    cleaned = [s.strip().lower() for s in segments]
    valid_parts = [c for c in cleaned if c.startswith('sensor')]

    # Distractor: irrelevant string transformation chain
    transformed = ''.join([part[6:] + '-' for part in valid_parts])[:-1]
    length_code = len(transformed.replace('-', ''))

    # Relevant: extract numeric suffix from first valid part
    if valid_parts:
        try:
            sensor_id = int(valid_parts[0][6:])
            return sensor_id  # Used later
        except ValueError:
            return 0
    return 0

def validate_sequence(seq):
    # Bit manipulation and modular arithmetic (suggested paradigm)
    checksum = 0
    for i, val in enumerate(seq):
        checksum ^= (val + i)  # XOR with index offset
    return checksum % 17 == 0  # Modular condition (not directly used)


def process_metrics(data, config):
    # Complex nesting level 3
    base_score = 0
    temp_log = []

    for entry in data:
        # Level 2
        if 'readings' in entry:
            count = analyze_readings(entry['readings'])

            # Level 3
            if count > config['limit']:
                adjusted = count // config['attenuation']
                temp_log.append(adjusted)

                # Early break (suggested paradigm)
                if adjusted > 10:
                    break

    # Slicing operation on temp_log (required)
    recent = temp_log[-3:] if len(temp_log) >= 3 else temp_log

    # Relevant calculation
    aggregate = sum(recent)

    # Multiple distractor variables
    shadow_value = aggregate * 1.5
    backup_flag = False
    debug_trace = [f"Step_{i}" for i in range(aggregate)]

    # Key result built from multiple concepts
    raw_diagnostic = aggregate * 1000

    # Final red herring: unused complex structure
    decoy_matrix = [[i*j for j in range(5)] for i in range(4)]
    metadata_checksum = sum(sum(row) for row in decoy_matrix) % 997

    final_diagnostic = raw_diagnostic + 123  # Actual answer

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate input data
health_data = [
    {
        'id': 'A',
        'readings': [60, 70, 80, 85, 90, 95],  # Only 80, 85, 90, 95 are multiples of 5
        'type': 'vital'
    },
    {
        'id': 'B',
        'readings': [50, 65, 75, 80, 85],      # 75, 80, 85 → all >75 and divisible by 5 → count=3
        'type': 'vital'
    },
    {
        'id': 'C',
        'readings': [40, 55, 70, 90, 95],      # 90, 95 → count=2
        'type': 'vital'
    }
]

thresholds = {
    'limit': 2,
    'attenuation': 1
}

# Extract sensor ID (used to seed something? No — it's a red herring)
sensor_core = extract_segments("Sensor500| SensorXYZ | sensor1024 ")
dummy_sequence = [3, 6, 9, 12]
valid_seq = validate_sequence(dummy_sequence)  # Returns True but unused

# Initiate main logic
final_diagnostic = process_metrics(health_data, thresholds)