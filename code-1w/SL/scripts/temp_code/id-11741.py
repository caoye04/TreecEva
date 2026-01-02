import itertools

# Simulated sensor data preprocessing with red herrings and complex flow
def transform_readings(raw_readings):
    scaled = [x * 0.7 for x in raw_readings]
    offset = sum(scaled) / len(scaled)
    adjusted = [x - offset + 2 for x in scaled]
    return adjusted

# Irrelevant transformation - decoy function
def analyze_pattern(seq):
    if not seq:
        return 0
    peak = max(seq)
    trough = min(seq)
    volatility = (peak - trough) / (peak + trough + 1e-8)
    return volatility * 100

# Core processing function with critical logic buried
def process_stream(data, indices):
    extracted = []
    for i in range(len(data)):
        if i in indices:
            extracted.append(data[i] ** 2)
        else:
            extracted.append(data[i] + 1)  # Distractor: most values modified this way

    # Bit manipulation red herring
    checksum = 0
    for val in extracted:
        checksum ^= int(val) & 0xFF

    # Real payload: apply logarithmic weighting only to selected positions
    weighted = []
    for j, v in enumerate(extracted):
        if j % 3 == 0 and v > 0:
            weighted.append(v * (j + 1))
        else:
            weighted.append(v)

    # Use of itertools - relevant but obscured
    grouped = [list(group) for k, group in itertools.groupby(weighted, key=lambda x: x > 0)]
    flattened = [item for group in grouped for item in group]  # Identity transform (decoy)

    return flattened

# Evaluation logic where answer emerges
def evaluate_purity(signal, limit):
    clean_signal = [x for x in signal if abs(x) <= limit]
    noise_ratio = (len(signal) - len(clean_signal)) / len(signal) if signal else 0

    # Critical computation path
    base_energy = sum(x ** 2 for x in clean_signal)
    normalized_energy = base_energy / (len(clean_signal) + 1e-8)

    # Decoy metrics
    entropy = 0
    hist = {}
    for x in signal:
        hist[int(x)] = hist.get(int(x), 0) + 1
    for count in hist.values():
        if count > 0:
            entropy -= (count / len(signal)) * ((count / len(signal)) ** 0.5)

    # Final score calculation — depends on prior steps
    purity_index = 1000 * (1 - noise_ratio) * (normalized_energy ** 0.5)
    return int(purity_index)

# === MAIN EXECUTION WITH DISTRACTORS ===
if __name__ == "__main__":
    # Input data — realistic structure
    raw_sensor_data = [1.2, -3.4, 5.6, 2.1, -0.8, 4.0, 6.7, -2.5, 0.3, 1.1]
    
    # Irrelevant auxiliary arrays
    baseline_calibrations = [0.1, 0.2, 0.15, 0.3, 0.25]
    fault_codes = {"F1": 101, "F2": 205, "OK": 0}
    device_status = "OK"
    
    # Transform data (relevant)
    processed_readings = transform_readings(raw_sensor_data)

    # Unused control flags — misleading
    debug_mode = False
    override_safety = False
    audit_trail = []

    # Key indices that determine actual computation path
    key_indices = {0, 3, 6, 9}  # Only these positions matter in process_stream
    
    # Threshold used in final evaluation
    threshold = 50.0

    # Decoy analysis
    pattern_metric = analyze_pattern(processed_readings)
    audit_trail.append(f"Pattern score: {pattern_metric:.2f}")

    # CRITICAL STATEMENT: filtration_score depends on correct tracing through multiple layers
    filtration_score = evaluate_purity(process_stream(processed_readings, key_indices), threshold)

    # Print result as required
    print(f"Result: {filtration_score}")