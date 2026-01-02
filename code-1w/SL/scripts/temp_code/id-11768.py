import itertools

# Simulated sensor array data with noise and calibration factors
def process_sensors(raw_readings, baseline):
    calibrated = []
    for val in raw_readings:
        adjusted = (val - baseline) * 1.05
        if abs(adjusted) > 0.1:
            calibrated.append(round(adjusted, 3))
    return calibrated

# Irrelevant helper: computes signal harmonics (not used in final path)
def compute_harmonics(frequency, order=3):
    return [frequency * (i + 1) for i in range(order)]

# Data transformation pipeline
def transform_sequence(seq):
    shifted = [(x << 1) ^ 3 for x in seq]  # Bit manipulation red herring
    filtered = [x for x in shifted if x % 2 == 1]  # Keep only odd values
    return list(itertools.accumulate(filtered, lambda a, b: a + (b // 3)))

# Misleading analysis branch: spectral weight calculation (dead end)
def spectral_weight(data):
    total = 0
    for i, d in enumerate(data):
        total += d * (i % 5 + 1) ** 0.5
    return round(total, 4)

# Core diagnostic logic (decoy function present to distract)
def evaluate_stability(readings, limit):
    cumulative = 0
    for r in readings:
        if r > limit:
            cumulative += r // 2
        else:
            cumulative -= r
    return abs(cumulative)

# Actual analysis function used in result
def analyze_pattern(values, thresh):
    count_above = sum(1 for v in values if v > thresh)
    rolling_avg = 0
    for i in range(1, len(values)):
        rolling_avg += (values[i] + values[i-1]) / 2
    
    # Key computation path
    adjustment_factor = len(values) // (count_above if count_above != 0 else 1)
    score = int(rolling_avg // adjustment_factor)
    
    # Decoy operations below
    _ = [x * 1.5 for x in values if x < thresh]  # Unused list comprehension
    _temp_sum = sum(x ** 2 for x in values)     # Dead computation
    
    return score

# Simulate system diagnostics
if __name__ == '__main__':
    # Raw sensor inputs (simulated)
    raw_data = [12, 8, 15, 6, 23, 9, 11, 14]
    base_offset = 7
    
    # Step 1: Calibrate sensor readings
    processed_signal = process_sensors(raw_data, base_offset)
    
    # Irrelevant diagnostic trace
    _harmonic_frequencies = compute_harmonics(440, 5)
    _unused_metric = spectral_weight(processed_signal)
    
    # Step 2: Transform into integer sequence for pattern analysis
    integer_stream = [int(x * 10) for x in processed_signal]
    transformed_data = transform_sequence(integer_stream)
    
    # Dead branch execution (no effect on result)
    _stability_score = evaluate_stability(transformed_data, 20)
    
    # Control thresholds
    threshold = 15
    buffer_limit = 30  # Unused parameter
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print final result
    print(f"Result: {final_diagnostic}")