from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def preprocess_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 90]
    stats = defaultdict(int)
    for val in filtered:
        if val > 50:
            stats['high'] += 1
        else:
            stats['low'] += 1

    # Distractor: unused computation
    avg_val = sum(filtered) / len(filtered) if filtered else 0
    outlier_count = sum(1 for x in raw_readings if x < 10 or x > 90)

    return filtered, stats

def analyze_trend(data):
    trend_scores = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_scores.append(1)
        elif data[i] < data[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    
    # Distractor: complex but unused analysis
    runs = 1
    for j in range(1, len(trend_scores)):
        if trend_scores[j] != trend_scores[j-1]:
            runs += 1
    
    pos_runs = sum(1 for k in range(len(trend_scores)) if trend_scores[k] == 1)
    return sum(trend_scores)

def calculate_final_score(clean_data):
    length_factor = len(clean_data) % 10
    base_score = sum(x * 0.1 for x in clean_data)
    
    # Use Counter to compute frequency-based adjustment
    freqs = Counter(clean_data)
    mode_score = freqs.most_common(1)[0][1] * 2 if freqs else 0
    
    # Distractor: irrelevant transformation
    squared_chain = [x**2 for x in clean_data if x % 3 == 0]
    temp_sum = sum(squared_chain[:5]) // len(squared_chain) if squared_chain else 1
    
    # Key logic steps:
    trend_value = analyze_trend(clean_data)
    adjustment = mode_score + abs(trend_value)
    final_score = base_score + adjustment + length_factor
    
    return final_score

# Main execution
raw_sensor_data = [15, 25, 25, 35, 45, 45, 45, 55, 65, 75, 75, 75, 75, 85, 95, 5, 50]
processed_data, summary_stats = preprocess_sensor_readings(raw_sensor_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")