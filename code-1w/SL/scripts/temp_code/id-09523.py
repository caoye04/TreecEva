import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else False

# Decoy transformation chain
def decoy_transform(seq):
    temp_a = [i ** 2 for i in seq]
    temp_b = [math.log(abs(i) + 1) for i in temp_a]
    temp_c = [int(i * 1.5) for i in temp_b]
    return temp_c  # Never actually used in main logic

# Red herring: complex bit manipulation with no effect
def misleading_bitwise(n):
    a = n ^ 0b101010
    b = (a << 3) & 0b11111111
    c = (b >> 2) | 0b00100100
    return c  # Computed but not used in critical path

# Core processing components
def encode_shift(value, key):
    return ''.join(chr((ord(c) - ord('a') + key) % 26 + ord('a')) if c.isalpha() else c for c in value)

def safe_cast(val):
    try:
        return float(val) if '.' in str(val) else int(val)
    except:
        return 0

# Data obfuscation layer (partially relevant)
def obscure_data(raw):
    offset = 7
    shifted = [x - offset for x in raw]
    inverted = [~x & 0xFF for x in shifted]  # Bitwise inversion within byte range
    return [x ^ 5 for x in inverted]  # Reversible xor mask

# Key transformation pipeline
def transform_sequence(seq):
    filtered = [x for x in seq if x % 2 == 1]  # Keep only odd numbers
    mapped = list(map(lambda x: x * 3 + 2, filtered))
    normalized = [x / max(mapped) * 100 for x in mapped]  # Scale to percentage
    return normalized

# Conditional reducer with short-circuit logic
def conditional_reduce(values, threshold=50.0):
    result = 0
    for v in values:
        if v < threshold or (v > 60 and v < 70):  # Complex condition with short-circuit
            result += v * 0.3
        else:
            result += v * 0.1
    return round(result, 4)

# Main data processor
def process_pipeline(stream):
    # Step 1: Obscure the input
    hidden = obscure_data(stream)
    
    # Step 2: Transform sequence (core logic)
    processed = transform_sequence(hidden)
    
    # Step 3: Apply conditional reduction
    score = conditional_reduce(processed)
    
    # Irrelevant side computation (distractor)
    audit_log = []
    for item in stream:
        hex_rep = hex(item).replace('0x', '')
        case_swapped = ''.join(c.upper() if c.islower() else c.lower() for c in hex_rep)
        audit_log.append(case_swapped)
    
    # Misleading intermediate (looks important, isn't)
    fake_entropy = sum(misleading_bitwise(len(audit_log) * 3)) if audit_log else 0
    
    # Final encoding step (red herring)
    encoded_tag = encode_shift('result', len(processed))
    
    # Actual answer derivation
    base_value = score * 1.75
    adjustment = len([x for x in stream if x > 10]) * 0.2
    final_output = base_value - adjustment
    
    return round(final_output, 4)

# Simulated sensor data stream (real input)
data_stream = [12, 15, 8, 23, 14, 7, 19, 4]

# Dead assignment (misleading)
diagnostic_flag = any(x < 0 for x in decoy_transform(data_stream))

# Critical execution point
final_output = process_pipeline(data_stream)

print(f"Result: {final_output}")