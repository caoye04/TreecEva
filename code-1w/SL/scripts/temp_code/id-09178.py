def analyze_signal(x, threshold=50):
    if x < 0:
        return (x ** 2) % 7
    elif x > 100:
        return (x // 3) % 5
    else:
        return (x + 13) % 11

# Irrelevant helper function (dead code path)
def deprecated_filter(val):
    return val >> 2 & 1

# Sensor simulation constants
calibration_offsets = [3, -7, 12, 0, 5]
signal_mask = (1 << 6) - 1  # 63
redundant_flag = False

# Simulated sensor readings (with decoy entries)
sensor_data = [
    42, 87, 15, 93, 58, 21, 66, 74, 33, 50,
    105, -8, 71, 44, 82, 59, 27, 68, 39, 47
]

# Unused diagnostic array (distractor)
diag_history = [0] * 10

# Complex calibration key involving bitwise and arithmetic ops
calibration_base = 0b110101
calibration_shift = len(calibration_offsets)  # 5
calibration_key = (calibration_base ^ 42) << (calibration_shift % 4)

# Secondary mask computed but only partially used
interim_mask = sum([i for i in calibration_offsets if i > 0]) % 29  # 27

# Data transformation with slicing and filtering
cleaned = [analyze_signal(x) for x in sensor_data]
filtered = cleaned[::2]  # Take every other element
processed = filtered[1:7]  # Slice out center segment

# Dummy operations with misleading intermediate results
accum = 0
for idx, val in enumerate(processed):
    accum += (val ^ idx) & 3
    if accum > 10:
        accum = accum % 7

# Decoy assignment chain
status_flags = {'init': True, 'ready': False, 'locked': True}
temp_diagnostic = accum * 2 + 1  # Not used later

# Core logic hidden among noise
primary_weight = sum(processed) // len(processed)
secondary_score = (processed[0] + processed[-1]) % 17
tertiary_pattern = (processed[2] ^ processed[4]) & signal_mask

# Multiple data structures with cross-reference
lookup_table = {
    0: 91, 1: 73, 2: primary_weight, 3: 88, 4: secondary_score
}

# Another red herring computation
checksum = 0
for k, v in lookup_table.items():
    checksum ^= (k + v) % 10

def process_readings(data_slice, key):
    base_value = sum(data_slice) + (key & 255)
    adjustment = base_value % 9
    if adjustment < 5:
        result = base_value // 3
    else:
        result = (base_value * 2) // 5
    # Final transformation using bit manipulation and rounding
    result = (result ^ key) & 0xFFFF
    return int(round(result / 1.7))

# Execute critical statement
final_diagnostic = process_readings(processed, calibration_key)

# Output the target result
print(f"Target result: {final_diagnostic}")