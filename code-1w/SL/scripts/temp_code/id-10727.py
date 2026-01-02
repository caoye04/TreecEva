from collections import defaultdict
from itertools import combinations

# Simulate sensor data with noise and valid readings
def generate_sensor_data():
    raw_data = [15, 18, 22, 25, 30, 35, 40]
    noise = [-2, 0, 1, 3]
    return [x + noise[i % len(noise)] for i, x in enumerate(raw_data)]

# Filter out unstable readings below threshold
def filter_stable_readings(data, threshold=20):
    return [x for x in data if x >= threshold]

# Compute pairwise correlations as a distraction
def compute_pairwise_correlations(data):
    corr_pairs = []
    for a, b in combinations(data, 2):
        corr_pairs.append((a - b) ** 2)  # Not actually correlation, just distractor
    return sum(corr_pairs)

# Calculate weighted score using filtered data
def calculate_weighted_average(filtered):
    weights = [1, 1.5, 2, 2.5, 3]  # Assume increasing reliability
    weighted_sum = sum(val * weights[i % len(weights)] for i, val in enumerate(filtered))
    return weighted_sum / len(filtered)

# Misleading function that computes unused statistics
def analyze_distribution(data):
    count_map = defaultdict(int)
    for x in data:
        count_map[x // 5] += 1
    excess_computation = 0
    for k, v in count_map.items():
        excess_computation += k * v ** 2
    return excess_computation  # Never used

# Main scoring logic
def calculate_final_score(raw_data):
    temp_data = raw_data.copy()
    
    # Step 1: Add offset to simulate calibration
    calibrated = [x + 1 for x in temp_data]
    
    # Step 2: Filter stable readings (only those >= 20)
    stable_readings = filter_stable_readings(calibrated)
    
    # Step 3: Compute distractor metrics (not used in final score)
    _ = compute_pairwise_correlations(stable_readings)
    _ = analyze_distribution(stable_readings)
    
    # Step 4: Calculate base average
    base_avg = sum(stable_readings) / len(stable_readings)
    
    # Step 5: Apply weighting scheme
    weighted_avg = calculate_weighted_average(stable_readings)
    
    # Step 6: Final adjustment based on length of stable data
    length_factor = len(stable_readings) * 0.5
    final_score = weighted_avg + length_factor - base_avg  # Net zero effect from base_avg?
    
    return round(final_score, 4)

# Execute
sensor_input = generate_sensor_data()
final_score = calculate_final_score(sensor_input)
print(f"Target result: {final_score}")