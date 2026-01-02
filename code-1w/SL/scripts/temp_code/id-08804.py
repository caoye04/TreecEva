def preprocess_signal(raw):    
    # Irrelevant transformation (dead path)
    if len(raw) > 100:
        return [x * 0.9 for x in raw]
    return raw

# Simulated sensor readings
temperature_readings = [23.5, 24.1, 25.3, 26.7, 27.2, 26.8, 25.9, 24.6]
humidity_readings = [45, 47, 52, 58, 61, 59, 54, 49]

# Distractor: unused signal processing
def filter_noise(signal):
    return [x for x in signal if x > 0]

# Unused but plausible function
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Misleading intermediate analysis
snapshot = temperature_readings[::2]
drift_estimate = sum(humidity_readings) / len(humidity_readings)  # Red herring

# Core logic disguised among distractions
def encode_sequence(seq):
    encoded = []
    for val in seq:
        if val > 25:
            encoded.append('H')
        elif val < 24:
            encoded.append('L')
        else:
            encoded.append('M')
    return ''.join(encoded)

def shift_cipher(text, key):
    # String manipulation with case conversion
    shifted = []
    for char in text.upper():
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            shifted.append(shifted_char)
        else:
            shifted.append(char)
    return ''.join(shifted)

# Data transformation chain
raw_pattern = encode_sequence(temperature_readings)
scrambled = shift_cipher(raw_pattern, 7)  # Apply cipher shift

# Another decoy variable
baseline_risk = len(scrambled) * 1.5

# Tuple unpacking and multiple assignments
primary_code, secondary_code = scrambled[:5], scrambled[5:]
flag_state, trigger_mode = True, 'AUTO'

# Conditional red herring
if flag_state and len(primary_code) == 5:
    trigger_mode = 'OVERRIDE'
    dummy_calc = baseline_risk * 2  # Dead computation

# Real processing begins here
transform_map = {'H': 3, 'M': 2, 'L': 1}
transformed_data = [transform_map[c] for c in raw_pattern]

# Critical distractor: complex-looking but unused bitwise logic
bit_flags = 0
for i, val in enumerate(transformed_data):
    bit_flags ^= (val << (i % 4))

# Actual answer derivation path
sequence_weight = sum(transformed_data)
length_factor = len(transformed_data)

# Combinatorics distraction
pair_count = 0
for i in range(len(transformed_data)):
    for j in range(i+1, len(transformed_data)):
        if transformed_data[i] + transformed_data[j] > 4:
            pair_count += 1

# Final analysis function
def analyze_pattern(data):
    base_score = sum(data)
    penalty = 0
    
    # Use string method to create illusion of dependency
    pattern_str = ''.join(map(str, data))
    if pattern_str.count('3') > 1:
        penalty += 2
    if '1' in pattern_str:
        penalty += 1
    
    # Actual formula
    adjustment = len(data) // 2
    return base_score - penalty + adjustment

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data)

# Output requirement
print(f"Result: {final_diagnostic}")