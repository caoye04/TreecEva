import math

# Simulated quantum sensor array diagnostics
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [val / max(filtered) for val in filtered]
    return normalized

# Irrelevant helper - dead path (never called)
def legacy_compatibility_mode(data):
    return [d * 0.95 for d in data if d > 0]

# Misleading transformation - looks important but unused in final path
def apply_fourier_shift(signal):
    shifted = []
    for i in range(len(signal)):
        shifted.append(signal[i] * math.sin(i + 0.5))
    return shifted

# Core diagnostic engine
def compute_entropy(readings):
    entropy = 0.0
    for val in readings:
        if val != 0:
            entropy -= val * math.log(abs(val))
    return round(entropy, 6)

# Auxiliary metric - distractor calculation
def calculate_coherence_index(data):
    total_pairs = 0
    coherent_pairs = 0
    for i in range(len(data) - 1):
        total_pairs += 1
        if (data[i] < 0 and data[i+1] < 0) or (data[i] > 0 and data[i+1] > 0):
            coherent_pairs += 1
    return coherent_pairs / total_pairs if total_pairs else 0

# Main analysis with multiple logic branches
# Only one branch leads to final result
def analyze_system_state(readings, factor):
    temp_buffer = []
    threshold = sum(abs(r) for r in readings) / len(readings) * factor
    
    # Distractor: complex bit manipulation on indices
    index_signature = 0
    for idx in range(len(readings)):
        index_signature ^= (idx << 2) & 0xFF
    
    # Real processing begins here
    adjusted = [r * factor for r in readings]
    
    # Conditional filtering - only values above dynamic threshold contribute
    significant = [a for a in adjusted if abs(a) >= threshold]
    
    # Multiple assignments - some irrelevant
    avg_magnitude, peak_value = sum(abs(s) for s in significant) / len(significant), max(abs(s) for s in significant)
    
    # Secondary filter based on phase (sign)
    positive_contributions = [s for s in significant if s > 0]
    negative_contributions = [s for s in significant if s < 0]
    
    # Compute stability ratio - red herring variable
    stability_ratio = len(positive_contributions) / len(negative_contributions) if negative_contributions else 0
    
    # Actual key computation: weighted entropy
    if not significant:
        base_entropy = 0.0
    else:
        base_entropy = compute_entropy([abs(s)/peak_value for s in significant])
    
    # Tertiary adjustment via mock neural gain
    neural_gain_profile = [math.tanh(abs(s)) for s in significant]
    effective_gain = sum(neural_gain_profile) / len(neural_gain_profile)
    
    # Final diagnostic formula - depends on entropy and gain
    diagnostic_score = (base_entropy * 100) * effective_gain
    
    # Dead code block - syntactically valid but unreachable
    # if False:
    #   fallback = 0
    #   for v in readings:
    #       fallback += int(abs(v * 10)) & 3
    #   diagnostic_score = fallback
    
    return round(diagnostic_score, 6)

# Unused data structure - creates distraction
system_logs = {
    'timestamp': '2024-05-18T12:00:00Z',
    'sensor_id': 'QSA-7X',
    'readings_count': 128,
    'status': 'nominal'
}

# Simulation parameters - some are decoys
calibration_factor = 1.75
quantum_noise_floor = 0.003
baseline_drift = -0.017

# Primary input data
quantum_readings = [
    0.12, -0.08, 0.35, 0.21, -0.15, 0.67, -0.42, 0.09,
    0.11, 0.19, -0.23, 0.51, 0.33, -0.29, 0.07, -0.14
]

# Spurious intermediate processing
buffer_snapshot = [round(q * 10, 2) for q in quantum_readings]
aggregate_moment = sum(q**3 for q in quantum_readings)

# Key execution point
final_diagnostic = analyze_system_state(quantum_readings, calibration_factor)

# Output result as required
print(f"Result: {final_diagnostic}")