def analyze_pattern(sequence, base_offset):
    if len(sequence) < 3:
        return 0
    
    # Irrelevant transformation (distractor)
    inverted = [base_offset * 2 + (i ^ 7) for i in range(len(sequence))]
    temp_sum = sum(inverted[:5]) if len(inverted) > 5 else sum(inverted)
    
    # Core logic disguised among noise
    transformed = list(map(lambda x: (x ** 2) % 97, sequence))
    accumulated = 0
    for idx, val in enumerate(transformed):
        if idx % 2 == 0 and val > 10:
            accumulated += val * (idx + 1)
        elif val <= 10:
            accumulated -= val

    # Dead path - never reached due to prior conditions
    if len(sequence) == 100:
        return -999  # decoy value

    return accumulated if accumulated != 0 else 99

# Unused helper function (red herring)
def validate_entry(code, rules):
    mask = sum([code & (1 << i) for i in range(8)])
    return mask in rules

# Distractor data structures
config_cache = {
    'mode': 'debug',
    'flags': [1, 1, 0, 1],
    'payload': 0xABCDE,
    'checksum': lambda x: (x * 31) % 65537
}

# Another red herring variable
buffer_overflow_sim = [i ^ (i >> 3) for i in range(10)]

# Primary input with mixed relevance
logic_flow = [3, 7, 12, 15, 8, 21, 4, 18]

# Threshold map contains both relevant and irrelevant keys
threshold_map = {
    'alpha': 5,
    'beta': 14,
    'gamma': 99,  # unused
    'delta': 12   # used as filter threshold
}

# Decoy control flow with early break
status_flags = []
for k in range(4):
    if k == 5:  # unreachable
        status_flags.append(True)
        break
    status_flags.append(False)

# Simulated preprocessing (partially relevant)
processed_inputs = []
for item in logic_flow:
    processed = item
    if item > threshold_map['beta']:
        processed = item - 7
    elif item < threshold_map['alpha']:
        processed = item + 5
    processed_inputs.append(processed)

# Key computation buried in abstraction
intermediate_score = analyze_pattern(processed_inputs, threshold_map['alpha'])

# Secondary distractor: bit manipulation with no downstream use
aggregate_flag = 0
for b in buffer_overflow_sim:
    aggregate_flag ^= (b << 2) | 0x3

# Real answer derivation path
scaling_factor = 3
adjustment = len([x for x in processed_inputs if x > threshold_map['delta']])
raw_diagnostic = intermediate_score * scaling_factor - (adjustment ** 2)

# Final mapping using lambda (core python feature)
classify = lambda x: x + 10 if x < 100 else x - 10
final_diagnostic = classify(raw_diagnostic)

# Additional misleading print (not the target)
# print(f"Debug: {temp_sum}, Flag: {aggregate_flag}")

print(f"Target result: {final_diagnostic}")