def analyze_trends(data, window_size):
    trends = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i + window_size]
        avg = sum(segment) / window_size
        trends.append(avg > 50)
    return trends


def calculate_weights(n):
    # Irrelevant helper function for distraction
    weights = [1]
    for i in range(1, n):
        weights.append(weights[-1] * 2 % 7)
    return weights

def filter_outliers(seq, limit=100):
    # Semi-relevant: modifies data but not used in final path
    return [x for x in seq if x <= limit]

def compute_baseline(history):
    total = 0
    count = 0
    for val in history:
        if val >= 0:
            total += val ** 0.5
            count += 1
    return int(total) if count else 0

def evaluate_performance(metrics, threshold):
    adjusted = []
    temp_offset = 0
    
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            temp_offset += val // (i + 1)
        else:
            temp_offset -= val % 5
    
    # Actual core logic
    base = sum(metrics) % 13
    modifier = len([m for m in metrics if m > threshold]) * 2
    
    # Distractor variables
    shadow_metrics = metrics[::-1]
    cumulative = 0
    for v in shadow_metrics:
        cumulative += v * 0.1
        if cumulative > 5:
            break
    
    fallback = compute_baseline(metrics)
    dummy_slice = shadow_metrics[2:5:2]
    
    # Core result computation
    raw_score = base + modifier
    
    # Additional conditional adjustment
    if raw_score > 10 and len(dummy_slice) > 0:
        raw_score -= 3
    elif raw_score < 5:
        raw_score += fallback % 4
    
    final_score = (raw_score * 7) % 100
    return final_score

# Main execution
sensor_readings = [45, 67, 23, 89, 56, 78, 34]
windowed_trends = analyze_trends(sensor_readings, 3)

# Unused transformation
processed_data = filter_outliers(sensor_readings, limit=90)
weights = calculate_weights(7)

baseline_value = compute_baseline(sensor_readings)
score_metrics = sensor_readings[1::2]  # Take every second reading starting from index 1
threshold = 40

final_score = evaluate_performance(score_metrics, threshold)
print(f"Target result: {final_score}")