from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810]
raw_readings = [127, 255, 64, 191, 32]
error_flags = [False, True, False, False, True]

# Irrelevant auxiliary mappings (distractor)
legacy_mapping = {'A': 65, 'B': 66, 'C': 67}
unused_buffer = bytearray(b'\x00\x01\x02\x03')
placeholder_data = {k: v for k, v in zip('XYZ', [1.1, 2.2, 3.3])}

# Core processing structures
log_entries = [
    {'time': t, 'val': v, 'err': e} 
    for t, v, e in zip(timestamps, raw_readings, error_flags)
]

system_state = {
    'active': True,
    'mode': 'diagnostic',
    'cache': defaultdict(int),
    'version': '3.7.1'
}

# Decoy function – never called (dead code path)
def legacy_calibrate(x):
    return (x >> 2) ^ 0xFF

# Auxiliary transformation lambdas (some used, some not)
bit_mask = lambda x: x & 0x7F
amplify = lambda x: x * 1.5
invert = lambda x: 255 - x  # Unused distractor
normalize = lambda x: round(x / 255.0, 3)

# Misleading intermediate aggregates (red herrings)
spurious_sum = sum([len(legacy_mapping), len(unused_buffer)])
temp_offset = math.floor(math.log2(256))
fake_checksum = spurious_sum * temp_offset - 42  # Looks important, unused

# Real signal extraction
filtered_values = [
    entry['val'] for entry in log_entries 
    if not entry['err'] and entry['val'] > 50
]

# Bit manipulation and statistical summary
def compute_signature(values):
    if not values:
        return 0
    xor_fold = 0
    for v in values:
        xor_fold ^= bit_mask(v)  # Apply meaningful mask
    mean_val = sum(values) / len(values)
    peak = max(values)
    return int(mean_val + (peak ^ xor_fold))

# Complex stateful processor
def process_metrics(entries, state):
    if not state['active']:
        return -1
    
    # Extract clean readings
    valid_vals = [e['val'] for e in entries if not e['err']]
    if len(valid_vals) < 2:
        return 0
    
    # Compute multiple metrics (some irrelevant)
    stats = {}
    stats['count'] = len(valid_vals)
    stats['range'] = max(valid_vals) - min(valid_vals)
    stats['entropy'] = Counter(valid_vals).most_common(1)[0][1]  # Frequency as proxy
    
    # Destructuring assignment (tuple unpacking)
    first, *middle, last = sorted(valid_vals)
    
    # Nested logic with red herring branches
    adjustment = 0
    if state['mode'] == 'debug':
        adjustment = -999  # Dead branch
    elif state['mode'] == 'diagnostic':
        if stats['range'] > 100:
            adjustment = 10
        else:
            adjustment = 5
    
    # Meaningful computation chain
    sig = compute_signature(valid_vals)
    normalized_vals = list(map(normalize, valid_vals))
    avg_norm = sum(normalized_vals) / len(normalized_vals)
    
    # Key decoy variable (looks like it's used, but isn't)
    phantom_score = int(avg_norm * 1000) + fake_checksum
    
    # Actual formula
    base = sig + adjustment
    modifier = int((first + last) / 2)
    
    # Final calculation
    result = base * 2 - modifier
    
    # Cross-structure update (side effect, not result)
    state['cache']['diagnostic_run'] += 1
    
    return result

# Spurious precomputation (misdirection)
prelim_result = compute_signature(raw_readings)
dummy_pair = (prelim_result, fake_checksum)

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_state)

# Output requirement
print(f"Result: {final_diagnostic}")