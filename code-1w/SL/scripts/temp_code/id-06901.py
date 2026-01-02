import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(math.sqrt(i) > 1 for i in x if i > 0)

# Decoy transformation chain
def decoy_transform(seq):
    shifted = [i << 2 for i in seq]
    return [j ^ 7 for j in shifted if j % 3 != 0]

# Real processing components
def normalize_signal(x):
    return [round(v / 3.7, 4) for v in x]

def encode_phase(signal):
    return [int(s * 2.4) & 255 for s in signal]

def compute_checksum(encoded):
    return sum((c * 113) % 257 for c in encoded) // 7

# Key lambda: applies conditional amplification based on entropy threshold
amplify_if_stable = lambda values, thresh: [
    v * 13 if sum(1 for x in values if x < 100) / len(values) > thresh else v * 2
    for v in values
]

# Simulated sensor data ingestion (irrelevant case conversion included)
data_source = 'AcTiVe_SeNsOr_04'
source_active = any(c.isupper() for c in data_source)
data_stream = [861, 122, 94, 653, 117, 83, 992, 101]

# Misleading intermediate computation (not used in final result)
temp_analysis = []
for val in data_stream:
    bin_str = bin(val)[2:]
    ones_ratio = bin_str.count('1') / len(bin_str)
    category = 'HIGH' if ones_ratio > 0.6 else 'LOW'
    temp_analysis.append({"value": val, "entropy": ones_ratio, "class": category})

# Another red herring: complex but unused transformation tree
dummy_tree = {
    'level1': {
        'branch_a': [x ** 0.5 for x in data_stream],
        'branch_b': [math.log(max(x, 1)) for x in data_stream]
    },
    'level2': {
        'aggregated': sum([x * x for x in data_stream])
    }
}

# Actual core logic hidden among distractions
def process_pipeline(input_data):
    # Step 1: Normalize
    normalized = normalize_signal(input_data)
    
    # Step 2: Encode
    encoded = encode_phase(normalized)
    
    # Step 3: Apply amplification via lambda if stability condition met
    amplified = amplify_if_stable(encoded, 0.6)
    
    # Step 4: Filter out values below median using manual calculation
    sorted_vals = sorted(amplified)
    mid = len(sorted_vals) // 2
    median = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    filtered = [v for v in amplified if v >= median]
    
    # Step 5: Integer division rounding chain
    reduced = sum(filtered) // len(filtered)  # Integer division with truncation
    adjusted = int(round(reduced / 1.8))  # Final adjustment step
    
    # Step 6: Compute checksum from original encoding (cross-reference)
    chk = compute_checksum(encoded)
    
    # Final output derived from two independent paths
    return (adjusted * 3) + (chk % 19)

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output must be printed in required format
print(f"Result: {final_output}")