from collections import defaultdict, Counter

# Simulated system telemetry data
timestamps = [100, 101, 102, 105, 107, 110, 115, 120]
raw_readings = [23.5, 24.1, 25.3, 26.0, 25.8, 27.2, 28.0, 29.1]
status_flags = ['OK', 'OK', 'WARN', 'OK', 'OK', 'ALERT', 'ALERT', 'OK']

# Irrelevant auxiliary data (distractor)
device_inventory = {'sensor_A': 1, 'sensor_B': 0, 'sensor_C': 1, 'sensor_D': 1}
redundant_map = {i: chr(65 + (i % 26)) for i in range(50)}
shadow_buffer = [x ** 0.5 for x in range(100, 110)]

# Misleading intermediate computation (dead path)
event_risk_score = 0
for flag in status_flags:
    if flag == 'ALERT':
        event_risk_score += 3
    elif flag == 'WARN':
        event_risk_score += 1

# Unused function (red herring)
def analyze_redundancy(buffer):
    return sum(b % 7 for b in buffer if b > 102)

# Real processing begins here
log_entries = list(zip(timestamps, raw_readings, status_flags))
system_thresholds = {
    'high_temp': 27.0,
    'spike_delta': 1.8,
    'stability_window': 3
}

# Decoy statistical summary (irrelevant)
mean_reading = sum(raw_readings) / len(raw_readings)
variance_proxy = sum((x - mean_reading) ** 2 for x in raw_readings)

def detect_spikes(readings, delta):
    spikes = []
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) >= delta:
            spikes.append(i)
    return spikes

# Another red herring: unused spike detection
spike_indices = detect_spikes(raw_readings, system_thresholds['spike_delta'])

# Core logic wrapped in distraction
config_modes = lambda x: 'A' if x < 26 else 'B' if x < 28 else 'C'
mode_distribution = Counter(config_modes(temp) for temp in raw_readings)

# Distractor: nested dictionary aggregation with no impact
summary_grid = defaultdict(lambda: defaultdict(int))
for ts, temp, flag in log_entries:
    bucket = 'day' if ts < 110 else 'night'
    category = 'stable' if flag == 'OK' else 'unstable'
    summary_grid[bucket][category] += 1

# Actual critical computation chain
window = system_thresholds['stability_window']
stability_violations = 0
for i in range(window, len(raw_readings)):
    window_avg = sum(raw_readings[i - window:i]) / window
    if raw_readings[i] > system_thresholds['high_temp'] and raw_readings[i] > window_avg * 1.1:
        stability_violations += 1

# Secondary condition using bitwise logic (relevant but obscured)
alert_count = status_flags.count('ALERT')
warning_count = status_flags.count('WARN')
security_lock = (alert_count << 2) ^ warning_count  # Bit manipulation red herring?

# Final diagnostic depends only on stability violations and threshold crossings
temp_exceedances = sum(1 for r in raw_readings if r > system_thresholds['high_temp'])

# Key assignment - this is where answer is determined
critical_load = temp_exceedances * 100 + stability_violations * 50

# Final processing function with decoys inside
def process_metrics(entries, thresholds):
    # Unused local structure
    temp_registry = defaultdict(list)
    for t, val, flag in entries:
        temp_registry[flag].append(val)
    
    # Real work hidden among distractions
    high_temp_count = sum(1 for _, val, _ in entries if val > thresholds['high_temp'])
    
    # Recompute stability violations (should match outer scope)
    readings = [val for _, val, _ in entries]
    window = thresholds['stability_window']
    violations = 0
    for i in range(window, len(readings)):
        avg = sum(readings[i - window:i]) / window
        if readings[i] > thresholds['high_temp'] and readings[i] > avg * 1.1:
            violations += 1
    
    # Correct diagnostic formula
    result = high_temp_count * 100 + violations * 50
    
    # Dead assignment (misleads via naming)
    final_integrity_score = result - (len(spike_indices) * 10)  # Not used
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Result: {final_diagnostic}")