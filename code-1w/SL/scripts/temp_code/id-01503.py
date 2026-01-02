from collections import defaultdict, Counter

# Simulated sensor readings with timestamps and types
timestamped_readings = [
    (100, 'temp', 23.5),
    (105, 'pressure', 1013.25),
    (110, 'temp', 24.1),
    (115, 'humidity', 45),
    (120, 'temp', 24.3),
    (125, 'pressure', 1012.9),
    (130, 'humidity', 47),
    (135, 'temp', 23.9)
]

# Misleading auxiliary data (distractor)
system_logs = [
    (98, 'startup'), (102, 'calibration'), (107, 'warning'), (118, 'info'), (128, 'debug')
]

# Group readings by type using defaultdict
data_by_type = defaultdict(list)
for ts, r_type, value in timestamped_readings:
    data_by_type[r_type].append(value)

# Compute averages (relevant for later steps)
averages = {}
for key in data_by_type:
    averages[key] = sum(data_by_type[key]) / len(data_by_type[key])

# Redundant and misleading computation: log frequency of events (not used later)
event_counter = Counter(event for _, event in system_logs)
useless_ratio = event_counter['warning'] / (event_counter.get('info', 1))

# Process temperature trend with list comprehension and enumerate
raw_temps = data_by_type['temp']
temp_changes = [
    raw_temps[i] - raw_temps[i-1]
    for i in range(1, len(raw_temps))
]
positive_trend_count = sum(1 for change in temp_changes if change > 0)

# Simulate confidence adjustment based on stability (distractor block)
stability_score = 0
if len(temp_changes) > 0:
    variance = sum((x - sum(temp_changes)/len(temp_changes))**2 for x in temp_changes) / len(temp_changes)
    stability_score = 1 / (1 + variance)  # Higher if changes are small

# Unused helper function (dead code path - distractor)
def smooth_data(values, factor=0.1):
    if not values:
        return []
    smoothed = [values[0]]
    for v in values[1:]:
        smoothed.append(smoothed[-1] * (1 - factor) + v * factor)
    return smoothed

# Analyze pressure-humidity correlation (semi-relevant, but only pressure used later)
correlation_data = []
pressure_vals = data_by_type['pressure']
humidity_vals = data_by_type['humidity']
for p, h in zip(pressure_vals, humidity_vals):
    correlation_data.append(p * h)

# Key processing function
def calculate_final_score(data_map):
    base = data_map['temp'][-1] * 10  # Last temp * 10
    adjustment = 0
    
    # Conditional logic chain with nested checks
    if averages['pressure'] < 1013.0:
        adjustment += 5
        if positive_trend_count >= 2:
            adjustment += 3
        else:
            adjustment -= 2
    else:
        adjustment -= 1
    
    # Boolean logic with short-circuit evaluation
    has_high_temp = data_map['temp'][-1] > 24.0 or len(data_map['temp']) > 5 and min(data_map['temp']) < 23.6
    bonus = 10 if has_high_temp and adjustment > 0 else 0
    
    return int(base + adjustment + bonus)

# Execute critical statement
processed_data = data_by_type
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")