def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > 30]
    normalized = [x / max(filtered) for x in filtered]
    rolled = normalized[-3:] + normalized[:-3]  # Circular shift
    return [round(x, 6) for x in rolled]


def generate_key(length):
    seed = 7
    key = []
    for i in range(length):
        seed = (seed * 97 + 13) % 1000
        key.append(seed % 15)
    return key

# Irrelevant helper - dead function
def decrypt_cipher(seq, key):
    result = []
    for i in range(len(seq)):
        result.append(seq[i] ^ key[i % len(key)])
    return result

# Another red herring: checksum with no effect
def compute_health_score(data):
    base = sum(data) * 0.7
    penalty = len([x for x in data if x < 5]) * 2
    return int(base - penalty)

# Misleading transformation chain
def transform_sequence(seq):
    temp_a = [x * 2 + 1 for x in seq]
    temp_b = [x for x in temp_a if x % 3 != 0]
    temp_c = temp_b[::-1]  # Reverse
    temp_d = [temp_c[i] + i for i in range(len(temp_c))]
    return temp_d[:len(seq)]

# Core analysis logic (obfuscated by surrounding noise)
def analyze_pattern(signal, keys):
    stage_1 = [int(s * 100) for s in signal]
    stage_2 = [stage_1[i] ^ keys[i % len(keys)] for i in range(len(stage_1))]
    stage_3 = [x for x in stage_2 if x % 2 == 1]  # Keep only odds
    
    # Real computation begins here
    accumulated = 0
    for i, val in enumerate(stage_3):
        if i % 2 == 0:
            accumulated += val * 3
        else:
            accumulated -= val
    
    # Secondary manipulation
    mod_factor = sum(keys) % 19
    accumulated = abs(accumulated) % 10000
    
    # Final adjustment using string-based key
    key_string = ''.join(map(str, sorted(set(keys))))
    pivot = int(key_string[1:3]) if len(key_string) >= 3 else 17
    result = (accumulated + pivot) * (mod_factor % 7)
    
    # Distractor: unused branching
    if result > 5000:
        result = result // 2
    if result < 100:  # Never triggers
        result *= 10
        
    return result

# Main execution flow
raw_sensor_data = [45, 12, 67, 89, 23, 91, 34, 78, 56, 88]
config_flags = [1, 0, 1, 1, 0, 1, 0, 0]  # Unused configuration
offset_lookup = {'a': 3, 'b': 7, 'c': 11}  # Dead data structure

processed_signal = preprocess_signal(raw_sensor_data)
encryption_key = generate_key(7)

# Fake processing steps (distractors)
encoded_stream = transform_sequence(encryption_key)
score = compute_health_score(raw_sensor_data)
verification_hash = sum(encoded_stream) ^ 255  # Unused

# Actual critical computation
final_diagnostic = analyze_pattern(processed_signal, encryption_key)

# Print result as required
print(f"Result: {final_diagnostic}")