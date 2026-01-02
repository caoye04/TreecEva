import math

# Simulated quantum register diagnostics with decoy computations
def preprocess_register(reg):
    # Irrelevant transformation (distractor)
    transformed = [(x << 2) ^ 0xA for x in reg]
    normalized = [t / max(transformed) for t in transformed if t != 0]
    return [round(n * 100) for n in normalized]

# Misleading auxiliary function that appears important but is unused in critical path
def deprecated_calibration_scan(data):
    checksum = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            checksum += val * 7
        elif val > 50:
            checksum -= val // 4
    return checksum % 1000

# Core data processing with red herring operations
def filter_anomalies(records):
    anomalies = []
    for idx, record in enumerate(records):
        # Complex but irrelevant filtering logic
        if len(record) < 5:
            continue
        score = sum(r ** 0.5 for r in record if r > 0) / len(record)
        if 10 < score < 25 and idx % 2 == 1:
            anomalies.append((idx, score))
    return anomalies  # Never actually used

# Real signal extraction buried in noise
def extract_coherence_pattern(seq):
    pattern = []
    for i, s in enumerate(seq):
        if i == 0:
            pattern.append(s)
        else:
            delta = s - seq[i-1]
            pattern.append(abs(delta) % 7)
    return pattern

# Critical function — performs actual computation leading to answer
def compute_stability_index(registers):
    # Step 1: Flatten registers using zip for parallel access
    transposed = list(zip(*registers))
    
    # Step 2: Compute phase coherence across qubits
    coherence_values = []
    for col in transposed:
        mean_val = sum(col) / len(col)
        variance = sum((x - mean_val) ** 2 for x in col) / len(col)
        coherence = math.exp(-variance / 10.0) if variance > 0 else 1.0
        coherence_values.append(coherence)
    
    # Step 3: Weighted aggregation
    total_weight = 0
    weighted_sum = 0
    for i, cv in enumerate(coherence_values):
        weight = 1 + (i % 3)
        weighted_sum += weight * cv
        total_weight += weight
    
    return round(weighted_sum / total_weight, 6)

# Higher-level analysis combining multiple concepts
def analyze_system_state(qregs, calib):
    # Distractor: process calibration data through unused pipeline
    processed_calib = [math.log(c + 1) for c in calib]
    sorted_calib = sorted(processed_calib, reverse=True)
    filtered_peaks = [x for x in sorted_calib if x > 2.0]  # Dead end
    
    # Red herring: anomaly detection call (result ignored)
    _ = filter_anomalies([[10,20,30], [40,50,60], [70,80,90]])
    
    # Actual key computation
    stability = compute_stability_index(qregs)
    
    # Additional decoy logic involving enumerate and bit shifts
    shift_accum = 0
    for i, pc in enumerate(processed_calib):
        if i % 2 == 0:
            shift_accum ^= int(pc) << (i % 4)
    
    # Final diagnostic combines real result with neutral offset
    final_diagnostic = int(stability * 10000) + 1234
    
    # Print required output format
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# --- Input Data Setup (real and decoy values) ---
quantum_registers = [
    [50, 60, 55, 70],
    [52, 58, 54, 68],
    [49, 61, 56, 72],
    [51, 59, 53, 69]
]

calibration_data = [45, 120, 88, 200, 155]  # Used only partially

# --- Unused variables and dead code paths (distraction layer) ---
decoys = {
    'timestamp': 1678886400,
    'version': 'QX-2.1',
    'baseline_noise': [0.1, 0.3, 0.2, 0.5],
    'legacy_mode': False
}

aux_data = []
for k, v in decoys.items():
    if isinstance(v, list):
        aux_data.extend(v)

# Another misleading intermediate
aggregate_metric = 0
for i, val in enumerate(aux_data):
    aggregate_metric += val * (i + 1)

# --- Key execution point ---
final_diagnostic = analyze_system_state(quantum_registers, calibration_data)