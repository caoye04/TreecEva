def analyze_pattern(sequence):
    return sum(ord(c) * (i + 1) for i, c in enumerate(sequence)) % 17

def validate_signal(signal_str):
    if len(signal_str) < 5:
        return False
    checksum = sum(analyze_pattern(signal_str[i:i+3]) for i in range(len(signal_str)-2))
    return checksum % 13 == 0

def transform_value(x, key):
    shifted = (x << 2) ^ key
    return (shifted + (shifted >> 3)) % 10007

def decode_sequence(seq, mask):
    result = 0
    for i, val in enumerate(seq):
        if i % 3 == 0:
            result += transform_value(val, mask)
        elif i % 4 == 2:
            result -= (val ^ mask) % 101
    return result % 5000

# Irrelevant signal processing functions (distractors)
def deprecated_filter(data):
    return [x for x in data if x & 1]  # Unused

def legacy_calibrate(arr):
    return [((x >> 1) | 7) ^ 3 for x in arr]  # Dead code path

def obsolete_hash(text):  # Misleading function
    return sum(ord(text[i]) << (i % 8) for i in range(len(text))) % 997

# Real computation begins
sensor_codes = ['ERR0', 'CAL2', 'SYNC', 'DATA']
calibration_key = sum(ord(ch) for ch in sensor_codes[1]) * 3  # Based on 'CAL2'

# Simulated sensor data with red herring values
raw_stream = [217, 134, 95, 192, 88, 201, 67, 144]
extraneous_weights = [0.1, 0.3, 0.5, 0.7, 0.9]  # Unused floating-point array

# Decoy logic block — looks important but unused
if len(raw_stream) > 5:
    adjusted = [x ^ 255 for x in raw_stream[:4]]
    normalized = [(y / 255.0) * 100 for y in adjusted]  # Never used

# Primary data transformation chain
filtered_data = [x for x in raw_stream if x > 100]
sorted_batch = sorted(filtered_data, reverse=True)
doubled_cycle = [(x * 2) % 256 for x in sorted_batch]

# Inject string-based computation using mandatory feature
status_tag = "Diag@Pass"
diag_prefix = status_tag.lower().replace("@", "").strip()  # Uses string methods
prefix_value = sum(ord(diag_prefix[i]) * (i+1) for i in range(len(diag_prefix)))

# Conditional logic with nested structure and distractor branches
if prefix_value > 400:
    temp_offset = 17
    if calibration_key % 2 == 1:
        temp_offset += 5
    else:
        temp_offset -= 3
        shadow_var = temp_offset * 2  # Red herring
else:
    temp_offset = 0

# Core calculation mixed with irrelevant steps
working_set = []
for idx, val in enumerate(doubled_cycle):
    if idx % 2 == 0:
        working_set.append(val + calibration_key)
    else:
        working_set.append(val - (calibration_key % 19))

# Add decoy mutation that seems relevant but isn't final
working_set = [w ^ 0xAA for w in working_set]  # Bitwise red herring

# Actual answer derivation buried in logic
aggregate = 0
for step in range(len(working_set)):
    if step == 0:
        aggregate = working_set[0] * 3
    elif step % 2 == 1:
        aggregate += transform_value(working_set[step], calibration_key)
    else:
        aggregate -= (working_set[step] + step) // 2

# Secondary validation (looks like it affects output, but doesn’t)
validation_code = "BETA7" if aggregate > 500 else "ALPHA3"
valid = validate_signal(validation_code)  # Calls complex but irrelevant logic

# Final processing with key variable
sensor_data = working_set.copy()

# Introduce string-based switch using case conversion
mode_flag = "TURBO"
enabled_modes = mode_flag.lower().split('U')  # Use of string method, partial split

scaling_factor = 2 if 'T' in mode_flag else 1

# The real final computation
interim = decode_sequence(sensor_data, calibration_key)
mod_adjust = (calibration_key + prefix_value) % 89
final_diagnostic = (interim + mod_adjust - temp_offset) % 100000

# Distractor: another unused diagnostic path
if final_diagnostic % 7 == 0:
    secondary_diag = (interim ^ mod_adjust) % 10000  # Never accessed

print(f"Result: {final_diagnostic}")