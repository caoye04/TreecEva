import math

# Irrelevant sensor simulation (dead code path)
def collect_sensor_data():
    return [0.1 * i for i in range(100)]

# Decoy function with misleading intermediate calculations
def analyze_signal_noise(signal):
    noise_floor = 0.041
    filtered = [s ** 2 for s in signal if s > noise_floor]
    return sum(filtered) / len(filtered) if filtered else 0

# Unused transformation chain
def transform_readings(data):
    shifted = [x + 0.5 for x in data]
    scaled = [math.log(y) if y > 0 else 0 for y in shifted]
    return [round(z, 3) for z in scaled]

# Core logic disguised among distractors
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 6)

# Bit manipulation red herring
def generate_checksum(arr):
    checksum = 0
    for val in arr:
        int_val = int(val * 100)
        checksum ^= int_val
        checksum = (checksum << 1) & 0xFFFF
    return checksum

# Real processing function buried in complexity
def extract_features(raw):
    # Distractor: unused feature candidates
    peaks = [x for x in raw if x > 0.7]
    troughs = [x for x in raw if x < 0.3]
    volatility = max(raw) - min(raw)
    
    # Relevant computation
    avg = sum(raw) / len(raw)
    deviation_sq = [(x - avg) ** 2 for x in raw]
    variance = sum(deviation_sq) / len(deviation_sq)
    return {'average': avg, 'variance': variance, 'count': len(raw)}

# Higher-level aggregator with conditional bypass
# (contains one active path among three)
def evaluate_stability(metrics):
    if metrics['variance'] < 0.05 and metrics['average'] > 0.4:
        return "STABLE"
    elif metrics['count'] > 50:
        return "FLUCTUATING"  # dead branch due to input size
    else:
        return "UNRELIABLE"      # dead branch

# Lambda-based combinator (partially relevant)
compose_weights = lambda f1, f2: (f1['average'] * 0.7) + (f1['variance'] * 0.3) + (f2 * 0.1)

# Set operations used as distraction
def detect_anomalies(readings):
    expected_range = set(round(i * 0.05, 2) for i in range(1, 21))
    observed = set(round(r, 2) for r in readings)
    anomalies = observed - expected_range
    return anomalies

# Main processing pipeline with hidden key logic
def process_metrics(signature, baseline):
    # Step 1: Extract features from signature (key step)
    sig_features = extract_features(signature)
    
    # Step 2: Irrelevant anomaly detection (distractor)
    _ = detect_anomalies(baseline)
    
    # Step 3: Compute entropy on baseline (red herring result not used)
    _ = compute_entropy(baseline)
    
    # Step 4: Simulate unused sensor collection (irrelevant)
    _ = collect_sensor_data()
    
    # Step 5: Generate checksum (computationally heavy but unused)
    _ = generate_checksum(baseline)
    
    # Step 6: Use lambda to combine average and variance into weight
    fused_weight = compose_weights(sig_features, sig_features['average'])
    
    # Step 7: Evaluate stability (result ignored)
    _ = evaluate_stability(sig_features)
    
    # Step 8: Final diagnostic calculation (ACTUAL ANSWER PATH)
    adjustment_factor = 1.0
    if sig_features['average'] >= 0.5:
        adjustment_factor = 1.2
    elif sig_features['average'] < 0.3:
        adjustment_factor = 0.8
        
    base_score = sig_features['average'] * 1000
    variance_penalty = sig_features['variance'] * 100
    final_diagnostic = (base_score - variance_penalty) * adjustment_factor
    
    return int(round(final_diagnostic))

# Ground truth input data
baseline_readings = [0.15, 0.18, 0.21, 0.23, 0.25, 0.24, 0.22, 0.20, 0.19, 0.17]
health_signature = [0.52, 0.54, 0.53, 0.55, 0.51, 0.56, 0.54, 0.53, 0.55, 0.52, 0.54, 0.53]

# Execute main logic
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Target result: {final_diagnostic}")