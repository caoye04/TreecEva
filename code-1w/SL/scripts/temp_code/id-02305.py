def preprocess_input(raw_string):
    sanitized = raw_string.strip().lower()
    tokens = sanitized.split(',')
    ascii_vals = [ord(c) for c in sanitized if c.isalpha()]
    checksum = sum(ascii_vals) % 19
    return tokens, checksum

raw_data = "XyZ, AbC, 42, Hello, World"
tokens, chk = preprocess_input(raw_data)

# Irrelevant transformation chain (distractor)
decoys = []
for i in range(len(tokens)):
    temp = ''
    for c in tokens[i]:
        if c.isalpha():
            temp += chr((ord(c.lower()) - 96) % 26 + 97)
    decoys.append(temp[::-1])

# Bit manipulation red herring
bit_fiddling = 0
for val in [chk, len(decoys), len(decoys[0]) if decoys else 0]:
    bit_fiddling ^= (val << 2) | (val >> 1)

# Real processing starts here — meaningful data
encoded_data = []
for idx, token in enumerate(tokens):
    length_factor = len(token)
    position_weight = idx + 1
    vowel_count = sum(1 for c in token if c.lower() in 'aeiou')
    encoded_value = (length_factor * position_weight) + (vowel_count ** 2)
    encoded_data.append(encoded_value)

# Validation key derived from non-obvious but deterministic logic
def generate_validation_key(data_list):
    total_chars = sum(len(t) for t in data_list)
    unique_starts = len(set(t[0].lower() for t in data_list if t))
    return (total_chars ^ unique_starts) + 5

validation_key = generate_validation_key(tokens)

# Decoy function that's defined but not used
def decrypt_sequence(seq, key):
    result = []
    for item in seq:
        decrypted = item
        for _ in range(key % 4):
            decrypted = (decrypted >> 1) ^ key
        result.append(decrypted)
    return result

# Another distraction: unused recursive accumulator
def accumulate_depth(seq, depth=0):
    if depth >= 3 or not seq:
        return 0
    return seq[0] + accumulate_depth(seq[1:], depth + 1)

# Core logic hidden among distractions
def process_results(data, key):
    adjusted_sum = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            adjusted_sum += val * key
        else:
            adjusted_sum -= val // (key if key != 0 else 1)
    # Additional conditional twist using string method side info
    flag_indicators = [t for t in tokens if 'o' in t.lower()]
    modifier = len(flag_indicators) * 3
    final = adjusted_sum + modifier
    
    # Hidden XOR correction based on initial checksum
    correction = chk ^ 7
    final ^= correction
    return final

# Execution point of interest
final_score = process_results(encoded_data, validation_key)

# Misleading print statements (simulating debug noise)
intermediate_result = bit_fiddling + accumulate_depth(encoded_data)
debug_dump = {'status': 'ok', 'level': 'deep', 'value': intermediate_result}

print(f"Result: {final_score}")