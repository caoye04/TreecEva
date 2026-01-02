import math

# Sensor calibration data (irrelevant for final result)
calibration_offsets = [0.12, -0.05, 0.34, 0.01, -0.21]
baseline_noise = sum([abs(x) for x in calibration_offsets])
adjusted_offsets = [round(x * 1.05, 3) for x in calibration_offsets]  # unused

# Simulated sensor readings from environmental monitoring system
raw_readings = [
    [14, 8, 23, 17, 42],
    [9, 16, 31, 11, 67],
    [25, 12, 19, 33, 58],
    [18, 29, 14, 21, 44],
    [11, 22, 35, 13, 71]
]

# Irrelevant statistical moment calculations
def skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0.0
    stddev = variance ** 0.5
    return sum(((x - mean) / stddev) ** 3 for x in data) / n

row_skew = [skewness(row) for row in raw_readings]  # computed but not used

# Real processing begins here
processed_data = []
for i, row in enumerate(raw_readings):
    filtered = [x for x in row if x % 2 == 1]  # keep only odd values
    shifted = [(x >> 1) for x in filtered]     # right bit shift by 1
    processed_data.append(shifted)

# Decoy transformation chain
shadow_copy = [row[:] for row in raw_readings]
for r in range(len(shadow_copy)):
    for c in range(len(shadow_copy[r])):
        shadow_copy[r][c] = (shadow_copy[r][c] ^ 7) + 3  # irrelevant obfuscation

# Threshold configuration map (used later)
threshold_map = {
    0: {'min': 5, 'penalty': 2},
    1: {'min': 4, 'penalty': 3},
    2: {'min': 6, 'penalty': 1},
    3: {'min': 3, 'penalty': 4},
    4: {'min': 7, 'penalty': 2}
}

# Auxiliary function that appears important but is never called
def compute_entropy(data_2d):
    freq = {}
    total = 0
    for row in data_2d:
        for val in row:
            freq[val] = freq.get(val, 0) + 1
            total += 1
    return -sum((count/total) * math.log2(count/total) for count in freq.values())

# Another red herring: complex list flattening and re-grouping
flat_raw = [item for sublist in raw_readings for item in sublist]
sorted_raw_desc = sorted(flat_raw, reverse=True)
top_quartile = sorted_raw_desc[:len(sorted_raw_desc)//4]
aggregated_stats = {
    'avg_top': sum(top_quartile) / len(top_quartile),
    'range': max(top_quartile) - min(top_quartile)
}  # never used

# Core analysis logic
mask_pattern = [1, 0, 1, 0, 1]
def apply_mask_and_sum(matrix, mask):
    return sum(
        matrix[i][j] for i in range(len(matrix))
        for j in range(len(matrix[i])) if mask[j] == 1
    )

masked_total = apply_mask_and_sum(raw_readings, mask_pattern)  # distraction

# Actual diagnostic analyzer
def analyze_readings(data, thresholds):
    score = 0
    for idx, segment in enumerate(data):
        # Use slicing to take at most first 3 elements
        relevant = segment[:3]
        
        # Count how many meet threshold minimum
        min_required = thresholds[idx]['min']
        penalty_factor = thresholds[idx]['penalty']
        
        valid_count = sum(1 for x in relevant if x >= min_required)
        
        # Apply conditional scoring
        if valid_count >= 2:
            contribution = valid_count * 7
        else:
            contribution = -penalty_factor * 2
        
        score += contribution
    
    # Final adjustment based on set property
    all_values = {val for row in data for val in row}
    if len(all_values) > 10:
        score += 5
    
    return score

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")