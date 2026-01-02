import math

# Simulated sensor data preprocessing pipeline
raw_readings = [3.2, 5.7, 1.8, 9.9, 4.3, 7.1, 2.5, 6.6]

def apply_calibration(x):
    return x * 1.08 - 0.3

calibrated = list(map(apply_calibration, raw_readings))

# Irrelevant transformation chain (distractor)
dummy_weights = [0.1, 0.3, 0.2, 0.4]
weight_sum = sum(dummy_weights)
normalized_weights = [w / weight_sum for w in dummy_weights]
weighted_avg = sum(calibrated[i] * normalized_weights[i % 4] for i in range(len(calibrated)))

# Red herring: unused statistical analysis
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data if x > 0]
    return -sum(p * math.log(p) for p in probs)

entropy_value = compute_entropy(calibrated)  # Dead computation

# Real processing begins here
baseline_offset = 0.87
adjusted = [math.pow(x + baseline_offset, 0.92) for x in calibrated]

# Noise filter simulation
def smooth_sequence(seq):
    result = [seq[0]]
    for i in range(1, len(seq) - 1):
        result.append((seq[i-1] + 2*seq[i] + seq[i+1]) / 4)
    result.append(seq[-1])
    return result

filtered = smooth_sequence(adjusted)

# Decoy function that looks important but isn't used in critical path
def deprecated_analysis(arr):
    peak = max(arr)
    valley = min(arr)
    return (peak - valley) / (peak + valley + 1e-8)

contrast_ratio = deprecated_analysis(filtered)  # Misleading intermediate

# Actual signal extraction
signal_mask = [1 if x > 5.0 else 0 for x in filtered]
masked_values = [filtered[i] for i in range(len(filtered)) if signal_mask[i]]

# Secondary filtering based on dynamic threshold
reference_key = sum([int(x * 10) % 7 for x in masked_values])

def generate_threshold_basis(n):
    series = [1, 1]
    for i in range(2, n):
        series.append(series[i-1] + series[i-2])
    return series

threshold_basis = generate_threshold_basis(reference_key % 6 + 5)  # Partially used
active_threshold = threshold_basis[-1] / 100.0

# Data transformation using lambda abstraction
transformer = lambda val: math.sin(val) + math.log(val + 1) if val > 0 else 0
transformed_data = [transformer(x) for x in masked_values]

# Spurious complexity: unused alternate transform
def alt_transform(z):
    if z < 0:
        return math.exp(z)
    elif z < 3:
        return z ** 1.5
    else:
        return math.sqrt(z) + 1

# Threshold function with closure (critical component)
base_floor = 0.45
def make_threshold(fixed_offset):
    def threshold_rule(x):
        return x > (active_threshold + fixed_offset) and x < 10.0
    return threshold_rule

threshold_func = make_threshold(base_floor)

# Core processing function
def process_metrics(values, validator):
    valid_count = 0
    total_score = 0.0
    for v in values:
        if validator(v):
            valid_count += 1
            total_score += v * v  # Emphasis on higher values
    
    # Final adjustment using bit manipulation (obscure but relevant)
    adjustment_factor = valid_count ^ 7  # XOR-based modulation
    if adjustment_factor == 0:
        adjustment_factor = 1
    
    # Introduce fractional decay based on count
    decay_rate = 1.0 / (valid_count + 1)
    net_result = (total_score * adjustment_factor) * (1 - decay_rate)
    
    # Dead code branch (never reached due to logic above)
    if valid_count > 100:
        backup_mode = True
        net_result = sum(values) / (adjustment_factor or 1)
    
    return net_result

# Critical assignment
final_diagnostic = process_metrics(transformed_data, threshold_func)

# Output requirement
print(f"Target result: {final_diagnostic}")