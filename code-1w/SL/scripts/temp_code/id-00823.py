from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic logic
def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    count = 0
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] > seq[i+2]:
            count += 1
    return count

def shift_register(value, direction='left', bits=3):
    # Irrelevant bit manipulation red herring
    if direction == 'left':
        return (value << bits) & 0xFFFF
    else:
        return (value >> bits) & 0xFFFF

def deprecated_filter(data):
    # Dead code path - never called
    return [x for x in data if x % 2 == 0]

def accumulate_weighted(items):
    # Unused complex calculation
    total = 0.0
    for i, v in enumerate(items):
        total += v * (0.9 ** i)
    return round(total, 4)

def validate_sequence(arr):
    # Distractor function with misleading intermediate logic
    if not arr:
        return False
    checksum = 0
    for x in arr:
        checksum ^= x
    return checksum % 7 == 0

def extract_features(data_stream):
    # Complex but partially irrelevant feature extraction
    features = defaultdict(int)
    counts = Counter(data_stream)
    
    features['peaks'] = analyze_pattern(data_stream)
    features['mode_val'] = counts.most_common(1)[0][1] if counts else 0
    features['entropy'] = sum(-(c/len(data_stream)) * (c/len(data_stream)) for c in counts.values()) if data_stream else 0
    
    # Red herring computation
    temp = 0
    for k, v in counts.items():
        if k % 4 == 0:
            temp ^= k + v
    features['dummy_key'] = temp
    
    return features

def process_readings(readings, config):
    # Core logic buried in distractions
    base = 0
    for val in readings[:10]:  # Only first 10 matter
        if val > config['limit']:
            base += val // 4
        elif val < config['floor']:
            base -= val % 7
    
    # Real answer depends on this conditional expression
    adjustment = sum(1 for x in readings if x in config['flags']) if config['flags'] else -5
    
    # Critical logic step hidden among noise
    raw_score = base * 3 - adjustment * 2
    
    # Decoy transformation chain
    transformed = [shift_register(x, 'left') for x in readings[:5]]
    dummy_result = accumulate_weighted(transformed)
    
    # Early return red herring (never triggers due to data)
    if len(readings) > 100 and validate_sequence(readings):
        return -999
    
    # Actual result computation
    final_diagnostic = raw_score + len(extract_features(readings)['flags_present'] if 'flags_present' in extract_features(readings) else [])
    
    # Final adjustment based on bitwise invariant
    flag_or = 0
    for f in config['flags']:
        flag_or |= f
    final_diagnostic += (flag_or & 7)  # Adds 5
    
    return final_diagnostic

# Main execution with decoys
if __name__ == "__main__":
    # Input data
    sensor_data = [12, 15, 10, 8, 23, 16, 9, 11, 14, 7, 6, 5, 4, 3, 2, 1]
    
    # Configuration with misleading entries
    thresholds = {
        'limit': 20,
        'floor': 6,
        'flags': [3, 5, 7],  # Used in adjustment and bit op
        'timeout': 999,       # Irrelevant
        'retries': 3          # Irrelevant
    }
    
    # Spurious pre-processing
    filtered_data = [x for x in sensor_data if x > 4]  # Not used later
    normalized = [round(x / max(sensor_data), 3) for x in sensor_data]  # Unused
    
    # Key statement
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")