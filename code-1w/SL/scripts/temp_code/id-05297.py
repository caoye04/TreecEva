def preprocess_input(raw_data):
    if not raw_data.strip():
        return 'INVALID'
    cleaned = raw_data.strip().lower()
    if 'err' in cleaned:
        return 'ERROR_FOUND'
    return cleaned.upper()

raw_logs = ['  SigNal_1 ', '  ', 'err_log ', 'Signal_2']
decoded_entries = []

for log in raw_logs:
    processed = preprocess_input(log)
    if processed not in ['INVALID', 'ERROR_FOUND']:
        decoded_entries.append(processed)

# Irrelevant transformation chain (distractor)
transformation_key = 7
scrambled = [str(hash(entry) % 1000) for entry in decoded_entries]
filtered_scrambled = [x for x in scrambled if int(x) > 500]
summary_hash = sum(int(x) * 2 for x in filtered_scrambled)

# Actual signal pattern setup (relevance)
pattern_buffer = [0b1010, 0b1100, 0b1111, 0b0001]
calibration_offset = len(decoded_entries) * 2

# Decoy function - looks important but unused
def compute_entropy(data):
    import math
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Another red herring: complex string analysis with no downstream use
audit_trace = "".join(decoded_entries)
shift_value = audit_trace.count('G')
rotated_chars = []
for c in audit_trace:
    if c.isalpha():
        rotated_chars.append(chr((ord(c) - ord('A') + shift_value) % 26 + ord('A')))
    else:
        rotated_chars.append(c)

transformed_trace = ''.join(rotated_chars)
trace_validity = transformed_trace.startswith('SIG') and 'NAL' in transformed_trace

# Core logic buried among distractions
def apply_mask(sequence, offset):
    result = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            result ^= (val << (offset % 4))  # bit shift based on offset
        else:
            result += (val & offset)  # bitwise AND with offset
    return result

# Secondary decoy: unused recursive function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

sequence_score = 0
for i in range(3):
    sequence_score += i ** 3

# Real computation path (non-obvious due to noise)
def analyze_signal(patterns, offset):
    temp_result = 0
    for p in patterns:
        if offset > 2:
            temp_result += (p ^ offset) % 5
        else:
            temp_result += p % 3
    aggregate = apply_mask(patterns, offset)
    final_component = temp_result * (offset // 2)
    return aggregate - final_component

# Unused diagnostic (misleading)
current_state = 'STANDBY'
if calibration_offset > 3:
    current_state = 'ACTIVE'
status_flag = hash(current_state) % 100

# Critical execution point
final_diagnostic = analyze_signal(pattern_buffer, calibration_offset)

print(f"Result: {final_diagnostic}")