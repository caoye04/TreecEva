from collections import defaultdict, Counter

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_readings):
    cleaned = []
    noise_count = 0
    for val in raw_readings:
        if abs(val) > 100:  # Assume values beyond ±100 are noise
            noise_count += 1
            continue
        if val % 2 == 0:
            cleaned.append(val * 0.95)  # Apply calibration
        else:
            cleaned.append(val * 1.05)
    
    # Distractor: analyze noise pattern (not used later)
    noise_pattern = [abs(raw_readings[i]) > 100 for i in range(len(raw_readings))]
    streaks = 0
    for i in range(len(noise_pattern)-1):
        if noise_pattern[i] and noise_pattern[i+1]:
            streaks += 1
    
    return cleaned

# Analyze frequency of calibrated values
def generate_stats(data):
    freq = Counter(data)
    mode_val = freq.most_common(1)[0][1]
    
    # Distractor computation: entropy approximation (unused)
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # Not real entropy, just looks plausible
    
    threshold = mode_val * 2
    outliers = [k for k, v in freq.items() if v < threshold and k < 0]
    return outliers

# Main scoring logic
def calculate_final_score(data_list):
    running_total = 0
    multiplier = 1
    history = defaultdict(int)
    
    for idx, val in enumerate(data_list):
        history[idx % 3] += 1
        
        if val > 0:
            running_total += int(val)
            if val > 50:
                multiplier *= 1.1
        elif val == 0:
            running_total += 5
        else:
            running_total -= int(abs(val) * 0.5)
    
    # Introduce minor adjustment based on distribution
    pos_vals = [v for v in data_list if v > 0]
    neg_vals = [v for v in data_list if v < 0]
    
    # Distractor: symmetry check (not directly impactful)
    balance_ratio = len(pos_vals) / (len(neg_vals) + 1)
    adjustment = 0
    if 0.8 < balance_ratio < 1.2:
        adjustment = 3
    
    final_value = running_total * multiplier + adjustment
    return int(final_value)

# Entry point
if __name__ == "__main__":
    raw_sensor_data = [105, -44, 22, -3, 77, 102, -55, 8, 12, -19, 99, -200, 41]
    
    # Distractor variables
    expected_range = [-100, 100]
    calibration_offset = sum([x for x in raw_sensor_data if x > 50]) * 0.01
    temp_snapshot = raw_sensor_data[::2]
    
    processed_data = preprocess_sensor_data(raw_sensor_data)
    outlier_flags = generate_stats(processed_data)
    final_score = calculate_final_score(processed_data)
    
    # Print result as required
    print(f"Result: {final_score}")