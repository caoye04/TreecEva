import math

# Simulated sensor data ingestion (realistic domain: environmental monitoring)
data_stream = [78, 65, 89, 92, 74, 88, 95, 63, 77, 82]

def clean_data(raw):
    # Irrelevant preprocessing step (distraction)
    cleaned = [x for x in raw if 50 <= x <= 100]
    normalization_factor = sum(cleaned) / len(cleaned)
    return [x / normalization_factor for x in cleaned]

calibration_offset = 1.02
offset_log = []
for i in range(5):
    offset_log.append(calibration_offset * (i + 1))  # Dead code path

# Actual relevant transformation chain
def transform_readings(data):
    squared = [x ** 2 for x in data]
    shifted = [x - 7000 for x in squared]  # Brings values into meaningful range
    return shifted

def generate_thresholds(count):
    # Complex but ultimately unused threshold generator (red herring)
    base = [math.sin(i * 0.5) * 100 for i in range(20)]
    filtered = list(filter(lambda x: x > 10, base))
    return {i: filtered[i % len(filtered)] for i in range(count)}

# Relevant mapping function
def create_lookup(keys):
    return {k: (k * 0.77 + 23) % 89 for k in keys}

transformed_data = transform_readings(clean_data(data_stream))

# Unused complex structure (distractor)
validation_matrix = [[i ^ j for j in range(8)] for i in range(8)]
hash_result = 0
for row in validation_matrix:
    for val in row:
        hash_result ^= val

# Key control structure with nested logic
status_flags = []
for val in transformed_data:
    if val > 100:
        status_flags.append('HIGH')
    elif val < -100:
        status_flags.append('LOW')
    else:
        status_flags.append('NORMAL')

# Decoy statistical analysis
mean_flag_length = sum([len(flag) for flag in status_flags]) / len(status_flags)
device_fingerprint = ''.join(sorted(set(''.join(status_flags))))

# Real threshold map used in final calculation
key_indices = [0, 2, 4, 6, 8]
threshold_map = create_lookup(key_indices)

# Irrelevant string manipulation (distractor)
log_header = "DIAG-REPORT-2024"
if log_header.startswith("DIAG"):
    parts = log_header.split('-')
    version_code = int(parts[-1])
    checksum = sum(ord(c) for c in log_header) % 100

# Core processing function with lambda and set operations
def process_metrics(metrics, thresholds):
    # Compute rolling min/max averages (relevant)
    window_sums = []
    for i in range(len(metrics) - 2):
        window_sums.append(sum(metrics[i:i+3]))
    
    avg_window = sum(window_sums) / len(window_sums)
    
    # Apply threshold corrections only at even indices (critical logic)
    corrected = []
    for idx, val in enumerate(metrics):
        if idx in thresholds:
            adjustment = thresholds[idx]
            adjusted_val = val * (1 + adjustment / 1000)
            corrected.append(adjusted_val)
        else:
            corrected.append(val)
    
    # Final aggregation using set-based filtering and lambda
    valid_set = set(range(0, len(corrected), 2))  # Only even positions
    filtered_values = [corrected[i] for i in range(len(corrected)) if i in valid_set]
    
    anomaly_detector = lambda x: abs(x) > 500
    anomalies = list(filter(anomaly_detector, filtered_values))
    
    # Critical computation path
    base_score = sum(filtered_values) / len(filtered_values)
    penalty = len(anomalies) * 18.6
    final_score = base_score - penalty
    
    # Secondary correction based on modular arithmetic
    mod_control = sum([i % 7 for i in key_indices])
    if mod_control % 3 == 0:
        final_score = final_score * 0.9
    
    return round(final_score, 6)

# Misleading diagnostic call (dead function)
def run_full_system_check():
    return hash(tuple(threshold_map.values())) % 1000

run_full_system_check()  # Called but result ignored

# --- KEY EXECUTION POINT ---
final_diagnostic = process_metrics(transformed_data, threshold_map)

# Output requirement
print(f"Target result: {final_diagnostic}")