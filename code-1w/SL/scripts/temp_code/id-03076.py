from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant readings
def collect_sensor_data():
    raw_readings = [
        (100, 'temp'), (105, 'temp'), (200, 'pressure'), (203, 'pressure'),
        (102, 'temp'), (198, 'pressure'), (300, 'flow'), (301, 'flow'),
        (101, 'temp'), (202, 'pressure'), (302, 'flow'), (400, 'level'),
        (401, 'level'), (103, 'temp'), (201, 'pressure')
    ]
    return raw_readings

def filter_anomalies(readings):
    # Group by type
    grouped = defaultdict(list)
    for val, typ in readings:
        grouped[typ].append(val)
    
    # Apply basic outlier rejection using median
    filtered = []
    for typ, vals in grouped.items():
        sorted_vals = sorted(vals)
        mid = len(sorted_vals) // 2
        median = sorted_vals[mid]
        # Accept values within ±5% of median
        for val in vals:
            if abs(val - median) / median <= 0.05:
                filtered.append((val, typ))
    
    return filtered

def compute_baseline_stats(data):
    # Irrelevant function: computes stats not used in final logic
    counts = Counter(typ for _, typ in data)
    averages = {typ: sum(v for v, t in data if t == typ) / counts[typ] for typ in counts}
    return averages  # Unused in main flow
def generate_threshold_map(types):
    # Real thresholds used in processing
    base_map = {t: {'min': 0.9 * ord(t[0]), 'max': 1.1 * ord(t[0])} for t in types}
    # Add decoy entries
    base_map['temp']['safe_range'] = (95, 105)
    base_map['temp']['calibration'] = [1.0, 0.99, 1.01]
    base_map['temp']['version'] = '2.1'
    return base_map
def analyze_trend(sequence):
    # Unused distraction: trend analysis not used
    if len(sequence) < 3:
        return 'stable'
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return 'increasing' if sum(diffs) > 0 else 'decreasing'
def process_readings(data, thresholds):
    # Extract values per type
    values_by_type = defaultdict(list)
    for val, typ in data:
        values_by_type[typ].append(val)
    
    # Compute aggregate score per type using complex logic
    diagnostics = {}
    for typ, vals in values_by_type.items():
        avg = sum(vals) / len(vals)
        expected_center = ord(typ[0])
        deviation_score = abs(avg - expected_center)
        
        # Use threshold bounds
        min_bound = thresholds[typ]['min']
        max_bound = thresholds[typ]['max']
        
        if min_bound <= avg <= max_bound:
            health = 1.0
        else:
            excess = max(avg - max_bound, min_bound - avg, 0)
            health = max(0, 1 - (excess / expected_center))
        
        # Apply non-linear weighting
        weighted_health = health ** 2 * (1 + 0.1 * len(vals))
        diagnostics[typ] = round(weighted_health, 6)
    
    # Composite diagnostic using bit manipulation for obscurity
    total_bits = 0
    for d in diagnostics.values():
        shifted = int(d * 1000000) & 0xFFFF
        total_bits ^= shifted << 1
        total_bits |= len(diagnostics)  # Redundant bit setting
    
    # Final result derived from XOR pattern
    final_diagnostic = sum(diagnostics.values()) * (total_bits & 0xFF)
    
    # Dead code path: never reached due to logic above
    if False and 'debug' in diagnostics:
        final_diagnostic *= 0.5
    
    return final_diagnostic

# Main execution with distractions
timestamp_log = [1680000000 + i*60 for i in range(20)]  # Unused time tracking
system_status = {'active_sensors': 4, 'version': 'X', 'mode': 'diagnostic'}

# Real pipeline
all_readings = collect_sensor_data()
filtered_data = filter_anomalies(all_readings)

# Irrelevant intermediate computations
baseline_stats = compute_baseline_stats(filtered_data)  # Computed but unused
size_distribution = [len(grouped_list) for grouped_list in [
    [v for v, t in filtered_data if t == 'temp'],
    [v for v, t in filtered_data if t == 'pressure'],
    [v for v, t in filtered_data if t == 'flow'],
    [v for v, t in filtered_data if t == 'level']
]]
sorted_sizes = sorted(size_distribution, reverse=True)
decoyness = sum(1 for x in sorted_sizes if x > 2) * 17  # Unused metric

# Generate actual threshold map
involved_types = ['temp', 'pressure', 'flow', 'level']
threshold_map = generate_threshold_map(involved_types)

# Key computation
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")