def preprocess_signal(data, threshold=0.5):
    """Irrelevant preprocessing function for signal filtering (dead code path)."""
    filtered = []
    for x in data:
        if abs(x) > threshold:
            filtered.append(x * 0.8)
    return filtered


def validate_checksum(sequence):
    """Misleading checksum validation (not used in actual logic)."""
    return sum(sequence) % 7 == 0


def transform_entry(val, shift):
    """Bit manipulation decoy - looks important but unused in main path."""
    shifted = (val << 2) ^ 5
    return shifted + shift

# Simulated sensor data streams (some irrelevant)
sensor_a = [1.2, 0.8, 3.1, 2.5, 4.0]
sensor_b = [0.9, 1.1, 2.8, 3.3, 3.9]
sensor_c = [1.0, 1.0, 1.0, 1.0, 1.0]  # Red herring: constant values

# Weight vectors with decoys
weights = [0.1, 0.2, 0.3, 0.2, 0.2]
alt_weights = [0.5, 0.1, 0.1, 0.1, 0.2]  # Unused alternative

# Irrelevant transformation matrix
decoymatrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
trace_sum = sum(decoymatrix[i][i] for i in range(3))  # Distractor computation

# Simulated transmission frames with metadata
corrupted_mask = [False, True, False, True, False]
frame_ids = [1001, 1002, 1003, 1004, 1005]

def extract_reliable_transmissions(sources, masks):
    """Filter out corrupted transmissions - actually used."""
    cleaned = []
    for idx, mask in enumerate(masks):
        if not mask:
            val = (sources[0][idx] + sources[1][idx]) / 2.0
            cleaned.append(val)
    return cleaned

transmissions = extract_reliable_transmissions([sensor_a, sensor_b], corrupted_mask)

# Decoy list comprehension with zip and enumerate (irrelevant)
_ = [f"{i}:{k}:{round(v,1)}" for i, (k,v) in enumerate(zip(frame_ids, sensor_c)) if v > 0.5]

# Real processing begins here
status_flags = [1 if x > 2.0 else 0 for x in transmissions]
activation_count = sum(status_flags)

# Core aggregation logic
scaling_factor = 1.5 if activation_count >= 2 else 0.8

# Key computational function
def compute_aggregate(readings, w):
    temp_result = 0.0
    for i, r in enumerate(readings):
        weighted_val = r * w[i]
        temp_result += weighted_val
    
    # Final nonlinear adjustment
    if temp_result > 3.0:
        temp_result = temp_result ** 1.1
    else:
        temp_result = temp_result ** 0.9
    
    return int(temp_result * 1000)  # Scale up to integer

# Dummy recursive decoy (never called)
def recursive_denoise(arr, depth):
    if depth == 0 or len(arr) == 0:
        return [abs(x) for x in arr]
    return recursive_denoise([x*0.9 for x in arr], depth-1)

# Critical statement
final_score = compute_aggregate(transmissions, weights)

# Output result
print(f"Result: {final_score}")