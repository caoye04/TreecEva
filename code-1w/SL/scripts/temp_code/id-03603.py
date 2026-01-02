from collections import defaultdict, Counter
import math

# Simulated system telemetry data (irrelevant but plausible)
telemetry_log = [
    {'sensor': 'temp', 'value': 72.5, 'status': 'OK'},
    {'sensor': 'pressure', 'value': 30.1, 'status': 'OK'},
    {'sensor': 'humidity', 'value': 45.0, 'status': 'OK'}
]

# Irrelevant helper function (dead code path)
def validate_sensor_readings(logs):
    for entry in logs:
        if entry['value'] < 0:
            return False
    return True

# Unused transformation map (distractor)
sensor_xform = {
    'temp': lambda x: x * 9/5 + 32,
    'pressure': lambda x: x * 29.53,
    'humidity': lambda x: min(x * 1.2, 100)
}

# Decoy cryptographic constants (misleading)
ENCRYPTION_ROUNDS = 16
PRIME_MODULUS = 65537
TEMPORAL_SALT = 2023

# Fake checksum that looks important but isn't used in final calculation
def legacy_checksum(data):
    result = 0
    for i, b in enumerate(data):
        result += (b ^ (i % 256)) * (i + 1)
    return result % 10000

# Auxiliary bit manipulation with partial relevance
def rotate_left(x, n, bits=32):
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)

# String obfuscation decoy (never called)
def scramble(text):
    return ''.join(chr(ord(c) ^ 13) for c in text)[::-1]

# Data buffer construction with embedded logic
raw_payload = "config_frame_0x1A"
data_buffer = [ord(c) for c in raw_payload]

# Artificial constraint from unused protocol spec
MAX_FRAME_SIZE = 256
FRAGMENT_OVERHEAD = 4

# Key derivation with red herring
key_seed = sum(data_buffer[::2]) * len(raw_payload)
access_key = (key_seed ^ 0xABCD) % 65536

# Secondary derived value (looks important, partially distractive)
derived_bias = int(math.sqrt(access_key)) ^ data_buffer[0]

# Frequency analysis of byte distribution (plausible but irrelevant)
byte_freq = Counter(data_buffer)
frequent_bytes = [b for b, cnt in byte_freq.items() if cnt > 1]

# Control flow distraction: simulate packet validation
is_valid_frame = len(data_buffer) < MAX_FRAME_SIZE and data_buffer[-1] != 0xFF
validation_score = 0
if is_valid_frame:
    validation_score += 100
    if len(frequent_bytes) == 0:
        validation_score += 50
else:
    validation_score -= 200  # unreachable due to input

# Real computation begins here — actual logic chain
working_state = defaultdict(int)
for i, val in enumerate(data_buffer):
    working_state[i % 4] ^= rotate_left(val ^ access_key, (i % 5) + 1)

# Intermediate digest using only part of the state
intermediate = 0
for k, v in working_state.items():
    intermediate += v * (k + 1) ** 2

# Actual core transformation: polynomial residue with bit folding
shift_reg = 0
for b in data_buffer:
    shift_reg = (shift_reg * 33 + b) & 0xFFFF

# Combine with access key using arithmetic and bitwise mix
masked_reg = (shift_reg ^ access_key) + derived_bias
scaled_reg = (masked_reg * 7) // 3

# Final integrity computation — depends on prior steps
def compute_integrity_value(buffer, key):
    base = 0
    for i, b in enumerate(buffer):
        # Mix position, value, and key with transcendental touch
        contribution = (b ^ key) * math.sin(i + 1)
        base += contribution
    
    # Round and fold into constrained space
    folded = int(abs(base) * 1000) % 50000
    
    # Final perturbation using working_state (critical cross-reference)
    global working_state
    bonus = sum(working_state.values()) % 100
    return folded + bonus

# Execute main computation
temp_result = legacy_checksum(data_buffer)  # distractor call
final_checksum = compute_integrity_value(data_buffer, access_key)

print(f"Result: {final_checksum}")