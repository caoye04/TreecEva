from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def analyze_entropy(seq):
    freq = defaultdict(int)
    for c in seq:
        freq[c] += 1
    entropy = 0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 3)

# Misleading transformation chain
def transform_sequence(raw_seq):
    temp_a = [x ^ 3 for x in raw_seq if x % 2 == 1]
    temp_b = [x + 5 for x in temp_a if x < 20]
    padding = [0] * (8 - len(temp_b)) if len(temp_b) < 8 else []
    return temp_b + padding  # Dead-end result

# Core logic disguised among distractions
def generate_threshold_map(keys, base_offset):
    mapping = defaultdict(float)
    for k in keys:
        if k % 3 == 0:
            mapping[k] = abs(math.sin(k + base_offset)) * 100
        elif k % 5 == 0:
            mapping[k] = abs(math.cos(k + base_offset)) * 50  # Partially unused
        else:
            mapping[k] = 25.0
    return mapping

# Distractor: Unused recursive function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Real computation with embedded noise
def compute_pattern_weights(signal, mask):
    weights = []
    offset = len(mask) // 2
    
    # Actual relevant loop
    for i in range(len(signal)):
        center = signal[i]
        left = signal[i - 1] if i > 0 else 0
        right = signal[(i + 1) % len(signal)]
        
        # Meaningful calculation
        neighborhood = left ^ right | center
        if neighborhood in mask:
            weights.append(neighborhood * mask[neighborhood])
        else:
            weights.append(1)
    
    # Red herring aggregation
    avg_weight = sum(weights) / len(weights)
    peak = max(weights)
    score = (avg_weight * 0.7) + (peak * 0.3)
    return round(score, 4)

# Main activation logic
def compute_activation(pattern, thresholds):
    accumulator = 0
    for idx, val in enumerate(pattern):
        if val in thresholds:
            contribution = int(thresholds[val]) * (idx + 1)
            accumulator += contribution
        else:
            accumulator += val % 7
    
    # Final nonlinear scaling
    if accumulator > 100:
        return int(math.log(accumulator) * 10)
    else:
        return accumulator + 10

# --- Execution Body ---

# Initial data (real input)
raw_signal = [12, 15, 9, 21, 7, 18, 3]

# Irrelevant sequence analysis (distractor)
char_stream = "aabbcdef"
char_count = defaultdict(int)
for ch in char_stream:
    char_count[ch] += 1

# Generate misleading intermediate values
entropy_value = analyze_entropy(char_stream)  # Used nowhere
transformed = transform_sequence(raw_signal)  # Not used in final path

# Real control flow buried in conditionals
if len(raw_signal) > 5:
    key_indices = [x for x in raw_signal if x > 10]
    offset_val = sum(x for x in raw_signal if x % 3 == 0)
    
    # This call is critical
    threshold_map = generate_threshold_map(key_indices, offset_val)

    # Noise: unused recursion
    fib_values = [fibonacci(i) for i in range(5)]  # fib not used

    # Construct pattern through bit manipulation
    final_pattern = []
    for x in raw_signal:
        shifted = (x << 1) & 31
        toggled = shifted ^ 7
        if toggled % 2 == 0:
            final_pattern.append(toggled + 2)
        else:
            final_pattern.append(toggled - 1)
    
    # Actual answer depends on this line
    activation_score = compute_activation(final_pattern, threshold_map)

    # More red herrings
    secondary_score = compute_pattern_weights(final_pattern, threshold_map)
    baseline = sum(final_pattern) / len(final_pattern)
    adjusted = baseline * (1 + entropy_value / 100)

# Output target variable
print(f"Result: {activation_score}")