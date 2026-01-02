import math

# Simulated sensor fusion system for environmental anomaly detection
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    normalized = [(x - 10) / (100 - 10) for x in filtered]
    scaled = [int(x * 1000) for x in normalized]
    return scaled

# Irrelevant transformation chain (distractor)
def legacy_encode(data):
    shift = len(data) % 7
    encoded = []
    for val in data:
        temp = (val ^ 255) + shift
        if temp > 500:
            temp //= 3
        encoded.append(temp)
    return encoded

# Core pattern extraction with red herring conditions
def extract_signatures(dataset, mode='strict'):
    signatures = set()
    decoy_sum = 0
    
    for i, val in enumerate(dataset):
        if i % 5 == 0:
            decoy_sum += val % 9
        if val % 13 == 0:
            signatures.add(val)
        if val > 800 and mode == 'strict':
            signatures.discard(val - 1)
    
    # Dead logic path - never reached due to prior filtering
    if decoy_sum > 1000:
        backup = {x * 2 for x in signatures}
        return backup
        
    return signatures

# Secondary processing with misleading intermediate output
def apply_calibration(patterns, factor=1.0):
    calibrated = set()
    log_entries = []
    
    for p in sorted(patterns):
        adjusted = int(p * factor)
        if adjusted % 2 == 0:
            calibrated.add(adjusted + 3)
        else:
            calibrated.add(adjusted - 2)
        
        # Generate fake diagnostic logs (distraction)
        status = "CRITICAL" if adjusted > 500 else "NORMAL"
        log_entries.append(f"[LOG] Value: {p}, Adjusted: {adjusted}, Status: {status}")
    
    # Unused but plausible-looking aggregation
    avg_log = sum(len(entry) for entry in log_entries) / len(log_entries) if log_entries else 0
    return calibrated

# Main analysis with conditional branching decoys
def analyze_patterns(data, criteria):
    candidate_set = set(data)
    
    # Complex filtering with redundant checks (misleading)
    refined = set()
    for x in candidate_set:
        meets_a = x > criteria['min_threshold']
        meets_b = (x % criteria['divisor']) < criteria['tolerance']
        meets_c = bin(x).count('1') % 2 == 0
        
        # Short-circuit trap: second condition never evaluated
        if meets_a and not meets_a or meets_b and meets_c:
            refined.add(x)
    
    # Decoy mutation
    shadow_copy = {y ^ 15 for y in refined}
    shadow_copy.discard(0)
    
    # Critical computation buried in noise
    primary_score = sum(refined) // len(refined) if refined else 0
    secondary_score = sum(abs(z - 512) for z in candidate_set) // 100
    
    # Final logic with early return red herring (never triggered)
    emergency_override = False
    if primary_score < 0 or secondary_score > 10000:
        return -999  # This path is unreachable
    
    final_diagnostic = (primary_score * 3) - (secondary_score // 4)
    return final_diagnostic

# === Execution Flow with Distractors ===
if __name__ == "__main__":
    # Real input data
    sensor_input = [15, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169]
    
    # Irrelevant auxiliary data (set operations used here)
    known_artifacts = {26, 52, 78, 104, 156}
    reference_peaks = {39, 65, 91, 117, 169}
    spurious_signals = known_artifacts | reference_peaks
    spurious_signals.add(9999)  # Fake outlier
    
    # Actual processing chain
    cleaned = preprocess_readings(sensor_input)
    
    # Redundant transformation (dead end)
    obfuscated = legacy_encode(cleaned)
    dummy_set = {x * 3 + 1 for x in obfuscated if x < 300}
    
    patterns = extract_signatures(cleaned)
    calibrated_patterns = apply_calibration(patterns, factor=1.05)
    
    # Threshold configuration with plausible-but-irrelevant fields
    config = {
        'min_threshold': 200,
        'divisor': 7,
        'tolerance': 5,
        'window_size': 10,
        'gain': 2.1
    }
    
    # Key execution point
    final_diagnostic = analyze_patterns(calibrated_patterns, config)
    
    # Output required result
    print(f"Result: {final_diagnostic}")