import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    return sum(-x * math.log2(x) for x in data if x > 0)

# Unused transformation (dead code path)
def legacy_transform(x):
    return (x ** 2 + 3 * x + 1) % 7

# Real processing chain begins
raw_signal = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4]

def normalize(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

def apply_filter(signal, kernel=lambda w: math.sin(w)):
    filtered = []
    for i in range(len(signal)):
        # Simulate convolution with sine-based kernel
        value = signal[i] * kernel(i * 0.5)
        filtered.append(abs(value))
    return filtered

# Distractor variables
baseline_offset = 0.37
reference_map = {i: round(math.cos(i), 3) for i in range(8)}
temp_checksum = sum(int(100 * v) for v in reference_map.values())

normalized_data = normalize(raw_signal)
applied_noise_correction = [x + 0.01 * math.tan(x) for x in normalized_data]  # red herring

# Actual relevant transformation
transformed_data = apply_filter(normalized_data)

# Decoy conditional block (never executed due to fixed condition)
if min(transformed_data) > 1.0:
    transformed_data = [math.log(x) for x in transformed_data]
elif max(temp_checksum, 999) == 999:
    transformed_data = [x * 1.5 for x in transformed_data]

# Thresholding logic with lambda abstraction
def threshold_func(x, limit=0.45):
    return int(x > limit)

# Diagnostic analyzer with nested logic
def analyze_pattern(seq, decision_rule):
    binary_seq = [decision_rule(x) for x in seq]
    
    # Compute rolling features (some irrelevant)
    pattern_weights = []
    for i in range(len(seq)):
        weight = 0
        if i > 0:
            weight += abs(seq[i] - seq[i-1]) * 100
        if i < len(seq) - 1:
            weight += math.sqrt(abs(seq[i+1] - seq[i])) * 50
        pattern_weights.append(round(weight, 2))
    
    # Irrelevant clustering attempt
    cluster_flag = False
    if len([w for w in pattern_weights if w > 20]) > 3:
        cluster_flag = True
    
    # Key diagnostic logic (hidden among distractors)
    activation_count = sum(binary_seq)
    transition_events = 0
    for j in range(1, len(binary_seq)):
        if binary_seq[j] != binary_seq[j-1]:
            transition_events += 1
    
    # Hidden calculation: this is where the answer comes from
    diagnostic_score = 0
    for idx, val in enumerate(transformed_data):
        if val > 0.45:
            diagnostic_score += int((val * 100) // (idx + 1))
    
    # Final computation using only specific elements
    focus_sum = sum(int(100 * transformed_data[i]) for i in [1, 3, 5])
    adjustment = activation_count * transition_events
    
    final_diagnostic = focus_sum - adjustment + diagnostic_score
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

# Print result as required
print(f"Target result: {final_diagnostic}")