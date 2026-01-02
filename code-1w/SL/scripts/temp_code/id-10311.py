from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def analyze_sensor_stream(raw_records, min_val, max_val):
    readings = [r['value'] for r in raw_records if 'value' in r]
    timestamps = [r['ts'] for r in raw_records if r.get('value', 0) > min_val]  # irrelevant extraction
    categories = defaultdict(int)
    for r in raw_records:
        if r.get('active'):
            categories[r['type']] += 1

    valid_readings = []
    for val in readings:
        if min_val < val < max_val:
            rounded = int(round(val / 2) * 2)  # round to nearest even
            valid_readings.append(rounded)

    # Dead code path - never used later
    outlier_count = sum(1 for v in readings if v <= min_val or v >= max_val)
    stats_snapshot = {
        'count': len(valid_readings),
        'sum': sum(valid_readings),
        'mode': max(Counter(valid_readings).values(), default=0)
    }

    return valid_readings

# Misleading auxiliary function that looks important but is unused
def compute_aggregate_score(data, weights=None):
    if not data:
        return -999
    weighted = [d * (weights[i % len(weights)] if weights else 1) for i, d in enumerate(data)]
    return sum(weighted) / len(weighted)

# Another decoy: complex bit analysis with no impact
def analyze_bit_pattern(number):
    binary_rep = bin(number)[2:]
    ones = binary_rep.count('1')
    zeros = binary_rep.count('0')
    alternations = sum(1 for i in range(len(binary_rep)-1) if binary_rep[i] != binary_rep[i+1])
    return (ones * 2) - zeros + (alternations // 3)

# Core logic buried among distractions
def filter_anomalies(dataset, criteria_map):
    result = []
    flags = criteria_map.get('flags', [])
    
    temp_store = []
    for item in dataset:
        if isinstance(item, dict) and 'status' in item:
            if item['status'] == 'OK':
                temp_store.append(item['reading'])
    
    # Actual filtering happens here, but obscured
    lower = criteria_map.get('low', 0)
    upper = criteria_map.get('high', float('inf'))
    for val in temp_store:
        if lower < val < upper:
            result.append(val)
    
    # Use string methods as distractor
    log_entry = "error,warning,info,debug"
    levels = log_entry.upper().split(',')
    threshold_mask = [len(level.strip()) for level in levels]  # unused list
    
    return result

# Real processing chain
def process_readings(data, limits):
    base = [x for x in data if x % 2 == 1]  # keep only odd numbers
    shifted = [x >> 1 for x in base]  # integer division by 2 via bit shift
    adjusted = [x + 5 for x in shifted if x > 2]  # transform and filter
    
    # Complex conditional expression - relevant
    scaled = [v * (1.5 if v < 10 else 0.8) for v in adjusted]
    
    # Final aggregation
    aggregate = 0
    for s in scaled:
        if s.is_integer():
            aggregate += int(s)
        else:
            aggregate += int(s * 2)  # double non-integral values and truncate
    
    return aggregate

# Irrelevant mathematical transformation
pi_approx = 3.14159
radius = 7
area_calc = int(pi_approx * (radius ** 2))  # red herring

# Unused statistical helper
def moving_average(seq, window=3):
    if len(seq) < window:
        return []
    return [sum(seq[i:i+window]) / window for i in range(len(seq)-window+1)]

# Simulated input data
sensor_logs = [
    {'value': 15.0, 'ts': 1001, 'type': 'temp', 'active': True},
    {'value': 8.0, 'ts': 1002, 'type': 'pressure', 'active': True},
    {'value': 23.0, 'ts': 1003, 'type': 'temp', 'active': True},
    {'value': 5.0, 'ts': 1004, 'type': 'flow', 'active': False},
    {'value': 12.0, 'ts': 1005, 'type': 'temp', 'active': True}
]

category_specs = {
    'flags': ['A', 'B'],
    'low': 6,
    'high': 20
}

# Execution flow with distractions
extracted = analyze_sensor_stream(sensor_logs, 5, 25)

# Fake dependency
weight_profile = [0.5, 1.0, 1.5]
score = compute_aggregate_score(extracted, weight_profile)  # unused

# Real data pipeline starts here
raw_input = [{'reading': x, 'status': 'OK'} for x in extracted]
filtered_data = filter_anomalies(raw_input, category_specs)

# Critical thresholds
threshold_levels = {
    'min_req': 1,
    'critical': 18
}

# Key statement
final_diagnostic = process_readings(filtered_data, threshold_levels)

# Print required output
print(f"Result: {final_diagnostic}")