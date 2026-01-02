import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 100

# Misleading transformation chain
def transform_signal(value):
    if value < 0:
        value = abs(value)
    temp = value * 1.5
    temp = int(temp ^ 0b1101)  # Bitwise red herring
    temp += sum([i for i in range(3) if i % 2])  # List comprehension with constant result
    return temp

# Simulate sensor drift (unused in final logic)
def apply_drift(samples):
    return [s + 0.01 * idx for idx, s in enumerate(samples)]

# Core processing pipeline
def decode_sequence(seq):
    decoded = []
    for item in seq:
        if item % 2 == 0:
            decoded.append(item // 2)
        else:
            decoded.append(item * 3 + 1)
    return decoded

def filter_anomalies(values):
    threshold = sum(values) / len(values)
    return [v for v in values if v <= threshold]  # List comprehension used meaningfully

def compute_checksum(arr):
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= (val + i) & 0xFF
    return checksum

def recursive_condense(lst):
    if len(lst) <= 1:
        return lst[0] if lst else 0
    return recursive_condense([lst[i] + lst[i+1] for i in range(0, len(lst)-1, 2)])

# Main data processor
def process_pipeline(stream):
    # Step 1: Decode the sequence
    stage1 = decode_sequence(stream)
    
    # Step 2: Filter anomalies
    stage2 = filter_anomalies(stage1)
    
    # Step 3: Transform (applies deterministic but misleading bit manipulation)
    stage3 = [transform_signal(x) for x in stage2]
    
    # Step 4: Condense using recursive pairing
    condensed = recursive_condense(stage3)
    
    # Step 5: Compute checksum
    chk = compute_checksum(stage3)
    
    # Step 6: Apply final adjustment
    adjusted = (condensed * 2) ^ chk  # XOR with checksum
    
    # Dead variables - irrelevant computations
    debug_trace = [legacy_calculate(n) for n in stream]
    drift_corrected = apply_drift(stream)
    dummy_aggregate = sum(drift_corrected) / len(drift_corrected)
    
    # Final output calculation
    scaling_factor = math.sin(math.pi / 4)  # ~0.707, constant
    preliminary = int(adjusted * scaling_factor)
    final_output = preliminary + 5  # Critical offset
    
    return final_output

# Simulated input data stream
initial_seed = [17, 8, 22, 5, 13, 4]
data_stream = initial_seed.copy()

# Execute main logic
final_output = process_pipeline(data_stream)
print(f"Target result: {final_output}")