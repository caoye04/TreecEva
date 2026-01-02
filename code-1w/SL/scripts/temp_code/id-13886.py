def preprocess_sequence(seq, config):
    # Irrelevant transformation branch
    if len(seq) > 100:
        return [x ** 0.5 for x in seq if x % 2 == 0]
    else:
        return [x for x in seq if x > 0]

# Misleading data initialization
dummy_cache = [i * 3 + 2 for i in range(15)]
lookup_matrix = [[i + j for j in range(5)] for i in range(5)]

# Real signal parameters
pattern_buffer = [64, 25, 9, 100, 49]
scaling_factor = 2.5
offset_correction = -1.2

# Decoy statistical summary (never used in final result)
stat_summary = {
    'mean': sum(dummy_cache) / len(dummy_cache),
    'max': max(dummy_cache),
    'entropy': 3.14159
}

# Threshold configuration with red herring entries
threshold_map = {
    'low_power': 8,
    'high_noise': 20,
    'edge_case': 5,
    'activation': 7,
    'deprecated_mode': 99  # Unused parameter
}

# Simulated sensor flags (partially relevant)
sensor_flags = {
    'calibrated': True,
    'override': False,
    'debug_mode': True  # Distractor
}

# Auxiliary function that appears important but is never called
def compute_hamming_weight(value):
    weight = 0
    while value:
        weight += value & 1
        value >>= 1
    return weight

# String-based identifier processing (seemingly unrelated but actually filters logic)
device_tag = "SENSOR_DIAGNOSTIC_V2"
token_filter = device_tag.lower().replace("_v", "").split("_")

# Conditional bypass that looks significant but always evaluates to False
if sensor_flags['debug_mode'] and not sensor_flags['override']:
    scaling_factor *= 0.5

# Key transformation: only certain roots are accepted based on threshold
root_candidates = []
for val in pattern_buffer:
    root = int(val ** 0.5)
    if root >= threshold_map['activation']:
        root_candidates.append(root)

# Secondary filter based on string token presence (uses token_filter)
filtered_roots = []
category_key = ''
if 'DIAGNOSTIC' in token_filter:
    category_key = 'critical'
    filtered_roots = [r for r in root_candidates if r % 2 == 1]  # Only odd roots kept
else:
    category_key = 'standard'
    filtered_roots = root_candidates

# Accumulation with offset and scaling (core calculation)
accumulated_score = 0
for idx, r in enumerate(filtered_roots):
    accumulated_score += (r + idx) * scaling_factor

# Bit manipulation decoy
bit_accum = 0
for x in dummy_cache[:10]:
    bit_accum ^= (x & 0xF)

# Control flow with dead branch
status_code = 200
if status_code == 404:
    fallback_value = sum(bit_accum, 100)
elif status_code == 500:
    fallback_value = -1

# Final analysis function combining multiple concepts
def analyze_signal(signal, thresholds):
    base = sum(signal)
    adjustment = len(signal) * offsets['shift'] if 'shift' in offsets else 0
    return int(base + adjustment)

# Offsets dictionary with misleading keys
offsets = {
    'padding': 0.5,
    'jitter': 1.1,
    'delta_t': 0.01
    # Note: 'shift' key is missing — intentional dead path
}

# Critical execution point
final_diagnostic = analyze_signal(filtered_roots, threshold_map)

# Extraneous logging output
log_entry = f"Final state: {category_key.upper()}, Code={status_code}"

# Output result as required
print(f"Result: {final_diagnostic}")