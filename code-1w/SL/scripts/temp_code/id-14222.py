from collections import defaultdict
from itertools import combinations

# Simulate sensor data with noise and valid readings
def preprocess_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if 0 <= x <= 100]
    baseline = sum(filtered) // len(filtered) if filtered else 0
    
    # Irrelevant transformation (distractor)
    squared_devs = [(x - baseline)**2 for x in filtered]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    
    # Normalize around baseline
    normalized = [x - baseline for x in filtered]
    return normalized, baseline

# Identify correlated fluctuations in sensor pairs
def detect_correlations(normalized_readings, window_size=3):
    correlation_count = 0
    temp_sums = []
    
    for i in range(len(normalized_readings) - window_size + 1):
        window = normalized_readings[i:i+window_size]
        avg_window = sum(window) / window_size
        temp_sums.append(avg_window)  # Distractor: collected but not used later
        
        if len(set(1 if x > 0 else 0 for x in window)) == 1:
            # All positive or all negative deviations
            correlation_count += 1
    
    # Extra computation that doesn't affect final result
    smoothed = [temp_sums[i] + temp_sums[i+1] for i in range(len(temp_sums)-1)] if len(temp_sums) > 1 else []
    return correlation_count

# Calculate final diagnostic score
def calculate_final_score(data_dict):
    total_weight = 0
    score = 0
    
    for key, values in data_dict.items():
        if len(values) == 0:
            continue
        mode_val = max(set(values), key=values.count) if values else 0
        unique_pairs = list(combinations(set(values), 2))
        pair_count = len(unique_pairs)
        
        # Weight based on diversity of readings
        diversity_bonus = 1 if pair_count > 5 else 0.5
        
        # Actual scoring logic
        base = sum(values) // len(values)
        contribution = base * diversity_bonus
        score += contribution
        total_weight += diversity_bonus
    
    return int(score // total_weight) if total_weight else 0

# Main execution
raw_sensor_data = [85, 90, 87, 88, 200, -5, 92, 85, 87, 0, 105, 88, 90]

# Step 1: Preprocess to filter and normalize
cleaned_readings, base_ref = preprocess_sensor_readings(raw_sensor_data)

# Step 2: Detect correlation patterns (used to modify processing logic)
corr_index = detect_correlations(cleaned_readings)

# Step 3: Prepare structured dataset for final scoring
processed_data = defaultdict(list)
for i, val in enumerate(cleaned_readings):
    bucket = 'high' if val >= base_ref else 'low'
    processed_data[bucket].append(abs(val) % 17)  # Transform into modular space

# Add artificial entry with no impact (dead code path distractor)
if len(processed_data['high']) < 5:
    processed_data['aux'].extend([1, 1, 1])  # Never contributes due to logic below

# Key statement: compute final score
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")