def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.1]
    magnitude = sum(abs(s) for s in filtered)
    peaks = [i for i, s in enumerate(filtered) if s > 0.5]
    return magnitude, len(peaks)


def compute_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = -sum((count / len(seq)) * log2(count / len(seq)) for count in freq.values())
    return entropy

# Irrelevant helper (distractor)
def validate_checksum(data):
    checksum = 0
    for b in data:
        checksum = (checksum + b) % 256
    return checksum == 42

# Unused transformation (dead code path)
def transform_coordinates(coords):
    return [(y * 2, x // 2) for x, y in coords if x % 2 == 0]

# Decoy metric with misleading intermediate result
total_inconsistencies = 0
for i in range(100):
    total_inconsistencies += (i * i) % 17

# Real signal data (simulated sensor readings)
sensor_readings = [
    [0.05, 0.3, 0.7, -0.2, 0.1],
    [0.4, 0.6, 0.01, 0.8, -0.5],
    [0.2, 0.9, 0.15, 0.33, 0.44]
]

# Simulated diagnostics map
diagnostics = {
    'threshold': 0.25,
    'gain': 1.8,
    'channels': ['A', 'B', 'C'],
    'calibration': [0.1, -0.05, 0.2]
}

# Auxiliary data with red herring values
aux_data = {
    'version': '2.1.5',
    'uptime': 87432,
    'errors_seen': 12,
    'last_reset': '2023-08-14'
}

# Process raw readings into metrics
readings = []
for idx, sample_set in enumerate(sensor_readings):
    mag, peak_count = analyze_signal(sample_set)
    adjusted_mag = mag * diagnostics['gain']
    normalized_peaks = peak_count / (len(sample_set) + 1)
    readings.append({
        'index': idx,
        'magnitude': adjusted_mag,
        'peaks': normalized_peaks,
        'quality': 'high' if adjusted_mag > 1.0 else 'low'
    })

# Misleading combinatorics calculation (distractor)
combination_total = 0
for i in range(1, len(readings) + 1):
    prod = 1
    for j in range(i):
        prod *= (j + 1)
    combination_total += prod

# Real processing function
def process_metrics(diag, data):
    base_score = 0
    stability_factors = []
    
    for entry in data:
        if entry['quality'] == 'high':
            base_score += entry['magnitude']
            stability_factors.append(entry['peaks'])
    
    # Use enumerate and zip: align channels with factors
    channel_map = {i: ch for i, ch in enumerate(diag['channels'])}
    zipped_factors = list(zip(stability_factors, [1.1, 0.9, 1.0]))  # weights
    weighted_stability = sum(sf * w for sf, w in zipped_factors)
    
    # Apply calibration offsets (tuple unpacking)
    c1, c2, c3 = diag['calibration']
    calibration_adjustment = abs(c1) + abs(c2) + abs(c3)
    
    # Final diagnostic score
    final_score = base_score + (weighted_stability * 100)
    final_score -= calibration_adjustment * 5
    
    # Dead branch: never executed due to fixed threshold (red herring)
    if base_score < 0:
        final_score *= 0.5  # unreachable
    
    return int(round(final_score))

# Execute main computation
final_diagnostic = process_metrics(diagnostics, readings)

# Print result as required
print(f"Target result: {final_diagnostic}")