def analyze_pattern(sequence, threshold):
    count = 0
    for i, val in enumerate(sequence):
        if val > threshold:
            count += 1
    return count

# Irrelevant helper (decoy)
def compute_entropy(data):
    import math
    total = sum(data)
    entropy = 0
    for x in data:
        prob = x / total if total else 0
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

# Unused transformation (dead code path)
def transform_signal(signal):
    shifted = [(x << 2) & 0xFF for x in signal]
    return [y ^ 0xAA for y in shifted]

# Real processing chain
def extract_features(raw_data):
    features = []
    for idx, (a, b) in enumerate(zip(raw_data[::2], raw_data[1::2])):
        diff = abs(a - b)
        rank = idx % 4
        if rank == 0:
            features.append(diff * 3)
        elif rank == 1:
            features.append(diff + 7)
        elif rank == 2:
            features.append(diff ** 2)
        else:
            features.append(diff // 2 if diff else 0)
    return features

# Misleading aggregation (red herring)
def assess_risk_level(values):
    avg = sum(values) / len(values) if values else 0
    level = 'LOW'
    if avg > 50:
        level = 'HIGH'
    elif avg > 25:
        level = 'MEDIUM'
    # This function is never called with real data
    return level

# Core logic disguised among noise
def validate_integrity(checksums):
    valid_count = 0
    for c in checksums:
        temp = c ^ 0xFFFF
        if (temp & (temp + 1)) == 0:  # Power of two check (bit trick)
            valid_count += 1
    return valid_count

def process_metrics(signature, baseline):
    # Step 1: Extract shape
    dims = (len(signature), len(baseline))
    
    # Step 2: Create paired deltas
    deltas = [abs(a - b) for a, b in zip(signature, baseline)]
    
    # Step 3: Analyze outlier distribution
    outliers = [d for d in deltas if d > 15]
    spike_rate = len(outliers) / len(deltas) if deltas else 0
    
    # Step 4: Compute diagnostic fingerprint
    fingerprint = []
    for i, d in enumerate(deltas):
        if i % 3 == 0:
            fingerprint.append(d * 2)
        elif i % 3 == 1:
            fingerprint.append(d + 5)
        else:
            fingerprint.append(d ** 1.5)
    
    # Step 5: Calculate stability score (intermediate red herring)
    stability_score = sum(fingerprint) / len(fingerprint) if fingerprint else 0
    
    # Step 6: Generate health signature from base
    encoded = [int(s * 1.7) % 256 for s in signature]
    
    # Step 7: Validate through bit criteria
    validation_mask = [e & 0x80 for e in encoded]  # High bit only
    trigger_events = sum(1 for m in validation_mask if m > 0)
    
    # Step 8: Combine into diagnostic core
    raw_diagnostic = len(deltas) * 3 + len(outliers) * 7 - trigger_events
    
    # Step 9: Apply correction based on pattern analysis
    feature_set = extract_features(baseline)
    complexity_index = analyze_pattern(feature_set, 10)
    
    # Step 10: Final adjustment using set logic
    unique_deltas = set(deltas)
    reference_peaks = {2, 3, 5, 7, 11, 13, 17}
    prime_overlap = len(unique_deltas.intersection(reference_peaks))
    
    # Step 11: Main computation
    final_diagnostic = raw_diagnostic + complexity_index * 4 - prime_overlap * 10
    
    # Step 12: Return result (this is the actual answer)
    return int(final_diagnostic)

# Simulated sensor readings (real input data)
baseline_readings = [12, 15, 10, 18, 22, 14, 8, 20]
health_signature = [10, 16, 11, 17, 20, 15, 9, 19]

# Dead assignment (distractor)
entropy_profile = compute_entropy([1, 2, 3, 4])

# Trigger the actual computation
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Target result: {final_diagnostic}")