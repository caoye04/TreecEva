def preprocess_input(raw_str):
    # Irrelevant string cleaning with distractor logic
    cleaned = raw_str.strip().lower().replace(' ', '_')
    tokens = cleaned.split('_')
    filtered = [t for t in tokens if len(t) > 1]
    return ''.join(filtered)

# Decoy transformation chain
transformation_key = [2, 3, 1, 4, 5]
def apply_cipher(data, key):
    shifted = []
    for i, c in enumerate(data):
        shift = key[i % len(key)]
        shifted.append(chr((ord(c) - 97 + shift) % 26 + 97))
    return ''.join(shifted)

# Unused recursive red herring
def calculate_entropy(s, index=0):
    if index >= len(s):
        return 0.0
    freq = s.count(s[index]) / len(s)
    contribution = -freq * __import__('math').log2(freq) if freq > 0 else 0
    return contribution + calculate_entropy(s, index + 1)

# Distractor: fake checksum used nowhere
checksum_log = []
def compute_legacy_checksum(data):
    total = 0
    for char in data:
        total += ord(char) * 7
    checksum = total % 1000
    checksum_log.append(checksum)  # Dead path
    return None  # Actually returns nothing

# Core irrelevant but plausible-looking processing
intermediate_flags = {'mode': 'legacy', 'debug': False}
def validate_sequence(seq):
    if not seq.isalpha():
        return False
    sorted_seq = ''.join(sorted(seq))
    reversed_seq = seq[::-1]
    return sorted_seq == reversed_seq or seq == seq[::-1]

# Real transformation path buried in noise
base_encoding = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
def encode_string(s):
    return [base_encoding.get(c, 0) for c in s]

def transform_sequence(nums):
    result = []
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(nums[i] ** 2)
        else:
            result.append(nums[i] * 2)
    return [x + 5 for x in result]

# Real pattern analysis (target logic)
def analyze_pattern(values):
    total = 0
    for v in values:
        if v > 10:
            total += v // 3
        else:
            total -= v * 2
    return total

# Misleading setup with decoy calls
raw_input_data = "bad cabbage hedged"
decoded_fragment = preprocess_input(raw_input_data)
encoded_letters = apply_cipher(decoded_fragment, transformation_key)  # Looks important

# Fake validation that seems critical
is_valid = validate_sequence(encoded_letters)
compute_legacy_checksum(encoded_letters)  # Logs but doesn't return

# Actual signal path
numeric_base = encode_string(decoded_fragment)  # a,b,c,d,e mapping
transformed_data = transform_sequence(numeric_base)

# Key statement containing answer
final_diagnostic = analyze_pattern(transformed_data)

print(f"Result: {final_diagnostic}")