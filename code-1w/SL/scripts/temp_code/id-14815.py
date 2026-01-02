from collections import defaultdict

# Simulate sensor data processing with noise filtering and scoring
def process_sensor_data(raw_readings):
    filtered = []
    noise_floor = 0.1
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return filtered

# Analyze distribution of significant readings
def analyze_distribution(values):
    dist = defaultdict(int)
    for v in values:
        bucket = int(v * 10)  # Bucket by tenths
        dist[bucket] += 1
    return dist

# Calculate final score based on weighted rarity and magnitude
def calculate_final_score(data, thresholds):
    processed = process_sensor_data(data)
    
    # Irrelevant: Track cumulative sum (not used in final logic)
    cumulative_sum = 0
    temp_vals = []
    for x in processed:
        cumulative_sum += x  # Distractor: computed but unused
        temp_vals.append(x ** 0.5)  # Distractor: irrelevant transformation
    
    distribution = analyze_distribution(processed)
    
    # Key scoring logic
    rare_weight = 0
    total_contribution = 0.0
    
    for bucket, count in distribution.items():
        magnitude_hint = bucket / 10.0
        # Only consider rare occurrences
        if count < thresholds['rarity_threshold']:
            rare_weight += 1
            total_contribution += magnitude_hint * count
    
    # Secondary distractor: unused loop over temp_vals
    smoothed_vals = []
    for tv in temp_vals:
        if tv > 0.5:
            smoothed_vals.append(tv * 0.9)
        else:
            smoothed_vals.append(tv * 1.1)
    
    # Final computation
    base_score = len(processed) * rare_weight
    adjustment = total_contribution if rare_weight > 0 else -5.5
    final_score = int(base_score + adjustment)
    
    # Additional red herring: modify list in place uselessly
    processed.reverse()
    processed.reverse()  # Undo
    
    return final_score

# Main execution
if __name__ == "__main__":
    raw_data = [0.05, -0.3, 0.7, -0.03, 0.15, 0.7, 0.21, -0.08, 0.95]
    config = {"rarity_threshold": 2}
    result = calculate_final_score(raw_data, config)
    print(f"Target result: {result}")