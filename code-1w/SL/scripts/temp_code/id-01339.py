import itertools

# Simulated sensor grid readings from a distributed environmental monitoring system
def generate_sensor_grid():
    base_values = [127, 255, 83, 194, 62]
    grid = [[v ^ (i * 17) + (j * 3) for j, v in enumerate(base_values)] for i in range(5)]
    return grid

# Irrelevant transformation: color space simulation (distraction)
def rgb_to_grayscale(r, g, b):
    return int(0.299 * r + 0.587 * g + 0.114 * b)

# Misleading data normalization function (dead code path)
def normalize_readings(data_list):
    max_val = max(max(row) for row in data_list)
    return [[val / max_val for val in row] for row in data_list]

# Core processing: filter out noise below significance threshold
def filter_noise(grid, min_threshold=50):
    flattened = list(itertools.chain.from_iterable(grid))
    filtered = [x for x in flattened if abs(x) > min_threshold]
    return filtered

# Bit manipulation based categorization (red herring)
def categorize_by_bits(value):
    ones = bin(value).count('1')
    if ones > 4:
        return 'high_entropy'
    elif ones == 0:
        return 'null'
    else:
        return 'low_entropy'

# Real logic: map thresholds by zone using dictionary lookup
threshold_map = {
    'core_zone': 75,
    'edge_zone': 45,
    'buffer_zone': 30,
    'monitor_zone': 60
}

# Auxiliary diagnostic scoring (decoy computation)
def compute_health_score(values):
    score = 0
    for v in values:
        if v % 2 == 0:
            score += 1
        if v & (v - 1) == 0:  # power of two
            score += 2
    return score * 0.7  # irrelevant final adjustment

# Recursive smoothing function (unused but plausible)
def smooth_sequence(seq, depth=0):
    if depth >= 2 or len(seq) < 2:
        return seq
    smoothed = [(seq[i] + seq[i+1]) // 2 for i in range(len(seq)-1)]
    return smooth_sequence(smoothed, depth + 1)

# Actual processing pipeline step
def analyze_peaks(readings):
    sorted_vals = sorted(readings, reverse=True)
    top_quartile = sorted_vals[:len(sorted_vals)//4]
    return sum(top_quartile) // len(top_quartile) if top_quartile else 0

# Main processing function with key logic
def process_readings(data, config):
    # Step 1: extract relevant region (slicing)
    region_a = data[1:4]
    flat_region = list(itertools.chain.from_iterable(region_a))
    
    # Step 2: apply dynamic filtering based on configuration
    core_limit = config['core_zone']
    monitor_limit = config['monitor_zone']
    primary_filtered = [v for v in flat_region if v > core_limit or v < -monitor_limit]
    
    # Step 3: transform via bitwise correction (XOR mask)
    corrected = [v ^ 0b1101 for v in primary_filtered]  # XOR with 13
    
    # Step 4: aggregate using mean of absolute deviations
    mean_val = sum(corrected) / len(corrected) if corrected else 0
    deviations = [abs(v - mean_val) for v in corrected]
    avg_dev = sum(deviations) / len(deviations) if deviations else 0
    
    # Step 5: final diagnostic computed from deviation statistic
    diagnostic_seed = int(avg_dev * 1.5)
    final_value = (diagnostic_seed ^ 257) + 113  # Final deterministic transformation
    
    return final_value

# --- Execution Sequence ---

# Generate raw sensor data
raw_grid = generate_sensor_grid()

# Apply noise filter (relevant)
filtered_data = filter_noise(raw_grid, min_threshold=40)

# Dead code: simulate visual overlay (irrelevant)
color_layers = [(r % 255, g % 255, 128) for r in raw_grid[0] for g in raw_grid[1]]
grayscale_montage = [rgb_to_grayscale(cl[0], cl[1], cl[2]) for cl in [color_layers[i:i+3] for i in range(0, len(color_layers), 3) if len(color_layers[i:i+3]) == 3]]

# Compute decoy health score (misleading intermediate)
spurious_score = compute_health_score(filtered_data)

# Perform actual analysis
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output target result
print(f"Target result: {final_diagnostic}")