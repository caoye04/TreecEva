import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
    offset = 0.5
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant signal smoothing (distractor)
def smooth(signal):
    if len(signal) < 3:
        return signal
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

# Noise injection function (dead code path - never called)
def inject_noise(data, level=0.1):
    import random
    return [x + random.uniform(-level, level) for x in data]

# Core transformation: square root normalization
def normalize(values):
    return [math.sqrt(x) for x in values if x > 0]

# Data mode classification (partially relevant)
def classify_mode(data):
    avg = sum(data) / len(data)
    if avg < 2.0:
        return 'IDLE'
    elif avg < 5.0:
        return 'ACTIVE'
    else:
        return 'OVERDRIVE'

# String-based status encoder (uses string methods - relevant)
def encode_status(mode, version='v2'):
    base = f"SYS-{mode}-INIT"
    encoded = base.lower().replace('-', '_')
    suffix = version.upper()
    return f"{encoded}_{suffix}"

# Bitwise integrity check (distractor)
def verify_checksum(value_list):
    checksum = 0
    for v in value_list:
        truncated = int(abs(v) * 100) & 0xFF
        checksum ^= truncated
    return checksum & 0xF

# Higher-order function for dynamic filtering (lambda use)
def create_filter(threshold):
    return lambda x: x >= threshold

# Signal processor combining multiple concepts
def process_signal(raw_readings):
    # Step 1: Normalize the readings
    normalized = normalize(raw_readings)
    
    # Step 2: Apply dynamic filter (threshold based on first element)
    threshold = normalized[0] * 1.5
    fil = create_filter(threshold)
    filtered = [x for x in normalized if fil(x)]
    
    # Step 3: Detect anomalies (simple derivative check)
    derivatives = []
    for i in range(1, len(filtered)):
        derivatives.append(filtered[i] - filtered[i-1])
    
    # Step 4: Compute energy metric
    energy = sum([d ** 2 for d in derivatives]) if derivatives else 0.0
    
    # Misleading intermediate (not used later)
    peak = max(filtered) if filtered else 0.0
    decay_rate = (filtered[-1] / filtered[0]) if len(filtered) > 1 else 1.0
    
    # Generate metadata (string manipulation)
    mode = classify_mode(filtered)
    tag = encode_status(mode, 'v3')
    
    # Return structured result
    return {
        'data': filtered,
        'energy_metric': energy,
        'tag': tag,
        'peak_value': peak,  # Dead field
        'decay': decay_rate   # Dead field
    }

# Diagnostic analyzer (key function)
def analyze_signal(diag_input):
    data = diag_input['data']
    energy = diag_input['energy_metric']
    
    # Compute harmonic mean (requires all positive)
    if not data:
        return 0.0
    
    inv_sum = sum(1/x for x in data)
    harm_mean = len(data) / inv_sum
    
    # Apply correction based on energy
    if energy > 1.0:
        adjustment = math.log(energy + 1)
    else:
        adjustment = 0.1
    
    # Final diagnostic score
    base_score = harm_mean * 100
    final_score = base_score + (adjustment * 50)
    
    # Decoy computation (bit manipulation distractor)
    int_rep = int(final_score)
    decoy_bits = (int_rep << 2) ^ 0xAA
n    decoy_result = (decoy_bits & 0xFFFF) >> 3
    
    return final_score

# Orchestration function
def run_diagnostics():
    # Collect raw sensor data
    readings = collect_readings()
    
    # Smooth signal (computation with no downstream effect)
    smoothed_readings = smooth(readings)
    
    # Process the original readings (this matters)
    processed_data = process_signal(readings)
    
    # Accidentally pass smoothed data to verify_checksum (red herring call)
    _useless_checksum = verify_checksum(smoothed_readings)
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execute and capture
result = run_diagnostics()