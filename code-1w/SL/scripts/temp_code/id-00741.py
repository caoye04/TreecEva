import math

# Simulated health monitoring system with diagnostic logic

def analyze_heart_rate(hr):
    if hr < 50:
        return -1
    elif 50 <= hr <= 100:
        return 0
    else:
        return 1

# Irrelevant utility - distractor
compute_bmi = lambda weight, height: weight / (height ** 2)

# Vital signs preprocessing
vital_transform = lambda x: (x * 1.08) + 7

baseline_readings = [65, 72, 58, 95, 110, 48]
processed_readings = [vital_transform(hr) for hr in baseline_readings]

# Decoy function - never used but looks important
def evaluate_stress_level(cortisol, activity):
    stress_index = cortisol * 0.3 + activity * 0.7
    return 'high' if stress_index > 75 else 'low'

# Unused data structures - red herring
historical_temperatures = {"day1": 36.5, "day2": 37.1, "day3": 38.0}
cardio_zones = {"warmup": (50, 70), "fat_burn": (70, 80), "aerobic": (80, 90)}

# Complex filtering using set operations - relevant only in part
abnormal_set = {i for i, hr in enumerate(processed_readings) if hr > 105}
warning_indices = set()
for i, hr in enumerate(processed_readings):
    if analyze_heart_rate(hr) == 1:
        warning_indices.add(i)

# Contrived intermediate calculation - misleading
aggregate_risk = sum([math.ceil(x/10)*2 for x in processed_readings if x > 80])

# Threshold logic generator - actually used
threshold_func = lambda t: t > 98.6

# Data masking with list comprehension - relevant
masked_data = [round(x, 1) for x in processed_readings if not math.isclose(x, 72.0)]

# Simulated multi-parameter health data
health_data = {
    'readings': masked_data,
    'flags': [analyze_heart_rate(hr) for hr in masked_data],
    'timestamp': '2023-10-05T08:00:00',
    'device_id': 'HMD-7X',
    'version': '2.1.0'
}

# Redundant transformation chain - distractor
transform_chain = [
    lambda x: x + 1.5,
    lambda x: x * 0.95,
    lambda x: abs(x - 0.1)
]

temp_val = 100.0
for op in transform_chain:
    temp_val = op(temp_val)  # This result is unused

# Core processing function with embedded logic
def process_metrics(data, threshold_checker):
    raw_values = data['readings']
    flag_sum = sum(data['flags'])
    
    # Compute derived statistic
    adjusted_mean = sum([v * 0.85 for v in raw_values]) / len(raw_values)
    
    # Conditional override path (never triggers due to data)
    if len([v for v in raw_values if v > 120]) > 2:
        return -999  # Emergency code - unreachable
    
    # Critical threshold check
    high_temp_count = len([v for v in raw_values if threshold_checker(v)])
    
    # Final diagnostic score: combination of flag sum and temperature anomalies
    diagnostic_score = (flag_sum * 100) + (high_temp_count * 50)
    
    # Dead code branch - looks important
    if data.get('version') == '1.0.0':
        diagnostic_score *= 0.5
        
    return int(diagnostic_score)

# Execute main logic
final_diagnostic = process_metrics(health_data, threshold_func)

# Print result as required
print(f"Target result: {final_diagnostic}")