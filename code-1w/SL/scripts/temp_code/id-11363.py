from itertools import combinations

def analyze_segments(data):
    segments = []
    temp_sum = 0
    for i, val in enumerate(data):
        temp_sum += val
        if (i + 1) % 3 == 0 or i == len(data) - 1:
            segments.append(temp_sum)
            temp_sum = 0
    return segments

def filter_outliers(values):
    mean_val = sum(values) / len(values)
    filtered = [v for v in values if abs(v - mean_val) <= 2 * (sum((x - mean_val)**2 for x in values) / len(values))**0.5]
    return filtered if len(filtered) > 0 else values

def generate_pairs(lst):
    # Irrelevant helper function – distractor
    return list(combinations(lst, 2))
def compute_checksum(arr):
    # Unused computation – red herring
    checksum = 0
    for i, x in enumerate(arr):
        checksum ^= (x + i) * 3
    return checksum

def calculate_final_score(raw):
    transformed = [x * 1.5 - 2 for x in raw]
    processed = []
    offset = 5
    for idx, val in enumerate(transformed):
        if idx % 2 == 0:
            processed.append(val + offset)
        else:
            processed.append(val - offset)
    
    segment_sums = analyze_segments(processed)
    cleaned = filter_outliers(segment_sums)
    
    # Misleading intermediate calculations
    aggregate = 0
    for val in cleaned:
        aggregate += val ** 2
    scale_factor = len(cleaned) if cleaned else 1
    
    # Simulated noise adjustment – not actually impactful due to override below
    noise_adjusted = aggregate / scale_factor
    final_score = int(noise_adjusted // 3)  # Key assignment point
    
    # Dead code path – unreachable but adds cognitive load
    if False:
        backup = sum(processed) * 0.75
        final_score = int(backup)
    
    return final_score

# Main execution flow
sensor_readings = [12, 8, 15, 23, 19, 4, 7, 31, 11]
intermediate_results = []
for reading in sensor_readings:
    if reading > 10:
        intermediate_results.append(reading)

enhanced_data = [x + 2 for x in intermediate_results]  # Minor preprocessing
processed_data = [x - 1 for x in enhanced_data if x % 2 == 1]  # Filter and adjust

# Extraneous set operation – looks important but unused later
unique_set = set(processed_data)
duplicate_check = len(processed_data) - len(unique_set)

# Key computational chain
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")