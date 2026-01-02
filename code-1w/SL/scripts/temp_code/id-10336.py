def sensor_calibrate(raw):
    return sum([x * 1.05 for x in raw if x > 0])

# Irrelevant helper function (dead code path)
def encrypt_signal(data):
    return ''.join([chr((ord(c) + 3) % 256) for c in str(data)])

# Another decoy transformation
def transform_coordinates(coord_list):
    return [(c[0] * 0.9, c[1] * 1.1) for c in coord_list]

# Unused constant
MAX_BUFFER_SIZE = 512

# Simulated sensor readings (with noise and irrelevant entries)
sensor_log = [
    [10, -1, 15, 20, 0],
    [8, 12, -5, 25],
    [18, 0, 14, -3, 7],
    [22, 11, 9]
]

# Decoy data structure
tower_metadata = {
    'id': 'T4X9',
    'location': 'N47.23E',
    'active': True,
    'version': '2.1.0'
}

# Distractor: fake checksum calculation (never used)
current_checksum = 0
for item in tower_metadata.values():
    if isinstance(item, str):
        current_checksum ^= sum([ord(c) for c in item])

# Real processing begins here
filtered_readings = []
for entry in sensor_log:
    cleaned = [x for x in entry if x >= 0]  # Remove negative noise
    if len(cleaned) > 0:
        avg = sum(cleaned) / len(cleaned)
        filtered_readings.append(avg)

# Apply calibration
calibrated = sensor_calibrate(filtered_readings)

# Introduce string-based distraction
status_flag = 'NORMAL'
diagnostic_code = 'OK-200'

# Case conversion red herring
status_normalized = status_flag.lower().replace('r', 'R').title()

diagnostic_tokens = diagnostic_code.split('-')
diagnostic_tokens.reverse()

token_sum = 0
for token in diagnostic_tokens:
    if token.isnumeric():
        token_sum += int(token)
    else:
        # String method misuse as distraction
        token_sum += len(token.encode('utf-8'))

# Begin actual analysis chain
baseline = 15.5
variance_pool = []

for val in calibrated:
    variance_pool.append((val - baseline) ** 2)

# Compute RMS (root mean square) deviation
rms_deviation = (sum(variance_pool) / len(variance_pool)) ** 0.5

# Data transformation with tuple unpacking distraction
snapshot = (rms_deviation, len(calibrated), token_sum)
metric_a, metric_b, _ = snapshot  # third value ignored

# Conditional logic with misleading branch
data_quality = 'high'
if metric_b < 3:
    adjustment_factor = 0.8
else:
    adjustment_factor = 1.05  # This branch is taken

# Real computation path
adjusted_rms = metric_a * adjustment_factor

# Simulate threshold crossings
threshold_events = 0
running_total = 0.0
for reading in calibrated:
    running_total += reading
    if reading > (baseline * 1.2):
        threshold_events += 1

# Weighted diagnostic score
weight_a = 0.6
weight_b = 0.4

# Final diagnostic depends only on these two values
primary_score = running_total / len(calibrated)
secondary_score = threshold_events * 100

# The real answer derivation
final_diagnostic = int(primary_score + secondary_score)

# Output requirement
print(f"Result: {final_diagnostic}")