from itertools import combinations

def analyze_sensor_readings(readings):
    # Preprocess: extract valid readings above threshold
    threshold = 25
    filtered = [r for r in readings if r > threshold]
    
    # Distractor: statistical noise calculation (not used later)
    avg = sum(filtered) / len(filtered) if filtered else 0
    variance = sum((x - avg) ** 2 for x in filtered) / len(filtered) if filtered else 0
    std_deviation = variance ** 0.5

    # Real computation: count how many pairs exceed interaction threshold
    interaction_limit = 60
    significant_pairs = 0
    for pair in combinations(filtered, 2):
        if sum(pair) > interaction_limit:
            significant_pairs += 1

    return significant_pairs


def transform_coordinates(coords_list):
    # Coordinate transformation with distractor logic
    transformed = []
    temp_squares = []  # dead storage
    for i, (x, y) in enumerate(coords_list):
        radius = (x**2 + y**2) ** 0.5
        angle = (x + y) * i  # irrelevant
        transformed.append({'index': i, 'radius': radius})
        temp_squares.append(angle ** 2)  # computed but unused

    # Unused helper structure
    metadata_map = {i: {'processed': True} for i in range(len(transformed))}

    return [t['radius'] for t in transformed]


def calculate_optimal_yield(data):
    base_score = 0
    adjustment_factor = 0.85

    # Key data processing
    for entry in data:
        if 'sensor' in entry:
            raw_values = entry['sensor']
            high_activity = analyze_sensor_readings(raw_values)
            base_score += high_activity * 2
        
        if 'coords' in entry:
            radii = transform_coordinates(entry['coords'])
            valid_radii = [r for r in radii if r > 10]
            base_score += len(valid_radii)

    # Final nonlinear scaling
    yield_value = (base_score ** 1.5) * adjustment_factor
    final_yield = int(yield_value)  # this will be the answer

    return final_yield

# Simulated multi-source input data
source_data = [
    {
        'sensor': [10, 30, 40, 50, 20],
        'coords': [(3, 4), (10, 10), (-5, 12)]
    },
    {
        'sensor': [26, 27, 24, 30],
        'coords': [(0, 0), (8, 15), (7, 24)]
    },
    {
        'sensor': [35, 35],
        'coords': [(1, 1), (5, 12)]
    }
]

# Intermediate distractor variables
checksum = sum(len(item.get('sensor', [])) for item in source_data)
dummy_lookup = {i: chr(65 + i) for i in range(10)}

# Data preprocessing step with zip and enumerate (relevant)
processed_data = []
for idx, item in enumerate(source_data):
    entry = {}
    if 'sensor' in item:
        # Normalize sensor data slightly
        offset = idx * 0.5
        entry['sensor'] = [val + offset for val in item['sensor']]
    if 'coords' in item:
        # Reorganize using zip
        xs, ys = zip(*item['coords'])
        entry['coords'] = list(zip(xs, [y + 1 for y in ys]))  # slight shift
    processed_data.append(entry)

# Core computation point
final_yield = calculate_optimal_yield(processed_data)

# Output result as required
print(f"Target result: {final_yield}")