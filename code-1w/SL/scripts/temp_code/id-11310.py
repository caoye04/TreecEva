import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_samples = [127, 255, 192, 64, 96, 160]
    processed = []
    for val in raw_samples:
        if val > 128:
            processed.append(val >> 2)
        elif val > 64:
            processed.append(val ^ 42)
        else:
            processed.append(val + 10)
    return processed

# Irrelevant auxiliary function – distractor
def compute_checksum(data):
    checksum = 0
    for item in data:
        checksum = (checksum ^ item) * 113 % 1009
    return checksum

# Data transformation with bit manipulation and filtering
def transform_signal(seq):
    shifted = [x << 1 for x in seq]
    filtered = [y for y in shifted if y & 1 == 0 and y % 3 != 0]
    inverted = [255 - z for z in filtered[:5]]
    return inverted

# Set-based anomaly detection – relevant
valid_range = set(range(100, 200))
error_codes = {1001, 2002, 3003}  # Distractor set

# Core pattern analyzer
def detect_anomalies(values, ref_set):
    anomalies = []
    for v in values:
        if v not in ref_set:
            anomalies.append(v)
    return set(anomalies)

# Secondary transformation – creates decoy intermediate result
def misleading_normalization(arr):
    total = sum(arr)
    norm_arr = [(x / total) * 100 for x in arr]
    return [round(n, 2) for n in norm_arr]  # Dead-end computation

# Main analysis function
threshold_set = {x for x in range(50, 150) if x % 7 == 0}  # Used later

# Complex multi-step pipeline
raw_data = collect_readings()
transformed_signal = transform_signal(raw_data)

# Decoy operations with string manipulation (irrelevant)
class_id = "SYS_DIAG_42"
diag_token = ''.join([c for c in class_id if c.isdigit()])
diag_code = int(diag_token) if diag_token else 0

# More distraction: tuple unpacking with unused variables
config_meta = ("voltage", "current", "resistance")
metric_type, _, _ = config_meta

# Additional irrelevant arithmetic chain
scaling_factor = 1.75
offset_adjustment = (scaling_factor * 8) - 6.2
interim_result = int(offset_adjustment ** 2)

# Real computation path begins
expanded_data = transformed_signal + [x | 15 for x in transformed_signal[-3:]]

# Filtering through set operations
common_flags = set(expanded_data) & threshold_set

# Another red herring: recursive function that is called but doesn't affect final result
def recursive_noise(level, seed):
    if level <= 1:
        return seed
    return recursive_noise(level - 1, seed ^ level) + seed

noise_trace = recursive_noise(5, 10)

# Actual core logic: analyze deviations using boolean and set logic
def analyze_pattern(data, limit_set):
    base_eval = [math.sqrt(d) if d > 0 else 0 for d in data]
    rounded_vals = [int(round(b)) for b in base_eval]
    
    # Key step: count how many fall outside threshold set
    outside_count = 0
    for rv in rounded_vals:
        if rv not in limit_set:
            outside_count += 1
    
    # Final computation: combine count with bit metric
    bit_sum = sum(1 for d in data if d & (d - 1) == 0 and d != 0)  # Count powers of two
    return outside_count * bit_sum + len(common_flags)

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, threshold_set)
print(f"Result: {final_diagnostic}")