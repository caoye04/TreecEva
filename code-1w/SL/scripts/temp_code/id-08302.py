import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7, 22.5]
humidity_readings = [45, 48, 50, 55, 60, 58, 53, 49]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant auxiliary data (distractor)
color_codes = ['FF0000', '00FF00', '0000FF', 'FFFF00', 'FF00FF']
user_preferences = {'theme': 'dark', 'units': 'metric', 'alerts': True}

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    mean = sum(data) / len(data)
    return [x - mean for x in data]  # Never used

def calculate_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 6)

# Core signal processing
scaling_factor = 1.75
adjusted_temps = [t * scaling_factor for t in temperature_readings]
dew_point_estimates = []
for i, (t, h) in enumerate(zip(temperature_readings, humidity_readings)):
    dew_point = t - ((100 - h) / 5)
    dew_point_estimates.append(round(dew_point, 2))

# Bitwise masking for sensor validation status (XOR-based checksum simulation)
sensor_flags = [0b1010, 0b1100, 0b1011, 0b0110, 0b1111, 0b1001, 0b0101, 0b1110]
valid_sensors = []
for flag in sensor_flags:
    parity_check = bin(flag ^ 0b1111).count('1')
    if parity_check % 2 == 0:
        valid_sensors.append(True)
    else:
        valid_sensors.append(False)

# Apply validity mask to data (only use valid sensors)
filtered_temps = [t for i, t in enumerate(adjusted_temps) if valid_sensors[i]]
filtered_dew = [d for i, d in enumerate(dew_point_estimates) if valid_sensors[i]]

# Construct threshold map with set operations (real logic path)
critical_temps = {round(t) for t in filtered_temps if t > 42.0}
moderate_temps = {round(t) for t in filtered_temps if 38.0 <= t <= 42.0}
acceptable_temps = set(range(30, 38))
overlapping_zones = critical_temps & moderate_temps  # Empty, but part of logic

threshold_map = {
    'critical': critical_temps - moderate_temps,
    'moderate': moderate_temps - critical_temps,
    'baseline': acceptable_temps
}

# Signal anomaly detection using string-encoded rules (string methods)
anomaly_rules = "CRIT:MAG>45|DEW<15|FLAG=ERR"
rules_list = anomaly_rules.split('|')
rule_conditions = {r.split(':')[0]: r.split(':')[1] for r in rules_list}

# Process data into diagnostic features
processed_data = []
for i, temp in enumerate(filtered_temps):
    magnitude = abs(temp)
    has_dew_risk = filtered_dew[i] < 15.0
    flag_status = 'ERR' if not valid_sensors[i] else 'OK'
    
    # Encode state as string for pattern matching
    state_string = f"MAG>{magnitude:.0f},DEW<{filtered_dew[i]},FLAG={flag_status}"
    
    # Check against rule patterns (string containment)
    triggers = 0
    for key, condition in rule_conditions.items():
        if condition in state_string:
            triggers += 1
    
    score = int(magnitude // 10) + triggers * 5
    processed_data.append({'index': i, 'score': score, 'state': state_string})

# Decoy analysis function (never called)
def deprecated_diagnostic(signal):
    return sum(s['score'] * 0.8 for s in signal) + 10

# Real analysis function
def analyze_signal(signal_packets, thresholds):
    base_value = 0
    adjustment = 0
    
    # Enumerate through packets with index tracking
    for idx, packet in enumerate(signal_packets):
        base_value += packet['score']
        
        # Conditional bit shift based on index
        if idx % 2 == 0:
            adjustment += packet['score'] << 1
        else:
            adjustment -= packet['score'] >> 1
        
        # String-based state inspection
        if 'CRIT' in packet['state'] and 'MAG>45' in packet['state']:
            adjustment += 100
    
    # Influence from threshold sizes
    for zone in thresholds.values():
        adjustment += len(zone) * 7
    
    # Final computation
    result = (base_value * 1.5) + adjustment
    
    # Secondary correction using entropy (red herring computation)
    dummy_entropy = calculate_entropy([len(thresholds[k]) for k in thresholds])
    final_adjust = int(result - (dummy_entropy * 10))
    
    return final_adjust

# Execute main analysis
temp_buffer = [24.5, 25.0]
humid_buffer = [52, 54]
# Unused buffer processing (distractor)
[math.sqrt(x) for x in temp_buffer]

final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")