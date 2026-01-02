import math

# Simulated sensor data and noise filtering system
def collect_sensor_data():
    raw_data = [3, 5, 8, 13, 21, 34, 55, 89, 144]
    noise_floor = 7
    adjusted = [x - noise_floor for x in raw_data if x > noise_floor]
    return adjusted

# Irrelevant auxiliary function (distractor)
def compute_checksum(data):
    checksum = 0
    for item in data:
        if item % 2 == 0:
            checksum ^= item << 2
        else:
            checksum += item >> 1
    return checksum * 3 % 100

# Signal transformation with red herring logic
def transform_signal(signal_stream):
    transformed = []
    temp_offset = 0
    for i, val in enumerate(signal_stream):
        if i % 3 == 0:
            temp_offset = int(math.sin(i + 1) * 5)
        # Complex but partially irrelevant transformation
        modified = val * 2 + int(math.log(val + 1, 2))
        modified -= temp_offset
        transformed.append(modified)
    return transformed

# Misleading pre-processing step (dead path)
def analyze_pattern(seq):
    if len(seq) < 10:
        return sum(x ** 0.5 for x in seq if x % 2 == 1)
    else:
        return 0

# Core processing function with critical logic buried
def filter_anomalies(data):
    anomalies = []
    clean = []
    for x in data:
        if x < 0:
            anomalies.append(x)
        elif x % 7 == 0 and x > 50:  # Rare condition (red herring)
            anomalies.append(x * 2)
        else:
            clean.append(x)
    return clean, anomalies

# Decoy function that looks important but isn't used in main flow
def compress_data(arr):
    result = []
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            result.append((arr[i] + arr[i+1]) // 1.5)
        else:
            result.append(arr[i] * 0.75)
    return result

# Main signal processor - key computation embedded
def process_signals(data, limit):
    magnitude_sum = 0
    adjustment_factor = 1.0
    
    # Simulate multi-stage processing
    for value in data:
        if value > limit:
            magnitude_sum += int(value ** 0.5)
        else:
            magnitude_sum += value // 2
    
    # Secondary correction pass (looks complex, limited impact)
    temp_series = [magnitude_sum // (i + 1) for i in range(1, 4)]
    adjustment_factor = sum(temp_series) / 100.0
    
    # Final non-linear scaling - this is where answer is formed
    final_scale = int((magnitude_sum * adjustment_factor) + 37)
    
    # Dead code branch (never reached due to prior logic)
    if len(data) > 100:
        backup = 0
        for x in data:
            backup += x % 11
        final_scale = backup
    
    return final_scale

# Unused utility (distractor)
def generate_metadata():
    metadata = {
        'version': '2.1',
        'nodes': 8,
        'active': True,
        'flags': [0b1010, 0b1100, 0b0011]
    }
    return metadata

# Orchestrator with misleading complexity
sensor_input = collect_sensor_data()
checksum_val = compute_checksum(sensor_input)  # Computed but unused

transformed_input = transform_signal(sensor_input)
pattern_score = analyze_pattern(transformed_input)  # Dead-end analysis

filtered_data, flagged = filter_anomalies(transformed_input)

# This compression is never applied (distractor)
if len(filtered_data) > 10:
    compressed = compress_data(filtered_data)

threshold = 15
final_output = process_signals(filtered_data, threshold)

# Extraneous print statements (simulating debug noise)
# print(f'Debug: Checksum={checksum_val}')
# print(f'Pattern score: {pattern_score}')
# print(f'Flagged anomalies: {len(flagged)}')

print(f'Result: {final_output}')