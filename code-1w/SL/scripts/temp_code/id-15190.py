import math

def analyze_signal(strength, noise):
    # Irrelevant signal processing function (dead code path)
    return (strength + noise) / (strength - noise + 1e-5)

def validate_checksum(data):
    # Unused validation logic (distractor)
    checksum = 0
    for d in data:
        checksum ^= d % 256
    return checksum == 0xFF

def extract_features(log_stream):
    # Distracting feature extraction with no impact on final result
    features = {}
    for entry in log_stream:
        if 'error' in entry:
            features[entry] = len(entry)
    return features

def compute_entropy(sequence):
    # Misleading entropy calculation (red herring)
    freq = {}
    for c in sequence:
        freq[c] = freq.get(c, 0) + 1
    entropy = 0.0
    for f in freq.values():
        p = f / len(sequence)
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 3)

def transform_key(signal_vector):
    # Obfuscating transformation that isn't used
    transformed = []
    for i, val in enumerate(signal_vector):
        transformed.append((val ^ (i * 3)) % 100)
    return transformed

def process_metrics(log_data, state):
    # Core logic embedded in distractions
    temp_buffer = []
    critical_flag = False
    accumulator = 0
    
    # Real logic starts here — multiple steps with interference
    for line in log_data:
        stripped = line.strip().lower()
        if 'critical' in stripped:
            critical_flag = True
        if 'readings:' in stripped:
            parts = stripped.split(':')
            numbers = [float(x) for x in parts[1].split(',')]
            temp_buffer.extend(numbers)
    
    # Actual computation chain (8-12 steps)
    if critical_flag and len(temp_buffer) > 0:
        avg_reading = sum(temp_buffer) / len(temp_buffer)
        squared_total = sum(x ** 2 for x in temp_buffer)
        rms_value = math.sqrt(squared_total / len(temp_buffer))
        
        # Conditional expression (required python feature)
        adjustment_factor = 1.75 if rms_value > 40 else 0.85
        
        intermediate_score = avg_reading * adjustment_factor
        
        # Dictionary operations (required python feature)
        diagnostics = {
            'baseline': 23.7,
            'reading_count': len(temp_buffer),
            'adjusted_avg': intermediate_score,
            'status_code': state['health']
        }
        
        # More real logic
        offset = diagnostics['baseline'] - diagnostics['adjusted_avg']
        penalty = 0
        
        if diagnostics['status_code'] == 'degraded':
            penalty = 12
        elif diagnostics['status_code'] == 'faulty':
            penalty = 27
        
        # Final computation
        raw_diagnostic = abs(offset) + penalty
        final_diagnostic = int(round(raw_diagnostic * 10))
        
        # Dead code branch (distractor)
        if final_diagnostic < 0:
            final_diagnostic = -1  # Never reached
        
        return final_diagnostic
    
    return -999

# Simulated input data
log_data = [
    "System boot complete",
    "INFO: readings: 12.5, 45.0, 67.3, 89.1, 23.4",
    "WARNING: minor fluctuation",
    "CRITICAL: anomaly detected",
    "DEBUG: readings: 34.2, 56.7, 78.9"
]

system_state = {
    'mode': 'diagnostic',
    'health': 'degraded',  # Triggers penalty
    'uptime': 1274,
    'version': '3.7.1'
}

# Unused variables (distractors)
noise_profile = [0.1, 0.4, 0.2, 0.6]
signal_log = [112, 107, 99, 105]
dummy_matrix = [[1,2],[3,4]]

# Key statement
final_diagnostic = process_metrics(log_data, system_state)

# Output result
print(f"Result: {final_diagnostic}")