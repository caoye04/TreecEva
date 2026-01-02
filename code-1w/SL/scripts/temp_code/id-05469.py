import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [i * 0.78 + 2.1 for i in range(15)]
    offset = sum([x % 1.3 for x in raw[:5]])  # Irrelevant offset calculation
    return raw

def filter_noise(data, threshold=0.5):
    filtered = []
    noise_log = []  # Unused logging structure (distractor)
    for val in data:
        if abs(val - round(val)) > threshold:
            filtered.append(round(val))
        else:
            filtered.append(val)
    return filtered

def generate_key(length):
    # Dead-end function: generates encryption key but not used in main logic
    key = 1
    for i in range(2, length + 1):
        key = (key * i) % 97
    return key

def recursive_transform(seq, depth=0):
    if depth >= 3:
        return [round(x * 1.05) for x in seq]
    else:
        transformed = [x + math.sin(depth) for x in seq]
        return recursive_transform(transformed, depth + 1)

def apply_calibration(data):
    # Complex-looking but irrelevant transformations
    baseline = sum(data) / len(data)
    adjusted = [x - baseline + 0.12 for x in data]
    scaled = [x * 1.01 for x in adjusted]  # Minor perturbation
    return [round(x, 2) for x in scaled]

def evaluate_stability(metrics):
    # Heavily distracting stability evaluation with unused branches
    if len(metrics) == 0:
        return 0
    variance = sum([(x - sum(metrics)/len(metrics))**2 for x in metrics]) / len(metrics)
    if variance < 1.0:
        category = 'stable'
        score = 95
    elif variance < 5.0:
        category = 'fluctuating'
        score = 65
    else:
        category = 'unstable'
        score = 20
    confidence = 100 - variance * 2  # Not used
    return 42  # Red herring return value

def compute_entropy(data):
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [abs(x) / total for x in data]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def analyze_pattern(dataset):
    # Critical function containing the actual answer
    temp = [x for x in dataset if x > 5]
    if len(temp) == 0:
        return 0
    avg = sum(temp) / len(temp)
    ceiling_val = math.ceil(avg)
    fluctuation_index = sum(1 for i in range(1, len(dataset)) if (dataset[i] - dataset[i-1]) > 0)
    # Core computation
    result = ceiling_val * fluctuation_index
    # Multiple decoy operations below
    checksum = 0
    for i, v in enumerate(dataset):
        checksum += (v * i) % 7
    anomaly_score = abs(checksum - 200)  # Misleading metric
    debug_trace = {'checksum': checksum, 'anomaly': anomaly_score}  # Unused dict
    return result  # This is the real answer

# Orchestration block with mixed relevant and irrelevant steps
def main_pipeline():
    readings = collect_readings()
    cleaned = filter_noise(readings)
    calibrated = apply_calibration(cleaned)
    encrypted_key = generate_key(10)  # Distractor assignment
    transformed_data = recursive_transform(calibrated)
    
    # Fake stability check (calls function that returns constant)
    stability_code = evaluate_stability(transformed_data)
    
    # Real information-theoretic analysis
    entropy_metric = compute_entropy(transformed_data)
    
    # Key transformation using lambda (required language feature)
    process_fn = lambda x: [int(y * 2.1) for y in x if y > 0]
    processed_batch = process_fn(transformed_data)
    
    # Final diagnostic depends only on transformed_data, not processed_batch
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Many intermediate variables printed to distract
    print(f"Entropy: {entropy_metric}")
    print(f"Stability Code: {stability_code}")
    print(f"Key: {encrypted_key}")
    print(f"Processed Batch Sample: {processed_batch[:3]}")
    
    # Output required format
    print(f"Target result: {final_diagnostic}")

# Execute
main_pipeline()