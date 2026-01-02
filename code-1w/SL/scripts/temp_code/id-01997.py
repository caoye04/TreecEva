def analyze_temperatures(raw_readings):
    adjusted_readings = [temp + 273.15 for temp in raw_readings if temp > -50]
    valid_range = [t for t in adjusted_readings if 200 <= t <= 350]
    average_temp = sum(valid_range) / len(valid_range) if valid_range else 0
    
    # Distractor: entropy calculation (not used)
    import math
    entropy = sum(math.log(t) for t in valid_range if t > 0) if valid_range else 0
    normalized_entropy = entropy / len(valid_range) if valid_range else 0

    # Irrelevant transformation
    scaled_values = [round(t * 1.05, 2) for t in valid_range]
    outlier_count = sum(1 for v in scaled_values if v > 320)

    return average_temp, len(valid_range), outlier_count


def preprocess_sensor_data(input_stream):
    # Simulate data cleaning
    cleaned = [float(x.strip()) for x in input_stream.split(',')]
    filtered = [c for c in cleaned if -100 <= c <= 100]
    
    # Extra processing that doesn't affect main result
    stats = {
        'positive': len([f for f in filtered if f > 0]),
        'negative': len([f for f in filtered if f < 0]),
        'zero': len([f for f in filtered if f == 0])
    }
    
    sorted_vals = sorted(filtered, reverse=True)
    top_quartile = sorted_vals[:len(sorted_vals)//4] if sorted_vals else []
    
    # Dead code path (only triggers on impossible condition)
    if len(filtered) > 1000:
        compressed = ','.join(map(str, top_quartile))
    else:
        compressed = None
    
    return filtered


def calculate_final_score(data_chunk):
    base_avg = sum(data_chunk) / len(data_chunk) if data_chunk else 0
    variance = sum((x - base_avg) ** 2 for x in data_chunk) / len(data_chunk) if data_chunk else 0
    std_dev = variance ** 0.5
    
    # Scoring logic
    score_components = [
        base_avg * 0.6,
        (10 - min(std_dev, 10)) * 0.4,  # Lower variation → higher score
        len([x for x in data_chunk if x >= base_avg]) * 0.1
    ]
    raw_score = sum(score_components)
    
    # Apply non-linear boost
    final_score = raw_score * (1 + 0.05 * (len(data_chunk) // 10))
    return round(final_score, 4)

# Main execution flow
sensor_input = "-5,23,-55,30,18,45,-2,33,100,101,-200,15,27"
data_pool = preprocess_sensor_data(sensor_input)
temperature_log = [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]

# Perform analysis (distractor call)
mean_temp, count_valid, anomalies = analyze_temperatures(temperature_log)

# Core data for scoring
processed_data = [x for x in data_pool if x != 100]  # Remove sensor calibration value

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")