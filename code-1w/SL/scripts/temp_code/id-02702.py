from collections import defaultdict

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_readings):
    cleaned = []
    noise_count = 0
    for val in raw_readings:
        if abs(val - 50) > 40:  # Filter extreme outliers
            noise_count += 1
            continue
        if val % 2 == 0:
            cleaned.append(val + 3)
        else:
            cleaned.append(val - 2)
    return cleaned, noise_count

def analyze_trends(data):
    trend_stats = defaultdict(int)
    increasing = decreasing = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increasing += 1
            trend_stats['up'] += 1
        elif data[i] < data[i-1]:
            decreasing += 1
            trend_stats['down'] += 1
        else:
            trend_stats['flat'] += 1
    return trend_stats, increasing - decreasing

def calculate_composite_weight(base, adjustment):
    # Irrelevant weighting function (not used in final logic)
    weight_map = {'low': 0.8, 'mid': 1.0, 'high': 1.3}
    level = 'mid'
    if adjustment > 10:
        level = 'high'
    elif adjustment < -5:
        level = 'low'
    return base * weight_map[level]

def calculate_final_score(data):
    total = 0
    peak_moment = None
    temp_offset = 0
    
    # Real computation path
    for idx, value in enumerate(data):
        if value > 45 and value < 75:
            total += value // 3
        if value > 60 and peak_moment is None:
            peak_moment = idx  # First high-value moment
    
    # Distractor block: semi-relevant but unused
    summary_stats = {}
    summary_stats['avg'] = sum(data) / len(data) if data else 0
    summary_stats['max'] = max(data) if data else 0
    summary_stats['min'] = min(data) if data else 0
    temp_offset = abs(summary_stats['max'] - summary_stats['min']) // 4
    
    # Final score adjustment based on actual logic
    if peak_moment and peak_moment < 10:
        total += 15
    total -= temp_offset  # Minor effect but not decisive
    
    # Red herring variable
    final_multiplier = 1.0
    if total > 100:
        final_multiplier = 0.9
    
    return int(total * final_multiplier)

# Main execution
raw_sensor_data = [105, 48, 52, 44, 61, 66, 39, 70, 22, 58, 85, 54, 41, 63]
processed_data, dropped = preprocess_sensor_data(raw_sensor_data)
trends, net_trend = analyze_trends(processed_data)
baseline_diagnostic = {k: v for k, v in trends.items() if v > 1}

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")