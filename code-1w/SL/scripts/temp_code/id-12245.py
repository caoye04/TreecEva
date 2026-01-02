from collections import defaultdict, Counter
import math

# Simulated telemetry data from distributed sensor array
telemetry_stream = [
    (1001, 'TEMP', 78.3), (1002, 'VIBR', 0.45), (1003, 'PRESS', 101.3),
    (1001, 'TEMP', 79.1), (1004, 'HUMID', 45.2), (1002, 'VIBR', 0.47),
    (1005, 'TEMP', 80.0), (1003, 'PRESS', 102.1), (1001, 'TEMP', 81.5),
    (1004, 'HUMID', 44.8), (1005, 'TEMP', 82.3), (1002, 'VIBR', 0.52)
]

# Irrelevant mapping - looks useful but unused in critical path
sensor_descriptions = {
    1001: 'Engine Room Temperature Sensor',
    1002: 'Turbine Vibration Monitor',
    1003: 'Hydraulic Pressure Gauge',
    1004: 'Ambient Humidity Detector',
    1005: 'Exhaust Gas Thermocouple'
}

# Distractor function - appears important but not used in main logic
def legacy_calibrate(values):
    adjusted = []
    for v in values:
        if v < 10:
            adjusted.append(v * 1.05)
        elif v > 100:
            adjusted.append(v * 0.95)
        else:
            adjusted.append(v)
    return [round(x, 2) for x in adjusted]

# Dead code path - never invoked
class DataNormalizer:
    def __init__(self):
        self.factor = 1.0
    
    def normalize(self, x):
        return x * self.factor

# Unused statistical helper
def rolling_average(data, window=3):
    if len(data) < window:
        return [sum(data)/len(data)]
    avgs = []
    for i in range(len(data)-window+1):
        avgs.append(sum(data[i:i+window]) / window)
    return avgs

# Main processing pipeline
log_data = defaultdict(list)
system_flags = defaultdict(int)

for sensor_id, metric_type, reading in telemetry_stream:
    log_data[metric_type].append(reading)
    if reading > 80 and metric_type == 'TEMP':
        system_flags['high_temp_alert'] += 1
    if metric_type == 'VIBR' and reading > 0.5:
        system_flags['vibration_warning'] = 1

# Red herring computation - calculates something plausible but unused
aggregated_stats = {}
for mtype, readings in log_data.items():
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    aggregated_stats[mtype] = {
        'mean': round(mean_val, 2),
        'std_dev': round(variance ** 0.5, 2),
        'peak': max(readings)
    }

# Decoy dictionary - mimics real output format but unused
temp_analysis = {
    'status': 'stable',
    'trend': 'increasing',
    'confidence': 0.87
}

# Critical preprocessing step disguised among distractors
transformed = []
for temp in log_data['TEMP']:
    normalized = (temp - 32) * (5/9)  # Convert to Celsius
    transformed.append(normalized)

# Another irrelevant counter
reading_counter = Counter([r[1] for r in telemetry_stream])

# Complex conditional that seems significant but sets unused flag
if system_flags['high_temp_alert'] >= 2 and system_flags['vibration_warning']:
    system_flags['critical_state'] = 3
else:
    system_flags['critical_state'] = 0  # This runs, but value unused

# Key intermediate result buried in noise
event_risk_score = 0
for t in log_data['TEMP']:
    if t >= 80:
        event_risk_score += int(t // 10)

# Distractor set operation - looks analytical but irrelevant
unique_sensors = {sid for sid, _, _ in telemetry_stream}

# Fake diagnostic with misleading name
diagnostic_checksum = sum(int(x) for x in log_data['TEMP']) % 17

# Real processing begins here — non-obvious due to noise
system_flags['data_points'] = len(telemetry_stream)

# Core logic interwoven with decoys
def analyze_temperature_profile(temps):
    sorted_temps = sorted(temps)
    median_temp = (sorted_temps[len(sorted_temps)//2] + sorted_temps[~(len(sorted_temps)//2)]) / 2
    base_index = math.log(median_temp, 2)
    fluctuation = max(temps) - min(temps)
    stability_factor = 100 / (fluctuation + 1) if fluctuation > 0 else 100
    return round(base_index * stability_factor)

# Secondary metric with red herring behavior
def compute_operational_load(flags):
    load = 0
    if flags['high_temp_alert']:
        load += flags['high_temp_alert'] * 15
    if flags['vibration_warning']:
        load += 25
    # This block looks important but doesn't affect final answer
    if flags.get('critical_state', 0) > 0:
        load *= 1.5  # Never reached
    return load

# Unused fallback mechanism
def default_remediation_level(score):
    thresholds = [10, 25, 50]
    for i, t in enumerate(thresholds):
        if score < t:
            return i
    return len(thresholds)

# Real transformation using defaultdict - key concept
processed_readings = defaultdict(list)
for typ, vals in log_data.items():
    processed_readings[f'{typ}_raw'].extend(vals)
    processed_readings[f'{typ}_scaled'] = [v * 1.01 for v in vals]  # Minor correction

# Actual core analysis function
def process_metrics(metrics_dict, flags):
    temps = metrics_dict['TEMP']
    vibrations = metrics_dict['VIBR']
    
    # Step 1: Base value from temperature median
    sorted_t = sorted(temps)
    med_t = (sorted_t[len(sorted_t)//2] + sorted_t[~(len(sorted_t)//2)]) / 2
    
    # Step 2: Apply logarithmic scaling
    base_value = math.log(med_t) * 100
    
    # Step 3: Adjust by vibration count above threshold
    vib_adjust = sum(1 for v in vibrations if v > 0.45)
    adjusted_value = base_value - (vib_adjust * 8.5)
    
    # Step 4: Integer division adjustment based on number of high-temp events
    high_temp_count = sum(1 for t in temps if t > 79)
    divisor = high_temp_count if high_temp_count > 0 else 1
    final_score = int(adjusted_value // divisor)
    
    # Step 5: Apply ceiling floor from system metadata
    if flags['data_points'] > 10:
        final_score += 5
    
    # Step 6: Final modulation via set intersection logic (decoy logic)
    temp_set = set(round(t) for t in temps)
    threshold_set = set(range(80, 85))
    overlap = len(temp_set & threshold_set)
    if overlap:
        final_score += overlap * 3  # Only adds 3 since 80,81,82 present
    
    return final_score

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")