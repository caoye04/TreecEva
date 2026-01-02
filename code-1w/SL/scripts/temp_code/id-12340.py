def analyze_pattern(sequence):
    """Irrelevant function: analyzes sequence patterns but not used in main logic."""
    count = 0
    for i in range(len(sequence)):
        if sequence[i] % 2 == 0:
            count += (i * sequence[i]) % 7
    return count

# Unused helper that looks important
def compute_entropy(arr):
    import math
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0
    total = len(arr)
    for v in freq.values():
        p = v / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Distractor variables
temp_buffer = [x**2 + 2*x + 1 for x in range(8)]
shadow_mask = sum([i << 2 for i in temp_buffer if i % 3 == 0])

# Real data
raw_data = [15, 22, 8, 33, 41, 19]
weights = [0.1, 0.3, 0.15, 0.25, 0.05, 0.1]

# Bit manipulation decoy
cipher_key = 0
for val in raw_data:
    cipher_key ^= (val & 255) >> 4

# Simulated sensor flags (some relevant, some not)
sensor_flags = {'temp': True, 'pressure': False, 'flow': True, 'calib': None}
status_codes = [200, 404, 503, 200, 200]
valid_codes = {code for code in status_codes if code == 200}  # set usage

# Core transformation pipeline
def transform_entry(val, idx, offset=10):
    adjusted = val - offset
    if idx % 2 == 0:
        adjusted = abs(adjusted ^ 7)  # XOR distraction with partial relevance
    else:
        adjusted = adjusted | 3  # OR operation red herring
    return max(adjusted, 1)  # ensure positive

def extract_features(data_list):
    indexed = []
    # enumerate and zip usage (required python features)
    for i, val in enumerate(data_list):
        transformed = transform_entry(val, i)
        score = transformed * (i + 1)
        indexed.append((i, val, transformed, score))
    
    # zip in action - looks like aggregation but only one part matters
    indices, _, _, scores = zip(*indexed)
    base_total = sum(scores) // len(scores) if scores else 0
    
    # Decoy statistic
    peak_ratio = max(scores) / min(scores) if min(scores) > 0 else 0
    
    return base_total  # Only this is used later

# Secondary weight adjustment - mostly irrelevant
adjusted_weights = []
for w in weights:
    adj_w = w * 1.1
    if adj_w > 0.2:
        adj_w = adj_w * 0.95  # minor perturbation
    adjusted_weights.append(round(adj_w, 4))

scaling_factor = 1.0
if len(raw_data) > 5:
    scaling_factor *= 0.9

# Main processing function
def process_metrics(dataset, influence):
    feature_base = extract_features(dataset)
    
    # Weighted sum using original weights, not adjusted_weights (distractor!)
    weighted_sum = 0.0
    for i, w in enumerate(influence):
        if i < len(dataset):
            weighted_sum += w * dataset[i]
    
    # Combine paths
    hybrid = (feature_base * 0.6) + (weighted_sum * 0.4)
    
    # Final nonlinear adjustment
    if hybrid > 30:
        hybrid = hybrid * 0.85 + 5
    elif hybrid > 20:
        hybrid = hybrid * 0.9
    else:
        hybrid = hybrid * 1.05
    
    # Critical masking via bitwise AND with scaling factor
    int_part = int(hybrid)
    masked = int_part & 0xFF  # Keep lower 8 bits
    
    # Final computation
    penalty = sum(1 for flag in sensor_flags.values() if flag is False)
    final_value = masked - penalty * 2
    
    # Dead code path (never executed due to data)
    if cipher_key > 1000:
        final_value = final_value ^ shadow_mask
    
    return final_value

# Execution point of interest
data = raw_data.copy()
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")