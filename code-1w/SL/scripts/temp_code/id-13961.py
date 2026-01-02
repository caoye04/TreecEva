from collections import defaultdict, Counter

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_readings):
    filtered_data = []
    noise_count = 0
    temp_buffer = []

    for val in raw_readings:
        if abs(val - 50) > 40:  # Likely noise
            noise_count += 1
            continue
        if val % 2 == 0:
            temp_buffer.append(val)
        else:
            filtered_data.append(val * 2)
    
    # Misleading aggregation (not used later)
    avg_noise = noise_count / len(raw_readings) if raw_readings else 0
    
    # Only odd-based doubled values are kept
    return filtered_data

# Analyze frequency and apply transformation
def transform_data(data_list):
    freq_map = Counter(data_list)
    transformed = []
    total_shift = 0

    for num in data_list:
        count = freq_map[num]
        shift = (num ^ count) % 7  # Bitwise XOR + modular arithmetic
        transformed.append(num + shift)
        total_shift += shift  # Distractor accumulator

    # Apply unnecessary smoothing (unused)
    smoothed = [sum(transformed[i:i+3]) / 3 for i in range(len(transformed) - 2)]
    
    return transformed

# Calculate final diagnostic score
def calculate_final_score(data):
    state_log = defaultdict(int)
    cumulative = 0
    peak = float('-inf')

    for x in data:
        state_log[x] += 1
        if x > peak:
            peak = x
        cumulative += x

    # Core logic: average contribution adjusted by peak
    adjustment = peak // 10
    base_avg = cumulative / len(data) if data else 0
    final_score = int(base_avg + adjustment)

    # Dead code branch - misleading control flow
    if len(state_log) > 100:
        final_score *= 2  # Never reached

    return final_score

# Main execution
if __name__ == '__main__':
    raw_sensor_input = [
        12, 55, 67, 43, 22, 78, 91, 44, 13, 15,
        34, 88, 29, 66, 39, 50, 72, 81, 19, 46
    ]
    
    processed_data = preprocess_sensor_data(raw_sensor_input)
    enhanced_data = transform_data(processed_data)
    final_score = calculate_final_score(enhanced_data)
    
    print(f"Result: {final_score}")