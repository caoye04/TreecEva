from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant readings
data_stream = [
    ('temp', 23.5), ('humidity', 45), ('temp', 24.1), ('pressure', 1013),
    ('humidity', 47), ('temp', 22.8), ('temp', 23.0), ('pressure', 1012),
    ('humidity', 44), ('temp', 24.0), ('light', 300), ('humidity', 46)
]

# Misleading auxiliary variables (distractors)
optimal_ranges = {
    'temp': (22, 25),
    'humidity': (40, 50),
    'pressure': (1000, 1020),
    'light': (200, 400)
}

redundant_flags = [True, False, True, True]
placeholder_matrix = [[0]*3 for _ in range(3)]
useless_sum = sum([x**2 for x in range(5)])  # Irrelevant computation

# Process raw data: group by type and filter valid entries
grouped = defaultdict(list)
for sensor_type, value in data_stream:
    grouped[sensor_type].append(value)

# Compute averages per sensor (semi-relevant)
averages = {}
for stype, values in grouped.items():
    averages[stype] = sum(values) / len(values)

# Apply arbitrary correction factors (some relevant, some not)
correction_map = {'temp': 1.02, 'humidity': 0.98, 'pressure': 1.005, 'light': 1.0}
corrected = {}
for key, val in averages.items():
    corrected[key] = val * correction_map.get(key, 1.0)

# Extract only temperature and humidity for final processing (key narrowing)
working_set = {k: corrected[k] for k in ['temp', 'humidity'] if k in corrected}

# Simulate historical baselines (distractor structure)
historical = defaultdict(lambda: 0)
historical.update({'temp': 23.2, 'humidity': 45.5})

# Compute deviation-based risk index (intermediate, partially used)
risk_index = 0
for param in working_set:
    current = working_set[param]
    base = historical[param]
    deviation = abs(current - base)
    if deviation > 0.5:
        risk_index += 1

# Prepare processed data structure (core input to final function)
processed_data = {
    'readings': working_set,
    'stats': {
        'count': len(data_stream),
        'missing_sensors': [s for s in optimal_ranges if s not in grouped],
        'redundant_count': useless_sum  # Dead-end field
    }
}

# Helper function with internal distraction
def calculate_final_score(data_dict):
    readings = data_dict['readings']
    temp_val = readings['temp']
    hum_val = readings['humidity']
    
    # Complex but mostly irrelevant transformation chain
    temp_scaled = (temp_val - 20) * 10
    hum_scaled = (hum_val - 40) / 5
    
    score_components = []
    for i in range(1, 4):
        comp = (temp_scaled + i) ** 0.5 * (hum_scaled / i)
        score_components.append(comp)
    
    # Real scoring logic buried among distractions
    base_score = sum(score_components)
    
    # Conditional adjustment based on count from data_dict (actual dependency)
    n = data_dict['stats']['count']
    adjustment_factor = 1.0
    if n > 10:
        adjustment_factor = 0.95
    elif n < 5:
        adjustment_factor = 1.05
    
    # Final calculation uses base_score and adjustment
    final_score = int(base_score * adjustment_factor)
    
    # Dead code branch (never executed due to prior filtering)
    if 'pressure' in data_dict['readings']:
        extra_bonus = data_dict['readings']['pressure'] * 0.01
        final_score += int(extra_bonus)
    
    return final_score

# Execute main logic
temp_buffer = [corrected['temp']] * 2  # Unused buffer
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")