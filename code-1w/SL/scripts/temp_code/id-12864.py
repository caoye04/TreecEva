def transform_signal(raw_values, factor):
    """Apply non-essential transformation to distract from core logic."""
    return [x * factor + 5 for x in raw_values if x > 0]


def validate_checksum(data):
    """Decoy validation function that is called but not relevant."""
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= val * (i + 1)
    return checksum % 17 == 0


def recursive_filter(items, limit):
    """Recursively trim list until sum is below limit."""
    if sum(items) <= limit:
        return items
    mid = len(items) // 2
    left = recursive_filter(items[:mid], limit)
    right = recursive_filter(items[mid:], limit)
    combined = left + right
    return combined if sum(combined) <= limit else left


def extract_features(dataset):
    """Extracts features using zip and enumerate; some results are irrelevant."""
    indices = [i for i, x in enumerate(dataset) if x % 4 == 0]
    paired = list(zip(dataset, [x*2 for x in dataset]))
    feature_sum = 0
    for i, (orig, doubled) in enumerate(paired):
        if i % 3 == 0:
            feature_sum += orig ^ doubled  # Bitwise distraction
    return feature_sum


def analyze_readings(data, config):
    """Core analysis function that computes final result."""
    temp = 0
    for i, val in enumerate(data):
        key = f'level_{min(i % 4, 2)}'
        bound = config[key]
        if val > bound:
            temp += val >> 1
        elif val < -bound:
            temp -= val & 7
        else:
            temp += val
    return temp + len(data)

# Irrelevant constants and decoy data structures
DECOY_MATRIX = [[i*j for j in range(5)] for i in range(5)]
TEMP_LOG = {f'entry_{i}': i**2 for i in range(10)}

# Simulated sensor readings (core input)
raw_sensor_data = [12, -5, 8, 20, -15, 3, 9, 11, -2, 7]

# Misleading pre-processing step (not used in final path)
cleaned = [x for x in raw_sensor_data if x != 0]
decoy_signal = transform_signal(raw_sensor_data, 1.5)

# Real processing begins here
filtered_data = recursive_filter(raw_sensor_data, 50)
feature_score = extract_features(filtered_data)

# Secondary distraction: unused dictionary operations
diagnostic_map = {f'code_{i}': extract_features([i+1]) for i in range(3)}

# Core configuration for analysis
threshold_map = {
    'level_0': 6,
    'level_1': 10,
    'level_2': 8
}

# Processed data that feeds into final calculation
processed_data = [x + (i % 3) for i, x in enumerate(filtered_data)]

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output the required result
print(f"Result: {final_diagnostic}")