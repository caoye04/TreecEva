import itertools

# Simulated sensor data preprocessing with distractions
def fetch_raw_sensor_data():
    return [0.7, -1.2, 3.5, 2.1, -0.8, 4.4, 1.9, -2.3]

def clean_data(raw):
    cleaned = []
    threshold = 0.5
    for x in raw:
        if abs(x) > threshold:
            cleaned.append(round(x * 1.05, 2))  # minor correction
    return cleaned

def compute_entropy(arr):
    # Irrelevant function - decoy for information theory enthusiasts
    from math import log
    total = sum(arr)
    entropy = 0
    for x in arr:
        prob = x / total if total != 0 else 0
        if prob > 0:
            entropy -= prob * log(prob, 2)
    return round(entropy, 4)

def generate_frequency_map(data):
    # Dead code path - never used in main logic
    freq = {}
    for d in data:
        bin_id = int(d // 1)
        freq[bin_id] = freq.get(bin_id, 0) + 1
    return freq

def shift_cipher(text, shift):
    # Completely irrelevant string operation - red herring
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def extract_features(signal):
    # Extracts key signal characteristics (actual relevant function)
    positive_count = len([x for x in signal if x > 0])
    negative_count = len([x for x in signal if x < 0])
    peak_magnitude = max(abs(x) for x in signal)
    zero_crossings = 0
    for i in range(1, len(signal)):
        if signal[i-1] * signal[i] < 0:
            zero_crossings += 1
    
    # Distractor: unused intermediate calculation
    avg_abs_change = sum(abs(signal[i] - signal[i-1]) for i in range(1, len(signal))) / (len(signal)-1) if len(signal) > 1 else 0
    
    return {
        'pos': positive_count,
        'neg': negative_count,
        'peak': peak_magnitude,
        'crossings': zero_crossings
    }

def validate_calibration(features, override=False):
    # Conditional branch with early returns - some misleading checks
    if features['peak'] > 4.0 and not override:
        return False  # Simulate failure on high peak
    if features['crossings'] < 2:
        return False
    if features['pos'] == 0:
        return False
    return True  # Most signals pass

def fuse_multi_source_data(primary, secondary):
    # Unused fusion logic - distractor
    combined = []
    for p, s in itertools.zip_longest(primary, secondary, fillvalue=0):
        combined.append(round((p + s * 0.3) / 1.3, 2))
    return combined

def analyze_signal(data):
    # Core analysis with critical answer derivation
    features = extract_features(data)
    
    # Multiple nested conditions with distracting branches
    if not validate_calibration(features):
        return -999
    
    score = 0
    score += features['pos'] * 10
    score += features['crossings'] * 15
    score -= features['neg'] * 5
    
    # Hidden key computation: depends on specific slicing pattern
    data_slice = data[1::2]  # every second element starting at index 1
    slice_sum = sum(data_slice)
    
    # Final adjustment using slice sum modulo operation
    adjustment = int(abs(slice_sum)) % 7
    score += adjustment
    
    # Decoy complex transformation (never affects final result)
    transformed = [round((x ** 2) * 0.1, 1) for x in data]
    temp_result = ''.join([str(int(t)) for t in transformed if t > 1])
    encoded = shift_cipher(temp_result, 3) if temp_result else '0'
    
    # Critical execution point
    final_diagnostic = score + len(encoded)  # encoded length is distraction
    
    # Red herring: unused min/max/average block
    stats = {
        'min': min(data),
        'max': max(data),
        'avg': round(sum(data)/len(data), 2),
        'range': max(data) - min(data)
    }
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    raw_data = fetch_raw_sensor_data()
    processed_data = clean_data(raw_data)
    
    # Irrelevant string processing to distract
    metadata_tag = 'SIGMONv2'
    shifted_tag = shift_cipher(metadata_tag, 13)
    tag_length = len(shifted_tag)
    
    # Dummy frequency analysis
    dummy_freq = generate_frequency_map(processed_data)
    
    # Actual key computation path
    final_diagnostic = analyze_signal(processed_data)
    
    # Output required result
    print(f"Result: {final_diagnostic}")