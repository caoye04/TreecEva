def analyze_sensor(stream, baseline=0.73):
    """Simulate multi-stage sensor analysis with noise filtering."""
    if not stream:
        return [0]

    # Irrelevant transformation: frequency mapping (dead path)
    freq_map = {i: val * 0.1 for i, val in enumerate(stream) if val > 5}
    temp_adjust = sum(freq_map.values()) * 0.3

    # Core signal extraction (relevant)
    filtered = [x for x in stream if 1.0 <= x <= 9.0]
    normalized = [(x - 1.0) / 8.0 for x in filtered]  # Scale to [0,1]

    # Distractor: unused statistical moment calculations
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized) if normalized else 0
    skewness = sum((x - mean_val) ** 3 for x in normalized) / len(normalized) if variance > 0 else 0

    # Red herring: entropy-like computation (not used later)
    import math
    entropy = -sum(p * math.log(p + 1e-9) for p in normalized if p > 0)

    # Relevant binning logic
    bins = [0] * 4
    for val in normalized:
        idx = min(int(val * 4), 3)
        bins[idx] += 1

    # Misleading intermediate result (unused final score)
    quality_score = sum(bins[i] * (i+1) for i in range(4)) / len(normalized) if normalized else 0

    return bins


def encrypt_payload(data):
    """Dummy encryption function - no actual use in final result."""
    encoded = []
    shift = 7
    for d in data:
        shifted = ((d * 100) + shift) % 256
        encoded.append(int(shifted))
    return encoded  # Dead end


def decode_signal(signal):
    """Reverse transformation - irrelevant but looks important."""
    result = []
    for s in signal:
        raw = (s - 128) / 100.0
        result.append(abs(raw))
    return result


def transform_coordinates(x, y):
    """Geospatial decoy function - never called"""
    lat = x * 0.001 + 37.0
    lon = y * 0.001 - 118.0
    return lat, lon

# Simulated IoT sensor readings (mV)
sensor_readings = [0.5, 2.3, 5.6, 8.1, 9.4, 1.2, 6.7, 3.8, 7.2, 10.1, 4.5]

# Step 1: Analyze core sensor pattern
analysis_result = analyze_sensor(sensor_readings)

# Distractor: encrypting result (never used)
ciphered = encrypt_payload(analysis_result)

# Step 2: Enrich with metadata (relevant)
labels = ['low', 'mid', 'high', 'critical']
enriched_data = dict(zip(labels, analysis_result))

# Fake calibration sequence (misleading)
calibration_keys = ['gain', 'offset', 'threshold']
calibration_values = [1.02, -0.05, 0.85]
calibration_map = dict(zip(calibration_keys, calibration_values))

# Decoy list comprehension with string manipulation
debug_tags = [f'tag_{l.upper()}_END' for l in labels]
processed_tags = [t.replace('tag_', '').lower() for t in debug_tags]
final_tag = ''.join([p[0] for p in processed_tags])  # 'lmhc'

# Spurious set operation (no impact)
unique_counts = set(analysis_result)
duplicate_check = len(analysis_result) != len(unique_counts)

# Conditional dead branch
if sum(analysis_result) > 20:
    adjusted = [x * 1.1 for x in analysis_result]
else:
    fake_log = [math.log(x + 1) for x in analysis_result]  # Computed but unused

# Core processing function (key)
def process_readings(data_dict):
    total = 0
    multiplier = 1
    for i, (key, value) in enumerate(data_dict.items()):  # enumerate usage
        if i % 2 == 0:
            total += value * multiplier
        else:
            total -= value // (multiplier + 1)
        multiplier += value % 3
    # Complex final adjustment
    adjustment = (data_dict['mid'] + data_dict['high']) * 0.5
    return int(total * 1.5 - adjustment)

# Execution point of interest
final_diagnostic = process_readings(enriched_data)

# Print required output
print(f"Result: {final_diagnostic}")