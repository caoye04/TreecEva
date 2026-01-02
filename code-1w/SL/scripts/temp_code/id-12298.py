def analyze_signal(samples, threshold=0.75):
    # Irrelevant preprocessing block (dead path)
    if len(samples) == 0:
        return -999

    normalized = [x / max(samples) for x in samples]
    filtered = [x for x in normalized if x > threshold]
    
    # Decoy computation with misleading intermediate
    entropy_proxy = 0
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            entropy_proxy += val * 0.33
        else:
            entropy_proxy -= val * 0.17

    # Real signal: count of values above threshold after normalization
    return len(filtered)


def transform_coordinates(coord_list):
    # Unused transformation function (red herring)
    polar = []
    for x, y in coord_list:
        r = (x**2 + y**2)**0.5
        theta = (y / r)
        polar.append((r, theta))
    return polar


def validate_integrity(check_sequence):
    # Checksum decoy with bit manipulation distractions
    checksum = 0
    for idx, val in enumerate(check_sequence):
        checksum ^= (val + idx) << 1
        checksum &= 0xFFFF
    
    # Actual logic: returns whether sequence has even length
    return len(check_sequence) % 2 == 0


def recursive_partition(data, limit):
    # Simple recursion disguised as complex
    if limit <= 0 or len(data) < 2:
        return [sum(data)]
    mid = len(data) // 2
    left = recursive_partition(data[:mid], limit - 1)
    right = recursive_partition(data[mid:], limit - 1)
    return left + right

# Main diagnostic workflow
sensor_readings = [120, 145, 160, 180, 200, 220, 240, 260]
scaled_readings = [x * 0.01 for x in sensor_readings]  # Pre-scale for later use

# Generate irrelevant alternate views
reversed_pairs = list(zip(scaled_readings, scaled_readings[::-1]))
duplicate_check = {x for x in scaled_readings}

# Real processing begins: identify peaks
peak_indices = []
for i in range(1, len(scaled_readings) - 1):
    if scaled_readings[i] > scaled_readings[i-1] and scaled_readings[i] > scaled_readings[i+1]:
        peak_indices.append(i)

# Apply analysis using prior function
analysis_result = analyze_signal(sensor_readings, threshold=0.8)

# Construct multi-stage processing chain (distractor-heavy)
processing_chain = {
    'stage_1': {'data': sensor_readings[:4], 'active': True},
    'stage_2': {'data': sensor_readings[4:], 'active': True},
    'stage_3': {'data': [], 'active': False}  # Dead stage
}

# Simulate validation key through string operations
config_token = 'DXZ9K2LMN'
validation_key = 0
for char in config_token:
    if char.isdigit():
        validation_key += int(char)
    elif char in 'LMN':
        validation_key *= 2

# Update chain dynamically (misleading complexity)
for stage_id, stage in processing_chain.items():
    if stage['active']:
        partitioned = recursive_partition(stage['data'], limit=2)
        stage['partitions'] = partitioned
        stage['count'] = len(partitioned)

# Hidden relevant logic: combine peak indices with analysis result
auxiliary_score = 0
for idx in peak_indices:
    auxiliary_score += sensor_readings[idx] // 10

# Critical computation hidden among distractors
temp_offset = sum(x for x in sensor_readings if x > 200) // 100
key_metric = analysis_result + len(peak_indices) + temp_offset

# Final aggregation with dictionary traversal
final_diagnostic = 0
metric_weights = {'analysis': 3, 'peaks': 2, 'offset': 1}

for label, block in processing_chain.items():
    if block['active']:
        final_diagnostic += block['count']

# Overwrite with actual formula (this is the real assignment)
final_diagnostic = key_metric  # Override previous accumulation

# Additional noise: unused tuple unpacking
_, _, *remaining = reversed_pairs

# Print final result as required
print(f"Result: {final_diagnostic}")