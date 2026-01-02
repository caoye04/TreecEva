def analyze_readings(raw_data, scale_factor):
    processed = []
    temp_offset = 0.75
    for val in raw_data:
        if val < 0:
            adjusted = abs(val) * scale_factor + temp_offset
        else:
            adjusted = val ** 0.5 * scale_factor
        processed.append(round(adjusted, 3))
    return processed


def generate_baseline(count, seed=100):
    # Distractor: Unused function
    import random
    random.seed(seed)
    return [random.randint(1, 50) for _ in range(count)]


def validate_sequence(seq):
    # Distractor: Partially executed but irrelevant
    checksum = 0
    for i, x in enumerate(seq):
        if i % 3 == 0:
            checksum += x * 2
        elif i % 3 == 1:
            checksum -= x // 3
    return checksum % 100 == 0


def extract_features(data_string):
    # Uses string methods
    tokens = data_string.strip().split(',')
    cleaned = [t.strip().zfill(4) for t in tokens]
    numeric_part = [int(c[-2:]) for c in cleaned if c.isdigit() or c[-2:].isdigit()]
    return [n for n in numeric_part if n % 2 == 1]


def compute_weighting(values, mode='normal'):
    weights = []
    total = sum(values)
    avg = total / len(values) if values else 1
    for v in values:
        if mode == 'inverse':
            w = 1 / (v + 1)
        else:
            w = (v + avg) ** 0.3
        weights.append(round(w, 4))
    return weights


def transform_signal(signal_seq):
    # Bit manipulation and logical ops
    result = []
    mask = 0b1010
    for s in signal_seq:
        s = s ^ mask
        s = (s << 1) & 0b1111
        s = s | (s >> 2)
        result.append(s & 0b1111)
    return result


def merge_diagnostics(a, b, c):
    # Irrelevant aggregation
    return (a * 2 + b * 3 + c * 5) // 10


def process_metrics(signature, thresholds):
    score = 0
    for key, value in signature.items():
        limit = thresholds.get(key, 10)
        if value > limit:
            score += value // limit
        elif value == limit:
            score += 1
        else:
            score -= 1
    return int(score * 1.5)

# Main execution with distractors
raw_input_data = [16, -9, 25, -4, 36]
scale_multiplier = 2.5

# Step 1: Analyze sensor readings
calibrated_readings = analyze_readings(raw_input_data, scale_multiplier)

# Step 2: Extract hidden features from config string
config_str = " A3 , B7 , CX , D9 , E0 "
feature_codes = extract_features(config_str)

# Step 3: Compute weighting profile (distractor usage)
weight_profile = compute_weighting(feature_codes, mode='normal')

# Step 4: Simulate signal transformation (bitwise path)
signal_chain = [5, 3, 12, 6]
transformed_signal = transform_signal(signal_chain)

# Step 5: Build health signature using only some components
health_signature = {
    'core_temp': int(calibrated_readings[0]),
    'voltage_stress': transformed_signal[2],
    'noise_level': len(weight_profile),
    'sync_jitter': feature_codes[1] if len(feature_codes) > 1 else 5
}

# Step 6: Define dynamic thresholds
threshold_map = {
    'core_temp': 8,
    'voltage_stress': 10,
    'noise_level': 3,
    'sync_jitter': 7
}

# Step 7: Process final diagnostic score
final_diagnostic = process_metrics(health_signature, threshold_map)

# Distractor variables
dummy_data = [x * 0.1 for x in raw_input_data if x > 0]
baseline_ref = generate_baseline(5)
valid = validate_sequence([1, 2, 3, 4, 5])
interim_result = merge_diagnostics(health_signature['core_temp'], health_signature['noise_level'], 15)

# Final output
print(f"Result: {final_diagnostic}")