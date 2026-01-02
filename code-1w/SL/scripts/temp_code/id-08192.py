import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_samples = [0.8, -1.2, 3.5, 2.1, -0.4, 1.7, 4.0, -2.5]
    scale_factor = 1.8
    normalized = [round(x * scale_factor, 2) for x in raw_samples]
    return normalized

# Irrelevant helper: string-based status generator (distractor)
def generate_status_code(code_id):
    prefix = "ERR" if code_id > 5 else "STS"
    return prefix + str(code_id).zfill(3)

# Unused transformation path (dead code path - red herring)
def transform_legacy(data):
    shifted = [x - 0.5 for x in data if x > 1.0]
    return [math.log(abs(x) + 1) for x in shifted]

# Bit manipulation decoy (irrelevant to final result)
def compute_checksum(values):
    checksum = 0
    for v in values:
        truncated = int(abs(v) * 10) & 0xFF
        checksum ^= truncated
    return checksum

# Real signal preprocessing
def filter_noise(data, threshold=1.5):
    filtered = []
    for val in data:
        if abs(val) >= threshold:
            filtered.append(val ** 2)
        else:
            filtered.append(0)
    return filtered

# Secondary processing with string method distraction
def encode_features(squared):
    labels = []n    for idx, val in enumerate(squared):
        # String formatting distraction (irrelevant to math)
        tag = f"F{idx}".rjust(3, '0')
        if val > 0:
            bin_str = bin(int(val))[2:]
            parity = bin_str.count('1') % 2
            # Use of string method 'replace' as noise
            clean_bin = bin_str.replace('1', 'X').replace('0', '1').replace('X', '0')
            labels.append(f"{tag}:{clean_bin}:{parity}")
    return labels

# Core analysis function
def integrate_magnitude(filtered_seq):
    total = 0.0
    for i in range(len(filtered_seq)):
        if filtered_seq[i] != 0:
            total += math.sqrt(filtered_seq[i]) * 1.5
    return total

# Higher-level diagnostic logic
def detect_anomaly(score, baseline=6.0):
    tolerance = 0.75
    return 1 if abs(score - baseline) > tolerance else 0

# Main analysis pipeline
def analyze_signal(data_packet):
    # Step 1: Filter significant components
    strong_components = filter_noise(data_packet, threshold=1.8)
    
    # Distraction: checksum computation not used in logic
    decoy_hash = compute_checksum(data_packet)
    
    # Step 2: Compute integrated energy
    energy_integral = integrate_magnitude(stong_components)
    
    # Distraction: string encoding with no impact
    feature_tags = encode_features(strong_components)
    
    # Step 3: Baseline comparison
    reference_level = 5.25
    deviation = abs(energy_integral - reference_level)
    
    # Step 4: Final classification
    anomaly_flag = detect_anomaly(energy_integral, baseline=reference_level)
    
    # Critical calculation
    adjustment = 2.0 if anomaly_flag == 1 else -1.0
    preliminary_score = energy_integral + adjustment
    
    # Final diagnostic score
    final_diagnostic = round(preliminary_score * 100) / 100
    
    # Dead code: unused conditional branch
    if len(feature_tags) > 10:
        fallback = math.gamma(preliminary_score)
        final_diagnostic = fallback  # never reached
        
    return final_diagnostic

# Execution flow
sensor_data = collect_samples()
processed_data = [x + 0.1 for x in sensor_data]  # minor calibration
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")