import math

# System calibration and fault detection simulation
def generate_calibration_data(base_offset):
    raw_samples = [base_offset + i * 1.5 for i in range(8)]
    filtered = [x for x in raw_samples if x % 2 != 0]
    return [round(x ** 0.5, 3) for x in filtered]


def analyze_phase_shift(signal_a, signal_b):
    # Irrelevant signal analysis (red herring)
    shifts = []
    for i in range(len(signal_a)):
        shift = (signal_b[i] - signal_a[i]) % 360
        shifts.append(shift)
    avg_shift = sum(shifts) / len(shifts)
    return avg_shift

# Decoy function - never called
def legacy_compatibility_mode(config):
    return {k: v * 2 for k, v in config.items()}

# Unused intermediate transformation
temp_registry = set()
for code in ['A7', 'B2', 'C9', 'D4']:
    temp_registry.add(code[0])
    temp_registry.add(code)

# Fault signature definitions (some are red herrings)
fault_signatures = {
    'F1': lambda x: x > 100,
    'F2': lambda x: x < 0,
    'F3': lambda x: math.isclose(x, 3.14159, abs_tol=1e-3),
    'F4': lambda x: isinstance(x, float) and x.is_integer()
}

# Sensor data preprocessing
def preprocess_sensors(raw_readings):
    normalized = []
    for val in raw_readings:
        if val < 0:
            val = abs(val)
        normalized.append(round(val * 1.07, 4))
    return normalized

# Core diagnostic engine
def detect_anomalies(dataset, threshold=2.5):
    anomalies = []
    moving_avg = sum(dataset[:3]) / 3
    
    for i in range(3, len(dataset)):
        if abs(dataset[i] - moving_avg) > threshold:
            anomalies.append(i)
        moving_avg = (moving_avg * 2 + dataset[i]) / 3  # Weighted update
    
    return set(anomalies)

# Main processing pipeline
def process_metrics(sequence, flags):
    # Step 1: Preprocess input sequence
    processed = preprocess_sensors(sequence)
    
    # Step 2: Detect anomaly indices
    anomaly_set = detect_anomalies(processed)
    
    # Step 3: Apply bitmask filtering based on fault flags
    mask = 0
    for bit in flags:
        mask |= (1 << bit)
    
    # Step 4: Compute diagnostic score using modular arithmetic
    base_score = 0
    for i, val in enumerate(processed):
        if i in anomaly_set:
            contribution = (val * 100) % 47
            base_score += int(contribution)
    
    # Step 5: Adjust score with bit manipulation
    adjusted_score = base_score ^ mask  # XOR with flag mask
    adjusted_score = (adjusted_score << 1) | (adjusted_score & 1)
    
    # Step 6: Final nonlinear transformation
    if adjusted_score > 1000:
        final = adjusted_score // 3
    else:
        final = adjusted_score * 2 + 17
    
    # Dead code path - misleading
    if final < 0:
        final = math.factorial(abs(final))
    
    return final

# Irrelevant string processing (distractor)
diag_log = "SYS|CAL|CHK|FLT"
log_parts = diag_log.split('|')
status_summary = ''.join([part[0] for part in log_parts])

# Generate real input data
base_sequence = generate_calibration_data(12)
calibration_sequence = [x * 8.5 for x in base_sequence]  # Scale up to realistic levels

# Define active fault flags (only bits 2 and 5 are meaningful)
fault_flags = [2, 5, 7]  # 7 is a red herring - no effect due to data range

# Execute main computation
final_diagnostic = process_metrics(calibration_sequence, fault_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")