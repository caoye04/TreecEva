def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    # Irrelevant transformation (dead logic path)
    temp_analysis = [x ** 2 + 2 * x + 1 for x in seq if x % 2 == 0]
    temp_analysis = list(map(lambda y: y - 1 if y > 5 else y, temp_analysis))

    # Distractor: complex but unused calculation
    decoy_score = sum([seq[i] * seq[i+1] for i in range(len(seq)-1)]) % 97
    decoy_score += sum(seq) // 7

    # Real logic starts here — only this part matters
    filtered = [x for x in seq if x > 0 and x % 3 == 0]
    transformed = [(x // 3) ^ i for i, x in enumerate(filtered)]  # Bitwise XOR with index
    if len(transformed) == 0:
        return 0
    
    rolling_hash = 0
    for val in transformed:
        rolling_hash = (rolling_hash * 7 + val) % 10007
    
    return rolling_hash


def validate_structure(arr):
    # Unused validation function — red herring
    if not arr:
        return False
    return all(isinstance(x, int) for x in arr)


def compute_diagnostic(signal):
    # Complex-looking but irrelevant diagnostics
    magnitude = sum(abs(x) for x in signal)
    peak = max(signal, default=0)
    baseline = magnitude / len(signal) if signal else 0
    deviation = sum((x - baseline) ** 2 for x in signal) ** 0.5
    
    # Decoy diagnostic flags
    flag_alpha = (magnitude % 5) == 0
    flag_beta = (peak & 1) == 1
    flag_gamma = len(signal) in [x for x in range(5, 15)]
    
    # None of these affect main result
    return deviation if flag_alpha else baseline


def process_sequence(input_data):
    # Main data pipeline
    stage1 = [x + 10 for x in input_data]
    
    # Apply filter based on dynamic condition
    threshold = sum(stage1) // len(stage1) if stage1 else 0
    stage2 = [x for x in stage1 if x < threshold + 5]
    
    # Introduce lambda-based transformation (required feature)
    modifier = lambda z: z * 2 if z % 4 == 0 else z + (z % 4)
    stage3 = [modifier(x) for x in stage2]
    
    # Secondary filtering
    stage4 = [x for x in stage3 if x % 2 == 1]  # Keep only odds
    
    # Key computation — checksum built step by step
    checksum = 0
    for i, v in enumerate(stage4):
        checksum = (checksum + v * (i + 1) * 3) % 987653
    
    # Distractor: another unused accumulator
    alt_sum = 0
    for x in stage3:
        alt_sum += x ^ (x << 1) % 100
    alt_sum = (alt_sum * 13) % 100000

    # Early return decoy — never reached due to logic
    if checksum < 0:
        return -1

    # Final interference: call unrelated analysis (its return is ignored)
    _ = analyze_pattern(input_data)
    _ = compute_diagnostic(input_data)

    return checksum

# Simulated sensor readings (real input)
data = [12, -5, 9, 0, 21, 3, 8, 6, 15, 4, 7]

# Target execution point
checksum = process_sequence(data)
print(f"Result: {checksum}")