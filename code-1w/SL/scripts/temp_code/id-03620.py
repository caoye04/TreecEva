import math

def analyze_text(text):
    # Distractor: text analysis function with no impact on final result
    words = text.split()
    word_lengths = [len(w) for w in words]
    avg_length = sum(word_lengths) / len(word_lengths) if words else 0
    vowel_count = sum(1 for c in text.lower() if c in 'aeiou')
    return {'avg_word_len': avg_length, 'vowels': vowel_count}

def validate_range(value, min_val, max_val):
    # Distractor: validation utility not used in critical path
    return min(max(value, min_val), max_val)

def compute_hash(key):
    # Distractor: unused cryptographic-style hash
    h = 0
    for char in key:
        h = (h * 31 + ord(char)) % 1000000
    return h

def transform_sequence(seq):
    # Distractor: complex transformation not contributing to answer
    transformed = []
    for i, x in enumerate(seq):
        if i % 2 == 0:
            transformed.append(x ** 2 - i)
        else:
            transformed.append(x + i * 2)
    return [t % 17 for t in transformed]

def calculate_entropy(values):
    # Distractor: advanced math operation with no effect
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def filter_outliers(data, threshold=2):
    # Distractor: statistical filtering not actually applied
    mean = sum(data) / len(data)
    std = math.sqrt(sum((x - mean)**2 for x in data) / len(data))
    return [x for x in data if abs(x - mean) <= threshold * std]

def shift_cipher(text, shift):
    # Distractor: string manipulation red herring
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decode_payload(payload):
    # Distractor: nested decoding with no real use
    temp = payload[::-1]
    temp = temp.replace('!', '').replace('@', '').replace('#', '')
    temp = ''.join(sorted(set(temp), key=temp.index))
    return temp.upper().strip()

def extract_features(record):
    # Distractor: feature engineering that isn't used
    features = {}
    features['len'] = len(record)
    features['digits'] = sum(c.isdigit() for c in record)
    features['special'] = sum(c in '!@#$%' for c in record)
    features['caps'] = sum(c.isupper() for c in record)
    return features

def process_metrics(data, config):
    # CORE FUNCTION: actual computation path
    base_value = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            base_value += val * config.get(f'w_{i}', 1)
        elif i % 3 == 1 and val > 50:
            base_value += int(math.sqrt(val)) * config[f'w_{i}']
        else:
            base_value -= val // 10
    
    modifier = 1.0
    keys = sorted(config.keys())
    for k in keys:
        if k.startswith('w_'):
            num_part = int(k[2:])
            if num_part % 2 == 0:
                modifier *= 1.1
            else:
                modifier *= 0.95
    
    temp_result = base_value * modifier
    
    # Simulated calibration step
    calibration_factor = 0.85
    intermediate = temp_result * calibration_factor
    
    # Final adjustment based on string length logic
    tag = "metric_v2"
    if len(tag) > 5 and 'v' in tag:
        version_num = int(tag[-1])
        intermediate -= version_num * 3.5
    
    # Critical assignment
    final_score = round(intermediate, 2)
    
    # Dead code path - misleading early exit
    if final_score < 0:
        return 0  # Never reached due to data setup
    
    return final_score

# Irrelevant global variables
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
API_ENDPOINT = "https://dummy.example.com"
LOG_LEVEL = "DEBUG"
CACHE_SIZE = 10000
ACTIVE_USERS = ['alice', 'bob', 'charlie']
SYSTEM_FLAGS = {"debug": False, "trace": True, "verbose": False}
VERSIONS = ["v1", "v2", "v3"]
BOOTSTRAP_NODES = [("node1", 8080), ("node2", 8081)]

# Inputs with mixed relevance
raw_data_stream = "sensor1:speed=85;sensor2:temp=45;sensor3:pressure=120"
data_parts = raw_data_stream.split(';')
extracted = [p.split('=')[1] for p in data_parts if '=' in p]
numeric_data = [int(v) for v in extracted]

# Real input data for core function
data = [72, 88, 63, 91, 44, 77, 56]
weights = {
    'w_0': 1.2,
    'w_1': 0.9,
    'w_2': 1,
    'w_3': 1.1,
    'w_4': 1,
    'w_5': 0.8,
    'w_6': 1.3
}

# Unused but plausible-looking preprocessing
buffer = [x + 5 for x in data]
scaled_buffer = [b * 1.05 for b in buffer]
smoothed = [(scaled_buffer[i-1] + scaled_buffer[i] + scaled_buffer[i+1]) / 3 
             for i in range(1, len(scaled_buffer)-1)]
smoothed = [data[0]] + smoothed + [data[-1]]  # padding back

# Call the main function
final_score = process_metrics(data, weights)

# Additional decoy operations
checksum = sum(ord(c) for c in f"score{final_score}") % 1000
audit_log = f"FINAL_SCORE_{final_score:.2f}_CHK{checksum}"
audit_log = audit_log.replace('_', '-')
audit_log = audit_log.lower()

# Output result as required
print(f"Result: {final_score}")