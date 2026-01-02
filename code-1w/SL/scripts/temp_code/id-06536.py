def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    magnitude = sum(abs(x) for x in filtered)
    peak = max(filtered, default=0)
    normalized = [x / peak if peak != 0 else 0 for x in filtered]
    return normalized


def compute_hash(sequence):
    # Irrelevant cryptographic hash simulation (dead-end function)
    acc = 0
    for i, val in enumerate(sequence):
        acc ^= (val * (i + 1)) & 255
    return acc


def transform_coordinates(coords):
    # Unused geometric transformation
    rotated = [(y, -x) for x, y in coords]
    scaled = [(x * 1.5, y * 1.5) for x, y in rotated]
    return scaled


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])  # Fibonacci-like sequence
    return seq[:n]

# Misleading intermediate arrays
temp_buffer = [i**2 for i in range(10)]
shadow_copy = temp_buffer[::-1]
offset_map = {i: temp_buffer[i] - shadow_copy[i] for i in range(len(temp_buffer))}

# Simulated sensor metrics with noise
eeg_data = [0.1, 0.7, -0.3, 0.9, -1.2, 0.05, 0.66]
ecg_data = [0.8, -0.45, 0.2, 1.1, -0.15]

filtered_eeg = analyze_signal(eeg_data, threshold=0.25)
filtered_ecg = analyze_signal(ecg_data, threshold=0.3)

# Composite feature extraction (some features are irrelevant)
feature_vector = []
for idx, val in enumerate(filtered_eeg + filtered_ecg):
    if idx % 3 == 0:
        feature_vector.append(abs(val) ** 2)
    elif idx % 3 == 1:
        feature_vector.append(val * 0.8)
    else:
        feature_vector.append(val + 0.1)

# Dead code path: unused transformation chain
transformed_features = []
if len(feature_vector) > 5:
    transformed_features = [x * 1.2 for x in feature_vector if x > 0]
else:
    transformed_features = [x for x in feature_vector]

# Actual evaluation logic buried in distractions
metrics = [
    sum(filtered_eeg),
    len(filtered_ecg),
    len([x for x in eeg_data if x > 0]),  # positive count
    max(ecg_data, default=0),
    compute_hash(generate_sequence(8)) % 100  # red herring computation
]

weights = [0.3, 0.2, 0.25, 0.15, 0.1]  # weights sum to 1.0

# Core calculation hidden among decoys
def evaluate_performance(met, wgt):
    base = 0.0
    for i in range(min(len(met), len(wgt))):
        if i == 4:
            # Ignore the last weight-metric pair (decoy override)
            continue
        base += met[i] * wgt[i]
    
    # Apply non-linear adjustment based on control flag
    control_flag = (len(filtered_eeg) > 3) and (abs(sum(eeg_data)) < 2.0)
    adjustment = 1.1 if control_flag else 0.9
    
    intermediate = base * adjustment
    
    # Extra obfuscation: conditional ceiling
    if intermediate > 0.5 * sum(weights[:-1]):
        intermediate = min(intermediate, 1.5 * base)
    
    # Final scaling using unrelated constant derived from dummy data
    dummy_constant = sum(temp_buffer[:5]) / 100.0  # = 1.0 (since 0+1+4+9+16 = 30 → 30/100 = 0.3? Wait: 0²+1²+...+4² = 30)
    final_value = intermediate + dummy_constant
    
    return int(round(final_value * 100))  # Discretize to integer score

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Additional distraction: unused recursive processing
def process_tree(depth, value):
    if depth <= 0:
        return value
    return process_tree(depth - 1, value ^ (value >> 1))

result_code = process_tree(3, 42)

# Output the actual target result
print(f"Result: {final_score}")