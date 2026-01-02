from collections import defaultdict, Counter

# Simulate sensor data with noise and valid readings
def generate_sensor_data():
    raw_data = [101, 102, 98, 105, 110, 97, 95, 100, 103, 104, 102, 101, 99]
    timestamps = list(range(len(raw_data)))
    return list(zip(timestamps, raw_data))

# Analyze trends in sensor values
def analyze_trend(data):
    increases = 0
    decreases = 0
    for i in range(1, len(data)):
        if data[i][1] > data[i-1][1]:
            increases += 1
        elif data[i][1] < data[i-1][1]:
            decreases += 1
    return increases - decreases

# Calculate moving average to smooth out noise
def moving_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        avg = sum(val for _, val in data[i:i+window]) / window
        smoothed.append(avg)
    return smoothed

# Misleading function - appears useful but not used in final calculation
def compute_variance(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance

# Core scoring logic
def calculate_final_score(sensor_readings):
    # Extract baseline statistics
    values_only = [val for _, val in sensor_readings]
    base_sum = sum(values_only)
    peak_count = sum(1 for v in values_only if v > 100)
    
    # Trend analysis
    trend_bias = analyze_trend(sensor_readings)
    
    # Apply conditional adjustment based on trend direction
    adjustment = 5 if trend_bias > 0 else -3
    
    # Simulate redundant structure: frequency counting (semi-relevant)
    freq_map = Counter(values_only)
    mode_value = freq_map.most_common(1)[0][1]  # Frequency of most common value
    
    # Moving average filtering (only last value used)
    filtered = moving_average(sensor_readings)
    last_filtered = round(filtered[-1], 2) if filtered else 0
    
    # Auxiliary computation that looks important but doesn't impact final score
    outlier_count = 0
    for val in values_only:
        if abs(val - 100) > 10:
            outlier_count += 1
    # ^ This is calculated but unused in final result — distractor

    # State tracking across multiple conditions
    state_flags = defaultdict(int)
    state_flags['high_peak'] = 1 if peak_count > 5 else 0
    state_flags['positive_trend'] = 1 if trend_bias > 0 else 0
    state_flags['stable_mode'] = 1 if mode_value >= 2 else 0

    # Final composition using only subset of computed values
    base_component = base_sum % 97  # Modular arithmetic
    dynamic_component = (trend_bias + adjustment) * state_flags['high_peak']
    final_score = base_component + dynamic_component + int(last_filtered)

    # Irrelevant transformation
    temp_result = [x * 0.9 for x in values_only if x % 2 == 0]
    temp_avg = sum(temp_result) / len(temp_result) if temp_result else 0
    # ^ Not used beyond this point

    return final_score

# Main execution
sensor_data = generate_sensor_data()
final_score = calculate_final_score(sensor_data)
print(f"Result: {final_score}")