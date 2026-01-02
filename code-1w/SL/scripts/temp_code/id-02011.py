import itertools

# Sensor array simulation with noise and calibration logic
def collect_sensor_data():
    raw_readings = [18, 22, 25, 14, 30, 28, 17, 21, 19, 24]
    noise_offset = [i % 3 for i in range(len(raw_readings))]
    return [raw_readings[i] + noise_offset[i] for i in range(len(raw_readings))]

def apply_mask(data, mask_type='high'):
    if mask_type == 'high':
        return [x for x in data if x > 20]
    else:
        return [x for x in data if x <= 20]

# Irrelevant helper: simulates unused diagnostic path
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just looks plausible
    return round(entropy, 4)

# Real processing function with distractors
def process_readings(data, factor):
    # Step 1: Normalize using factor
    normalized = [round(x * factor, 2) for x in data]
    
    # Distractor: Unused transformation branch
    if len(normalized) > 100:
        inverted = [1000 / x for x in normalized]
        smoothed = list(itertools.accumulate(inverted, lambda a, b: (a + b) / 2))
    
    # Step 2: Categorize readings
    categories = {}
    for val in normalized:
        key = int(val // 10)
        if key not in categories:
            categories[key] = []
        categories[key].append(val)
    
    # Step 3: Compute weighted diagnostic index
    weights = {k: len(v) * k for k, v in categories.items()}
    total_weight = sum(weights.values())
    
    # Distractor: Dead code path based on impossible condition
    if False and 'debug' in categories:
        backup_mode = True
        temp_cache = set()
        for item in categories['debug']:
            temp_cache.add(item * 2)

    # Step 4: Aggregate diagnostic score
    diagnostic_sum = 0
    for k, w in weights.items():
        diagnostic_sum += k * w
    
    # Final adjustment using modular arithmetic
    adjusted_diagnostic = diagnostic_sum % 97763
    
    # Distractor: Unused data structure transformations
    decoy_pairs = list(itertools.combinations(normalized[:5], 2))
    decoy_sums = {pair: sum(pair) for pair in decoy_pairs}
    filtered_decoy = {k: v for k, v in decoy_sums.items() if v > 40}
    
    # Real result computation
    final_value = adjusted_diagnostic + 100
    return final_value

# Secondary irrelevant function: simulates system health check
def evaluate_stability(metrics):
    if not metrics:
        return 'N/A'
    avg = sum(metrics) / len(metrics)
    threshold_map = {'low': 15, 'med': 25, 'high': 35}
    status = 'stable'
    for th in threshold_map.values():
        if avg > th:
            status = 'overwatch'
    return status

# Main execution flow
sensor_data = collect_sensor_data()

# Distractor: multiple assignments with partial usage
clean_data, auxiliary_log = sensor_data.copy(), []
log_entry = f"Raw collection size: {len(clean_data)}"
auxiliary_log.append(log_entry)

# Filter data using irrelevant branching
if len(clean_data) % 2 == 0:
    filtered_data = apply_mask(clean_data, 'high')
else:
    filtered_data = apply_mask(clean_data, 'low')

# More red herrings: unused statistical analysis
duplicates_check = set()
duplicate_count = 0
for item in sensor_data:
    if item in duplicates_check:
        duplicate_count += 1
    else:
        duplicates_check.add(item)

# Calibration logic with misleading constants
calibration_baseline = 2.718
adjustment_ratio = 0.85
version_code = 'CAL-ALPHA'

calibration_factor = (calibration_baseline * adjustment_ratio) / 2.0  # Actual factor used

# Irrelevant sorting operation on decoy data
sorted_aux = sorted([x * 2 for x in auxiliary_log.__str__().split() if x.isdigit()], reverse=True)

# Key statement - target of evaluation
calibration_factor = round(calibration_factor, 2)
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Additional distraction: unused dictionary aggregation
diagnostic_report = {
    'readings_count': len(filtered_data),
    'calibration_used': calibration_factor,
    'diagnostic_code': 97763,
    'system_hash': sum([ord(c) for c in version_code]) % 1000
}

# Output the true answer
print(f"Result: {final_diagnostic}")