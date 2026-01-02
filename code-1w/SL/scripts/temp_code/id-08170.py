import math

def analyze_signal_strength(signal):
    # Irrelevant helper function (dead code path)
    return sum([x ** 0.5 for x in signal if x > 10])

def dummy_transform(data):
    # Distractor function with no real impact
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val * 1.5 + 2)
        else:
            transformed.append(val // 3)
    return transformed

def compute_checksum(sequence):
    # Bitwise manipulation red herring
    checksum = 0
    for num in sequence:
        checksum ^= int(num * 3) & 255
    return checksum

def extract_features(records):
    # Unused feature extraction (misleading intermediate)
    features = []
    for idx, entry in enumerate(records):
        if idx < len(records) // 2:
            features.append(math.log(abs(entry) + 1) * idx)
        else:
            features.append(entry ** 0.3)
    return features

def validate_integrity(trace):
    # Decoy validation logic
    total = sum(abs(x) for x in trace)
    threshold = 1000 * (len(trace) / 5)
    return total < threshold

def preprocess_input(raw):
    # Real preprocessing used later
    cleaned = [x for x in raw if isinstance(x, (int, float)) and x >= 0]
    normalized = [x / 100.0 for x in cleaned]
    return normalized

def generate_basis(n):
    # Generates calibration matrix (actually used)
    basis = []
    for i in range(n):
        row = []
        for j in range(n):
            value = (i + 1) ** ((j % 3) + 1)
            row.append(value)
        basis.append(row)
    return basis

def decode_sequence(stream):
    # Another distractor using string methods
    stream_str = ''.join(map(str, [int(x) for x in stream[:5]]))
    parts = stream_str.split('1')
    joined = 'X'.join([p.zfill(3) for p in parts])
    return int(joined[-6:]) if len(joined) >= 6 else 0

def process_readings(data, matrix):
    # Core logic hidden among distractions
    filtered = [x for x in data if x * 100 % 2 == 0]  # Only even scaled values
    temp_state = []
    
    # Matrix-weighted transformation
    weights = matrix[2]  # Use third row of matrix
    for i, reading in enumerate(filtered):
        index = i % len(weights)
        adjusted = reading * weights[index]
        temp_state.append(round(adjusted, 4))
    
    # Critical computation: sum with offset
    base_sum = sum(temp_state)
    
    # Apply non-linear correction factor
    correction_factor = math.sin(len(temp_state) * math.pi / 6)
    corrected = base_sum * (1 + correction_factor)
    
    # Final diagnostic depends on this
    final_diagnostic = int(corrected * 100)  # Scale up for precision
    
    # Red herring: modify but don't use
    final_diagnostic ^= 12345
    final_diagnostic += decode_sequence(temp_state)
    final_diagnostic ^= 12345  # Undo to preserve determinism
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated sensor readings (mixed types and noise)
    raw_sensor_stream = [
        200, 'error', 400, None, 600, 300, 500, 700, 100, 900,
        800, 1000, 1100, 1200, 1300, 1400, 1500
    ]
    
    # Irrelevant metadata
    device_info = {'model': 'X200', 'firmware': 'v3.4.1'}
    timestamp_log = [1680000000 + i*60 for i in range(20)]
    
    # Real processing begins
    sensor_data = preprocess_input(raw_sensor_stream)
    
    # Generate actual calibration matrix
    calibration_matrix = generate_basis(4)
    
    # Dummy operations to mislead
    dummy_result = dummy_transform(sensor_data)
    feature_set = extract_features(sensor_data)
    signal_metric = analyze_signal_strength(sensor_data)
    
    # Key integrity check (passes but irrelevant)
    is_valid = validate_integrity(sensor_data)
    
    # Compute unused checksum
    checksum_value = compute_checksum(sensor_data)
    
    # Critical statement
    final_diagnostic = process_readings(sensor_data, calibration_matrix)
    
    # Output result
    print(f"Result: {final_diagnostic}")