import math

# Simulated sensor array diagnostics with embedded interference
def analyze_sensor_array(raw_readings, threshold_multiplier=1.3):
    normalized = [x * 0.98 for x in raw_readings if x > 0]
    filtered = [val for val in normalized if math.sin(val) > -0.7]
    
    # Irrelevant transformation (dead path)
    inverted_map = {i: int(100 / (v + 1)) for i, v in enumerate(normalized)}
    decoy_sum = sum([inverted_map[k] for k in inverted_map if k % 2 == 0])  # unused

    # Actual signal extraction
    peak = max(filtered)
    base_level = sum(filtered) / len(filtered)
    fluctuation_index = (peak - base_level) / base_level
    
    # Distractor: complex but unused bit manipulation
    masked_values = []
    for v in filtered:
        shifted = int(v * 10) << 2
        masked = shifted ^ 0xFF
        masked_values.append(masked & 0xFFFF)
    
    # Another red herring: string-based checksum (never used)
    status_sig = "diagnostic_" + "_".join(map(str, [len(normalized), len(filtered), int(base_level)]))
    checksum = sum(ord(c) for c in status_sig if c.isdigit()) * 0.3

    # Real processing path begins here
    critical_band = [f for f in filtered if f > base_level * threshold_multiplier]
    return critical_band, base_level, fluctuation_index


def transform_sequence(seq, key):
    # Apply XOR shift cipher (distractor)
    ciphered = ''.join([chr((ord(c) ^ key) % 95 + 32) for c in seq])
    reversed_chunks = [ciphered[i:i+3][::-1] for i in range(0, len(ciphered), 3)]
    
    # Unused decoding attempt
    try:
        decoded = ''.join([chunk[::-1] for chunk in reversed_chunks])
    except:
        decoded = "error"
    
    # Real action: return length-based metric
    return len(seq) % 7

# Decoy data structure - looks important but unused
system_registry = {
    'nodes': ['A1', 'B2', 'C3'],
    'active': True,
    'version': '3.7.1',
    'payload': [transform_sequence('encrypted_stream', 42), 0, 0]
}

# High-interference main logic
raw_input_stream = [12.4, -1.2, 15.6, 0.0, 18.1, 9.8, 22.3, -3.4, 17.9, 14.2]

# Dead computation branch with misleading intermediate result
temp_snapshot = raw_input_stream[::2]  # every other reading
snapshot_avg = sum(temp_snapshot) / len(temp_snapshot)
snapshot_flag = 'EVEN_ONLY' if snapshot_avg > 15 else 'LOW_EVEN'

# Begin real diagnostic chain
primary_band, base_ref, index_var = analyze_sensor_array(raw_input_stream, 1.3)

# Complex conditional distractor (appears to modify logic but doesn't)
case_weight = 1.0
if len(primary_band) > 3:
    case_weight *= 1.1
elif index_var > 0.4:
    case_weight *= 0.9
    backup_frame = [math.log(x + 1) for x in raw_input_stream]  # dead end
else:
    case_weight = 0.8

# Red herring: set operations that seem relevant
unique_primary = set(round(p, 1) for p in primary_band)
expected_set = {12.1, 15.3, 17.7, 21.8, 17.9}
difference_score = len(expected_set - unique_primary) * 2.5  # unused

# Real accumulation with slicing distraction
working_buffer = primary_band + [base_ref * 1.1, index_var * 5]
trimmed = working_buffer[1:-1]  # remove first and last
accum = 0
for i, val in enumerate(trimmed):
    if i % 2 == 0:
        accum += val * 0.7
    else:
        accum += val * 0.3

# String method distractor
debug_tag = "sensor_flow|stage_2|mode_A"
segments = debug_tag.split('|')
valid_modes = [s for s in segments if s.startswith('mode')]
mode_value = ord(valid_modes[0][-1]) if valid_modes else 65  # unused

# Key function with multiple responsibilities and distractions
def aggregate_metrics(data_chunk, offset):
    # Set operation that appears significant
    history_log = set()
    for d in data_chunk:
        history_log.add(round(d * 2) // 2)
    
    # Bit manipulation decoy
    flag_register = 0
    for d in history_log:
        flag_register ^= int(d) & 0xF
        flag_register = (flag_register << 1) | (flag_register >> 3)
        flag_register &= 0xFF
    
    # Real calculation buried in noise
    base_total = sum(d ** 0.5 for d in data_chunk)  # sqrt sum
    adjustment = math.cos(offset % math.pi)
    temp_result = base_total * adjustment
    
    # Final step using prior accumulated value
    global accum
    final_component = accum * 0.4 + temp_result * 0.6
    
    # Distraction: unused dictionary aggregation
    summary_stats = {
        'count': len(history_log),
        'flag': flag_register,
        'adjusted': round(final_component, 2)
    }
    
    return int(round(final_component))

# Trigger execution
base_offset = 4.7
interim_diagnostic = transform_sequence('validation_key', 13)
temp_data = primary_band[:]

# Critical statement
final_diagnostic = aggregate_metrics(temp_data, base_offset)

print(f"Result: {final_diagnostic}")