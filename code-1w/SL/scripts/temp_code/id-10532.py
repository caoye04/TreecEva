import math

# Simulated sensor array data from environmental monitoring station
def fetch_sensor_array():
    return [
        (120.5, 88.2, 70.1, 95.3),
        (110.3, 85.7, 72.6, 93.0),
        (115.8, 87.1, 71.3, 94.5),
        (119.0, 86.9, 73.0, 96.1),
        (117.3, 88.0, 70.9, 95.7)
    ]

def calculate_stability_index(readings):
    # Irrelevant stability metric (dead end)
    base = sum(r[0] for r in readings) / len(readings)
    variance = sum((r[1] - base) ** 2 for r in readings)
    return variance / len(readings)

def extract_critical_band(data):
    # Extracts band used in final calculation
    band = []
    for i, row in enumerate(data):
        if i % 2 == 0:
            band.append(row[2])  # Only even rows contribute
        else:
            temp_val = row[3] * 0.1  # Distractor computation
            band.append(temp_val)     # Misleading inclusion
    return band

def compute_entropy(values):
    # Unused complex distractor function (red herring)
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 6)

def apply_correction_factor(x, level=2):
    # Bit manipulation red herring
    if x < 70:
        shifted = int(x * 10) << 1
        return shifted ^ 5
    return int(x)

def filter_outliers(stream, limit=1.5):
    # Dead code path — never actually used in main logic
    mean_val = sum(stream) / len(stream)
    std_dev = (sum((x - mean_val) ** 2 for x in stream) / len(stream)) ** 0.5
    return [x for x in stream if abs(x - mean_val) <= limit * std_dev]

def aggregate_magnitude(samples):
    # Correct processing path begins here
    magnitude = 0
    for idx, val in enumerate(samples):
        if idx == 0:
            magnitude += val * 2
        elif idx % 2 == 0:
            magnitude += val + 5
        else:
            magnitude += round(val * 0.5)
    return magnitude

def validate_consistency(seq):
    # Complex but irrelevant validation chain
    checksum = 0
    for a, b in zip(seq[:-1], seq[1:]):
        checksum += abs(a - b) * 100
    return checksum < 500

def derive_reference_key(items):
    # Decoy transformation with tuple unpacking distraction
    keys = []    
    for item in items:
        a, b, c, d = item
        ref = (a // 10) ^ (b // 10) | int(c)
        keys.append((ref, c))  # Partially used later as decoy
    return keys

def process_readings(raw_data, config_thresholds):
    # Core logic buried within distractions
    
    # Distractor: unused derived structures
    keymap = derive_reference_key(raw_data)
    stability = calculate_stability_index(raw_data)
    entropy_metric = compute_entropy([r[1] for r in raw_data])
    
    # Real signal extraction
    signal_band = extract_critical_band(raw_data)
    
    # Apply correction (only some values matter)
    corrected = []
    for val in signal_band:
        corrected.append(apply_correction_factor(val))
    
    # Filter not applied — just shown to mislead
    # filtered = filter_outliers(corrected)  # Commented out: dead path
    
    # Main aggregation
    score = aggregate_magnitude(corrected)
    
    # Final adjustment using config (thresholds used only partially)
    adjustment = 0
    for t in config_thresholds['levels']:
        if t > 70:
            adjustment += 2
    
    # Critical result
    final_diagnostic = score * 3 - adjustment
    
    # Extra misleading branches
    if validate_consistency(signal_band):
        final_diagnostic += 100  # Never triggers due to data
    
    return final_diagnostic

# Orchestration block
collected_data = fetch_sensor_array()
thresholds = {
    'levels': [65, 72, 68, 75],
    'flags': { 'mode': 'safe', 'debug': False },
    'weights': (0.1, 0.3, 0.6)
}

# Execution point of interest
final_diagnostic = process_readings(collected_data, thresholds)

print(f"Result: {final_diagnostic}")