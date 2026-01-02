from collections import defaultdict, Counter

# Simulate sensor data with some noise and redundancy
def get_sensor_readings():
    raw_data = [10, 15, 10, 20, 25, 15, 30, 20, 10, 25]
    noise_offset = [i % 3 for i in range(len(raw_data))]
    return [raw_data[i] + noise_offset[i] for i in range(len(raw_data))]

# Filter out redundant consecutive values
def remove_consecutive_duplicates(data):
    if not data:
        return []
    result = [data[0]]
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            result.append(data[i])
    return result

# Analyze frequency of readings
def analyze_frequency(cleaned):
    freq = Counter(cleaned)
    # Misleading computation: unused in final path
    rare_values = [k for k, v in freq.items() if v < 2]
    common_values = [k for k, v in freq.items() if v >= 2]
    temp_sum = sum(rare_values) * 0.5  # red herring
    return common_values

# Transform data into weighted bins
def bin_data(values):
    binned = defaultdict(int)
    for v in values:
        if v < 15:
            binned['low'] += v
        elif v < 25:
            binned['medium'] += v * 1.1
        else:
            binned['high'] += v * 1.2
    # Extra unnecessary transformation
    normalized = {k: round(v / 1.1, 2) for k, v in binned.items()}
    return binned  # actual return used

# Core scoring logic
def calculate_risk_factor(bins):
    base_risk = 0
    if 'high' in bins and bins['high'] > 30:
        base_risk += 15
    if 'medium' in bins:
        base_risk += 5
    return base_risk

# Final score calculation incorporating multiple factors
def calculate_final_score(data_map):
    risk = calculate_risk_factor(data_map)
    raw_total = sum(data_map.values())
    adjustment = 0
    
    # Complex but partially irrelevant logic
    if 'low' in data_map and data_map['low'] > 10:
        adjustment += 3
    elif 'low' not in data_map:
        adjustment -= 2

    # Key computation path
    score = raw_total - risk + adjustment
    
    # Dead code branch (never reached due to structure)
    for key in data_map:
        if key == 'ultra':
            score *= 0.9
            break
    
    return int(score)

# Main execution flow
if __name__ == '__main__':
    readings = get_sensor_readings()
    processed_data = remove_consecutive_duplicates(readings)
    frequent_values = analyze_frequency(processed_data)
    binned_data = bin_data(frequent_values)
    final_score = calculate_final_score(binned_data)
    print(f"Result: {final_score}")