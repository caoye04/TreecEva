import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 80, 96, 112, 224]
    scaling_factor = 0.75
    adjusted = [r * scaling_factor for r in raw_readings]
    return adjusted

def filter_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    threshold = 1.5 * std_dev
    filtered = [x for x in data if abs(x - mean_val) <= threshold]
    # Irrelevant transformation
    inverted = [1 / (x + 1) for x in data]
    _ = [math.log(y + 1) for y in inverted]  # Dead computation
    return filtered

def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val) ^ (i << 2)
    return checksum

def encode_timestamp(hour, minute, second):
    # Complex but irrelevant timestamp encoding
    encoded = (hour << 6) | (minute << 1) | (second >> 4)
    mask = 0xFFFF
    return encoded & mask

def decrypt_sequence(seq, key):
    # Decoy decryption that isn't used in final path
    rotated = []
    for item in seq:
        rotated.append(((int(item) >> key) | (int(item) << (8 - key))) & 0xFF)
    return rotated

def transform_features(values):
    # Apply non-linear transformation
    features = []
    for v in values:
        transformed = math.sin(v / 100) * math.cos(v / 75) + math.sqrt(abs(v) / 50)
        features.append(round(transformed, 6))
    # Extra unused operations
    zipped = list(zip(features[::2], features[1::2]))
    _ = [a + b for a, b in zipped]  # Computation with no effect
    return features

def recursive_reduce(arr, depth=0):
    if depth >= 3 or len(arr) == 1:
        return arr[0] if arr else 0
    reduced = []    
    for i in range(0, len(arr) - 1, 2):
        combined = (arr[i] + arr[i+1]) / 2
        reduced.append(combined)
    return recursive_reduce(reduced, depth + 1)

def analyze_readings(data):
    # Critical function: performs final analysis
    magnitude = sum(x**2 for x in data) ** 0.5
    avg = sum(data) / len(data)
    fluctuation_index = max(data) - min(data)
    
    # Red herring: complex bit analysis
    bit_volume = 0
    for val in data:
        bits = bin(int(abs(val) * 10))[2:]
        bit_volume += bits.count('1')
    _ = bit_volume >> 4  # Unused intermediate
    
    # Real computation path
    stability_score = (avg / (fluctuation_index + 1)) * 100
    normalized_energy = magnitude / (len(data) + 1)
    
    # Key logic step chain
    interim = math.tanh(stability_score / 50)
    adjustment = math.log(1 + normalized_energy)
    response_factor = interim * adjustment
    
    # Final diagnostic calculation (answer depends only on this)
    final_diagnostic = int(round((response_factor * 1000)))
    
    # Distractor: string-based tagging (irrelevant)
    tags = ['stable', 'moderate', 'critical']
    status_label = tags[0] if response_factor > 0.5 else tags[1] if response_factor > 0.2 else tags[2]
    tag_length = len(status_label)
    _ = ''.join([chr((ord(c) + tag_length) % 256) for c in status_label])  # No impact
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    readings = collect_sensor_data()
    cleaned = filter_outliers(readings)
    processed_data = transform_features(cleaned)
    
    # Irrelevant side computations
    chk = generate_checksum(cleaned)
    ts_code = encode_timestamp(14, 32, 48)
    dummy_decrypt = decrypt_sequence(cleaned, 3)
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_data)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")