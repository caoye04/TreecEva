from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 45, 'status': 'active'},
    {'sensor': 'pressure', 'value': 1013, 'status': 'active'},
    {'sensor': 'temp', 'value': 47, 'status': 'active'},
    {'sensor': 'vibration', 'value': 88, 'status': 'warning'},
    {'sensor': 'pressure', 'value': 1015, 'status': 'active'},
    {'sensor': 'temp', 'value': 44, 'status': 'active'},
    {'sensor': 'vibration', 'value': 95, 'status': 'warning'},
    {'sensor': 'temp', 'value': 50, 'status': 'critical'}
]

# Irrelevant statistical tracker (distractor)
class DistributionTracker:
    def __init__(self):
        self.history = []
        self.moments = defaultdict(float)

    def update(self, x):
        self.history.append(x)
        n = len(self.history)
        if n > 0:
            self.moments['mean'] = sum(self.history) / n
            self.moments['variance'] = sum((x - self.moments['mean'])**2 for x in self.history) / n

# Unused function (red herring)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data)) ** 0.5
    return [(x - mean_val) / (std_dev + 1e-8) for x in data]

# Misleading intermediate calculation (dead path)
redundant_aggregate = 0
for entry in telemetry_stream:
    redundant_aggregate += entry['value'] * 0.1
    if entry['status'] == 'critical':
        redundant_aggregate -= 5  # Distracting adjustment

# Real processing begins here
status_priority = {'active': 1, 'warning': 2, 'critical': 3}
sensor_readings = defaultdict(list)
alert_levels = defaultdict(int)

for entry in telemetry_stream:
    sensor = entry['sensor']
    value = entry['value']
    status = entry['status']
    sensor_readings[sensor].append(value)
    alert_levels[status] += 1

# Compute rolling thresholds (partially relevant)
rolling_avg = {}
for sensor, values in sensor_readings.items():
    rolling_avg[sensor] = sum(values[-3:]) / min(3, len(values))

# Decoy dictionary transformation (irrelevant)
decoy_map = {k: int(math.sqrt(v[-1]) * 2) for k, v in sensor_readings.items() if v}

# Conditional logic chain with embedded key computation
system_health = 100
for status, count in alert_levels.items():
    if status == 'warning':
        system_health -= count * 5
    elif status == 'critical':
        system_health -= count * 15

# Bit manipulation distraction
temp_bitmask = 0
for val in sensor_readings.get('temp', []):
    temp_bitmask ^= (val << 1) | (val & 1)

# Dictionary-based rule engine (core logic)
rules_engine = {
    'high_temp': lambda x: any(v > 48 for v in x),
    'rising_pressure': lambda x: len(x) > 1 and x[-1] > x[0],
    'unstable_vibration': lambda x: max(x) - min(x) > 20 if len(x) > 1 else False
}

# Rule evaluation with short-circuiting (key step)
evaluation_trace = {}
for name, rule in rules_engine.items():
    readings = sensor_readings.get(name.split('_')[-1], [])
    evaluation_trace[name] = rule(readings) if readings else False

# Recursive depth simulation (distractor)
def calculate_entropy(values, depth=0):
    if depth >= 2 or not values:
        return 0.0
    probs = Counter(values).values()
    total = sum(probs)
    entropy = -sum((p / total) * math.log2(p / total) for p in probs if p > 0)
    return entropy + calculate_entropy([p // 2 for p in probs if p > 1], depth + 1)

entropy_score = calculate_entropy(list(alert_levels.values()))

# Core diagnostic logic
primary_flags = sum(1 for outcome in evaluation_trace.values() if outcome)

# Secondary health modifier
if alert_levels.get('critical', 0) > 0:
    primary_flags *= 2

# Final analysis function
def analyze_metrics(state):
    base = state['health']
    flags = state['flags']
    # Critical threshold check
    if any(v > 49 for v in state['readings']['temp']):
        adjustment = -20
    else:
        adjustment = 0
    # Nested conditional with tuple unpacking
    multipliers = [1.0, 1.2, 1.5]
    severity_level = min(flags, 3)
    scaling_factor = multipliers[severity_level - 1] if severity_level > 0 else 1.0
    
    # Complex but ultimately irrelevant bitwise component (distraction)
    magic_offset = 0
    for i, val in enumerate(state['readings']['pressure']):
        magic_offset += (val ^ (i * 3)) & 7
    
    intermediate = (base - abs(adjustment)) * scaling_factor
    # Final non-linear transformation
    result = int(intermediate + math.cos(magic_offset) * 2)
    return result

# Assemble system state
system_state = {
    'health': system_health,
    'flags': primary_flags,
    'readings': dict(sensor_readings),
    'timestamp': '2023-12-05T10:30:00Z'
}

# Execute critical statement
final_diagnostic = analyze_metrics(system_state)
print(f"Target result: {final_diagnostic}")