from collections import defaultdict

# Simulated sensor data processing pipeline
def process_sensor_readings(raw_data):
    filtered_data = [x for x in raw_data if 10 <= x <= 100]
    normalized = [(x - 10) / 90 * 100 for x in filtered_data]
    return sorted(normalized, reverse=True)

# Misleading auxiliary function (not used in final computation)
def calculate_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

# Core evaluation logic
def evaluate_performance(metrics, threshold):
    high_performers = defaultdict(int)
    temp_buffer = []
    
    for i, val in enumerate(metrics):
        if val > threshold:
            high_performers[i % 5] += 1
            temp_buffer.append(val * 0.85)
        else:
            temp_buffer.append(val * 0.1)
    
    # Red herring: complex-looking but unused structure
    snapshot_log = {f"entry_{i}": v for i, v in enumerate(temp_buffer[:10])}
    
    # Actual scoring logic
    base_score = sum(high_performers.values()) * 10
    adjustment = len([v for v in metrics if v > threshold + 20])
    bonus = 5 if adjustment > 2 else 0
    
    # Distractor variables
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    peak_reading = max(metrics) if metrics else 0
    decay_factor = 0.95 ** len(metrics)
    
    final_score = base_score + (adjustment * 7) + bonus
    return final_score

# Initialization data
raw_input_stream = [85, 92, 45, 15, 67, 34, 78, 88, 55, 60, 23, 90, 76, 65, 50]
base_threshold = 60

# Processing steps
processed_metrics = process_sensor_readings(raw_input_stream)
intermediate_stats = [x * 1.1 for x in processed_metrics if x > 50]  # Unused path
metric_data = processed_metrics[::2]  # Every other element

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")