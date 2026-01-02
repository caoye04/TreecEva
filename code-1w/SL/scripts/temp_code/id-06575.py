import itertools

def analyze_pattern(sequence, mask):
    accumulator = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            accumulator += val ^ mask
        else:
            accumulator -= val & (mask >> 1)
    return accumulator

def evaluate_stability(readings):
    temp_log = [abs(r - 50) for r in readings]
    baseline = sum(temp_log) / len(temp_log)
    adjustment = 0
    for t in temp_log:
        if t > baseline:
            adjustment += t * 0.1
    return baseline + adjustment

def generate_key(seeds):
    key = 0
    for s in seeds:
        key ^= (s * 3) % 257
    return key

def decode_fragment(fragment):
    # Irrelevant decoding logic (dead path)
    decoded = ''.join(chr((f % 94) + 33) for f in fragment)
    return hash(decoded) % 100

def main_diagnostic():
    # Simulated sensor readings (real data)
    sensor_array = [85, 42, 73, 55, 61, 44, 79]
    calibration_mask = 0b1101

    # Real processing branch
    processed_signal = analyze_pattern(sensor_array, calibration_mask)

    # Distractor: fake signal chain
    decoy_signals = [[80, 40, 70], [88, 45, 72], [82, 41, 74]]
    fake_aggregates = []
    for ds in decoy_signals:
        fake_aggregates.append(sum(x ** 0.5 for x in ds))

    # Another red herring: stability evaluation (not used in final result)
    dummy_readings = [52, 48, 55, 49, 53, 51, 50]
    stability_score = evaluate_stability(dummy_readings)  # Unused

    # Real computation: construct health signature
    health_signature = []
    for idx, val in enumerate(sensor_array):
        shifted = val << 1
        if idx % 3 == 0:
            health_signature.append(shifted | calibration_mask)
        elif idx % 3 == 1:
            health_signature.append(shifted & ~calibration_mask)
        else:
            health_signature.append(shifted ^ calibration_mask)

    # Generate unused cryptographic key (distractor)
    seed_sequence = [17, 23, 19, 29]
    crypto_key = generate_key(seed_sequence)

    # Build threshold map with dictionary operations
    levels = ['critical', 'high', 'medium', 'low']
    base_values = [90, 70, 50, 30]
    threshold_map = {lvl: base * 1.1 for lvl, base in zip(levels, base_values)}
    threshold_map['dynamic'] = processed_signal * 0.2  # Not used

    # Conditional expression red herring
    fallback_mode = True if sum(health_signature) > 500 else False

    # Real function that determines answer
    def process_metrics(signature, thresholds):
        total = 0
        # Use itertools to create combinations (only for side effect of iteration)
        for combo in itertools.combinations(signature[:4], 2):
            diff = abs(combo[0] - combo[1])
            if diff > thresholds['medium']:
                total += diff // 10
        # Actual critical calculation
        pivot = signature[2] & 0xFF
        modifier = len([x for x in signature if x % 2 == 1])
        return (pivot * 3) - (modifier * 7) + 100

    # Critical assignment
    final_diagnostic = process_metrics(health_signature, threshold_map)

    # Dead code path
    if final_diagnostic < 0:
        backup_chain = decode_fragment(sensor_array)
        final_diagnostic = backup_chain

    # Print result as required
    print(f"Result: {final_diagnostic}")

main_diagnostic()