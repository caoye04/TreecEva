import math

# Sensor simulation and diagnostic analysis system
def collect_sensor_readings():
    raw_values = [2.1, 3.7, 4.5, 1.9, 6.3, 5.0, 3.2]
    timestamps = ['t0', 't1', 't2', 't3', 't4', 't5', 't6']
    labeled_readings = {ts: val for ts, val in zip(timestamps, raw_values)}
    return labeled_readings

# Irrelevant distraction: environmental metadata not used in computation
def get_environment_metadata():
    return {
        'humidity': 45.2,
        'pressure': 1013.25,
        'temperature': 22.1,
        'altitude': 87.0
    }

# Decoy function that looks important but is never called
def legacy_calibrate(values):
    adjusted = []
    for v in values:
        if v > 5.0:
            adjusted.append(v * 0.85)
        else:
            adjusted.append(v * 1.05)
    return adjusted

# Distractor: unused signal filtering function
def bandpass_filter(signal_list):
    filtered = []
    for i in range(1, len(signal_list) - 1):
        smoothed = (signal_list[i-1] + signal_list[i] + signal_list[i+1]) / 3.0
        filtered.append(smoothed)
    return [signal_list[0]] + filtered + [signal_list[-1]]

# Real processing begins here
processed_data = []
def process_sensor_data(raw_readings):
    global processed_data
    temp_store = []
    for key, value in raw_readings.items():
        squared = value ** 2
        log_val = math.log(squared + 1)
        normalized = log_val / (squared ** 0.5) if squared != 0 else 0
        temp_store.append((key, normalized, value))
    
    # Extract only normalized values above threshold
    thresholded = [item for item in temp_store if item[1] > 0.4]
    processed_data = [item[2] for item in sorted(thresholded, key=lambda x: x[1], reverse=True)]
    
    # Distractor: unused transformation
    inverted_map = {round(item[1], 3): item[0] for item in temp_store}
    
    return processed_data

# Complex threshold logic with red herring components
threshold_map = {}
def initialize_thresholds(data):
    global threshold_map
    base = sum(data) / len(data)
    variance = sum((x - base) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    # Real thresholds
    threshold_map['critical'] = base + 1.5 * std_dev
    threshold_map['warning'] = base + 0.5 * std_dev
    
    # Distractor: irrelevant categories
    threshold_map['placeholder_x'] = 999.9
    threshold_map['placeholder_y'] = -1.0
    threshold_map['debug_mode'] = False
    
    # Unused statistical measures
    skewness = sum((x - base)**3 for x in data) / (len(data) * std_dev**3)
    kurtosis = sum((x - base)**4 for x in data) / (len(data) * std_dev**4) - 3
    
    return threshold_map

# Core analysis function — contains the actual answer path
def analyze_readings(data, thresholds):
    if not data or 'critical' not in thresholds:
        return -999
    
    critical_level = thresholds['critical']
    warning_level = thresholds['warning']
    
    # Real logic: count how many readings exceed critical threshold
    critical_count = sum(1 for x in data if x > critical_level)
    warning_count = sum(1 for x in data if x > warning_level)
    
    # Intermediate misleading calculation
    pseudo_index = (critical_count * 100) + warning_count
    
    # Real decision path
    if critical_count >= 2:
        severity = 3
    elif critical_count == 1:
        severity = 2
    elif warning_count >= 3:
        severity = 1
    else:
        severity = 0
    
    # Actual answer computation
    diagnostic_code = severity * 1000 + critical_count * 100 + warning_count
    
    # Distractor: unused complex string encoding based on readings
    hex_tags = []
    for d in data:
        int_part = int(d)
        frac_part = int(round((d - int_part) * 100))
        combined = (int_part << 8) | frac_part
        hex_tag = hex(combined)[2:].upper().zfill(6)
        if 'A' in hex_tag:
            set_ops = set(hex_tag).intersection(set('ABCDEF'))
            if len(set_ops) > 1:
                reversed_chunks = [hex_tag[i:i+2] for i in range(0, len(hex_tag), 2)][::-1]
                joined = ''.join(reversed_chunks)
                hex_tags.append(joined)
    
    # Another decoy: tuple-based state tracking not used
    state_log = []
    for i, val in enumerate(data):
        state_log.append((i, 'high' if val > critical_level else 'low', round(val, 2)))
    
    return diagnostic_code

# Execution flow
sensor_readings = collect_sensor_readings()
env_meta = get_environment_metadata()  # stored but unused
raw_vals = [v for v in sensor_readings.values()]

processed_data = process_sensor_data(sensor_readings)
threshold_map = initialize_thresholds(raw_vals)

# Key statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Target result: {final_diagnostic}")