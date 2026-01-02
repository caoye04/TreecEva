def preprocess_signal(data):
    # Irrelevant preprocessing function (dead end)
    return [x * 2 for x in data if x % 3 == 0]


def compute_entropy(seq):
    # Misleading auxiliary calculation (not used in final result)
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def shift_cipher(text, offset):
    # Distractor: string manipulation not related to main logic
    shifted = ''.join(chr((ord(c) - ord('a') + offset) % 26 + ord('a')) if c.isalpha() else c for c in text)
    return shifted[::-1]  # Reversed for extra distraction


def evaluate_threshold(value, reference=150):
    # Decoy function with red herring logic
    if value < reference * 0.5:
        return 'LOW'
    elif value > reference * 1.5:
        return 'HIGH'
    else:
        return 'MEDIUM'


def decode_instruction(code_tuple):
    # Unrelated decoding operation (unused path)
    a, b, c = code_tuple
    return (a ^ b) + (c << 1)


def analyze_pattern(sequence, limit):
    # Core relevant function
    temp_result = 0
    for i in range(len(sequence)):
        if i % 2 == 0 and sequence[i] > limit:
            temp_result += sequence[i] * (i + 1)
        elif i % 3 == 0:
            temp_result -= sequence[i]
    
    # Additional relevant transformation
    adjustment_factor = 0
    for val in sequence:
        if val & (val - 1) == 0 and val > 1:  # Check if power of two
            adjustment_factor += 1
    
    return temp_result + (adjustment_factor * 17)

# Main execution flow
raw_input = [12, 25, 48, 52, 64, 91, 128, 144]

# Irrelevant data structures
lookup_map = {k: chr(97 + (k % 26)) for k in range(200)}
feature_flags = {'debug': False, 'trace': True, 'verbose': 'none'}
config_params = {'max_iter': 1000, 'tolerance': 1e-4, 'active': True}

# Unused signal processing
filtered_data = preprocess_signal(raw_input)
entropy_value = compute_entropy([x % 10 for x in raw_input])

cipher_tag = shift_cipher('diagnostic', 7)

# Key variables for actual computation
activation_sequence = [x * 2 - 3 for x in raw_input]
threshold = sum(x for x in activation_sequence if x % 4 == 0) // 10

# Dead code path
if len(raw_input) > 10:
    dummy = decode_instruction((10, 20, 30))
    feature_flags['extra'] = True

# Conditional expression (required python feature)
status_flag = 'ready' if threshold > 50 else 'pending'

# Dictionary usage (required python feature)
metrics = {
    'base_count': len(raw_input),
    'adjusted_sum': sum(activation_sequence),
    'threshold_level': threshold,
    'status': status_flag
}

# Actual key computation begins here
logic_sequence = []
for idx, val in enumerate(activation_sequence):
    if idx % 2 == 0:
        logic_sequence.append(val + idx)
    else:
        logic_sequence.append(val - (idx % 5))

# Final diagnostic depends on analyze_pattern
final_diagnostic = analyze_pattern(logic_sequence, threshold)

# Print required output
print(f"Result: {final_diagnostic}")