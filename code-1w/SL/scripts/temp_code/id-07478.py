from collections import defaultdict
import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_data):
    filtered = []
    noise_floor = 0.003
    for val in raw_data:
        if abs(val) > noise_floor:
            filtered.append(round(val * 1000))
    return filtered

# Irrelevant helper: spectral decomposition (unused)
def decompose_spectrum(signal):
    result = []
    for i in range(len(signal)):
        component = 0
        for j in range(i + 1):
            component += signal[j] * math.sin(i * j * 0.1)
        result.append(component)
    return result

# Signal pattern analyzer with bit masking
def detect_anomalies(sequence, threshold=5):
    count_map = defaultdict(int)
    anomaly_flags = []
    cumulative = 0
    
    for x in sequence:
        bin_rep = bin(x & 0xFFFF).count('1')
        parity = bin_rep % 2
        count_map[parity] += 1
        
        temp_score = 0
        if x > threshold:
            temp_score += x ^ 7
        if x < -threshold:
            temp_score -= x | 3
            
        # Red herring: intermediate score not used later
        dummy_diagnostic = (temp_score * 1.5) % 100
        
        anomaly_flags.append(parity == 1 and abs(x) > threshold)
        cumulative += abs(x) // (abs(parity - 0) + 1)
    
    # Dead code path: never accessed in execution
    if False:
        fallback = sum(count_map.values()) * -1
        return [fallback]
        
    return anomaly_flags, cumulative

# Core logic: pattern and mask interaction
def analyze_signal(buffer, mask):
    shifted = 0
    for i, val in enumerate(buffer):
        if i % 2 == 0:
            shifted ^= (val << 1) & mask
        else:
            shifted ^= (val >> 2) | mask
    
    # Secondary transformation chain
    transformed = shifted
    transformed = (transformed ^ (transformed << 3)) & 0xFFFF
    transformed = (transformed ^ (transformed >> 5)) & 0xFFFF
    transformed = (transformed ^ (transformed << 2)) & 0xFFFF
    
    # Final adjustment based on string-derived key (distractor usage)
    key_hint = 'diagnose_872'
    offset = int(key_hint[-3:])  # Extract 872
    adjusted = (transformed - offset) * 2
    
    # Decoy variable with plausible name but no impact
    calibration_checksum = sum([ord(c) for c in key_hint]) * 17
    
    return adjusted

# Unused function: mimics important logic but disconnected
def validate_consistency(trace):
    return len(trace) % 4 == 0 and sum(trace) != 0

# Simulated telemetry stream
telemetry_stream = [
    -0.001, 0.002, -0.0001, 0.0045, 0.012, -0.008,
    0.023, 0.018, -0.015, 0.009, 0.011, -0.006
]

# Signal processing pipeline
raw_deltas = [-23, 15, -37, 42, 29, -51, 18, 33, -26]
decoy_input = [x * 2 for x in raw_deltas if x > 0]  # Unused branch

processed = preprocess_readings(telemetry_stream)
anomaly_result, activity_total = detect_anomalies(processed, threshold=4)

# Setup for target computation
pattern_buffer = [x + 10 for x in raw_deltas]
fault_mask = 0xFF  # 8-bit mask for diagnostics

# Introduce irrelevant string processing
log_entry = "ERR_CODE_285_RESET"
error_digits = ''.join(filter(str.isdigit, log_entry))
reset_code = int(error_digits) % 100  # Distractor

# Key diagnostic computation
final_diagnostic = analyze_signal(pattern_buffer, fault_mask)

# Print required output
print(f"Result: {final_diagnostic}")