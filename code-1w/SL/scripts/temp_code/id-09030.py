def preprocess_input(raw):
    # Irrelevant preprocessing with decoy transformations
    temp = [x * 1.5 + 2 for x in raw if x > 0]
    normalized = [n / max(temp) for n in temp]
    return [round(n, 3) for n in normalized]

# Dead function - never called
def auxiliary_transform(seq):
    return [seq[i] ^ i for i in range(len(seq))]

# Decoy data structures
decoys = {
    'offsets': [3, 1, 4, 1, 5],
    'flags': [True, False, True],
    'junk_data': list(range(100, 110))
}

# Actual working data
raw_data = [8, 12, 5, 16, 3]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Distractor: complex-looking but unused calculation
aggregate = sum([a * b for a, b in zip(raw_data, raw_data[::-1])]) // len(raw_data)

# Another red herring: bitmask analysis (unused)
binary_flags = []
for num in raw_data:
    bit_count = bin(num).count('1')
    parity = 'even' if bit_count % 2 == 0 else 'odd'
    binary_flags.append(parity)

# Conditional expression with misleading intermediate
status = 'valid' if all(x > 0 for x in raw_data) else 'invalid'

# Real computation begins here
processed = preprocess_input(raw_data)

# Key distraction: multiple similar functions
def compute_weighted_sum(values, w):
    # This function is NOT used; deliberate misdirection
    return sum(v * w[i] for i, v in enumerate(values))

# Used function: applies non-linear transformation before weighting
def compute_final_score(vals, ws):
    # Apply logarithmic scaling to dampen large values
    scaled = [v if v <= 1 else (v ** 0.5) for v in vals]
    
    # Introduce early return red herring (never triggered)
    if len(ws) != len(scaled):
        return -999
    
    total = 0.0
    for idx, (val, weight) in enumerate(zip(scaled, ws)):
        # Simulate feature interaction
        adjustment = 1.0
        if idx > 0 and scaled[idx-1] > 1.5:
            adjustment = 0.9
        total += val * weight * adjustment
    
    # Additional logic step: apply bonus if sum exceeds threshold
    if total > 2.0:
        total += 0.5
    
    # Final nonlinear cap
    total = round(total ** 1.1, 6)
    
    # Dead code block: unreachable due to above logic
    if total < 0:
        total = abs(total)
        total *= 0.5
    
    return total

# Unused alternate version
final_score_alt = sum(processed) * 0.8

# Critical execution point
final_score = compute_final_score(data=processed, weights=weights)

# Output result as required
print(f"Target result: {final_score}")