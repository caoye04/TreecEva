import itertools

# Simulated sensor grid data from environmental monitoring array
data_stream = [14, 7, 23, 5, 16, 31, 8, 11, 19, 27, 3, 13, 9, 22, 30]

# Irrelevant calibration constants (distractor variables)
calib_a = 0.87
calib_b = 1.03
global_offset = 4.5
baseline_shift = -2.1

# Realtime thresholds for anomaly detection
thresholds = {'minor': 10, 'moderate': 20, 'severe': 25}

# Legacy system flags (dead code path)
legacy_mode_enabled = False
if legacy_mode_enabled:
    fallback_buffer = [0] * 15
    for i in range(len(fallback_buffer)):
        fallback_buffer[i] = data_stream[i] % 7

# Data normalization using moving window average (relevant preprocessing)
normalized = []
for i in range(2, len(data_stream)):
    window_avg = (data_stream[i-2] + data_stream[i-1] + data_stream[i]) / 3
    normalized.append(round(window_avg))

# Apply threshold filter to detect high-risk readings (core logic step 1)
high_risk = [x for x in normalized if x > thresholds['moderate']]

# Bit manipulation for error checking (relevant but indirect)
error_flags = 0
for val in data_stream:
    error_flags ^= val  # XOR accumulation for checksum
    error_flags &= 0xFF  # Keep within byte range

# Decoy statistical analysis (irrelevant computation)
mean_val = sum(data_stream) / len(data_stream)
variance = sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)
std_dev = variance ** 0.5
outliers = [x for x in data_stream if abs(x - mean_val) > 2 * std_dev]

# Construct diagnostic map using dictionary operations (core logic step 2)
diag_map = {}
for idx, reading in enumerate(high_risk):
    category = 'critical' if reading >= thresholds['severe'] else 'moderate'
    diag_map[f'pos_{idx}'] = {
        'value': reading,
        'category': category,
        'checksum': (reading ^ error_flags) & 0xF
    }

# Simulate hardware register state (distractor structure)
register_bank = [
    {'addr': 0x10, 'val': 255, 'locked': True},
    {'addr': 0x11, 'val': 180, 'locked': False},
    {'addr': 0x12, 'val': 95, 'locked': True}
]

# Complex filtering with set operations and itertools (core logic step 3)
unique_high = list(set(high_risk))
sorted_combinations = list(itertools.combinations(sorted(unique_high), 2))
valid_pairs = [pair for pair in sorted_combinations if (pair[0] + pair[1]) % 7 == 0]

# Secondary filter based on pair sum divisibility (core logic step 4)
evaluated_sums = [sum(pair) for pair in valid_pairs]
filtered_data = [s for s in evaluated_sums if s > 35]

# Threshold mapping with redundant reassignment (core logic step 5)
threshold_map = {
    'alert_level': max(filtered_data) // 10 if filtered_data else 1,
    'recovery_time': 0,
    'retry_limit': 3
}
threshold_map['recovery_time'] = len(filtered_data) * 2

# Function to process final diagnostics (core logic step 6)
def process_readings(readings_list, config_map):
    if not readings_list:
        return -1
    
    # Multi-step transformation
    base_score = sum(readings_list)
    modifier = config_map['alert_level']
    
    # Integer division and rounding sequence
    raw_result = base_score // modifier
    adjusted = round(raw_result * 0.85)
    
    # Additional bit shifting for final encoding
    encoded = (adjusted << 1) | (modifier & 0x1)
    
    # Red herring: unused branch
    if base_score < 0:
        for i in range(5):
            encoded += (i * 3) % 7
    
    return encoded

# Dead function - never called (decoy)
def legacy_diagnostic(seq):
    result = 0
    for x in seq:
        result = (result * 31 + x) % 10007
    return result

# Final computation (key statement)
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result for evaluation
print(f"Result: {final_diagnostic}")