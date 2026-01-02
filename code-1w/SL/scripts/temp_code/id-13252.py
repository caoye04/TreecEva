import math

# Simulated sensor data processing with red herrings and complex flow
def preprocess_sensor(stream, mode='calibrate'):
    if mode == 'calibrate':
        return [x * 1.05 for x in stream]
    elif mode == 'filter':
        return [x for x in stream if x > 0]
    else:
        return stream[::-1]

# Irrelevant transformation: audio-specific, not used in final path
def apply_fourier(signal):
    result = []
    for i in range(len(signal)):
        coeff = 0
        for j in range(len(signal)):
            angle = 2 * math.pi * i * j / len(signal)
            coeff += signal[j] * (math.cos(angle) - math.sin(angle))
        result.append(round(coeff, 3))
    return result

# Distractor function: looks important but unused
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Real transformation chain
base_signal = [12, -8, 15, 7, 0, -3, 9]
offset_corrected = [x + 5 for x in base_signal]  # Shift to eliminate negatives early
filtered_data = [x for x in offset_corrected if x % 2 == 1]  # Keep only odds

# Multi-step mapping with lambda and conditional expression
mapper = lambda val: val ** 2 if val < 10 else val + 10
mapped_data = [mapper(x) for x in filtered_data]

# Red herring: complex bit manipulation on unrelated copy
tainted_copy = mapped_data.copy()
for i in range(len(tainted_copy)):
    if tainted_copy[i] > 20:
        # Bit twiddling that affects nothing
        tainted_copy[i] = (tainted_copy[i] << 1) ^ 7 | 3
    else:
        tainted_copy[i] = (tainted_copy[i] >> 1) & 15

# Actual relevant transformation
transformed_data = []
for x in mapped_data:
    if x < 50:
        transformed_data.append((x * 3) % 17)
    else:
        transformed_data.append(int(math.sqrt(x)))

# Decoy data structure
audit_log = {
    'raw_checksum': sum(base_signal) ^ 0xFF,
    'interim_peak': max(mapped_data),
    'processing_steps': 7,
    'validations_passed': False  # Misleading status
}

# Core analysis function with nested logic
def analyze_pattern(seq):
    if not seq:
        return -1
    
    # Conditional expression with embedded logic
    base_score = sum(x if x % 3 == 0 else (-x if x % 5 == 0 else 0) for x in seq)
    
    # Multiple nested conditions
    bonus = 0
    for x in seq:
        if x > 5:
            if any(y == x-1 for y in seq):  # Check for consecutive
                if x % 2 == 0:
                    bonus += 3
                else:
                    bonus += 5
        if x == 13:
            bonus += 10  # Superstition-based decoy, never triggered
    
    # Final adjustment using modular arithmetic and length
    n = len(seq)
    adjustment = (bonus * n) % 11
    
    # Key calculation
    raw_result = base_score + adjustment
    
    # Final nonlinear scaling
    return int(raw_result * 1.5) if raw_result > 0 else int(raw_result * 0.5)

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data)

# Dead code path: never executed
if __debug__:
    verify_chain = apply_fourier(base_signal)
    audit_log['final_integrity'] = compute_entropy(verify_chain)

print(f"Result: {final_diagnostic}")