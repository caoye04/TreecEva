import math

# Simulated sensor array data (real measurements)
sensor_readings = [104, 95, 112, 88, 97, 123, 109, 92]

timestamps = [1634567800, 1634567860, 1634567920, 1634567980, 1634568040, 1634568100, 1634568160, 1634568220]

# Irrelevant metadata (distractor)
device_info = {
    'model': 'X250',
    'location': 'Sector 7G',
    'firmware': 'v2.1.9',
    'serial': 'SN7890-XZ'
}

# Calibration coefficients (partially relevant, but some are red herrings)
calibration_map = {
    'gain': 1.03,
    'offset': -4.2,
    'noise_floor': 85,
    'saturation_limit': 120,
    'temp_comp': 0.15  # unused in final calculation
}

# Signal processing pipeline
processed_data = []
for i, reading in enumerate(sensor_readings):
    adjusted = (reading + calibration_map['offset']) * calibration_map['gain']
    if adjusted > calibration_map['saturation_limit']:
        adjusted = calibration_map['saturation_limit']
    processed_data.append(round(adjusted))

# Decoy function - looks important but unused (dead code path)
def legacy_process(data):
    result = 0
    for x in data:
        result += x ** 0.5 * 2.1
    return int(result % 100)

# Another decoy: complex transformation not used later
decoy_transform = set()
for idx, val in enumerate(processed_data):
    if idx % 2 == 0:
        decoy_transform.add(val // 3)
    else:
        decoy_transform.discard(val // 3) if (val // 3) in decoy_transform else None

# Threshold analysis setup (key logic begins here)
thresh_high = 105
thresh_low = 95
emergency_threshold = 115

thresholds = {
    'normal': (thresh_low, thresh_high),
    'warning': (thresh_high, emergency_threshold),
    'critical': (emergency_threshold, float('inf'))
}

# Character frequency map from device ID (irrelevant distractor)
device_id = "X250_Sector7G"
char_freq = {}
for c in device_id:
    char_freq[c] = char_freq.get(c, 0) + 1

# Core diagnostic engine
status_counter = {'normal': 0, 'warning': 0, 'critical': 0}
peak_magnitude = 0

for value in processed_data:
    if value > peak_magnitude:
        peak_magnitude = value

    if value < thresholds['normal'][1]:
        status_counter['normal'] += 1
    elif value < thresholds['warning'][1]:
        status_counter['warning'] += 1
    else:
        status_counter['critical'] += 1

# Secondary analysis with zip (required feature)
consecutive_pairs = []
for curr, next_val in zip(processed_data, processed_data[1:]):
    consecutive_pairs.append(abs(next_val - curr))

avg_fluctuation = sum(consecutive_pairs) / len(consecutive_pairs) if consecutive_pairs else 0

# Tertiary signal assessment
complexity_score = 0
for i, (idx, val) in enumerate(enumerate(processed_data)):
    complexity_score += (i + 1) * (val % 7)  # arbitrary weighting

# Final decision logic
primary_weight = status_counter['critical'] * 10
secondary_weight = math.floor(avg_fluctuation)

dynamic_factor = 1
if peak_magnitude >= emergency_threshold:
    dynamic_factor = 2
elif avg_fluctuation > 12.0:
    dynamic_factor = 1.5

# Misleading intermediate (looks like final answer but isn't)
preliminary_diag = (primary_weight + secondary_weight) * dynamic_factor

# Actual key computation
baseline = 50
risk_adjustment = (status_counter['warning'] * 3) + (status_counter['critical'] * 8)
volatility_penalty = int(avg_fluctuation // 2)

# Final diagnostic score calculation
final_diagnostic = baseline + risk_adjustment - volatility_penalty

# Irrelevant cleanup (distractor)
unused_list = [x for x in range(5) if x > 10]
placeholder_dict = {k: v for k, v in zip(['a','b'], [1,2])}

# Critical output (must print exactly this format)
Result: final_diagnostic