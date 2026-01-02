def preprocess_readings(raw_readings):
    # Irrelevant transformation: converts to percentage (not used in final logic)
    normalized = [(x - 20) * 1.5 for x in raw_readings if x > 10]
    filtered = [x for x in raw_readings if x >= 0]
    return [x for x in filtered if x < 100]

# Simulated sensor readings (some out-of-range values included)
sensor_readings = [23, 45, -5, 67, 120, 34, 91, 5, 105]

# Decoy data structures
decoys = {
    'calibration_offsets': [0.1, -0.3, 0.4, 0.0],
    'version': '2.1a',
    'deprecated_flags': {1, 3, 7}
}

# Unused function that looks important
def compute_stability_index(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return round(variance ** 0.5, 3)

# Thresholds for system health analysis (used later)
thresh_map = [
    ('voltage', 70),
    ('current', 40),
    ('temperature', 90)
]
thresholds = dict(thresh_map)

# Processed dataset with irrelevant operations
raw_data_log = {'entries': len(sensor_readings), 'type': 'diagnostic'}
processed_readings = preprocess_readings(sensor_readings)

# Add dummy transformations that don't affect outcome
shifted_data = list(map(lambda x: x + 5 if x < 50 else x - 10, processed_readings))
indexed_data = list(enumerate(shifted_data, start=1))

# Create a set of high-value indices (distractor)
high_indices = {i for i, val in indexed_data if val > 75}

# Core data for analysis
system_data = []
for idx, reading in enumerate(processed_readings):
    status_flag = 0
    if reading > thresholds['temperature']:
        status_flag = 2
    elif reading > thresholds['current']:
        status_flag = 1
    entry = {
        'id': idx + 1000,
        'val': reading,
        'flag': status_flag,
        'meta': f"S{idx % 3}"
    }
    system_data.append(entry)

# Another decoy: zipping unrelated sequences
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
combined_tags = list(zip(names, shifted_data))

# Key function: analyzes system metrics and computes diagnostic score
def analyze_metrics(metrics, limits):
    critical_count = 0
    warning_count = 0
    total_score = 0.0

    # Extract values using enumerate for alignment with metadata
    for i, record in enumerate(metrics):
        val = record['val']
        meta_prefix = record['meta'][0]

        # Real logic begins
        if val > limits['temperature']:
            critical_count += 1
            total_score += val * 0.8
        elif val > limits['current']:
            warning_count += 1
            total_score += val * 0.5
        else:
            total_score += val * 0.2

        # Red herring: complex bit manipulation on meta (unused)
        shift_amt = int(meta_prefix[1:]) if meta_prefix.isdigit() else (i % 4)
        decoy_flag = (record['flag'] << 2) ^ 5
        _ = decoy_flag & 0xFF  # Dead operation

    # Core calculation buried in distractions
    base = critical_count * 1000
    bonus = warning_count * 100
    penalty = len([r for r in metrics if r['val'] < 20]) * 10

    # Final diagnostic formula
    final_score = base + bonus - penalty + int(total_score)

    # Irrelevant string aggregation
    flags_used = set(r['flag'] for r in metrics)
    _ = ''.join(chr(65 + f) for f in flags_used)  # Unused

    return final_score

# Execute key statement
final_diagnostic = analyze_metrics(system_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")