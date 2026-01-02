from collections import defaultdict

# Simulate sensor data with noise and redundancy
def preprocess_data(raw):
    processed = []
    noise_offset = 0.05
    for item in raw:
        temp = item * 0.98 + noise_offset
        if temp > 25.0:
            temp -= 0.15
        processed.append(round(temp, 2))
    return processed

# Filter out unstable readings
def filter_outliers(seq):
    counts = defaultdict(int)
    for val in seq:
        truncated = int(val)
        counts[truncated] += 1
    
    # Identify mode range
    mode_val = max(counts, key=counts.get)
    filtered = [x for x in seq if int(x) in (mode_val-1, mode_val, mode_val+1)]
    
    # Distractor computation: unused statistical moment
    mean = sum(filtered) / len(filtered) if filtered else 0
    variance_proxy = sum((x - mean) ** 2 for x in filtered) / (len(filtered) if filtered else 1)
    skew_attempt = sum((x - mean) ** 3 for x in filtered) / (len(filtered) if filtered else 1)

    return filtered

# Apply weighted aggregation
def calculate_final_score(readings, importance_weights):
    total_weight = sum(importance_weights)
    normalized_weights = [w / total_weight for w in importance_weights]
    
    score = 0.0
    temp_buffer = []
    
    for i, val in enumerate(readings):
        # Extended logic with conditional scaling
        if val < 20:
            scaled = val * 1.1
        elif val < 24:
            scaled = val * 1.05
        else:
            scaled = val * 0.95
            
        # Accumulate using weight cycling (distractor: buffer not fully used)
        weight = normalized_weights[i % len(normalized_weights)]
        contribution = scaled * weight
        temp_buffer.append(contribution * 0.9)  # Partially decayed
        
        score += contribution
    
    # Secondary adjustment based on trend (only uses last few values)
    window = readings[-3:] if len(readings) >= 3 else readings
    if len(window) == 3 and window[0] < window[1] < window[2]:
        score *= 1.03
    
    # Final rounding to simulate precision limit
    return round(score, 2)

# Main execution block
if __name__ == "__main__":
    raw_sensor_data = [26.3, 24.1, 25.8, 26.0, 24.5, 27.1, 25.9, 26.2]
    config_weights = [1, 2, 1, 2]
    
    # Irrelevant intermediate transformation (dead path)
    reversed_data = [x for x in reversed(raw_sensor_data)]
    avg_reversed = sum(reversed_data) / len(reversed_data)
    adjusted_avg = avg_reversed * 0.99
    
    cleaned = preprocess_data(raw_sensor_data)
    validated = filter_outliers(cleaned)
    
    # Key computational step
    final_score = calculate_final_score(validated, config_weights)
    
    # Print result as required
    print(f"Result: {final_score}")