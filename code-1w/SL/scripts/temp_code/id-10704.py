def analyze_sequence(data_stream):
    checksum = 0
    for val in data_stream:
        checksum ^= val
        checksum = (checksum + (val % 7)) % 251
    return checksum


def validate_pattern(signal):
    if len(signal) < 5:
        return False
    pattern_match = sum(1 for i in range(len(signal)-1) if signal[i] < signal[i+1])
    return pattern_match > len(signal) // 2

# Irrelevant helper - dead logic path
def deprecated_filter(x):
    return x & 0x5F

# Unused transformation table
transform_map = {i: (i * 11) % 97 for i in range(50)}

# Distractor variables
buffer_limit = 4096
retries = 3
timeout_ms = 1500
payload_size = 256  # unused

# Baseline calibration (red herring)
calibration_keys = [17, 23, 29, 31, 37]
dummy_state = set()
for k in calibration_keys:
    dummy_state.add(k ** 2 % 19)

# Real input generation with subtle logic
raw_samples = [n * 3 + (n % 4) for n in range(1, 10)]
sampled_data = [x for x in raw_samples if x % 2 == 1]  # only odds

# Injected string manipulation (required feature)
data_tag = "sensor_log_v2"
version_code = int(data_tag.split('_')[-1][1:])  # extracts 2

# Bit manipulation and filtering
filtered_stream = []
bit_flags = 0
for item in sampled_data:
    bit_flags |= item & 7
    if (item ^ version_code) % 5 != 0:  # conditional filter
        filtered_stream.append(item)

# Set operation (required feature): simulate seen residues
residue_pool = {x % 13 for x in filtered_stream}
extension_set = {x + 5 for x in residue_pool if x < 8}
active_residues = residue_pool & extension_set  # intersection

# Primary computation chain
health_signature = analyze_sequence(filtered_stream)

baseline_offset = 0
for r in active_residues:
    baseline_offset += (r * r) % 17

# Secondary red herring loop (no effect on output)
temp_accum = 0
for i in range(12):
    temp_accum += (i * temp_accum + 1) % 100  # self-dependent but unused

# Core processing function
def process_metrics(health, offset):
    intermediate = health ^ offset
    intermediate = (intermediate * 3) % 199
    if intermediate % 2 == 0:
        intermediate += 17
    # Complex adjustment
    adjustment = 0
    for digit_str in str(intermediate):
        adjustment += int(digit_str)**2
    result = intermediate + adjustment
    # Final twist: use of string method again
    flag_str = "adjust_high" if result > 100 else "low_fix"
    if 'high' in flag_str:
        result -= len(flag_str)
    return result

# Critical assignment
final_diagnostic = process_metrics(health_signature, baseline_offset)

# Output requirement
print(f"Result: {final_diagnostic}")