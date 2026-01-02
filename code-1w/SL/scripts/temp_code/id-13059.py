from collections import defaultdict, Counter

def preprocess_signals(raw_readings):
    processed = []
    temp_buffer = []
    for idx, val in enumerate(raw_readings):
        if idx % 2 == 0:
            temp_buffer.append(val * 1.5)
        else:
            temp_buffer.append(val + 2)
    
    # Misleading normalization (not actually used in final result)
    normalized = [x / max(temp_buffer) * 100 for x in temp_buffer]
    
    # Actual processing path
    for i in range(len(temp_buffer)):
        if temp_buffer[i] > 50:
            processed.append(int(temp_buffer[i]) & 255)  # Bitwise clamp
        else:
            processed.append(int(temp_buffer[i]) | 10)
    return processed

def analyze_trends(data_stream):
    trend_counter = defaultdict(int)
    changes = []
    for i in range(1, len(data_stream)):
        diff = data_stream[i] - data_stream[i-1]
        changes.append(diff)
        if diff > 0:
            trend_counter['up'] += 1
        elif diff < 0:
            trend_counter['down'] += 1
    
    # Dead code - never accessed later
    stats_summary = dict(trend_counter)
    avg_change = sum(changes) / len(changes) if changes else 0
    
    # Distractor: complex but unused structure
    detailed_log = {f'step_{i}': {'delta': changes[i], 'cumulative': sum(changes[:i+1])} 
                   for i in range(len(changes))}
    
    return trend_counter['up'] - trend_counter['down']

def calculate_final_score(dataset):
    score = 0
    freq_map = Counter(dataset)
    
    # Key scoring logic
    for val, count in freq_map.items():
        if count >= 2:
            score += val * count
        else:
            score -= val % 7
    
    # Irrelevant transformations
    squared_values = [x**2 for x in dataset if x > 0]
    filtered_squares = list(filter(lambda x: x < 1000, squared_values))
    average_square = sum(filtered_squares) / len(filtered_squares) if filtered_squares else 0
    
    # Another distractor loop
    cumulative_xor = 0
    for v in dataset:
        cumulative_xor ^= int(v * 1.1)
    
    return score + len(dataset)

# Main execution flow
raw_sensor_data = [34, 45, 22, 67, 45, 22, 89, 12, 34, 45]
processed_data = preprocess_signals(raw_sensor_data)
trend_metric = analyze_trends(processed_data)
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")