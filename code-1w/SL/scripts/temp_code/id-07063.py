import itertools

# Sensor calibration constants (some are decoys)
BASE_SENSITIVITY = 0.87
OFFSET_CORRECTION = -2.1
DECOY_THRESHOLD = 999.9
UNUSED_SCALE = 42.0

# Simulated environmental sensor readings over time
time_series_data = [
    [12.5, 13.1, 11.9, 14.2],
    [13.3, 12.8, 13.0, 13.5],
    [11.7, 12.4, 13.1, 12.9],
    [14.0, 13.8, 14.1, 13.6],
    [12.6, 12.1, 11.8, 12.3]
]

# Irrelevant mapping for unused sensor type
decoymap = {k: v for k, v in enumerate('WXYZ')}

# Preprocess: normalize and filter anomalies
def preprocess_readings(raw_batches):
    cleaned_batches = []
    global_offset = OFFSET_CORRECTION  # Used
    
    for batch in raw_batches:
        adjusted = [round(x + BASE_SENSITIVITY + global_offset, 3) for x in batch]
        # Filter out values above a real threshold
        filtered = [x for x in adjusted if x < 15.0]  # Real filter
        if len(filtered) > 2:  # Only keep stable batches
            cleaned_batches.append(filtered)
    return cleaned_batches

# Misleading function that looks important but isn't used
def legacy_calibrate(x):
    return (x * UNUSED_SCALE) % 7.0

# Another red herring: complex transform with no downstream use
def spectral_transform(seq):
    result = 0
    for i, val in enumerate(seq):
        result += val * (i + 1) ** 0.5
    return result / (len(seq) + 1e-8)

# Real processing pipeline
processed_data = preprocess_readings(time_series_data)

# Decoy accumulation using itertools (unused)
combinations_test = list(itertools.combinations_with_replacement([1, 2], 3))
deep_entropy = sum(abs(hash(str(c))) % 100 for c in combinations_test)  # Unused

# Real analysis logic
aggregated_stats = []
for idx, segment in enumerate(processed_data):
    mean_val = sum(segment) / len(segment)
    variance = sum((x - mean_val) ** 2 for x in segment) / len(segment)
    # Weighted diagnostic score
    if idx % 2 == 0:
        weight = 1.1
    else:
        weight = 0.9
    score = (mean_val * 0.7) - (variance * 0.3) * weight
    aggregated_stats.append(round(score, 4))

# Higher-order reduction using lambda and itertools
group_pairs = list(itertools.pairwise(aggregated_stats))
fluctuation_index = sum(map(lambda pair: abs(pair[1] - pair[0]), group_pairs))

# Auxiliary irrelevant calculation
fake_trend = sum(aggregated_stats[i] * (0.5 ** i) for i in range(len(aggregated_stats)))  # Not used

# Core diagnostic analyzer
def analyze_readings(stats):
    base_level = sum(stats) / len(stats)
    adjustment_factor = 0.85 if fluctuation_index > 2.0 else 1.15
    
    # Simulate conditional hardware response
    response_curve = [
        base_level * (1 + 0.1 * i) for i in range(4)
    ]
    
    # Final computation path
    cumulative = 0
    for val in response_curve:
        cumulative += val * adjustment_factor
        cumulative = round(cumulative, 5)
    
    # Apply final non-linear correction
    final_value = cumulative ** 1.05
    
    # Dead code branch (never reached due to logic above)
    if DECOY_THRESHOLD < final_value:
        final_value *= 0.1
    
    return int(round(final_value))

# Trigger key statement
final_diagnostic = analyze_readings(processed_data)
print(f"Target result: {final_diagnostic}")