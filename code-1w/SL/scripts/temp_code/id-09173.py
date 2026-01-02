import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum(i ** 2 for i in range(x))

# Distractor data structures
decoys = {
    'mask': [1, 0, 1, 1],
    'flags': (False, True, True),
    'offsets': (-3, 5, -7)
}

# Misleading intermediate computations
shadow_value = 0
for k in range(4):
    shadow_value += (k * k) % 3

# Core transformation components
token_map = lambda x: (x >> 1) ^ 0xA

# Unused but plausible-looking processing chain
def legacy_filter(seq):
    return [item for item in seq if item % 2 == 0]

# Real processing functions
def decode_sequence(seq):
    result = 0
    for val in seq:
        if val > 5:
            result += token_map(val)
        else:
            result -= val
    return abs(result)

def apply_correction(value, mode=True):
    if mode:
        temp = value | 0b1101
        temp ^= 0b1010
        return temp if temp % 2 == 0 else temp + 1
    return value

def build_context(keys):
    ctx = {}
    for i, key in enumerate(keys):
        ctx[key] = i * 3 + 2
    return ctx

def process_pipeline(raw):
    # Step 1: Initial unpacking
    header, payload = raw[0], raw[1]
    
    # Step 2: Header-based adjustment
    adjustment = (header ^ 0x5) & 0xF
    
    # Step 3: Decode payload using bit manipulation
    decoded = decode_sequence(payload)
    
    # Step 4: Apply bitwise correction
    corrected = apply_correction(decoded)
    
    # Step 5: Context injection (tuple unpacking)
    context_keys = ('alpha', 'beta', 'gamma')
    context_vals = tuple(build_context(context_keys).values())
    ctx_sum = sum(context_vals) // len(context_vals)
    
    # Step 6: Conditional override (short-circuit logic)
    override_flag = False and (ctx_sum > 100)
    interim = override_flag and 999 or (corrected + adjustment + ctx_sum)
    
    # Step 7: Final scaling via lambda transformation
    scaler = lambda x: round(x * 1.5, 6)
    final_scaled = scaler(interim)
    
    # Step 8: Red herring floating point accumulation
    phantom_accum = 0.0
    for _ in range(3):
        phantom_accum += 0.111111
    
    # Actual output
    return int(final_scaled)

# Critical execution point
config_tuple = (0xB, [6, 3, 8, 4])
data_chunk = config_tuple
final_output = process_pipeline(data_chunk)
print(f"Result: {final_output}")