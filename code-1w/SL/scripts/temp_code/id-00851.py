import itertools

# Sensor data processing simulation with noise filtering and calibration
raw_readings = [1024, 512, 256, 1024, 768, 896, 384, 128, 640, 576]
noise_floor = 128
calibration_map = {256: 1.1, 512: 1.25, 768: 1.4, 1024: 1.6}
dummy_tracker = {i: 0 for i in range(10)}

def collect_diagnostics(data):
    stats = {}
    stats['peak'] = max(data)
    stats['trough'] = min(data)
    stats['span'] = stats['peak'] - stats['trough']
    stats['density'] = len([x for x in data if x > 500])
    return stats

def apply_mask(signal, mask_value=255):
    # Irrelevant masking function (not used in main logic)
    return [s & mask_value for s in signal]

def generate_combinations(values):
    # Dead utility: generates unused combinations
    return list(itertools.combinations(values, 3))

def filter_artifacts(readings, threshold):
    # Remove values below noise floor
    cleaned = [r for r in readings if r >= threshold]
    # Add irrelevant transformation
    temp_analysis = [c * 0.9 for c in cleaned if c % 256 == 0]
    spike_count = sum(1 for i in range(1, len(cleaned)) if abs(cleaned[i] - cleaned[i-1]) > 200)
    return cleaned

def compute_entropy(data):
    # Distractor function: calculates symbolic entropy but unused
    from math import log2
    freqs = {}
    for d in data:
        freqs[d] = freqs.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freqs.values())
    return round(entropy, 4)

def derive_key(readings_list):
    # Misleading key derivation with red herring logic
    base = sum(r // 64 for r in readings_list) * 3
    modifier = len([r for r in readings_list if r & (r - 1) == 0])  # Count powers of two
    return base + modifier * 7

def validate_integrity(chunk):
    # Unused validation stub
    checksum = sum(chunk) % 256
    return checksum < 100

def process_readings(dataset, scale):
    # Core logic hidden among distractions
    baseline = sum(dataset) / len(dataset)
    adjusted = [d * scale for d in dataset]
    deviation = sum(abs(a - baseline * scale) for a in adjusted)
    category_bins = {'high': 0, 'medium': 0, 'low': 0}
    for val in adjusted:
        if val > 800:
            category_bins['high'] += 1
        elif val > 400:
            category_bins['medium'] += 1
        else:
            category_bins['low'] += 1
    # Critical computation
    diagnostic_score = int((deviation // 100) + category_bins['high'] * 10)
    return diagnostic_score

# Begin main execution flow
initial_stats = collect_diagnostics(raw_readings)

# Generate unused combinatorial set (red herring)
combination_set = generate_combinations(raw_readings)

# Filter out low-amplitude noise
filtered_data = filter_artifacts(raw_readings, noise_floor)

# Compute irrelevant entropy metric
entropy_metric = compute_entropy(filtered_data)

# Derive misleading key
false_key = derive_key(filtered_data)

# Determine calibration factor using map lookup (only 1024 and 768 are present)
calibration_factor = sum(calibration_map[r] for r in set(filtered_data) if r in calibration_map)

# Perform core processing on filtered data with computed factor
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Print result as required
print(f"Result: {final_diagnostic}")