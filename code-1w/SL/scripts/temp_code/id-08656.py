from collections import defaultdict

# Simulate sensor data with noise and redundant readings
data_stream = [
    ("temp", 23.5), ("humid", 45), ("temp", 24.1), ("press", 1013), ("humid", 46),
    ("temp", 22.9), ("temp", 23.0), ("humid", 44), ("press", 1012), ("humid", 45)
]

# Misleading auxiliary data that appears relevant but isn't used in final calculation
noise_floor = 0.75
baseline_offset = 1.2
reference_map = {"A": 10, "B": 20, "C": noise_floor * 10}

# Aggregate sensor readings by type using defaultdict
raw_aggregates = defaultdict(list)
for sensor_type, value in data_stream:
    raw_aggregates[sensor_type].append(value)

# Compute mean values per sensor type
averages = {}
for stype, readings in raw_aggregates.items():
    avg = sum(readings) / len(readings)
    averages[stype] = round(avg, 2)

# Extract specific values — only 'temp' and 'humid' are actually used later
temp_avg = averages.get("temp", 0)
humid_avg = averages.get("humid", 0)
press_avg = averages.get("press", 0)  # Computed but not used

# Intermediate transformation with distractor logic
deviation_score = abs(temp_avg - 23.0) * 10
redundancy_penalty = len(data_stream) - len(raw_aggregates)  # Looks meaningful, unused

# Simulate feature engineering with list comprehensions
features = [f"{k}_{round(v*1.1)}" for k, v in averages.items()]
feature_lengths = [len(f) for f in features]  # Distractor computation

# Weighted scoring — only temp and humid contribute
weights = {'temp': 0.6, 'humid': 0.4}
score_components = {
    'temp': temp_avg * weights['temp'],
    'humid': humid_avg * weights['humid']
}

# Dead code path — never executed but looks important
def debug_validation(data):
    return all(isinstance(x, (int, float)) for x in data)

# Main scoring function
def calculate_final_score(data_dict):
    s = 0
    if 'temp' in data_dict:
        s += data_dict['temp'] * 1.5
    if 'humid' in data_dict:
        s += data_dict['humid'] * 0.8
    return int(s)  # Final score is integer

# Process only the average values as input
deferred_data = {k: round(v, 2) for k, v in averages.items()}

# Key statement: compute final score from processed data
final_score = calculate_final_score(deferred_data)

# Print result for evaluation
print(f"Result: {final_score}")