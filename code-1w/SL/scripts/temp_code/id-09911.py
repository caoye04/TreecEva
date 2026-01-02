def analyze_sensor_data(raw_readings, threshold=0.75):
    # Irrelevant preprocessing: normalize data (not actually used in final path)
    normalized = [x / max(raw_readings) for x in raw_readings if x > 0]
    filtered = [x for x in raw_readings if x > sum(raw_readings) / len(raw_readings)]

    # Distractor: complex but unused transformation chain
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            transformed.append(val ** 0.5 * (i + 1))
        else:
            transformed.append(val / 2.0)

    # Real computation begins: frequency analysis of digit patterns
    digit_frequencies = {}
    for reading in raw_readings:
        for digit in str(int(reading)):
            digit_frequencies[int(digit)] = digit_frequencies.get(int(digit), 0) + 1

    # Use set operations to identify rare digits
    all_digits = set(range(10))
    present_digits = set(digit_frequencies.keys())
    rare_digits = all_digits - present_digits  # digits never observed

    # Summation of positional contributions (only even-indexed matter)
    positional_sum = 0
    for idx, val in enumerate(raw_readings):
        if idx % 2 == 0:
            positional_sum += val * (idx + 1)

    # Tuple unpacking with red herring variables
    (baseline, _, amplitude) = (raw_readings[0], raw_readings[1], raw_readings[-1] - raw_readings[0])

    # Accumulate weighted score using enumerate and zip
    weights = [1, 2, 1, 3, 2]
    score_components = []
    for i, (val, w) in enumerate(zip(raw_readings[:5], weights)):
        adjusted = val * w
n        score_components.append(adjusted)

    aggregate_score = sum(score_components) / len(score_components)

    # Dead code path: looks important but unused
    def legacy_calibrate(x):
        return (x + 0.5) ** 2

    # Control flow with misleading intermediate
    if len(present_digits) > 5:
        correction_factor = 1.1
    else:
        correction_factor = 0.9  # This will be taken

    # Offset depends on rare digit count (decoy logic)
    offset_value = len(rare_digits) * 100  # Major red herring: inflates importance

    # Unused recursive function (dead artifact)
    def calculate_depth(n):
        return 1 + calculate_depth(n-1) if n > 0 else 0

    # Key execution point — answer derived here
    final_diagnostic = aggregate_score * correction_factor + offset_value

    # Print required output
    print(f"Result: {final_diagnostic}")

# Simulate sensor input (deterministic)
sensor_input = [142, 83, 267, 194, 335]
analyze_sensor_data(sensor_input)