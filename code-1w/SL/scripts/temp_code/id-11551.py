def analyze_growth_pattern(data, threshold=0.75):
    """Irrelevant analysis function (decoy)"""
    return [x for x in data if x > threshold]

# Irrelevant constants (distractors)
CALIBRATION_FACTOR = 0.987
BASELINE_OFFSET = -23.45
MAX_ITERATIONS = 500

# Real input data
sensor_readings = [0.65, 0.72, 0.83, 0.77, 0.69, 0.88, 0.74, 0.81]

# Distractor: unused complex transformation
def transform_signal(signal):
    return [round((x ** 1.5) * CALIBRATION_FACTOR, 3) for x in signal if x > 0.7]

# Terrain codes: 1=flat, 2=slope, 3=ridge, 4=valley
terrain_map = [1, 2, 3, 4, 2, 3, 1, 4]

# Simulated cluster scores from image segmentation
cluster_scores = [45, 67, 89, 52, 73, 91, 64, 77]

# Red herring: fake neural network weights
nn_weights = [0.1, 0.3, 0.5, 0.7, 0.9]

# Unused recursive function (dead code path)
def predict_yield_recursive(depth, acc=0.0):
    if depth <= 0:
        return acc
    return predict_yield_recursive(depth-1, acc + (acc * 0.1))

# Bit manipulation decoy
current_state = 0b110101
mask = 0b111100
filtered_state = current_state & mask  # Result: 52 (misleading intermediate)

# Real calculation function
def calculate_harvest_efficiency(clusters, terrain):
    # Step 1: Normalize cluster scores
    max_score = max(clusters)
    normalized = [c / max_score for c in clusters]
    
    # Step 2: Apply terrain penalty using bitwise check (only ridge and valley affected)
    adjusted = []
    for norm, ter in zip(normalized, terrain):
        penalty = 0.1 if ter & 0b11 in (0b11, 0b10) else 0.0  # ridges(3) and valleys(4) penalized
        adjusted.append(norm - penalty)
    
    # Step 3: Filter valid zones (adjusted > 0.5)
    valid_zones = [val for val in adjusted if val > 0.5]
    
    # Step 4: Count transitions between terrain types
    transitions = 0
    for i in range(len(terrain) - 1):
        if terrain[i] != terrain[i+1]:
            transitions += 1
    
    # Step 5: Compute efficiency score
    base_efficiency = sum(valid_zones)
    penalty_factor = transitions * 0.02
    efficiency = base_efficiency - penalty_factor
    
    # Step 6: Use enumerate to find high-yield indices
    high_yield_indices = []
    for idx, score in enumerate(clusters):
        if score >= 70:
            high_yield_indices.append(idx)
    
    # Step 7: Compute average cluster of high-yield areas
    if high_yield_indices:
        avg_high_cluster = sum(clusters[i] for i in high_yield_indices) / len(high_yield_indices)
    else:
        avg_high_cluster = 0
    
    # Step 8: Final adjustment using set logic (overlap with optimal zones)
    optimal_terrain = {2, 3}  # slope and ridge preferred
    actual_set = set(terrain)
    overlap_count = len(optimal_terrain & actual_set)  # intersection
    enhancement = overlap_count * 0.05
    
    final = efficiency + enhancement - (avg_high_cluster * 0.01)
    
    return round(final, 6)

# Misleading intermediate computation (red herring)
temp_analysis = analyze_growth_pattern(sensor_readings)
transformed = transform_signal(sensor_readings)

# Key statement
final_yield = calculate_harvest_efficiency(cluster_scores, terrain_map)

# Print result
print(f"Target result: {final_yield}")