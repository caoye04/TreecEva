import math

def analyze_signal_strength(signal):
    if not signal:
        return 0
    peak = max(signal)
    avg = sum(signal) / len(signal)
    normalized_peak = peak / (avg + 1e-9)
    return int(normalized_peak)


def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Irrelevant helper (dead path)
def compress_sequence(seq):
    result = []
    for x in seq:
        if x not in result:
            result.append(x)
    return result

# Unused transformation function
def shift_cipher(text, key=3):
    return ''.join(chr((ord(c) - 97 + key) % 26 + 97) if c.islower() else c for c in text)

# Misleading diagnostic flag (red herring)
legacy_mode_active = False
emergency_override = True

# Simulated system log data with mixed types
log_data = [
    {'timestamp': 1001, 'level': 'INFO', 'value': 45, 'source': 'sensor_A'},
    {'timestamp': 1003, 'level': 'WARN', 'value': 67, 'source': 'sensor_B'},
    {'timestamp': 1005, 'level': 'INFO', 'value': 23, 'source': 'sensor_A'},
    {'timestamp': 1008, 'level': 'ERROR', 'value': 91, 'source': 'sensor_C'},
    {'timestamp': 1010, 'level': 'INFO', 'value': 55, 'source': 'sensor_B'},
]

# System thresholds (some are decoys)
system_thresholds = {
    'critical': 85,
    'warning': 60,
    'info_floor': 20,
    'legacy_limit': 77,  # unused
    'peak_response_cap': 1000  # red herring
}

# Auxiliary computation (partially relevant)
signal_chain = [45, 67, 23, 91, 55]
analyzed_strength = analyze_signal_strength(signal_chain)

# Entropy analysis on levels
log_levels = [entry['level'] for entry in log_data]
level_entropy = compute_entropy(log_levels)  # constant due to fixed input

# Decoy set operations
active_sources = {entry['source'] for entry in log_data}
target_sources = {'sensor_A', 'sensor_B', 'sensor_C', 'sensor_D'}
redundant_intersection = active_sources & target_sources
expansion_check = active_sources | {'sensor_X', 'sensor_Y'}

# Conditional expression with distractor logic
mode_flag = 'enhanced' if len(active_sources) > 2 and not legacy_mode_active else 'basic'

# Linear search for highest value entry (relevant)
max_entry = None
for entry in log_data:
    if max_entry is None or entry['value'] > max_entry['value']:
        max_entry = entry

# Extract critical value
highest_value = max_entry['value'] if max_entry else 0

# Compute average value (used later)
avg_value = sum(entry['value'] for entry in log_data) / len(log_data)

# Simulated calibration offset (distractor)
calibration_map = {k: v * 1.05 for k, v in system_thresholds.items()}
adjusted_critical = calibration_map['critical']

# Bit manipulation decoy
event_flags = 0
for entry in log_data:
    if entry['level'] == 'ERROR':
        event_flags |= 1 << 2
    elif entry['level'] == 'WARN':
        event_flags |= 1 << 1

# Unused flag propagation
if event_flags & 4:
    emergency_override = True

# Core processing function
def process_metrics(logs, thresholds):
    values = [entry['value'] for entry in logs]
    
    # Metrics
    mean_val = sum(values) / len(values)
    above_critical = len([v for v in values if v > thresholds['critical']])
    above_warning = len([v for v in values if v > thresholds['warning']])
    
    # Set-based filtering
    high_readings = {v for v in values if v > thresholds['warning']}
    mid_readings = {v for v in values if thresholds['info_floor'] <= v <= thresholds['warning']}
    
    # Conditional expression tree
    severity_score = (
        3 if above_critical > 0 else
        2 if above_warning > 1 else
        1 if above_warning == 1 else
        0
    )
    
    # Composite diagnostic index
    stability_factor = len(values) / (len(high_readings) + 1)
    entropy_component = compute_entropy([v // 10 for v in values])  # bucketed
    
    # Final formula (combines multiple concepts)
    raw_diagnostic = (
        (mean_val * stability_factor) + 
        (severity_score * 10) - 
        (entropy_component * 5)
    )
    
    # Final adjustment
    return int(round(raw_diagnostic))

# Execute main logic
final_diagnostic = process_metrics(log_data, system_thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")