def analyze_trend(values):
    if not values:
        return 0
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return avg, variance

# Simulate sensor data drift over time
time_series = [0.5, 0.7, 0.6, 0.8, 1.2, 1.4, 1.3, 1.6]
baseline, spread = analyze_trend(time_series)

# Irrelevant transformation - distractor
distorted = [round(x ** 0.5, 3) for x in time_series if x > 0.7]
length_check = len(distorted) > 5

# System parameters
device_id = "SNSR-7X"
threshold = 1.0 if '7' in device_id else 0.9
activation_flag = True

# Compute deviation from ideal baseline
current_reading = 1.5
expected_baseline = 1.0

if current_reading > baseline:
    deviation = (current_reading - baseline) * 100 / baseline
else:
    deviation = 0

# Secondary metric - misleading relevance
consistency_score = 100 - (spread * 10) if spread < 0.5 else 80

# Conditional expression using string method - required feature
status_label = "STABLE" if device_id.lower().endswith("7x") else "UNSTABLE"

# Core logic hidden among distractions
def calculate_performance(base, dev, thresh):
    if base < thresh:
        adjustment = 1.2
    else:
        adjustment = 0.9
    
    # Multiple factors influence final score
    raw_score = (100 - dev) * adjustment
    
    # Nested condition with short-circuiting
    penalty = 10 if activation_flag and deviation > 40 else 0
    
    # Final computation
    result = raw_score - penalty
    
    # Dead code path - distractor
    if False:
        result = max(result, 50)
        backup = "unused"
    
    return int(result)

# Key statement
final_score = calculate_performance(baseline, deviation, threshold)

print(f"Result: {final_score}")