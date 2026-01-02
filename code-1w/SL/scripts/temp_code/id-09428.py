from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic evaluation

def analyze_pattern(sequence):
    # Irrelevant helper: analyzes repeating patterns (not used in final result)
    count = Counter(sequence)
    most_common_val = count.most_common(1)[0][1]
    return sum(1 for v in count.values() if v == most_common_val)

def validate_checksum(record):
    # Dead code path: checksum validation never actually invoked
    return sum(ord(c) for c in record) % 7 == 0

def decode_signal(signal_str):
    # Misleading transformation: looks important but unused later
    decoded = ''.join(chr(int(signal_str[i:i+2], 16)) for i in range(0, len(signal_str), 2) if signal_str[i:i+2].isdigit())
    return len(decoded) if decoded else -1

def collect_metrics(entries):
    # Gathers frequency stats – appears useful but is a distractor
    freq_stats = defaultdict(int)
    for e in entries:
        freq_stats[e['zone']] += e['readings'][0]  # Only first reading taken
    return {k: v for k, v in freq_stats.items() if v > 50}

def filter_anomalies(raw_data, mode='strict'):
    # Critical function: filters out low-confidence readings
    cleaned = []
    for item in raw_data:
        confidence = item.get('confidence', 0)
        if mode == 'strict' and confidence >= 0.75:
            cleaned.append(item)
        elif mode == 'loose' and confidence >= 0.5:
            cleaned.append(item)
    return cleaned

def compute_baseline(readings):
    # Computes truncated average after removing extremes
    trimmed = sorted(readings)[1:-1]  # Remove min and max
    return round(sum(trimmed) / len(trimmed), 3) if trimmed else 0.0

def generate_threshold_map(zones):
    # Creates mapping of zone -> dynamic threshold (used in final step)
    base_map = {zone: (ord(zone[0]) * 1.7) % 25 for zone in zones}
    # Add dummy keys to mislead
    base_map['calibration'] = 999.9
    base_map['override'] = -1.0
    return base_map

def process_readings(data_chunk, thresholds):
    # Core logic: computes weighted diagnostic score
    aggregate = 0
    zone_totals = defaultdict(float)
    
    for entry in data_chunk:
        z = entry['zone']
        vals = entry['readings']
        weight = entry['confidence'] * 100
        
        # Real computation
        avg_val = compute_baseline(vals)
        zone_totals[z] += avg_val * weight
    
    # Apply threshold scaling
    for z in zone_totals:
        if z in thresholds and z != 'X99':  # Exclude dummy zone
            adjustment = thresholds[z]
            zone_totals[z] *= (adjustment / 20.0)
    
    aggregate = int(sum(abs(x) for x in zone_totals.values()) + 0.5)
    return aggregate

# --- Main execution ---

# Simulated IoT sensor input (real source)
sensor_data = [
    {'zone': 'A1', 'readings': [23, 25, 22, 26, 24], 'confidence': 0.81, 'device': 'S1-A'},
    {'zone': 'B2', 'readings': [19, 18, 20, 21], 'confidence': 0.92, 'device': 'S2-B'},
    {'zone': 'A1', 'readings': [24, 23, 25], 'confidence': 0.76, 'device': 'S1-C'},
    {'zone': 'C3', 'readings': [31, 33, 30, 35, 32], 'confidence': 0.68, 'device': 'S3-A'},  # Below threshold
    {'zone': 'B2', 'readings': [17, 19, 20, 18, 21, 22], 'confidence': 0.85, 'device': 'S2-D'},
    {'zone': 'D4', 'readings': [40, 42], 'confidence': 0.95, 'device': 'S4-X'},
    {'zone': 'X99', 'readings': [999, -999], 'confidence': 0.10, 'device': 'TEST'}  # Junk data
]

# Irrelevant preprocessing steps
checksummed_devices = [d['device'] for d in sensor_data if d['device'].endswith('A')]
decoded_signal = decode_signal('48656c6c6f')  # 'Hello' in hex, unused

# Extract unique zones
all_zones = list({entry['zone'] for entry in sensor_data})

# Distractor: collect metrics that are never used
effective_metrics = collect_metrics(sensor_data)

# Another red herring: pattern analysis on zone chars
zone_chars = ''.join(z for z in all_zones)
pattern_score = analyze_pattern(zone_chars)  # Uses Counter

# Actual pipeline begins here
filtered_data = filter_anomalies(sensor_data, mode='strict')  # Only high-confidence entries

# Generate dynamic thresholds based on zones present
unique_filtered_zones = {entry['zone'] for entry in filtered_data}
threshold_map = generate_threshold_map(unique_filtered_zones)

# Remove decoy keys from threshold map
if 'calibration' in threshold_map:
    del threshold_map['calibration']
if 'override' in threshold_map:
    del threshold_map['override']

# Core computation occurs here
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")