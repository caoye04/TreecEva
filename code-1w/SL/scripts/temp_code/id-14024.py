import math

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.00314
TEMPORAL_BUFFER = [0.1, 0.2, 0.5, 0.8]
RECALIBRATION_FACTOR = 1.007

# Quantum register simulation with decoherence tracking
quantum_registers = [
    {'state': 513, 'decoherence': 0.002, 'flagged': False},
    {'state': 257, 'decoherence': 0.005, 'flagged': True},
    {'state': 129, 'decoherence': 0.001, 'flagged': False},
    {'state': 65, 'decoherence': 0.003, 'flagged': True}
]

# Irrelevant signal processing chain
def preprocess_signal(data):
    filtered = [x * 0.95 for x in data if x > 0.3]
    smoothed = sum(filtered) / len(filtered) if filtered else 0
    return smoothed * RECALIBRATION_FACTOR

# Fake entropy estimator (dead code path)
def estimate_entropy(registers):
    total_entropy = 0
    for r in registers:
        if r['decoherence'] > 0.0025:
            total_entropy += math.log(r['decoherence'] * 1000)
    return round(total_entropy, 4)

# Misleading diagnostic that looks important but isn't used
legacy_diagnostics = {
    'voltage_stability': 0.987,
    'phase_coherence_avg': 0.0025,
    'anomaly_score': sum(r['decoherence'] * 100 for r in quantum_registers)
}

# Core analysis logic (uses lambda for bit transformation)
transform_register = lambda reg: (
    (reg >> 1) ^ (reg << 2)
) & 0xFFFF  # Bit manipulation with XOR and shifts

# Secondary filter based on flagged status (partially relevant)
def apply_quality_filter(registers):
    return [r for r in registers if not r['flagged']]

# Main analyzer - only this function contributes to final answer
def analyze_system_state(registers):
    # Step 1: Filter out flagged registers
    active_regs = apply_quality_filter(registers)
    
    # Step 2: Extract and transform raw state values
    transformed = []
    for reg in active_regs:
        raw_val = reg['state']
        processed = transform_register(raw_val)
        transformed.append(processed)
    
    # Step 3: Compute weighted contribution (weights decay with index)
    weighted_sum = 0
    for i, val in enumerate(transformed):
        weight = 0.5 ** i  # Decreasing weights: 1, 0.5, 0.25...
        weighted_sum += val * weight
    
    # Step 4: Apply non-linear compression using tanh-like curve
    compressed = int(math.tanh(weighted_sum / 10000) * 10000)
    
    # Step 5: Cross-check with parity consensus
    parities = [bin(t).count('1') % 2 for t in transformed]
    consensus = 1 if sum(parities) > len(parities) / 2 else 0
    
    # Step 6: Final adjustment based on consensus bit
    result = compressed + (13 * consensus)
    
    # Dead code branch - never executed due to above logic
    if len(parities) == 0 and compressed > 5000:
        result = int(result * 0.9)
        
    return result

# Auxiliary monitoring (irrelevant)
current_monitoring_state = {
    'timestamp': 1678886400,
    'sensor_id': 'QX-9B',
    'mode': 'diagnostic'
}

# Simulated execution sequence
signal_baseline = preprocess_signal(TEMPORAL_BUFFER)
entropy_profile = estimate_entropy(quantum_registers)

# Key statement
final_diagnostic = analyze_system_state(quantum_registers)

# Output result
print(f"Target result: {final_diagnostic}")