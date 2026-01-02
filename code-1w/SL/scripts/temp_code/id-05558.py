import math

# Simulated sensor data and calibration parameters
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 50, 44, 46]
raw_signal = [0.88, 0.91, 0.85, 0.93, 0.87]

def calibrate_sensor(signal, factor=1.02):
    # Irrelevant calibration function (not used in final path)
    return [s * factor for s in signal]

def validate_readings(temps):
    # Dead code path: validates but doesn't affect main logic
    return all(20 < t < 30 for t in temps)

def accumulate_diagnostics(data):
    # Accumulates weighted diagnostics with red herring calculations
    base_score = sum(d * 1.1 for d in data)
    adjustment = 0
    for i in range(len(data)):
        if i % 2 == 0:
            adjustment += math.sin(data[i])  # Distractor computation
        else:
            adjustment += math.cos(data[i])  # Another misleading term
    return base_score + adjustment * 0.1  # Minor effect, looks important

def encode_timestamp(year, month, day):
    # Unused utility function — dead code
    return f'{year}{month:02d}{day:02d}'

def normalize_vector(vec):
    # Decoy function that looks critical but is unused
    norm = math.sqrt(sum(v**2 for v in vec))
    return [v / norm for v in vec] if norm > 0 else vec

def preprocess_signal(sig):
    # Actual preprocessing step
    filtered = [s for s in sig if s > 0.85]  # Only keep strong signals
    return [f * 1.25 for f in filtered]  # Amplify for analysis

def compute_entropy(data):
    # Misleading complexity: computes entropy but not used in final result
    total = sum(data)
    probs = [(d / total) for d in data]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 6)

def assess_stability(indices):
    # Red herring function: appears related but irrelevant
    if len(indices) < 3:
        return 'UNSTABLE'
    trend = sum(indices[i] <= indices[i+1] for i in range(len(indices)-1))
    return 'STABLE' if trend >= len(indices)/2 else 'VOLATILE'

def generate_checksum(values):
    # Bit manipulation distractor
    chk = 0
    for v in values:
        chk ^= int(v * 100) & 0xFF
        chk = (chk << 1 | chk >> 7) & 0xFF  # Rotate left
    return chk

def analyze_signal(data):
    # Core analysis logic
    magnitude = sum(data)
    if magnitude > 3.0:
        level_code = 3
    elif magnitude > 2.5:
        level_code = 2
    else:
        level_code = 1
    
    # Conditional expression used meaningfully
    modifier = 1.75 if any(d > 1.0 for d in data) else 1.25
    
    # Final diagnostic score computed here
    diagnostic_value = magnitude * modifier + level_code * 0.5
    
    # Irrelevant string transformation — distractor
    status_tag = 'OK' if diagnostic_value > 3.0 else 'CHECK'
    status_log = f'Status: {status_tag}, Code={level_code}'
    status_words = status_log.split()
    joined = '-'.join([word.lower() for word in status_words if len(word) > 2])
    
    # This assignment is just to create noise
    dummy_report = f'Diagnostic complete. Words: {len(status_words)}, Key: {joined}'
    
    return diagnostic_value

# Begin actual relevant execution flow
valid_temp = validate_readings(temperature_readings)  # Called but result not used
entropy_metric = compute_entropy(humidity_readings)  # Computed but unused
checksum = generate_checksum(raw_signal)  # Another decoy calculation

processed_signal = preprocess_signal(raw_signal)

# The key statement that produces the target variable
final_diagnostic = analyze_signal(processed_signal)

# Print final result as required
print(f"Target result: {final_diagnostic}")