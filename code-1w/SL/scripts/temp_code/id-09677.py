from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def generate_noisy_sensor_data():
    raw_readings = [23.5, 24.1, 23.5, 25.0, 24.1, 26.3, 25.0, 23.5]
    timestamps = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
    sensor_data = list(zip(timestamps, raw_readings))
    return sensor_data

# Process and clean data: remove duplicates, apply calibration offset
def process_sensor_data(data):
    seen_values = set()
    unique_readings = []
    calibrated_readings = []
    
    for ts, val in data:
        if val not in seen_values:
            seen_values.add(val)
            unique_readings.append(val)
            calibrated_readings.append(round(val + 0.2, 1))  # calibration
    
    # Misleading redundant computation (distractor)
    average_raw = sum(r[1] for r in data) / len(data)
    temp_analysis = {"avg": average_raw, "count": len(data)}
    
    return calibrated_readings

# Analyze frequency of original values (red herring)
def analyze_redundancy(raw_data):
    values_only = [val for _, val in raw_data]
    freq = Counter(values_only)
    repeated = [v for v, count in freq.items() if count > 1]
    return len(repeated)

# Core scoring logic based on processed values
def calculate_final_score(calibrated):
    base_score = 0
    bonus = 0
    
    # Scoring rules:
    for i, val in enumerate(calibrated):
        if val > 24.0:
            base_score += int(val * 2)
        else:
            base_score -= int(val)
            
        # Bonus condition (only triggers once)
        if i == 2 and val > 23.5:
            bonus = 15
    
    # Distractor: complex unused conditional branch
    if len(calibrated) % 2 == 0 and sum(calibrated) < 100:
        adjustment = -5
    else:
        adjustment = 0  # never applied but looks relevant
    
    # Final score ignores adjustment; only base_score + bonus matters
    final = base_score + bonus
    
    # Extra distraction: slicing and reversing for no effect
    reversed_slice = calibrated[::-1][1:4]
    temp_sum = sum(reversed_slice)
    
    return final

# Execution flow
sensor_input = generate_noisy_sensor_data()
data_redundancy = analyze_redundancy(sensor_input)  # dead-end analysis
processed_data = process_sensor_data(sensor_input)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")