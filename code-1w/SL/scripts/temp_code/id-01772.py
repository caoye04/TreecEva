from collections import defaultdict, Counter
import math

# Simulated sensor data processing system with diagnostic analysis
def generate_pattern_stream(seed_value, length):
    stream = []
    state = seed_value
    for _ in range(length):
        state = (state * 937 + 19) % 101
        if state % 3 == 0:
            stream.append('A')
        elif state % 5 == 0:
            stream.append('B')
        else:
            stream.append('C')
    return stream

def compute_entropy(signal):
    freqs = Counter(signal)
    total = len(signal)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def extract_features(data):
    # Irrelevant feature extraction - red herring
    features = defaultdict(int)
    for d in data:
        features['len_' + d] += 1
        features['ord_sum'] += ord(d)
    return dict(features)

def evaluate_stability(sequence):
    changes = 0
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            changes += 1
    rate = changes / len(sequence)
    return rate < 0.6

def build_threshold_map(config_level):
    # Decoy thresholds - mostly unused
    base_map = defaultdict(float)
    base_map['A'] = 0.1 * config_level
    base_map['B'] = 0.3 * config_level
    base_map['C'] = 0.2 * config_level
    base_map['entropy_cap'] = 1.5 + (config_level * 0.1)
    base_map['dummy_offset'] = 42.0  # Dead value
    return dict(base_map)

def filter_anomalies(raw_data, mode='strict'):
    # Unused function - dead path
    cleaned = []
    for x in raw_data:
        if x in 'ABC' and x != 'X':
            cleaned.append(x)
    return cleaned

def validate_sequence(seq):
    # Superfluous validation
    if not seq:
        return False
    valid_chars = set('ABC')
    return all(c in valid_chars for c in seq)

def analyze_signal(buffer, thresholds):
    # Core logic hidden among distractions
    primary_count = Counter(buffer)
    total = len(buffer)
    
    # Red herring: complex but unused calculation
    weighted_score = 0.0
    for k, v in primary_count.items():
        weighted_score += v * (ord(k) - 64) * 0.1
    
    # Misleading intermediate
    temp_diagnostic = math.sin(len(primary_count)) * 100
    
    # Actual signal quality metric
    max_freq = max(primary_count.values())
    dominance_ratio = max_freq / total
    
    # Real decision logic
    entropy_val = compute_entropy(buffer)
    stability = evaluate_stability(buffer)
    
    # Key branching logic (non-obvious)
    if entropy_val <= thresholds['entropy_cap'] and stability:
        if dominance_ratio > 0.45:
            result_code = 300 + int(dominance_ratio * 100)
        else:
            result_code = 200 + primary_count.get('A', 0)
    else:
        result_code = 100 + int(temp_diagnostic) % 50
    
    # Final transformation
    final_adjustment = result_code ^ 1337  # Bitwise red herring?
    return final_adjustment - 1337  # Neutralizes XOR -> reveals true path

# Irrelevant global variables
SYSTEM_MODE = 'diagnostic'
CALIBRATION_FACTOR = 0.87
BUFFER_LIMIT = 500
VERSION_TAG = 'v2.1'

# Generate main data
pattern_buffer = generate_pattern_stream(seed_value=17, length=88)

# Unused data transformations
encoded_stream = [ord(c) % 5 for c in pattern_buffer]
duplicate_filtered = [c for i, c in enumerate(pattern_buffer) if c != pattern_buffer[i-1]]

# Build configuration map
threshold_map = build_threshold_map(config_level=7)

# Dummy preprocessing (no effect)
data_snapshot = pattern_buffer.copy()
if len(data_snapshot) > 50:
    slice_point = len(data_snapshot) // 3
    data_snapshot = data_snapshot[slice_point:]

# Critical execution point
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")