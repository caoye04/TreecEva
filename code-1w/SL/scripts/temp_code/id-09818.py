from collections import defaultdict

# Simulate sensor data aggregation and anomaly scoring
def collect_readings():
    raw_data = [102, 95, 110, 98, 100, 103, 97, 101, 105, 99]
    processed = [x - 95 for x in raw_data if x > 90]  # baseline correction
    return processed

def calculate_trend(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return trend

def filter_outliers(data, factor=1.5):
    median_val = sorted(data)[len(data)//2]
    deviation = [abs(x - median_val) for x in data]
    mad = sorted(deviation)[len(deviation)//2]  # median absolute deviation
    threshold = mad * factor
    filtered = [x for x in data if abs(x - median_val) <= threshold]
    return filtered, median_val

def compute_entropy(data):
    from math import log2
    freq = defaultdict(int)
    for x in data:
        freq[x] += 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def process_metrics(sensor_data, config):
    # Step 1: Initial filtering
    clean_data, base_ref = filter_outliers(sensor_data)
    
    # Step 2: Trend analysis
    trend_index = calculate_trend(clean_data)
    
    # Step 3: Entropy calculation
    signal_entropy = compute_entropy(clean_data)
    
    # Irrelevant distraction: buffer simulation
    buffer_size = 8
    padding = [0] * (buffer_size - (len(clean_data) % buffer_size))
    padded_data = clean_data + padding
    data_chunks = [padded_data[i:i+buffer_size] for i in range(0, len(padded_data), buffer_size)]
    chunk_count = len(data_chunks)
    
    # Distraction: unused transformation
    transformed = [round(x ** 0.5, 2) for x in clean_data if x > 0]
    avg_transform = sum(transformed) / len(transformed) if transformed else 0
    
    # Core logic: composite score
    anomaly_weight = config['anomaly_factor']
    trend_weight = config['trend_sensitivity']
    entropy_boost = 1 + (signal_entropy * 0.1)
    
    # Misleading intermediate: not directly used
    temp_score = (abs(trend_index) * 3.1) + (base_ref * 0.2)
    adjustment = (chunk_count * 0.5) - (len(padding) * 0.1)
    
    # Final computation
    final_score = (
        (anomaly_weight * len([x for x in sensor_data if x > config['upper_limit']])) +
        (trend_weight * abs(trend_index)) +
        (signal_entropy * 10)
    ) * entropy_boost
    
    # Additional red herring: sorting unrelated list
    dummy_list = [5, 2, 9, 1, 7]
    dummy_list.sort(reverse=True)
    squared_sum = sum([x**2 for x in dummy_list])
    
    return int(round(final_score))

# Main execution
readings = collect_readings()
data = readings.copy()

thresholds = {
    'upper_limit': 104,
    'anomaly_factor': 7,
    'trend_sensitivity': 4
}

interim_result = calculate_trend(data)
baseline_median = sorted(data)[len(data)//2]
dummy_flag = False

for val in data:
    if val < 90:
        dummy_flag = True

# Key statement
final_score = process_metrics(data, thresholds)
print(f"Result: {final_score}")