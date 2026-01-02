def analyze_pattern(sequence):
    """Irrelevant helper function for pattern detection (dead code path)"""
    return [i for i, x in enumerate(sequence) if x % 3 == 0]

# Sensor simulation constants (some irrelevant)
BASE_OFFSET = 17
CALIBRATION_FACTOR = 0.89
NOISE_THRESHOLD = 4.5
TEMPORAL_WINDOW = 128
REDUNDANT_SCALE = 2.71828  # Unused constant (distractor)

# Real data structures
sensor_data = [
    43, 21, 56, 12, 78, 33, 67, 14, 81, 92,  
    19, 44, 53, 62, 77, 38, 85, 91, 16, 73
]

calibration_matrix = [
    [1, 0, -1],
    [2, 1,  0],
    [0, -1, 1]
]

# Decoy transformation (not used in final computation)
def transform_legacy(data):
    shifted = [x - BASE_OFFSET for x in data]
    wrapped = [(x % 25) + 10 for x in shifted]
    return [wrapped[i] * (i % 4 + 1) for i in range(len(wrapped))]

# Auxiliary diagnostic (misleading intermediate result)
preliminary_score = sum(x ** 0.5 for x in sensor_data if x > 30) // 1

# Bit manipulation red herring
bit_flags = 0
for i, val in enumerate(sensor_data):
    if val % 7 == 0:
        bit_flags |= (1 << (i % 8))

# Unused recursive counting (dead code path)
def count_transitions(arr, idx=0, acc=0):
    if idx >= len(arr) - 1:
        return acc
    diff = abs(arr[idx] - arr[idx + 1])
    return count_transitions(arr, idx + 1, acc + (1 if diff > 10 else 0))

transition_count = count_transitions(sensor_data)  # Computed but unused

# Core processing function
def apply_calibration(readings, matrix):
    result = []
    size = len(matrix)
    for i in range(0, len(readings) - size + 1, size - 1):
        chunk = readings[i:i+size]
        if len(chunk) == size:
            calibrated = 0
            for j, val in enumerate(chunk):
                calibrated += val * matrix[j][j]  # Diagonal only
            result.append(calibrated)
    return result

# Secondary filter with zip and enumerate (partially relevant)
def filter_anomalies(data_list):
    filtered = []
    for idx, val in enumerate(data_list):
        context = data_list[max(0, idx-1):idx+2]
        avg = sum(context) / len(context)
        if abs(val - avg) <= NOISE_THRESHOLD * 1.5:
            filtered.append(val)
        else:
            filtered.append(avg)  # Smooth anomalies
    return filtered

# Main processing pipeline
def process_readings(sensors, calib):
    # Step 1: Apply diagonal-only calibration matrix
    calibrated = apply_calibration(sensors, calib)
    
    # Step 2: Misleading intermediate aggregation
    dummy_aggregate = 0
    for a, b in zip(calibrated, reversed(calibrated)):
        dummy_aggregate += a ^ b  # Bitwise XOR (irrelevant)
    
    # Step 3: Use enumerate to adjust based on index parity
    indexed_adjust = []
    for i, v in enumerate(calibrated):
        shift = -1 if i % 2 == 0 else 1
        indexed_adjust.append(v + shift * (i + 1))
    
    # Step 4: Filter using sliding context
    cleaned = filter_anomalies(indexed_adjust)
    
    # Step 5: Final checksum-like reduction
    total = 0
    multiplier = 1
    for item in cleaned:
        total += item * multiplier
        multiplier = (multiplier * 2) % 9  # Modular cycling
    
    # Step 6: Final adjustment (answer depends on this)
    final_value = int(total % 10000) - 5000
    return final_value

# Execution point of interest
final_diagnostic = process_readings(sensor_data, calibration_matrix)
print(f"Target result: {final_diagnostic}")