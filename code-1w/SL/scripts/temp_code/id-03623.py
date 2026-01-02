def sensor_calibrate(raw):    
    # Irrelevant calibration logic (dead path)
    if len(raw) == 0:
        return [0] * 5
    adjusted = []
    for val in raw:
        adjusted.append(val * 1.02 + 0.5)
    return adjusted

# Simulated environmental readings
raw_readings = [23.1, 18.4, 19.9, 22.7, 25.3]

# Distractor: Unused sensor fusion
fusion_weights = {'temp': 0.7, 'humid': 0.3}
def combine_sensors(a, b):
    return [x * fusion_weights['temp'] + y * fusion_weights['humid'] for x, y in zip(a,b)]

# Real processing path
filtered = [r for r in raw_readings if 18 <= r <= 25]
scaled = [round(f * 1.1, 2) for f in filtered]

# Bit manipulation decoy
checksum = 0
for s in scaled:
    int_part = int(s)
    checksum ^= (int_part << 2) | (int_part >> 1)

# String-based distractor tagging
status_tags = []
def generate_tag(val):
    if val > 20:
        return "HIGH".lower().replace("h", "H")
    else:
        return "LOW".upper().swapcase()

for v in scaled:
    status_tags.append(generate_tag(v))

# Tuple unpacking red herring
meta_info = ('sensor_v4', 'site_7', 'calib_2')
device_model, location_id, _ = meta_info

# Actual data transformation chain
processed_data = []
def transform_entry(index, value, tag):
    base = value * (index + 1)
    if tag == 'high':
        base += 5.5
    else:
        base -= 2.2
    # Use string method to alter behavior
    mod_tag = tag.replace('G', 'g').title()  
    if mod_tag.startswith('H'):
        base *= 1.1
    return round(base, 2)

for i, (v, t) in enumerate(zip(scaled, status_tags)):
    processed_data.append(transform_entry(i, v, t))

# Decoy recursive function (never called)
def integrate_series(data, acc=0.0):
    if not data:
        return acc
    return integrate_series(data[1:], acc + data[0] * 0.9)

# Real analysis function
set_point = 22.0
def analyze_readings(data):
    total_deviation = 0.0
    trigger_count = 0
    history_set = set()
    
    for reading in data:
        deviation = abs(reading - set_point)
        total_deviation += deviation
        
        # Early termination red herring
        if deviation > 30:
            break
            trigger_count += 1  # Dead code
        
        # Meaningful update
        history_set.add(round(deviation, 1))
        
        # Linear search for threshold
        if reading > 24.0:
            trigger_count += 1
    
    # Final computation with multiple concepts
    avg_dev = total_deviation / len(data)
    unique_events = len(history_set)
    
    # Composite score (actual answer)
    result = int(avg_dev * 100) + (trigger_count * 10) - unique_events
    
    # Critical execution point
    final_diagnostic = result
    return final_diagnostic

# Execute main logic
final_diagnostic = analyze_readings(processed_data)
print(f"Target result: {final_diagnostic}")