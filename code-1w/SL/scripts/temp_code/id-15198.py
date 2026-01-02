import math

def preprocess_sensor(readings):
    # Irrelevant transformation (dead code path)
    normalized = [r / 100.0 for r in readings]
    filtered = []
    for r in readings:
        if r > 50 and r < 300:  # Real filter
            filtered.append(r * 0.95)
    return filtered

def transform_sequence(data):
    # Distractor function – looks important but unused
    return [d ** 2 for d in data[::2]]

def compute_entropy(values):
    # Misleading intermediate calculation
    total = sum(values)
    probs = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return round(entropy, 4)

def decode_pattern(seq):
    # Unused complex logic (red herring)
    shifted = seq[-3:] + seq[:-3]
    xor_key = 0
    for s in shifted:
        xor_key ^= int(s)
    return xor_key % len(seq)

def validate_signal(signal):
    # Dead validation branch with side computation
    if len(signal) == 0:
        return False
    peak = max(signal)
    avg = sum(signal) / len(signal)
    fluctuation = peak - avg
    tolerance = 0.1 * avg
    score = 0
    if fluctuation > tolerance:
        score += 10
    else:
        score += 5
    # This score is never used
    return True

def analyze_readings(data, limit):
    # Core logic embedded in noise
    adjusted = []
    for val in data:
        if val < limit:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.9)
    
    # Real key computation
    base_sum = sum(adjusted)
    correction_factor = len(adjusted) if len(adjusted) > 0 else 1
    raw_diagnostic = base_sum / correction_factor
    
    # Apply non-linear adjustment (critical step)
    if raw_diagnostic > 150:
        raw_diagnostic -= 27.3
    elif raw_diagnostic < 100:
        raw_diagnostic += 12.7
    
    # Secondary adjustment based on parity (hidden dependency)
    if int(raw_diagnostic) % 2 == 0:
        raw_diagnostic *= 1.05
    else:
        raw_diagnostic *= 0.95
    
    return int(round(raw_diagnostic))

# Simulated sensor input (real data source)
sensor_readings = [120, 145, 98, 210, 176, 89, 134, 167]

# Dead variables and misleading preprocessing
entropy_check = compute_entropy(sensor_readings)
valid = validate_signal(sensor_readings)
decoy_result = decode_pattern(sensor_readings)
transformed_junk = transform_sequence(sensor_readings)

# Actual processing chain
processed_data = preprocess_sensor(sensor_readings)
threshold = 150

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")