def process_readings(logs):
    processed = []
    for log in logs:
        temp = log['temp'] + 273.15
        pressure_adj = log['pressure'] * 0.987
        # Irrelevant transformation
        dummy_calc = (temp * pressure_adj) % 113
        if temp > 500:
            efficiency = 0.85 - (temp - 500) * 0.0002
        else:
            efficiency = 0.75 + (temp - 300) * 0.001
        processed.append({'efficiency': efficiency, 'status': log['status']})
    return processed

# Dead function - never used
def analyze_vibration(data):
    total_power = 0
    for d in data:
        total_power += d.get('vibration_x', 0) ** 2 + d.get('vibration_y', 0) ** 2
    return total_power // 100

# Decoy data structure
system_cache = {
    'calibration': [0.98, 1.02, 0.99],
    'last_updated': '2023-12-01',
    'checksum': 5678
}

# Bitwise red herring
security_flag = 0b10101010
access_level = security_flag & 0b11110000
is_authorized = access_level >> 4 == 10

# Real input data
sensor_logs = [
    {'temp': 450, 'pressure': 101.3, 'status': 'active'},
    {'temp': 520, 'pressure': 98.7, 'status': 'active'},
    {'temp': 300, 'pressure': 105.0, 'status': 'standby'},
    {'temp': 610, 'pressure': 95.0, 'status': 'active'}
]

# Threshold configuration (used later)
threshold_map = {
    'efficiency_floor': 0.77,
    'min_readings': 2
}

# Set operations as distractor
active_statuses = {'active', 'running', 'online'}
inactive_statuses = {'standby', 'offline'}
duplicate_check = active_statuses.intersection(inactive_statuses)  # Empty set

# List comprehension with side effect?
baseline_scores = [round(item['temp'] * 0.01, 2) for item in sensor_logs]

# Enumerate and zip usage (partially relevant)
turbine_ids = ['TURB-01', 'TURB-02', 'TURB-03', 'TURB-04']
turbine_data = []
for i, log in enumerate(process_readings(sensor_logs)):
    zipped = list(zip(turbine_ids, [log] * len(turbine_ids)))
    turbine_data.append({
        'id': turbine_ids[i],
        'raw': sensor_logs[i],
        'analysis': log,
        'score': baseline_scores[i]
    })

# Unused recursive function (decoy)
def compute_residual(x, depth=0):
    if depth >= 3 or x < 10:
        return x
    return compute_residual(x // 2, depth + 1) + compute_residual(x // 3, depth + 1)

# Real aggregation logic
valid_count = 0
summed_efficiency = 0.0
over_threshold = []

for unit in turbine_data:
    analysis = unit['analysis']
    if analysis['status'] != 'active':
        continue
    if analysis['efficiency'] >= threshold_map['efficiency_floor']:
        summed_efficiency += analysis['efficiency']
        valid_count += 1
        over_threshold.append(unit['id'])

# Additional distraction: complex filtering
recent_updates = {tid: idx for idx, tid in enumerate(turbine_ids) if idx % 2 == 0}
update_risk = sum(recent_updates.values()) * 0.1  # Unused

# Final computation
if valid_count >= threshold_map['min_readings']:
    average_efficiency = summed_efficiency / valid_count
    penalty_factor = len(turbine_data) - len(over_threshold)
    adjusted_score = average_efficiency * 100 - penalty_factor * 1.5
else:
    adjusted_score = 50.0

# Key derived variable
intermediate_diagnostic = round(adjusted_score, 3)

# Final transformation using bitwise (misleading use)
crc_checksum = 0
for c in f"{intermediate_diagnostic}":
    crc_checksum ^= ord(c)
final_diagnostic = intermediate_diagnostic + (crc_checksum * 0.01)

# Print result
print(f"Result: {final_diagnostic}")