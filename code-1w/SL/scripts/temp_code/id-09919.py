from collections import defaultdict, Counter
import math

# Simulated quantum sensor array diagnostics with noise filtering
def preprocess_readings(raw_readings):
    filtered = []
    noise_floor = 0.02
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(round(val * 1000))
    return [x for x in filtered if x % 2 == 1]  # Keep only odd-scaled values

# Legacy function (dead code path - not used but looks relevant)
def deprecated_normalization(data):
    max_val = max(data)
    return [int(x / max_val * 100) for x in data]

# Signal coherence analysis
def calculate_coherence(sequence):
    coherence_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            coherence_score += 1
        else:
            coherence_score -= 0.5
    return round(coherence_score, 3)

# Frequency pattern extraction using bit manipulation
def extract_frequency_patterns(values):
    freq_map = defaultdict(int)
    for v in values:
        # Bitwise analysis of magnitude
        abs_v = abs(v)
        high_bits = (abs_v >> 4) & 0b1111
        low_bits = abs_v & 0b1111
        pattern_key = (high_bits ^ low_bits) | (low_bits << 2)
        freq_map[pattern_key] += 1
    return freq_map

# Main diagnostic engine
def analyze_system_state(readings, flags):
    # Irrelevant distraction: initialize unused monitoring structures
    telemetry_buffer = [0]*512
    calibration_sequence = [i**2 for i in range(10) if i % 3 != 0]
    checksum_log = set()
    
    # Preprocess sensor data
    processed = preprocess_readings(readings)
    
    # Distraction: complex but unused statistical analysis
    mean_val = sum(processed) / len(processed) if processed else 0
    variance = sum((x - mean_val)**2 for x in processed) / len(processed) if processed else 0
    entropy_proxy = -sum((x / 1000) * math.log(abs(x)/1000 + 1e-8) for x in processed) if processed else 0
    
    # Flag-based conditional processing
    critical_mode = any(f in flags for f in ['ERR_CRITICAL', 'OVRD_ENABLE'])
    debug_trace = flags.get('DEBUG_LEVEL', 0)
    
    # Real computation begins: coherence analysis
    if len(processed) < 3:
        base_score = sum(processed)
    else:
        base_score = int(calculate_coherence(processed[:10]) * 100)
    
    # Frequency pattern contribution
    patterns = extract_frequency_patterns(processed)
    pattern_bonus = sum(k % v for k, v in patterns.items() if k < 50) // 3 if patterns else 0
    
    # Red herring: elaborate unused neural weight simulation
    synaptic_weights = []
    for i in range(8):
        temp_weight = 0
        for j in range(i+1):
            temp_weight += (j * (i-j)) ** 1.5
        synaptic_weights.append(temp_weight)
    normalized_weights = [w / max(synaptic_weights) for w in synaptic_weights]
    
    # Decoy final calculation (never executed due to override)
    phantom_result = sum(normalized_weights) * base_score
    
    # ACTUAL result construction
    intermediate = base_score + pattern_bonus
    
    # Apply flag modifiers
    if critical_mode:
        intermediate *= 2
    if debug_trace > 5:
        intermediate += 50
    
    # Final transformation using bitwise and arithmetic mix
    final_diagnostic = (intermediate ^ 0x1F) + (intermediate & 0xFF) - 17
    
    # Output target variable
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
quantum_readings = [
    0.0012, -0.0034, 0.0056, 0.0078, -0.0019, 0.0023, 0.0067, -0.0045,
    0.0089, 0.0011, -0.0062, 0.0073, 0.0048, 0.0091, -0.0027
]
system_flags = {
    'STATUS': 'ACTIVE',
    'ERR_CRITICAL': True,
    'OVRD_ENABLE': False,
    'DEBUG_LEVEL': 3
}

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_readings, system_flags)