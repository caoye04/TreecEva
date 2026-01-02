from collections import defaultdict, Counter
from itertools import combinations

# Simulate sensor readings with noise and validity flags
def generate_sensor_data():
    raw_readings = [105, 98, 110, 102, None, 108, 95, 113, None, 107]
    timestamps = list(range(10))
    valid_flags = [True, True, False, True, False, True, True, False, False, True]
    return list(zip(raw_readings, timestamps, valid_flags))

# Filter valid data and apply calibration offset
def preprocess_data(sensor_data):
    calibrated_readings = []
    temp_store = []
    for reading, ts, valid in sensor_data:
        if reading is not None and valid:
            adjusted = reading - 10  # Calibration
            calibrated_readings.append(adjusted)
            temp_store.append(ts)  # Irrelevant: timestamp not used later
    return calibrated_readings

# Analyze trends using simple thresholds and bit flags
def detect_trends(readings):
    trend_flags = 0
    increasing_count = 0
    decreasing_count = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            increasing_count += 1
            trend_flags |= (1 << i % 8)
        elif readings[i] < readings[i-1]:
            decreasing_count += 1
            trend_flags ^= (1 << (i % 8))
    return trend_flags, increasing_count, decreasing_count

# Evaluate overall performance based on multiple metrics
def evaluate_performance(data_stream):
    # Preprocess to get clean, calibrated values
    processed = preprocess_data(data_stream)
    
    # Track frequency of certain values (distractor: not directly used)
    freq_map = Counter(processed)
    rare_values = [k for k, v in freq_map.items() if v == 1]
    
    # Compute modular checksum (semi-relevant)
    checksum = sum(x % 7 for x in processed) * 2
    
    # Detect trend patterns
    flags, up, down = detect_trends(processed)
    
    # Secondary processing: pair analysis (mostly irrelevant)
    pairs = list(combinations(processed[:5], 2))
    valid_pairs = 0
    for a, b in pairs:
        if abs(a - b) <= 8:
            valid_pairs += 1  # Distractor computation
    
    # Core logic: score based on upward trends and checksum
    base_score = up * 15
    penalty = down * 7
    adjustment = checksum % 11
    final_score = base_score - penalty + adjustment
    
    # Dead code branch - never executed due to logic
    if len(rare_values) > 10:
        final_score += 100
    
    return final_score

# Main execution
sensor_input = generate_sensor_data()
data_log = {'input': sensor_input, 'system_id': 'SNSR-7'}  # Unused metadata

# Execute evaluation
final_score = evaluate_performance(sensor_input)
print(f"Result: {final_score}")