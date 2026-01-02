import itertools

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 21.4, 20.9]
humidity_readings = [45, 52, 58, 61, 48, 55, 60, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1008, 1014, 1016]

# Irrelevant auxiliary metrics (distractor data)
sound_levels = [32, 41, 38, 55, 60, 43, 37, 40]  # Decoy sensor data
light_intensity = [800, 950, 1100, 1200, 700, 650, 1000, 880]  # Not used in logic

# Mapping of station IDs to calibration thresholds (dictionary operation)
threshold_map = {
    'S01': {'temp': 24.0, 'humidity': 55},
    'S02': {'temp': 23.5, 'humidity': 50},
    'S03': {'temp': 22.0, 'humidity': 58},
    'S04': {'temp': 25.0, 'humidity': 60}
}

# Misleading transformation: creates unused composite index
composite_index = []
for t, h, p in zip(temperature_readings, humidity_readings, pressure_readings):
    index_val = (t * 0.5) + (h * 0.3) + (p * 0.001)
    composite_index.append(round(index_val, 2))

# Dead code path: never invoked function (red herring)
def analyze_acoustic_patterns(data):
    return sum(x ** 0.5 for x in data if x > 40)

# Real processing begins: filter stations based on temperature deviation
active_stations = []
stale_markers = [False] * len(temperature_readings)
for i, temp in enumerate(temperature_readings):
    if abs(temp - 22.5) <= 3.0:  # Valid range around baseline
        active_stations.append(i)
    else:
        stale_markers[i] = True  # Mark as stale (unused later)

# Apply dual-condition filtering using logical short-circuiting
filtered_data = []
for idx in active_stations:
    temp = temperature_readings[idx]
    humid = humidity_readings[idx]
    valid_conditions = (
        (temp >= 20.0 and humid <= 60) or
        (temp < 20.0 and humid > 55 and idx % 2 == 0)
    )
    if valid_conditions:  # Early inclusion based on relaxed criteria
        filtered_data.append({'index': idx, 't': temp, 'h': humid})

# Unused list comprehension with bit manipulation distraction
shifted_flags = [((h << 1) & 255) ^ 17 for h in humidity_readings]

# Core diagnostic engine with dictionary and itertools usage
def process_readings(readings, thresholds):
    if not readings:
        return -1
    
    # Generate all pairwise combinations to simulate interference analysis
    combos = list(itertools.combinations(readings, 2))
    total_drift = 0.0
    
    for pair in combos:
        a, b = pair[0], pair[1]
        t_diff = abs(a['t'] - b['t'])
        h_diff = abs(a['h'] - b['h'])
        total_drift += (t_diff * 1.5) + (h_diff * 0.8)
    
    # Aggregate by simulated station key mapping
    station_keys = list(thresholds.keys())
    cumulative_score = 0
    
    for entry in readings:
        # Map index to station via modulo (simulated assignment)
        station_key = station_keys[entry['index'] % len(station_keys)]
        t_ref = thresholds[station_key]['temp']
        h_ref = thresholds[station_key]['humidity']
        
        # Compute deviation score
        t_dev = abs(entry['t'] - t_ref)
        h_dev = abs(entry['h'] - h_ref)
        cumulative_score += int(t_dev + h_dev)
    
    # Final diagnostic is combination of drift and deviation
    final_value = int(total_drift) + cumulative_score
    
    # Insert irrelevant mutation (dead operation)
    _ = [x * 1.05 for x in readings if 'extra' in x]  # No effect
    
    return final_value

# Execute main computation
baseline_check = sum(1 for t in temperature_readings if t > 25)  # Distractor count

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")