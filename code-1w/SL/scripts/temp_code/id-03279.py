def analyze_pattern(seq):
    """Irrelevant helper function for pattern analysis (dead code path)."""
    if len(seq) < 2:
        return False
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

# Misleading sensor calibration constants (distractors)
CALIBRATION_OFFSET = 0.789
TEMPORAL_FACTOR = 1.045
BASELINE_DRIFT = -0.211
MAX_SENSITIVITY = 9.87
MIN_RESOLUTION = 0.003

# Real and fake data structures
sensor_names = ['alpha', 'beta', 'gamma', 'delta']
sensor_ids = [101, 102, 103, 104]

# Actual sensor readings (core data)
sensor_data = [12, 8, 15, 6]
thresholds = [10, 9, 14, 7]

# Irrelevant transformation chain (red herring)
encoded_data = []
for idx, val in enumerate(sensor_data):
    shifted = val << 1
    masked = shifted & 0xFF
    normalized = masked / 255.0
    encoded_data.append(round(normalized * 100, 2))

# Unused intermediate calculations (misleading)
avg_encoded = sum(encoded_data) / len(encoded_data)
adjusted_offsets = [CALIBRATION_OFFSET * x for x in encoded_data]
drift_corrected = [x + BASELINE_DRIFT for x in adjusted_offsets]

# Dummy state tracker (decoy)
current_state = {
    'active': True,
    'mode': 'diagnostic',
    'version': '2.1.0',
    'checksum': 0xDEADBEEF
}

# Simulated time-series expansion (irrelevant recursion)
def expand_series(arr, depth):
    if depth <= 0 or len(arr) >= 16:
        return arr
    return expand_series(arr + [arr[-1] + 1], depth - 1)

expanded = expand_series([1], 3)

# Core logic disguised among noise
status_flags = []
for i, (reading, limit) in enumerate(zip(sensor_data, thresholds)):
    # Key conditional logic embedded in loop
    if reading > limit:
        status_flags.append(2)
    elif reading == limit:
        status_flags.append(1)
    else:
        status_flags.append(0)

# Bit manipulation red herring
packed_flags = 0
for bit in status_flags:
    packed_flags = (packed_flags << 2) | bit

# Another decoy function
def validate_checksum(data):
    return sum(data) % 16 == 0

# Critical processing function
def process_readings(readings, limits):
    total_exceedance = 0
    penalty_factor = 1.5
    bonus_credit = 0.8
    
    # Main computation with nested conditions
    for val, thresh in zip(readings, limits):
        diff = val - thresh
        if diff > 0:
            total_exceedance += diff * penalty_factor
        elif diff == 0:
            total_exceedance += bonus_credit
        else:
            total_exceedance -= abs(diff) * 0.2
    
    # Non-linear adjustment
    if total_exceedance > 10:
        total_exceedance *= 0.9
    elif total_exceedance < 0:
        total_exceedance = abs(total_exceedance) * 1.1
    
    # Final clamping
    return int(total_exceedance + 0.5)

# Execution point of interest
final_diagnostic = process_readings(sensor_data, thresholds)

# Print required output
print(f"Result: {final_diagnostic}")