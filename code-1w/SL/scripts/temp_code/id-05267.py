def collect_sensor_data():
    raw_sequences = [7, 2, 9, 4, 1, 8, 3, 6, 5]
    base_offset = 3
    adjusted = [x + base_offset for x in raw_sequences]
    return adjusted


def filter_outliers(data_stream, limit=10):
    filtered = [x for x in data_stream if x < limit]
    outlier_count = len(data_stream) - len(filtered)
    temp_result = sum(filtered) * 0.5  # distractor
    return filtered


def generate_checksum(items):
    checksum = 0
    for i, val in enumerate(items):
        checksum ^= (val << (i % 4))  # bit manipulation red herring
    return checksum % 100


def map_zones(readings):
    zone_bounds = { 'A': (5, 8), 'B': (9, 12), 'C': (13, 16) }
    distribution = { key: 0 for key in zone_bounds }
    
    for reading in readings:
        for zone, (low, high) in zone_bounds.items():
            if low <= reading <= high:
                distribution[zone] += 1
    
    zone_set = set(distribution.keys())
    expected_zones = {'A', 'B', 'C'}
    consistency_flag = zone_set == expected_zones
    
    # Distractor: complex but unused transformation
    normalized = []
    total = sum(distribution.values())
    if total > 0:
        for z in ['A','B','C']:
            normalized.append(distribution[z] / total * 100)
    
    return distribution


def compute_rolling_average(data, window=3):
    rolling = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        rolling.append(round(window_avg, 2))
    midpoint_value = rolling[len(rolling)//2] if rolling else 0
    return rolling


def build_hierarchy(zones, counts):
    # Irrelevant hierarchical construction
    hierarchy = {}
    for idx, (z, c) in enumerate(zip(zones, counts)):
        level = 'root' if idx == 0 else f'child_{idx}'
        hierarchy[level] = { 'zone': z, 'count': c, 'id': hash(z) % 1000 }
    return hierarchy


def integrate_metadata(primary, meta_overlay):
    # Fake integration logic with no real impact
    enhanced = primary.copy()
    for k, v in meta_overlay.items():
        enhanced[k] = { 'value': v, 'status': 'verified' }
    return enhanced


def validate_sequence(arr):
    if len(arr) < 5:
        return False
    sorted_copy = sorted(arr)
    gaps = [sorted_copy[i+1] - sorted_copy[i] for i in range(len(sorted_copy)-1)]
    gap_consistency = all(g == 1 for g in gaps)
    return gap_consistency


def analyze_readings(data, thresholds):
    # Core logic embedded within distractions
    segment_a = data[:4]
    segment_b = data[4:]
    
    sum_a = sum(segment_a)
    sum_b = sum(segment_b)
    
    diff_metric = abs(sum_a - sum_b)
    
    # Real computation path
    threshold_val = thresholds['critical']
    adjustment_factor = thresholds['scale']
    
    # Actual answer derivation
    base_score = diff_metric * adjustment_factor
    penalty = 0
    
    if sum_a > sum_b:
        penalty = 15
    else:
        penalty = 7
    
    final_score = base_score - penalty
    
    # Unused transformations (red herrings)
    inverted = [1.0/(x+1) for x in data]
    product_chain = 1
    for x in data:
        product_chain = (product_chain * x) % 1000
    
    return int(final_score)

# Main execution flow
sensor_output = collect_sensor_data()  # [10, 5, 12, 7, 4, 11, 6, 9, 8]
sanitized_readings = filter_outliers(sensor_output, limit=12)  # removes 12?
# Correction: limit=12 keeps values <12, so 12 is removed? No — 12 is not <12 → removed
# So sanitized: [10,5,7,4,11,6,9,8] → wait: original +3: [7+3=10, 2+3=5, 9+3=12→excluded, 4+3=7, 1+3=4, 8+3=11, 3+3=6, 6+3=9, 5+3=8]
# Thus: [10,5,7,4,11,6,9,8] → length 8

checksum_diagnostic = generate_checksum(sanitized_readings)  # irrelevant

zone_distribution = map_zones(sanitized_readings)
# Classify:
# A: 5-8 → 5,7,6,8 → count=4
# B: 9-12 → 10,11,9 → count=3
# C: 13-16 → none → 0
# So zone_distribution = {'A':4, 'B':3, 'C':0}

rolling_stats = compute_rolling_average(sanitized_readings)

is_valid = validate_sequence(sanitized_readings)  # sorted: [4,5,6,7,8,9,10,11] → gaps all 1 → True

zones_list = ['A', 'B', 'C']
counts_list = [zone_distribution[z] for z in zones_list]  # [4,3,0]

hierarchy_tree = build_hierarchy(zones_list, counts_list)

metadata_bundle = { 'calib': 0.98, 'source': 'primary' }
enhanced_data = integrate_metadata(zone_distribution, metadata_bundle)

# Threshold configuration — only this matters for final answer
threshold_map = {
    'critical': 18,
    'scale': 4  # used in analyze_readings
}

processed_data = sanitized_readings  # alias for clarity

# Key statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")