from collections import defaultdict, Counter

# Simulated thermal sensor array data processing
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
base_temperatures = [23.5, 24.1, 22.8, 25.6, 26.3]
fluctuation_pattern = [0.3, -0.2, 0.5, -0.4, 0.6]

# Irrelevant auxiliary mapping (distractor)
status_codes = {'OK': 200, 'WARN': 302, 'ERROR': 500}
code_lookup = {v: k for k, v in status_codes.items()}

# Generate synthetic thermal readings over 6 time steps
thermal_readings = []
for t in range(6):
    step_reading = []
    for i in range(len(sensor_ids)):
        # Physics-based fluctuation model (partially relevant)
        variation = fluctuation_pattern[i] * (t % 3) ** 0.5 if t > 0 else 0
        measured = round(base_temperatures[i] + variation + (0.1 * t), 2)
        step_reading.append(measured)
    thermal_readings.append(step_reading)

# Dead code path - never called (red herring)
def deprecated_analysis(data):
    return sum(sum(row) for row in data) / (len(data) * len(data[0]))

# Auxiliary statistical tracker (misleading intermediate)
avg_tracker = []
for reading in thermal_readings:
    avg_tracker.append(round(sum(reading) / len(reading), 2))

# Decoy function that looks important but isn't used
def compute_thermal_gradient(seq):
    if len(seq) < 2:
        return 0
    return round((seq[-1] - seq[0]) / len(seq), 3)

# Real processing begins here — pattern analyzer
reliability_score = 0
for reading in thermal_readings:
    for temp in reading:
        if temp > 25.0:
            reliability_score += 1

# Bit manipulation mask for sensor anomaly detection (hybrid logic)
sensor_mask = 0b11111
anomaly_filter = 0b10101
active_sensors = sensor_mask & ~anomaly_filter  # Result: 0b01010

# Destructuring with irrelevant components
primary_nodes = ['S1', 'S3', 'S5']
backup_nodes = ['S2', 'S4']
selected_primary, _, selected_backup = primary_nodes[0], primary_nodes[1], backup_nodes[1]

# Core pattern analysis with string-derived condition (unique mix)
def analyze_pattern(readings):
    # Use of string method on encoded state (required feature)
    system_state = "normal,caution,alert,critical"
    states = system_state.split(',')
    threshold_level = len(states[1])  # 'caution' -> length 6
    
    # Frequency counting of high-temp events (collections.Counter)
    hot_events = []
    for step in readings:
        for idx, val in enumerate(step):
            if val > 25.0:
                hot_events.append(sensor_ids[idx])
    
    event_count = Counter(hot_events)
    
    # Secondary filter using defaultdict (required feature)
    severity_map = defaultdict(int)
    for sensor, count in event_count.items():
        if count >= threshold_level - 3:  # threshold_level=6 → 3
            severity_map[sensor] = count * 100
    
    # Control flow with nested conditions and bit logic
    diagnostic = 0
    for i, sensor in enumerate(sensor_ids):
        base = base_temperatures[i]
        # Key logic embedded in complex condition
        if base > 24.0 and severity_map[sensor] > 0:
            # Bitwise inclusion check
            if (active_sensors >> i) & 1:
                diagnostic += severity_map[sensor] >> 2
            else:
                diagnostic += 10
        elif base <= 24.0:
            diagnostic -= (i + 1) * 2
    
    # Final adjustment based on pattern symmetry (hidden rule)
    first_avg = sum(thermal_readings[0]) / len(thermal_readings[0])
    last_avg = sum(thermal_readings[-1]) / len(thermal_readings[-1])
    if abs(last_avg - first_avg) > 1.0:
        diagnostic = int(diagnostic * 1.1)
    
    return diagnostic

# Execution point of interest
final_diagnostic = analyze_pattern(thermal_readings)

# Print required result
print(f"Target result: {final_diagnostic}")