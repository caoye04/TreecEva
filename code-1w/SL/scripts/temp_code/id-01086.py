from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def preprocess_sensor_data(raw_readings):
    filtered = []
    noise_counter = 0
    for val in raw_readings:
        if abs(val - 50) < 20:  # Ignore extreme outliers
            filtered.append(val)
        else:
            noise_counter += 1  # Track but don't use later
    return filtered

# Identify dominant reading patterns
def find_mode(readings):
    count = Counter(readings)
    return count.most_common(1)[0][0]

# Transform data using non-linear scaling based on context
def apply_contextual_gain(readings, base_gain=1.0):
    adjusted = []
    mode_val = find_mode(readings)
    gain_factor = 1.0
    
    for r in readings:
        if r > mode_val:
            gain_factor = base_gain * 1.2
        elif r < mode_val:
            gain_factor = base_gain * 0.85
        else:
            gain_factor = base_gain
        adjusted.append(r * gain_factor + 5)  # Add offset
    
    # Unused transformation path (dead code path - distractor)
    temp_debug = [x * 0.9 for x in adjusted if x > 60]
    
    return adjusted

# Calculate final weighted score with decayed contributions
def calculate_final_score(data, weights):
    score = 0.0
    decay = 0.95
    contribution_log = defaultdict(float)
    
    for i, val in enumerate(data):
        weight = weights[i % len(weights)]
        contribution = val * weight * (decay ** i)  # Exponential decay over position
        contribution_log[f'item_{i}'] += contribution
        score += contribution
    
    # Irrelevant aggregation (distractor)
    avg_contribution = sum(contribution_log.values()) / len(contribution_log) if contribution_log else 0
    anomaly_count = sum(1 for v in data if v < 30)

    # Final nonlinear adjustment
    if score > 100:
        score = score * 0.9 + 10
    else:
        score = score * 1.1

    return int(score)

# Main execution
if __name__ == "__main__":
    raw_sensor_input = [55, 48, 52, 49, 51, 50, 47, 53, 49, 50, 120, -10, 51, 48]
    config_weights = [0.8, 1.1, 0.9, 1.0]
    
    # Step 1: Clean data
    clean_data = preprocess_sensor_data(raw_sensor_input)
    
    # Step 2: Apply transformation (includes internal mode detection)
    enhanced_data = apply_contextual_gain(clean_data, base_gain=1.05)
    
    # Step 3: Compute final score
    final_score = calculate_final_score(enhanced_data, config_weights)
    
    # Debug prints (irrelevant to result)
    debug_summary = {"size": len(enhanced_data), "min": min(enhanced_data), "max": max(enhanced_data)}
    
    print(f"Result: {final_score}")