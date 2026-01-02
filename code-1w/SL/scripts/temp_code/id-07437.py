def preprocess_signal(raw):    
    # Irrelevant signal smoothing (dead-end computation)
    smoothed = [raw[i] + (raw[i-1] + raw[i+1]) / 2 for i in range(1, len(raw)-1)]
    normalized = [x / max(raw) for x in raw]
    return normalized

# Sensor simulation parameters (distractors)
baseline_offset = 0.17
sampling_rate = 100  
filter_window = 5

# Core data input
raw_sensor_data = [84, 23, 56, 91, 12, 67, 38, 45, 72, 29]

# Outlier detection (misleading path)
def detect_outliers(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean)**2 for x in data) / len(data))**0.5
    return [i for i, x in enumerate(data) if abs(x - mean) > 2 * std_dev]

outliers = detect_outliers(raw_sensor_data)

# Primary processing pipeline
processed_data = []
for val in raw_sensor_data:
    temp = (val * 3 + 17) % 101
    if temp % 2 == 0:
        processed_data.append(temp // 7)
    else:
        processed_data.append(temp // 5)

# Checksum decoy (irrelevant validation)
data_checksum = sum(processed_data[i] * (i + 1) for i in range(len(processed_data))) % 97

# Threshold logic with slicing distraction
effective_slice = processed_data[2:7:2]  # Uses slicing but result not critical
temp_adjustment = sum(effective_slice) / len(effective_slice)

threshold = 8.5

# Real analysis function (depends only on processed_data and threshold)
def analyze_readings(readings, limit):
    count_above = 0
    running_total = 0.0
    for i, r in enumerate(readings):
        if i % 3 == 0:
            running_total += r * 1.1
        elif r > limit:
            count_above += 1
            running_total += r * 0.9
        else:
            running_total -= 1.5
    # Final computation: modular arithmetic and conditional weighting
    adjustment = (count_above * 100) % 73
    return int(running_total) + adjustment

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")