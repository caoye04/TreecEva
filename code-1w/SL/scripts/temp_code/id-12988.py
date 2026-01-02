from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor array data (real measurements mixed with noise)
sensor_logs = [
    'temp:72.4,hum:34,vib:0.21,freq:56.7',
    'temp:73.1,hum:36,vib:0.19,freq:57.0',
    'temp:71.8,hum:33,vib:0.25,freq:55.8',
    'temp:72.4,hum:35,vib:0.22,freq:56.2',
    'temp:73.1,hum:37,vib:0.20,freq:57.1',
    'temp:69.5,hum:32,vib:0.31,freq:54.3',
    'temp:70.2,hum:30,vib:0.33,freq:53.9'
]

# Irrelevant auxiliary data — decoy for environmental correlation analysis
aux_environment = {
    'pressure': [101.3, 101.5, 101.4, 101.2, 101.6],
    'light': ['high', 'low', 'med', 'high', 'med'],
    'co2_level': [410, 415, 408, 420, 412]
}

# Misleading precomputed stats (unused in final logic)
temp_averages = [72.4, 73.1, 71.8, 72.4, 73.1, 69.5, 70.2]
humidity_trends = [34, 36, 33, 35, 37, 32, 30]
vibration_peaks = [0.21, 0.19, 0.25, 0.22, 0.20, 0.31, 0.33]

# Fake transformation — looks important but unused
def deprecated_normalize(data_list):
    mean_val = sum(data_list) / len(data_list)
    return [(x - mean_val) / mean_val for x in data_list]

# Unused recursive function to calculate harmonic mean (red herring)
def harmonic_mean_recursive(lst, n=None):
    if n is None:
        n = len(lst)
    if n == 1:
        return 1 / lst[0]
    return n / ((n-1)/harmonic_mean_recursive(lst, n-1) + 1/lst[n-1])

# Real processing begins here

# Parse raw logs into structured format
parsed_readings = []
for log in sensor_logs:
    entries = log.split(',')
    reading = {}
    for entry in entries:
        key, val = entry.split(':')
        reading[key] = float(val)
    parsed_readings.append(reading)

# Extract temperature values for baseline drift check (partially relevant)
temps = [r['temp'] for r in parsed_readings]
baseline_temp = sum(temps) / len(temps)
drift_threshold = 2.0

# Flag readings with abnormal vibration or frequency drop
flags = []
for i, r in enumerate(parsed_readings):
    vib_alert = r['vib'] > 0.24
    freq_alert = r['freq'] < 55.0
    temp_drift = abs(r['temp'] - baseline_temp) > drift_threshold
    flags.append({'index': i, 'vib': vib_alert, 'freq': freq_alert, 'drift': temp_drift})

# Filter only readings that have no active flags (critical step)
valid_indices = [
    f['index'] for f in flags 
    if not (f['vib'] or f['freq'] or f['drift'])
]

filtered_data = [parsed_readings[i] for i in valid_indices]

# Dead code path: attempt to correlate with non-existent wind speed
if 'wind' in aux_environment:
    adjustment_factor = 0.95
else:
    adjustment_factor = 1.0  # never applied due to missing data

# Decoy statistical summary using list comprehensions and Counter
humidity_modes = Counter([str(int(r['hum'])) for r in parsed_readings]).most_common(2)
frequent_humidities = [int(h[0]) for h in humidity_modes]

# Advanced filtering: find readings where temp and hum are both above median
all_temps = sorted([r['temp'] for r in parsed_readings])
all_hums = sorted([r['hum'] for r in parsed_readings])
median_temp = all_temps[len(all_temps)//2]
median_hum = all_hums[len(all_hums)//2]

# This block looks sophisticated but is unused
enhanced_candidates = [
    r for r in parsed_readings 
    if r['temp'] > median_temp and r['hum'] > median_hum
]

# Real signal processor: compute weighted health index
weights = {'temp': 0.4, 'vib': 0.35, 'freq': 0.25}

# Function to process filtered sensor data
def process_readings(readings):
    if not readings:
        return 0.0
    composite_scores = []
    for r in readings:
        # Normalize each metric to ideal baseline
        temp_norm = abs(r['temp'] - 72.0) / 72.0
        vib_norm = r['vib'] / 0.25
        freq_norm = abs(r['freq'] - 60.0) / 60.0
        # Weighted anomaly score (lower = better)
        score = 100 * (
            weights['temp'] * temp_norm + 
            weights['vib'] * vib_norm + 
            weights['freq'] * freq_norm
        )
        composite_scores.append(score)
    # Return inverse of average anomaly (health metric)
    avg_anomaly = sum(composite_scores) / len(composite_scores)
    return int(1000 - avg_anomaly)

# Misdirection: complex itertools usage with no impact
cyclic_patterns = list(cycle(['A', 'B', 'C']))[:10]
combo_pairs = list(combinations(['base', 'aux', 'meta'], 2))

# Final computation — this is the key statement
final_diagnostic = process_readings(filtered_data)

# Output result as required
print(f"Target result: {final_diagnostic}")