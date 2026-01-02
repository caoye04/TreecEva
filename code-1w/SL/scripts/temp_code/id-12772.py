from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_log = [
    'ERROR: disk_usage=95%, cpu_temp=80',
    'INFO: disk_usage=60%, cpu_temp=55',
    'WARNING: disk_usage=82%, cpu_temp=70',
    'ERROR: disk_usage=98%, cpu_temp=85',
    'INFO: disk_usage=40%, cpu_temp=45'
]

# Parse logs and extract numeric values
disk_usages = []
cpu_temps = []
for entry in telemetry_log:
    if 'disk_usage' in entry:
        start = entry.find('disk_usage=') + 11
        end = entry.find('%', start)
        disk_usages.append(float(entry[start:end]))
    if 'cpu_temp' in entry:
        start = entry.find('cpu_temp=') + 9
        cpu_temps.append(float(entry[start:start+2]))

# Irrelevant string processing - red herring
log_strings = [entry.upper().replace(':', ';') for entry in telemetry_log]
segment_parts = []
for s in log_strings:
    segment_parts.extend(s.split(';'))
keyword_count = Counter([word for word in segment_parts if len(word) > 4])

# Decoy statistical analysis (never used later)
avg_disk = sum(disk_usages) / len(disk_usages)
median_cpu = sorted(cpu_temps)[len(cpu_temps)//2]
max_temp = max(cpu_temps)

# Real computation begins: performance metric transformation
baseline_config = {
    'threshold': 80.0,
    'weight_factor': 0.35,
    'decay_rate': 0.9,
    'history_limit': 3
}

metrics = defaultdict(float)
for i, usage in enumerate(disk_usages):
    severity = max(0, usage - baseline_config['threshold'])
    time_weight = baseline_config['decay_rate'] ** (len(disk_usages) - i - 1)
    metrics['anomaly_score'] += severity * time_weight

# Add auxiliary metrics with distractions
fake_metrics = {}
for key in ['a', 'b', 'c', 'd']:
    fake_metrics[key] = (ord(key) * 2) % 7  # Dead code path

# String-based control flow decoy
temp_band = ''
if max(cpu_temps) > 75:
    temp_band = 'CRITICAL'
elif max(cpu_temps) > 65:
    temp_band = 'ELEVATED'
else:
    temp_band = 'NORMAL'

# Distractor: unused complex calculation
system_stress = 0
for t in cpu_temps:
    system_stress += math.log(t + 1) * 1.5

# Actual signal extraction via slicing and filtering
event_severity = [s for s in disk_usages if s > baseline_config['threshold']]
if len(event_severity) == 0:
    base_impact = 0
else:
    base_impact = sum(event_severity) / len(event_severity)

# Complex multi-step transformation with embedded logic
rolling_adjustment = 1.0
correction_history = []
for i in range(len(disk_usages)):
    if i > 0 and disk_usages[i] > disk_usages[i-1]:
        rolling_adjustment *= 0.92
    correction_history.append(rolling_adjustment)

# Final processing with tuple unpacking distraction
aux_data = [(1, 2), (3, 4), (5, 6)]
for x, y in aux_data:
    _ = x ** y  # Unused computation

# Core algorithm: weighted anomaly aggregation
def process_performance(metrics_dict, config):
    raw_score = metrics_dict['anomaly_score']
    adjustment = config['weight_factor'] * (1 + len(correction_history[-config['history_limit']:]))
    
    # Apply nonlinear transformation
    if raw_score > 50:
        processed = raw_score * adjustment * 0.7
    elif raw_score > 20:
        processed = raw_score * adjustment
    else:
        processed = raw_score * adjustment * 1.2
    
    # Final clamping and rounding
    processed = max(10, min(processed, 950))
    return round(processed)

# Introduce misleading alternate result path (unused)
tentative_result = sum([int(baseline_config['weight_factor'] * 100), len(telemetry_log)])

# Critical execution point
final_score = process_performance(metrics, baseline_config)

# Output the target result
print(f"Result: {final_score}")