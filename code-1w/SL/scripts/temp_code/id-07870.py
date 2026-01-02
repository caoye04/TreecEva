import math

# Simulated sensor array data (temperature, pressure, humidity)
sensor_inputs = [
    (23.5, 101.3, 45.0),
    (25.0, 102.1, 47.8),
    (22.8, 100.9, 50.1),
    (26.7, 103.4, 44.3),
    (24.1, 101.8, 48.5)
]

# Irrelevant backup copy
temp_backup = [row for row in sensor_inputs]

# Mapping of zone IDs to thresholds
zone_config = {'A': 24.0, 'B': 25.5, 'C': 23.0}

# Unused secondary map (distractor)
pressure_ref = {'A': 101.0, 'B': 102.5, 'C': 100.5}

# Preprocessing: convert to dictionaries for easier access
processed_data = []
for i, (t, p, h) in enumerate(sensor_inputs):
    zone_id = chr(65 + (i % 3))  # A, B, C cyclically
    processed_data.append({
        'zone': zone_id,
        'temp': t,
        'press': p,
        'humid': h,
        'index': i,
        'score': round((t * 0.7) + (h * 0.3), 2)  # Distractor metric
    })

# Dead code path — never called
def legacy_calibrate(data_list):
    return [d['temp'] * 0.95 for d in data_list]

# Threshold map based on zone configuration
def build_threshold_map(zones):
    base = {}
    for k, v in zones.items():
        base[k] = {
            'temp_upper': v + 1.5,
            'temp_lower': v - 1.5,
            'alert_temp': v + 2.0
        }
    return base

threshold_map = build_threshold_map(zone_config)

# Extraneous transformation (not used in final logic)
flat_list = []
for entry in processed_data:
    flat_list.extend([entry['temp'], entry['press']])

# Secondary analysis that computes unused metrics
rolling_avg = 0
if len(processed_data) > 0:
    rolling_avg = sum(e['temp'] for e in processed_data) / len(processed_data)

# Another red herring: hypothetical correction factor
correction_applied = False
hypothetical_offset = 0.0
if rolling_avg > 25.0:
    hypothetical_offset = -0.5
    correction_applied = True

# Core diagnostic logic
abnormal_count = 0
high_risk_zones = set()
summary_stats = {
    'stable': 0,
    'elevated': 0,
    'critical': 0
}

for record in processed_data:
    zone = record['zone']
    temp = record['temp']
    limits = threshold_map[zone]
    
    # Determine status using conditional expression
    status = ('critical' if temp >= limits['alert_temp']
              else 'elevated' if temp > limits['temp_upper']
              else 'stable')
    
    summary_stats[status] += 1
    
    if status == 'critical':
        abnormal_count += 1
        high_risk_zones.add(zone)
    elif status == 'elevated':
        abnormal_count += 0.5  # Partial weighting

# Decoy function — looks important but unused
def compute_variance(data):
    mean_val = sum(d['temp'] for d in data) / len(data)
    return sum((d['temp'] - mean_val)**2 for d in data) / len(data)

# Final analysis with multiple inputs and logic paths
def analyze_readings(readings, thresholds):
    total_risk = 0
    zone_risk_levels = {}
    
    for r in readings:
        z = r['zone']
        t = r['temp']
        lim = thresholds[z]
        risk_score = 0
        
        if t > lim['alert_temp']:
            risk_score = 3
        elif t > lim['temp_upper']:
            risk_score = 2
        elif t < lim['temp_lower']:
            risk_score = 1
        
        # Accumulate per-zone max risk
        if z not in zone_risk_levels or risk_score > zone_risk_levels[z]:
            zone_risk_levels[z] = risk_score
    
    # Composite index calculation
    base_index = sum(zone_risk_levels.values()) * 100
    adjustment = math.floor(abs(summary_stats['critical'] - summary_stats['stable']) * 10)
    
    # Final diagnostic score
    result = int(base_index + adjustment)
    
    # Hidden logic: if no critical readings, apply bonus reduction
    if summary_stats['critical'] == 0:
        result -= 50  # Stabilization bonus
    
    return result

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Irrelevant sorting of a side list
sorted_pairs = sorted([(d['temp'], d['humid']) for d in processed_data], key=lambda x: x[0])

# Print final answer as required
print(f"Target result: {final_diagnostic}")