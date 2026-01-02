import math

def analyze_signal_strength(signal):
    # Irrelevant function - dead code path
    return sum([x ** 0.5 for x in signal if x > 10])

def decode_frequency_pattern(seq):
    # Decoy function with misleading intermediate logic
    temp_result = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            temp_result += val * 1.5
        else:
            temp_result -= val / 2
    return temp_result

def validate_checksum(data):
    # Unused validation routine (distractor)
    checksum = 0
    for d in data:
        checksum ^= int(d * 3) & 0xFF
    return checksum == 0x7A

def extract_features(raw):
    # Another irrelevant transformation
    return [math.log(abs(x) + 1) for x in raw]

def filter_outliers(values, threshold=2.5):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

def map_to_grid(coordinates):
    # Red herring operation on unused coordinate system
    grid = {}
    for idx, (x, y) in enumerate(coordinates):
        key = f'{int(x)}:{int(y)}'
        grid[key] = idx
    return grid

def process_readings(data):
    # Core relevant logic begins here
    normalized = [x * 0.1 for x in data]  # Scale down sensor inputs

    # Apply filtering to remove noise (relevant step)
    filtered = filter_outliers(normalized, threshold=2.0)

    # Transform using piecewise function
    transformed = []
    for v in filtered:
        if v < 0.5:
            transformed.append(math.sin(v * math.pi))
        elif v < 1.0:
            transformed.append(0.5)
        else:
            transformed.append(math.cos(v * math.pi / 2))

    # Use enumerate and zip (required Python features)
    indexed = list(enumerate(transformed))
    pairs = list(zip(transformed[:-1], transformed[1:]))

    # Compute correlation-like metric across adjacent readings
    coherence_score = 0.0
    for i, (a, b) in enumerate(pairs):
        coherence_score += (a * b) / (i + 1)  # Weighted accumulation

    # Final non-linear transformation
    adjustment_factor = len(filtered) / len(data)  # Data retention ratio
    final_diagnostic = int((coherence_score * 1000) * adjustment_factor)

    # This print is required for traceability
    print(f'Result: {final_diagnostic}')
    return final_diagnostic

# Simulated sensor input (deterministic)
sensor_data = [12, 45, 8, 67, 34, 23, 56, 78, 33, 29, 31, 76, 88, 44, 30]

# Unused variables - red herrings
dummy_coords = [(1.2, 3.4), (2.5, 6.7), (3.8, 5.1), (4.0, 8.2)]
feature_set = extract_features(sensor_data)
signal_analysis = analyze_signal_strength(sensor_data)
frequency_map = decode_frequency_pattern(sensor_data)
grid_layout = map_to_grid(dummy_coords)

# Key execution point
final_diagnostic = process_readings(sensor_data)