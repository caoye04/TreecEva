def process_entry(entry):
    # Irrelevant transformation
    clean_entry = entry.strip().lower().replace(' ', '_')
    parts = clean_entry.split(':')
    if len(parts) < 2:
        return None

    key, value_str = parts[0], parts[1]
    
    # Misleading conversion path
    temp_value = 0
    for c in value_str:
        if c.isdigit():
            temp_value = temp_value * 10 + int(c)
    
    # Decoy logic: looks important but unused later
    if 'error' in key:
        temp_value += 100
    elif 'warning' in key:
        temp_value += 50

    return (key, temp_value)

# Dead function - never called
def legacy_parse(log_data):
    count = 0
    for line in log_data:
        if 'deprecated' in line:
            count += 1
    return count

# Unused helper with red herring logic
def compute_health_score(raw_values):
    total = sum(raw_values)
    penalty = 0
    for v in raw_values:
        if v > 200:
            penalty += v // 10
    return total - penalty  # Never used

# Simulated system log with structured noise
system_log_raw = [
    'timestamp: 1678901234',
    'cpu_load: 76',
    'mem_usage: 432',
    'disk_io: 189',
    'network_rx: 945',
    'temp_core: 67',
    'fan_speed: 2300',
    'error_count: 3',
    'processes: 128'
]

# Parse log into structured data using relevant logic
system_log = []
for line in system_log_raw:
    parsed = process_entry(line)
    if parsed:
        system_log.append(parsed)

# Thresholds for diagnostics - some are decoys
thresholds = {
    'cpu_load': 80,
    'mem_usage': 500,
    'disk_io': 200,
    'network_rx': 1000,
    'temp_core': 70,
    'fan_speed': 3000,
    'irrelevant_metric': 999  # Unused threshold
}

# Secondary distraction: build auxiliary map that isn't fully used
metric_units = {}
for key, _ in system_log:
    if key == 'cpu_load':
        metric_units[key] = '%'
    elif 'mem' in key:
        metric_units[key] = 'MB'
    elif 'speed' in key:
        metric_units[key] = 'RPM'
    else:
        metric_units[key] = 'unit'  # Generic fallback

# Core diagnostic logic buried in distractions
active_alerts = 0
marginal_readings = 0
primary_metrics = ['cpu_load', 'mem_usage', 'temp_core']  # Key subset

# Real processing begins here — 3 levels of nesting
for key, value in system_log:
    if key in thresholds:
        threshold_val = thresholds[key]
        if value > threshold_val:
            active_alerts += 1
        elif value > threshold_val * 0.9:
            marginal_readings += 1  # Near-threshold detection

        # Bit manipulation red herring
        bit_analysis = (value ^ threshold_val) & 0xF
        if bit_analysis > 10:
            # This block runs but doesn't affect outcome
            dummy_flag = True

# Another layer of misdirection: transform logs via string ops
serialized_diagnostics = []
for entry in system_log:
    serial_key = ''.join([c.upper() for c in entry[0] if c in 'aeiou'])  # Useless compression
    if serial_key:
        serialized_diagnostics.append(f"{serial_key}:{entry[1] % 25}")

# Critical computation hidden among noise
base_score = 100
base_score -= active_alerts * 15
base_score -= marginal_readings * 5

# Final nonlinear adjustment using logical and arithmetic ops
if active_alerts == 0:
    stability_bonus = 20
    if marginal_readings == 0:
        stability_bonus += 10
    base_score += stability_bonus
elif base_score < 50:
    # Severe degradation path — not triggered
    base_score = max(base_score, 30)

# Destructuring fake-out
*top_tier, last_critical = [x[0] for x in system_log if x[0] in thresholds]

# The real answer computation
final_diagnostic = 0
for key, value in system_log:
    if key in primary_metrics:
        threshold = thresholds[key]
        deviation = abs(value - threshold)
        final_diagnostic += deviation * (1 if value <= threshold else -1)

# Print required result
print(f"Result: {final_diagnostic}")