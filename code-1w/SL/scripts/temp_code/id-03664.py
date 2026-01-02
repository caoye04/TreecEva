import math

# Simulated sensor data from a distributed environmental monitoring system
def generate_sensor_readings():
    base_values = [2.1, 3.5, 4.0, 2.8, 5.2, 3.9, 4.7]
    noise = [0.1 * math.sin(i) for i in range(7)]
    return [base_values[i] + noise[i] for i in range(7)]

# Irrelevant auxiliary function – simulates temperature calibration (not used in final result)
def calibrate_temperature(raw_readings):
    adjusted = []
    for val in raw_readings:
        if val < 3.0:
            adjusted.append(val * 1.15)
        elif val > 4.5:
            adjusted.append(val * 0.92)
        else:
            adjusted.append(val)
    return adjusted

# Misleading transformation – appears important but unused in critical path
def transform_logarithmic(data):
    return [math.log(x + 1e-5) for x in data]

# Signal processing with multiple steps and distractors
def preprocess_signal(raw_data):
    # Step 1: Normalize using z-score (relevant)
    mean_val = sum(raw_data) / len(raw_data)
    variance = sum((x - mean_val) ** 2 for x in raw_data) / len(raw_data)
    std_dev = math.sqrt(variance)
    normalized = [(x - mean_val) / std_dev for x in raw_data]
    
    # Distractor: Apply dummy filter that's never used
    filtered_dummy = [x for x in normalized if x > -1.0]
    
    # Distractor: Create bit-mask pattern from signal (unused)
    bit_flags = []
    for x in normalized:
        flag = int((x * 100) % 8)
        bit_flags.append((flag << 2) ^ 5)
    
    # Actual relevant transformation: scale to [-5, 5]
    scaled = [max(-5.0, min(5.0, x * 2.5)) for x in normalized]
    return scaled

# Decoy analysis function – referenced in comments but not called
def legacy_analysis(signal):
    score = 0
    for x in signal:
        if x > 0:
            score += math.exp(-1/x)
        else:
            score -= math.exp(1/(x+1e-5))
    return abs(score)

# Core logic: detect anomalies using threshold crossings and parity check
# Combines boolean logic, list operations, and arithmetic

threshold = 3.0
def detect_anomalies(scaled_signal):
    crossings = []
    for i in range(1, len(scaled_signal)):
        if scaled_signal[i-1] < threshold <= scaled_signal[i]:
            crossings.append(i)
        elif scaled_signal[i-1] > threshold >= scaled_signal[i]:
            crossings.append(-i)
    
    # Compute anomaly signature using XOR of absolute indices
    signature = 0
    for idx in crossings:
        signature ^= abs(idx)
    
    # Additional decoy computation (never used)
    entropy = 0.0
    counts = {x: crossings.count(x) for x in set(crossings)}
    for count in counts.values():
        p = count / len(crossings) if crossings else 0.1
        entropy -= p * math.log(p + 1e-7)
    
    return signature

# Higher-level processor combining multiple concepts
processed_data = []
def process_chain(input_readings):
    global processed_data
    stage1 = preprocess_signal(input_readings)
    
    # Distractor: use zip and enumerate in a side calculation
    labeled = list(enumerate(stage1))
    corrections = [i * 0.01 for i in range(len(stage1))]
    adjusted_with_index = [val + corrections[i] for i, val in labeled]
    
    # Another red herring: set operation with no impact
    unique_abs = set(abs(x) for x in adjusted_with_index)
    magnitude_pairs = list(zip(adjusted_with_index, corrections))
    
    # Final relevant step: bin values into categories
    bins = []
    for x in stage1:
        if x < -2.5:
            bins.append(0)
        elif x < 0:
            bins.append(1)
        elif x < 2.5:
            bins.append(2)
        else:
            bins.append(3)
    
    # Use lambda for mapping (required feature) – actually used
    encoder = lambda b: (b + 1) * 10
    encoded_bins = [encoder(b) for b in bins]
    
    # Store result in global for main analysis
    processed_data = encoded_bins

# Main analysis function with recursion and logical conditions
def analyze_signal(encoded_features):
    # Recursive helper to compute weighted depth sum
    def recursive_weight(index, depth):
        if depth == 0 or index >= len(encoded_features):
            return 0
        current = encoded_features[index]
        left = recursive_weight(index * 2 + 1, depth - 1)
        right = recursive_weight(index * 2 + 2, depth - 1)
        return current + left + right
    
    # Compute structure resembling tree traversal
    total_impact = 0
    for root in range(2):
        contribution = recursive_weight(root, 3)
        total_impact += contribution * (root + 1)
    
    # Boolean logic chain with short-circuit evaluation (distractor)
    is_stable = len(encoded_features) > 0 and all(x < 30 for x in encoded_features)\
                 and (encoded_features[0] > 10 or encoded_features[-1] > 10)
    stability_flag = 1 if is_stable else 0
    
    # Real computation: sum of even-positioned elements minus odd-positioned
    positional_sum = sum(encoded_features[i] * (-1)**i for i in range(len(encoded_features)))
    
    # Combine results through non-linear mapping
    non_linear_adj = math.tanh(positional_sum / 100.0)
    
    # Final diagnostic uses only positional_sum and stability_flag
    # All other intermediate values are distractions
    final_diagnostic = int(positional_sum + stability_flag * 10)
    
    # Dead code path – looks like it modifies result but unreachable
    if False:
        backup_estimator = sum(math.sqrt(x + 10) for x in encoded_features)
        final_diagnostic = int(backup_estimator)
    
    return final_diagnostic

# --- Execution Flow ---
raw_sensor_data = generate_sensor_readings()

# Apply preprocessing chain
process_chain(raw_sensor_data)

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Output result as required
print(f"Result: {final_diagnostic}")