from collections import defaultdict, Counter

# Simulated sensor network data with metadata
def fetch_sensor_network():
    raw_readings = [
        (101, 23.5, 'temp'), (102, 45.0, 'pressure'), (103, 23.5, 'temp'),
        (104, 60.2, 'humidity'), (105, 45.0, 'pressure'), (106, 23.5, 'temp'),
        (107, 70.1, 'flow'), (108, 60.2, 'humidity'), (109, 45.0, 'pressure')
    ]
    return raw_readings

def validate_checksum(log_entry):
    # Irrelevant validation function (dead code path)
    return sum(ord(c) for c in str(log_entry)) % 7 == 0

def parse_location(node_id):
    # Misleading location mapping (not used in final logic)
    locations = {
        101: 'north-wing', 102: 'east-wing', 103: 'north-wing',
        104: 'west-wing', 105: 'east-wing', 106: 'north-wing',
        107: 'south-wing', 108: 'west-wing', 109: 'east-wing'
    }
    return locations.get(node_id, 'unknown')

def extract_type(readings):
    # Extracts type using zip and enumerate (relevant)
    ids, values, types = zip(*readings)
    type_count = Counter(types)
    primary_type = type_count.most_common(1)[0][0]
    return primary_type, dict(type_count)

def apply_calibration(value, sensor_type):
    # Complex calibration with red herring cases
    calibrations = {'temp': 1.05, 'pressure': 0.98, 'humidity': 1.02, 'flow': 0.93}
    if sensor_type in calibrations:
        adjusted = value * calibrations[sensor_type]
        if adjusted > 50:
            adjusted -= 5  # Distractor adjustment (unused)
        return adjusted
    return value

def filter_anomalies(data):
    # Filter by value thresholds (some are decoys)
    temp_threshold = 25.0
    pressure_threshold = 44.0  # Critical threshold
    humidity_threshold = 65.0
    valid_entries = []
    anomaly_log = []
    for record in data:
        nid, val, stype = record
        if stype == 'pressure' and val < pressure_threshold:
            anomaly_log.append(nid)  # Logged but not used
        if stype == 'temp' and val > temp_threshold:
            continue  # Skip high temp
        if stype == 'humidity' and val > humidity_threshold:
            continue  # Skip high humidity
        valid_entries.append(record)
    return valid_entries

def aggregate_by_type(entries):
    # Group using defaultdict (relevant)
    grouped = defaultdict(list)
    for nid, val, stype in entries:
        grouped[stype].append(val)
    return grouped

def compute_stability_index(grouped_data):
    # Compute mean and spread (only mean is used later)
    stats = {}
    for stype, values in grouped_data.items():
        mean_val = sum(values) / len(values)
        variance = sum((v - mean_val) ** 2 for v in values) / len(values)
        stability = mean_val / (variance + 1e-5)
        stats[stype] = {'mean': mean_val, 'stability': stability}
    return stats

def generate_threshold_map(primary_type, counts):
    # Creates threshold map; only 'pressure' threshold matters
    base_map = {t: 1.1 * c for t, c in counts.items()}
    base_map['pressure'] = 44.5  # Used in filtering later
    base_map['temp'] = 0  # Red herring
    base_map['dummy'] = 999  # Decoy entry
    return base_map

def process_readings(data, thresholds):
    # Final processing with key logic
    filtered = [r for r in data if not (r[2] == 'pressure' and r[1] >= thresholds['pressure'])]
    calibrated_values = [
        apply_calibration(val, typ) for _, val, typ in filtered
    ]
    total = sum(calibrated_values)
    count = len(calibrated_values)
    final_diagnostic = int(total - count * 10)  # Core computation
    return final_diagnostic

# --- Execution Flow ---
sensor_data = fetch_sensor_network()
main_type, type_distribution = extract_type(sensor_data)

# Dead code paths with misleading usage
for entry in sensor_data:
    node_id, reading, s_type = entry
    location_tag = parse_location(node_id)
    is_valid = validate_checksum(location_tag)  # Unused result

# Main processing pipeline
filtered_data = filter_anomalies(sensor_data)
aggregated = aggregate_by_type(filtered_data)
metrics = compute_stability_index(aggregated)
threshold_map = generate_threshold_map(main_type, type_distribution)
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Result: {final_diagnostic}")