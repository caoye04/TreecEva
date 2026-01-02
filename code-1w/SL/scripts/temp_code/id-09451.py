import math

# Irrelevant helper function (decoy)
def unused_transform(x):
    return [val ** 2 + 1 for val in x if val % 3 == 0]

# Another decoy: complex-looking but unused calculation
total_offset = sum([i * (i - 1) for i in range(10)]) * 2.5

# Simulated sensor data with noise
def generate_signal():
    base = [math.sin(i * 0.5) * 100 for i in range(20)]
    noise = [i % 7 - 3 for i in range(20)]
    return [round(base[i] + noise[i], 2) for i in range(20)]

# Signal preprocessing with slicing and filtering
def preprocess(signal_data):
    # Trim start/end using slicing (relevant)
    trimmed = signal_data[3:-3]
    
    # Apply moving average filter
    filtered = []
    for i in range(1, len(trimmed) - 1):
        avg = (trimmed[i-1] + trimmed[i] + trimmed[i+1]) / 3
        filtered.append(round(avg, 2))
    
    # Unused transformation path (red herring)
    if len(filtered) > 10:
        _ = [x * 1.5 for x in filtered[::2]]

    return filtered

# Bit manipulation for checksum (partially relevant)
def compute_checksum(values):
    checksum = 0
    for v in values:
        normalized = int(abs(v)) % 256
        checksum ^= normalized  # XOR into checksum
    return checksum & 0xFF  # Limit to 8 bits

# Set-based anomaly detection (uses set operations)
def detect_anomalies(data):
    rounded_set = {round(x) for x in data}
    bounds = set(range(-100, 101))
    anomalies = rounded_set - bounds  # Out-of-bound values
    return len(anomalies)

# Higher-order function with lambda (irrelevant but plausible)
decay_function = lambda f: (lambda x: x * (0.95 ** f))
apply_decay = decay_function(5)

# Core analysis combining multiple concepts
def analyze_signal(cleaned):
    # Step 1: Compute energy (sum of squares)
    energy = sum([x ** 2 for x in cleaned]) / len(cleaned)

    # Step 2: Count zero-crossings
    zero_crossings = 0
    for i in range(1, len(cleaned)):
        if (cleaned[i-1] < 0 <= cleaned[i]) or (cleaned[i-1] >= 0 > cleaned[i]):
            zero_crossings += 1

    # Step 3: Use lambda in a trivial way (distraction)
    scale = lambda x: x * 1.05
    energy = scale(energy)

    # Step 4: Checksum of integer parts (bitwise relevance)
    chk = compute_checksum(cleaned)

    # Step 5: Detect statistical outliers using sets
    outlier_count = detect_anomalies(cleaned)

    # Step 6: Modular arithmetic rhythm detection
    rhythm_pattern = sum([i for i, x in enumerate(cleaned) if x > 0]) % 7

    # Step 7: Conditional adjustment based on multiple thresholds
    diagnostic_score = energy
    if zero_crossings > 5:
        diagnostic_score += 100
    if chk < 50:
        diagnostic_score -= 25
    if outlier_count == 0:
        diagnostic_score += 50

    # Step 8: Final transformation (key logic)
    final_weight = (rhythm_pattern + 1) or 1
    diagnostic_score /= final_weight

    # Irrelevant late-stage computation (misleading)
    _temp_diag = math.log2(diagnostic_score + 100) * chk

    return int(round(diagnostic_score))

# Main execution flow
if __name__ == "__main__":
    raw_sensor_data = generate_signal()
    processed_data = preprocess(raw_sensor_data)
    
    # Dead code branch: never executed (distractor)
    debug_mode = False
    if debug_mode:
        print(f"Raw: {raw_sensor_data}")
        print(f"Processed: {processed_data}")
    
    # Key statement
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")