from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic logic
def fetch_sensor_readings():
    return [248, 516, 74, 193, 442, 87, 311, 66, 503, 129]

def preprocess_signal(raw_values):
    filtered = []
    noise_floor = 65
    for val in raw_values:
        if val > noise_floor:
            filtered.append(val & 511)  # Mask to 9 bits
    return [v for v in filtered if v % 2 == 1]  # Keep only odd values

def generate_checksum(sequence):
    # Irrelevant checksum - red herring
    return sum(s ^ (s >> 3) for s in sequence) % 1000

def decode_frequency_band(data):
    # Misleading transformation - not used in final result
    band_map = defaultdict(int)
    for item in data:
        band = (item // 100) % 4
        band_map[band] += 1
    return dict(band_map)

def shift_key_matrix(values, offset):
    # Unused complex transformation - dead path
    matrix = [[0]*4 for _ in range(4)]
    idx = 0
    for i in range(4):
        for j in range(4):
            if idx < len(values):
                matrix[i][j] = (values[idx] << 2) ^ offset
            idx += 1
    flattened = [matrix[r][c] for r in range(4) for c in range(4)]
    return flattened[:len(values)]

def compute_entropy(vector):
    total = sum(vector)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in vector if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

def extract_features(dataset):
    feature_set = defaultdict(list)
    temp_stats = []
    
    for i, val in enumerate(dataset):
        feature_set['parity'].append(val & 1)
        feature_set['high_nibble'].append((val >> 4) & 15)
        feature_set['bit_count'].append(bin(val).count('1'))
        
        # Decoy computation
        temp_stats.append((val ** 2) % 97)
    
    # Real feature used later
    mode_bits = Counter(feature_set['bit_count']).most_common(1)[0][0]
    
    # Fake aggregation
    avg_high = sum(feature_set['high_nibble']) / len(feature_set['high_nibble'])
    
    return mode_bits

def transform_signal_integrity(raw_log):
    processed = [x ^ 0xAA for x in raw_log]  # XOR scramble
    adjusted = [p - 10 for p in processed if p > 100]
    normalized = [n | 1 for n in adjusted]  # Force odd
    return normalized

def analyze_pattern(signal, reference):
    base_score = 0
    for i in range(min(len(signal), len(reference))):
        if signal[i] > reference[i]:
            base_score += (signal[i] & reference[i]) % 7
        else:
            base_score -= (signal[i] ^ reference[i]) % 5
    
    # Final result depends on this modification
    adjustment_factor = len([x for x in signal if x & 8])
    return base_score + adjustment_factor

# Main execution flow
if __name__ == '__main__':
    readings = fetch_sensor_readings()
    
    # Irrelevant baseline stats
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    entropy_metric = compute_entropy(readings)
    
    # Primary processing chain
    clean_signal = preprocess_signal(readings)
    transformed_data = transform_signal_integrity(clean_signal)
    
    # Generate unused diagnostic map - distractor
    frequency_profile = decode_frequency_band(readings)
    checksum_value = generate_checksum(transformed_data)
    
    # Extract key pattern used in analysis
    dominant_bit_count = extract_features(transformed_data)
    
    # Construct reference sequence based on feature
    key_sequence = [(dominant_bit_count * 73) % 256 for _ in range(len(transformed_data))]
    for i in range(len(key_sequence)):
        key_sequence[i] = (key_sequence[i] + (i * 17)) % 512
    
    # Dead code path - looks important but unused
    dummy_matrix = shift_key_matrix(transformed_data, 8)
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, key_sequence)
    
    # Output target result
    print(f"Result: {final_diagnostic}")