import math

def analyze_pattern(seq):
    # Irrelevant helper function (dead code path)
    return sum([x ** 2 for x in seq if x % 2 == 0])

def decrypt_key(token):
    # Distractor function with bit manipulation red herring
    key = 0
    for i, c in enumerate(token[:5]):
        key ^= ord(c) << (i % 3)
    return key % 17

def validate_sequence(s):
    # Unused validation logic (misleading intermediate)
    return s.startswith('SIG') and s.endswith('END') and len(s) > 6

def shift_window(data, window=3):
    # Decoy transformation with slicing
    shifted = []
    for i in range(len(data)):
        segment = data[max(0, i - window):i]
        if segment:
            shifted.append(sum(segment) / len(segment))
        else:
            shifted.append(0)
    return shifted

def compute_entropy(values):
    # Seemingly important but irrelevant computation
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def extract_features(raw):
    # Processes raw string into numeric features (partial distractor)
    cleaned = ''.join(c for c in raw if c.isdigit() or c in '+-')
    parts = cleaned.split('+')
    numbers = []
    for part in parts:
        if part and part != '-':
            try:
                numbers.append(abs(int(part)))
            except:
                continue
    return numbers[::2]  # Slicing every second element

def process_readings(data, config):
    # Core relevant function with embedded logic chain
    base_offset = config['offset']
    factor = config['gain'] * 1.5
    threshold = config['threshold']

    # Real signal processing begins
    filtered = [x for x in data if abs(x - base_offset) > threshold]
    adjusted = [round((val - base_offset) * factor, 4) for val in filtered]

    # Key combinatoric step: count valid pairs modulo prime
    count = 0
    for i in range(len(adjusted)):
        for j in range(i + 1, len(adjusted)):
            if (adjusted[i] + adjusted[j]) > 10.0:
                count += 1
    mod_count = count % 97

    # Critical transformation using dictionary lookup
    map_table = {i: ((i * 11) % 97) for i in range(100)}
    mapped_value = map_table[mod_count]

    # Final arithmetic using modular exponentiation
    exponent = (mapped_value * 3) % 43
    power_result = pow(7, exponent, 97)

    # Insertion of decoy operation (string slicing)
    signature = "DIAGNOSTIC_LOG_OUTPUT"
    sig_part = signature[8:15].lower()  # 'nostic_' — irrelevant

    # Real result built from numeric chain
    intermediate = (power_result * 17) + 42
    final_diagnostic = int(intermediate ^ 0xAA)  # Bitwise XOR as final step

    return final_diagnostic

# Main execution block with mixed data
sensor_data = [12.1, 15.3, 8.7, 23.4, 9.2, 11.8, 25.9, 7.6]
calibration_matrix = {
    'offset': 10,
    'gain': 2.0,
    'threshold': 2.0,
    'sensitivity': 0.95,
    'version': 'SIGv2-END'
}

# Dead variable assignments (red herrings)
temp_log = "RAW+1123+456+789+END"
diag_features = extract_features(temp_log)
analysis_key = decrypt_key("aXm9L")
entropy_score = compute_entropy(diag_features)
windowed = shift_window(sensor_data)

# Key computation point
final_diagnostic = process_readings(sensor_data, calibration_matrix)

# Output the target result
print(f"Result: {final_diagnostic}")