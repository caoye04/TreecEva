import math

# Irrelevant helper function (decoy)
def compute_noise_factor(data):
    return sum([x ** 0.5 for x in data if x > 5])

# Misleading intermediate transformation
def transform_sequence(seq):
    shifted = [(x * 2 + 1) % 256 for x in seq]
    return [s ^ 42 for s in shifted]  # Bit manipulation red herring

# Unused but plausible-looking diagnostic function
def run_diagnostics(payload):
    if len(payload) < 10:
        return False
    checksum = 0
    for i, val in enumerate(payload):
        checksum += val * (i + 1)
    return checksum % 17 == 0

# Distractor: complex-looking but unused sorting logic
def hierarchical_sort(arr):
    arr_sorted = sorted(arr, reverse=True)
    mid = len(arr_sorted) // 2
    return arr_sorted[mid:] + arr_sorted[:mid]

# Core logic disguised among noise
logistical_vector = [8, 12, 16, 4, 20, 24]
scaling_factor = 0.75
system_phase = 'gamma'

# Irrelevant string-based distraction
diagnostic_tag = "SYS_GAMMA_DIAG_0x1C"
if 'GAMMA' in diagnostic_tag.lower():
    scaling_factor *= 1.1

# Fake state update
current_state = {'mode': 'idle', 'level': 0}
if current_state['mode'] == 'active':
    current_state['level'] += 1

# Real computation buried in distractions
def process_threshold(values, mode):
    base = sum(v ** 0.5 for v in values)  # Square root summation
    if mode == 'gamma':
        base *= 1.6
    return int(base)

# Another decoy function using bitwise and string methods
def encode_fragment(data_str):
    binary_rep = ''.join([bin(ord(c))[2:].zfill(8) for c in data_str[:4]])
    flipped = ''.join('1' if b == '0' else '0' for b in binary_rep[:32])
    return int(flipped, 2) >> 5

# Key function that computes the actual answer
def evaluate_thermal_response(inputs, phase):
    # Step 1: Filter relevant components
    filtered = [x for x in inputs if x % 4 == 0 and x > 6]
    
    # Step 2: Apply square and reduce
    squared = [x ** 2 for x in filtered]
    
    # Step 3: Sum and take logarithm
    total = sum(squared)
    log_total = math.log(total)  # ln(8^2 + 12^2 + 16^2 + 20^2 + 24^2) = ln(64+144+256+400+576)=ln(1440)
    
    # Step 4: Apply phase multiplier
    if phase == 'gamma':
        adjusted = log_total * 3.2
    else:
        adjusted = log_total * 2.1
    
    # Step 5: Add constant from conditional logic
    offset = 0
    tag_code = "THERM_3000"
    if tag_code.startswith("THERM") and tag_code.endswith("3000"):
        offset += 7
    
    # Step 6: Use string length in final adjustment
    flag_suffix = "_ADJ_Z"
    offset += len(flag_suffix)  # Adds 6
    
    # Final adjustment
    result = adjusted + offset  # ln(1440)*3.2 + 13
    return result

# Unused but plausible variable assignment
temporal_weights = [scaling_factor * i for i in range(1, 6)]

# Dead code path (never called)
if system_phase == 'delta':
    baseline = compute_noise_factor(logistical_vector)

# Real execution path
processed_input = transform_sequence(logistical_vector)  # Computed but not used

# Actual key statement
thermal_capacity = evaluate_thermal_response(logistical_vector, system_phase)

# Print result as required
print(f"Target result: {thermal_capacity}")