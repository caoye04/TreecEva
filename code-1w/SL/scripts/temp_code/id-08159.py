from collections import defaultdict, Counter

# Simulate system telemetry data
telemetry_logs = [
    'ERROR: disk full', 'INFO: user login', 'WARNING: high latency',
    'ERROR: timeout', 'INFO: file saved', 'WARNING: low memory',
    'ERROR: disk full', 'INFO: user logout', 'WARNING: high latency'
]

# Parse logs into structured form
log_data = defaultdict(list)
error_count = 0
priority_flags = [False, True, False]

for log in telemetry_logs:
    level, message = log.split(': ', 1)
    log_data[level].append(message)
    if level == 'ERROR':
        error_count += 1

# Irrelevant statistical summary (distractor)
summary_stats = {}
for k, v in log_data.items():
    summary_stats[k] = len(v) ** 0.5

# Simulate sensor array with bit-flip noise (red herring)
sensor_readings = [0b1101, 0b1011, 0b1110, 0b0111]
filtered_sensors = []
for val in sensor_readings:
    flipped = ((val >> 1) & 0b111) | ((val & 1) << 3)
    filtered_sensors.append(flipped ^ 0b1010)

# Unused recursive function (dead code path)
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n-1) + calculate_depth(n-2)

# Real processing begins: extract metrics from logs
metric_keys = ['errors', 'warnings', 'info_events']
metrics = {}
metrics['errors'] = len(log_data.get('ERROR', []))
metrics['warnings'] = len(log_data.get('WARNING', []))
metrics['info_events'] = len(log_data.get('INFO', []))

# Additional derived metric with slicing distraction
distinct_issues = list(set(log_data.get('WARNING', [])))
metrics['unique_warnings'] = len(distinct_issues[::2])  # every other unique warning

# Weight configuration for evaluation (misleading alternate weights below)
weights = {'errors': -2.0, 'warnings': -1.5, 'info_events': 0.8}
alt_weights = {'errors': -1.0, 'warnings': -0.5}  # decoy

# Auxiliary calculation with zip and enumerate (partially relevant)
temp_adjustments = [0.1, -0.2, 0.3]
for i, adj in enumerate(temp_adjustments):
    if i % 2 == 0:
        weights['info_events'] += adj

# Core evaluation logic
performance_contributions = []
for key in metric_keys:
    if key in weights:
        performance_contributions.append(metrics[key] * weights[key])

# Final aggregation using multiple steps
raw_total = sum(performance_contributions)
normalization_factor = max(1.0, metrics['errors'])
adjusted_total = raw_total / normalization_factor

# Secondary adjustment based on unique warnings threshold
if metrics['unique_warnings'] >= 1:
    adjusted_total -= 0.5

# Critical assignment statement
final_score = int(round(adjusted_total * 10))

# Output result as required
print(f"Result: {final_score}")