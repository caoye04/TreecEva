import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, 1.8, 4.5, 2.7, 5.1, 3.6, 2.9, 4.4, 3.8, 2.2]
noise_floor = 1.5
calibration_offset = 0.3

# Irrelevant auxiliary variables (distractors)
temp_buffer = [0] * len(raw_readings)
system_flags = {'active': True, 'debug': False, 'version': '2.1.5'}
checksum_history = []
redundant_sum = 0

# Signal preprocessing with slicing and filtering
cleaned_signal = [x for x in raw_readings if x > noise_floor]
shifted_data = [x + calibration_offset for x in cleaned_signal]
squared_envelope = [x**2 for x in shifted_data]

# Misleading intermediate computation (dead path)
event_count = 0
for val in squared_envelope:
    if val > 15:
        event_count += 1
        temp_buffer[0] = event_count  # Unused assignment

# Distractor: complex but unused transformation chain
transform_chain = lambda seq: list(map(math.sqrt, filter(lambda x: x > 4, seq)))
filtered_sqrt = transform_chain(squared_envelope)  # Computed but not used

# Real data path begins here
window_size = 3
processed_data = []
for i in range(len(shifted_data) - window_size + 1):
    window_avg = sum(shifted_data[i:i+window_size]) / window_size
    processed_data.append(round(window_avg, 3))

# Set-based anomaly detection (irrelevant but plausible)
unique_values = set(round(x, 1) for x in shifted_data)
anomaly_thresholds = {3.5, 4.8, 5.2}
detected_anomalies = unique_values & anomaly_thresholds  # Non-empty but unused

# Accumulation via dictionary aggregation (partially relevant)
bin_map = {}
for val in processed_data:
    key = int(val)
    bin_map[key] = bin_map.get(key, 0) + 1

# Decoy function that looks important
def compute_entropy(data):
    total = sum(data)
    probs = [x/total for x in data if x > 0]
    return -sum(p * math.log(p) for p in probs)

entropy_value = compute_entropy(list(bin_map.values()))  # Computed but irrelevant

# Actual diagnostic logic
status_codes = [100, 201, 100, 305, 100]
valid_codes = {100, 201, 305}

# Core reasoning: count valid codes, apply bitwise mask based on length
code_mask = len(valid_codes) << 2
active_diagnostics = sum(1 for c in status_codes if c in valid_codes)
masked_result = active_diagnostics ^ code_mask  # XOR operation

# Final integration with lambda and set operations
integrate_diagnostic = lambda x, y: x * 17 + len(y)

# Key statement
final_diagnostic = integrate_diagnostic(masked_result, detected_anomalies)

print(f"Result: {final_diagnostic}")