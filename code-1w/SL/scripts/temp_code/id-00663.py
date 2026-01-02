import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(duration):
    samples = []
    for t in range(1, duration + 1):
        sample = (t * 1.7) % 5 + math.sin(t / 3)
        samples.append(round(sample, 3))
    return samples

# Irrelevant helper: computes entropy (not used in final result)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

# Misleading transformation: looks important but unused later
def transform_signal(data):
    transformed = []
    shift = len(data) % 7
    for val in data:
        transformed.append((val * 1.23 + shift) % 10)
    return [round(x, 2) for x in transformed]

# Decoy function: appears related but never called in critical path
def calibrate_system(ref_value):
    adjustment = 0
    for i in range(5):
        if ref_value > 3:
            adjustment += math.log(ref_value + i)
        else:
            adjustment -= math.sqrt(abs(ref_value - i))
    return round(adjustment, 3)

# Auxiliary check: used to create red herring variables
def validate_integrity(data):
    checksum = sum(abs(x) for x in data[:10]) * 100
    threshold = 25.0
    status = 'OK' if checksum > threshold else 'FAIL'
    # Creates misleading intermediate
    debug_flag = True if checksum % 2 == 0 else False
    return status, round(checksum, 2), debug_flag

# Core pattern analyzer: actually used in computation
def detect_anomalies(seq):
    anomalies = 0
    for i in range(1, len(seq) - 1):
        prev, curr, next_val = seq[i-1], seq[i], seq[i+1]
        if curr > prev and next_val < curr and (curr - prev) > 1.5:
            anomalies += 1
    return anomalies

# Real processing chain — only this contributes to final answer
def extract_features(data):
    magnitude = sum(x ** 2 for x in data) ** 0.5
    peaks = sum(1 for i in range(1, len(data)-1) if data[i] > data[i-1] and data[i] > data[i+1])
    avg = sum(data) / len(data)
    normalized_peak = peaks / (magnitude + 1e-8)
    return {
        'magnitude': round(magnitude, 3),
        'peaks': peaks,
        'balance': round(avg, 3),
        'score': round(normalized_peak, 4)
    }

# Conditional expression used as required
# Determines processing mode based on feature balance
# Actual key logic path

def analyze_pattern(buffer):
    features = extract_features(buffer)
    anomaly_count = detect_anomalies(buffer)
    
    # Critical conditional expression (required python feature)
    base_score = features['score'] if features['balance'] > 0.5 else features['score'] * 0.7
    
    # Red herring variables — look influential but are distractions
    temp_correction = math.cos(len(buffer) % 4)  # Unused in final
    fallback_mode = (features['magnitude'] < 10) or (anomaly_count == 0)
    
    # Real formula
    raw_diagnostic = base_score * 100 + anomaly_count * 5
    
    # Another decoy calculation
    simulated_load = 0
    for i in range(3):
        simulated_load += math.exp(-i * 0.5) * features['balance']
    # Not used beyond here
    
    # Final adjustment — only one that matters
    adjustment_factor = 1.2 if anomaly_count >= 3 else 0.9
    final_diagnostic = round(raw_diagnostic * adjustment_factor, 4)
    
    return final_diagnostic

# --- Execution begins ---

# Collect real signal data (duration chosen so results are deterministic)
signal_buffer = collect_samples(12)

# Dead code path — executed but not contributing
entropy_diagnostic = compute_entropy([int(10*x) for x in signal_buffer])  # Irrelevant discretization

# More distraction: run validation that produces unused tuple
validation_status, system_check, flag = validate_integrity(signal_buffer)

# Transform but do not use result
distorted = transform_signal(signal_buffer)  # Dead assignment

# Call decoy calibration with arbitrary seed
calibration_offset = calibrate_system(signal_buffer[0])  # Unused

# Key statement: compute the actual answer
final_diagnostic = analyze_pattern(signal_buffer)

# Print result as required
print(f"Result: {final_diagnostic}")