from collections import defaultdict
import math

# Simulated sensor data with metadata tags
data_stream = [
    ('temp', 'A7', 34.2), ('humidity', 'B3', 65), ('temp', 'A7', 36.1), 
    ('pressure', 'C9', 1013), ('temp', 'D2', 29.8), ('humidity', 'B3', 70),
    ('temp', 'A7', 35.9), ('pressure', 'C9', 1011), ('flow', 'D2', 45),
    ('temp', 'A7', 33.7), ('humidity', 'X5', 40), ('flow', 'D2', 47)
]

# Irrelevant transformation: dummy hash mapping (red herring)
dummy_hash = {chr(i): i*3 for i in range(65, 75)}

# Misleading intermediate: aggregate by label only (unused later)
label_count = defaultdict(int)
for _, label, _ in data_stream:
    label_count[label] += 1

# Distractor function: never called
def decrypt_signal(seq):
    return [math.sin(x) * 1.5 for x in seq if x > 0]

# Another decoy: complex but unused structure
system_state = {
    'nodes': {k: {'active': True, 'load': (ord(k[0]) + int(k[1])) % 7} 
             for k in label_count.keys()},
    'version': '2.1a',
    'calibration': tuple(round((i + 0.1)**1.1, 2) for i in range(5))
}

# Relevant: extract temperature readings from sensor A7 only
temp_A7_readings = [val for typ, lbl, val in data_stream if typ == 'temp' and lbl == 'A7']

# Distractor: string processing with no impact
log_header = "SENSOR_DIAG_V2"
header_lower = log_header.lower()
split_parts = header_lower.split('_')
joined = ''.join([part.capitalize() for part in split_parts])

# Threshold policy map (used later)
threshold_map = defaultdict(lambda: (0.0, 100.0))
threshold_map['temp'] = (30.0, 40.0)   # Valid range for temp
threshold_map['humidity'] = (50, 80)   # Ignore humidity logic

# Filter function: only temps within high-confidence zone
# Uses lambda to filter values strictly above 34.0
valid_range_filter = lambda x, th: x > th[0] and x < th[1]
filtered_A7_high = [v for v in temp_A7_readings if valid_range_filter(v, (34.0, 40.0))]

# Build filtered data including other types (but only A7 temps matter)
filtered_data = []
for typ, lbl, val in data_stream:
    if typ == 'temp' and lbl == 'A7' and val > 34.0:
        filtered_data.append(('T_HIGH', val))
    elif typ == 'pressure' and lbl == 'C9':
        adjusted = round(val / 10, 2)
        filtered_data.append(('P_NORM', adjusted))  # Dead path

# Unused accumulator
pressure_accum = 0
for typ, val in filtered_data:
    if typ == 'P_NORM':
        pressure_accum += val

# Core processing function
def process_readings(data, thresholds):
    # Extract only T_HIGH entries
    raw_vals = [v for t, v in data if t == 'T_HIGH']
    
    # Dead computation: average of non-existent P_NORM
    p_avg = sum(v for t, v in data if t == 'P_NORM') / max(1, len([1 for t, _ in data if t == 'P_NORM']))
    
    # Base score from count
    base_score = len(raw_vals) * 100
    
    # Precision adjustment: mean deviation from 35.0
    deviations = [abs(rv - 35.0) for rv in raw_vals]
    if deviations:
        mean_dev = sum(deviations) / len(deviations)
        penalty = int(mean_dev * 20)  # Each 0.05 dev => -1 point
    else:
        mean_dev = 0
        penalty = 0
    
    # Bonus for stability: small deviation
    bonus = 15 if mean_dev < 1.0 else 5 if mean_dev < 2.0 else 0
    
    # Final diagnostic score
    result = base_score - penalty + bonus
    
    # Irrelevant formatting
    status_flag = 'OK' if result > 200 else 'CHECK'
    confidence = round((1.0 - min(mean_dev, 3.0)/3.0), 3)
    
    # Critical return value
    return int(result)

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")