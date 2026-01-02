def analyze_system_load(loads, threshold=75):
    """Irrelevant helper function – never called."""
    return [load for load in loads if load > threshold]

# Distractor: Unused but plausible data structures
temporary_cache = [0] * 200
redundant_map = {i: i * 2 for i in range(50)}
backup_logs = [(x, x % 10) for x in range(100)]

# Core data – subtle initialization
log_entries = [
    {'timestamp': 1, 'cpu': 60, 'mem': 40, 'disk': 80},
    {'timestamp': 2, 'cpu': 85, 'mem': 55, 'disk': 60},
    {'timestamp': 3, 'cpu': 70, 'mem': 90, 'disk': 30},
    {'timestamp': 4, 'cpu': 90, 'mem': 88, 'disk': 75}
]

system_thresholds = {'cpu': 80, 'mem': 85, 'disk': 70}

# Decoy function – looks important but unused
def generate_health_report(data):
    stats = {}
    for k in ['cpu', 'mem', 'disk']:
        values = [entry[k] for entry in data]
        stats[k] = {
            'avg': sum(values) / len(values),
            'peak': max(values),
            'alerts': len([v for v in values if v > 80])
        }
    return stats

# Red herring: complex-looking but dead code path
class DiagnosticEngine:
    def __init__(self):
        self.version = '2.1'
        self.active = False  # Never activated

    def run_diagnostics(self, entries):
        return sum(len(str(e)) for e in entries) % 1000

engine = DiagnosticEngine()

# Irrelevant transformation chain
shadow_copy = []
for idx, entry in enumerate(log_entries):
    temp = entry.copy()
    temp['index_offset'] = idx * 2 + 1
    shadow_copy.append(temp)

# Unused accumulator
phantom_total = 0
for i in range(len(shadow_copy)):
    phantom_total += shadow_copy[i]['index_offset']

# Key processing logic buried in distractions
def evaluate_anomaly(entry, thresholds):
    anomalies = 0
    for resource, value in entry.items():
        if resource in thresholds and value > thresholds[resource]:
            anomalies += 1
    return anomalies > 1  # Critical condition: more than one over threshold

# Secondary red herring: string manipulation with no impact
dummy_tags = []
for entry in log_entries:
    tag = ''
    for k, v in entry.items():
        if isinstance(v, int) and v % 25 == 0:
            tag += k[0].upper()
    dummy_tags.append(tag)

decoded_sequence = ''.join(sorted(set(''.join(dummy_tags))))

# Real logic begins here – masked by prior noise
def extract_critical_flags(entries):
    flags = []
    for entry in entries:
        flag_value = 0
        if entry['cpu'] > 85:
            flag_value |= 1
        if entry['mem'] > 85:
            flag_value |= 2
        if entry['disk'] > 85:
            flag_value |= 4
        flags.append(flag_value)
    return flags

# Accumulate severity scores – relevant but obscured
severity_pool = []
for entry in log_entries:
    severity = 0
    if entry['cpu'] > system_thresholds['cpu']:
        severity += 3
    if entry['mem'] > system_thresholds['mem']:
        severity += 4
    if entry['disk'] > system_thresholds['disk']:
        severity += 2
    severity_pool.append(severity)

# Real signal: count entries with multiple threshold breaches
multi_breach_count = 0
for entry in log_entries:
    breach_count = 0
    for key in ['cpu', 'mem', 'disk']:
        if key in system_thresholds and entry[key] > system_thresholds[key]:
            breach_count += 1
    if breach_count >= 2:
        multi_breach_count += 1

# Misleading intermediate: looks like final result
preliminary_score = sum(severity_pool) * len([f for f in extract_critical_flags(log_entries) if f > 0])

# Another decoy: uses enumerate and zip but irrelevant
enumerated_pairs = list(enumerate(zip(log_entries, severity_pool)))
summary_hash = 0
for i, (entry, score) in enumerated_pairs:
    summary_hash += i * (entry['timestamp'] ^ score)

# Actual core computation – combines multiple concepts
baseline = 100
adjustment_factor = 0.75

# Data transformation using tuple unpacking and filtering
filtered_with_index = []
for i, entry in enumerate(log_entries):
    if entry['cpu'] > 70 or entry['mem'] > 70:
        filtered_with_index.append((i, entry))

# Use of zip to align indices and severity
indices, filtered_entries = zip(*filtered_with_index) if filtered_with_index else ([], [])
linked_severities = [severity_pool[i] for i in indices]

# Final metric calculation – depends on multiple steps
aggregate_risk = sum(linked_severities)
context_weight = len(filtered_entries) + multi_breach_count

# Hidden logic: correction based on specific pattern
pattern_match = 0
for entry in filtered_entries:
    if entry['cpu'] > 80 and entry['mem'] < 90:
        pattern_match += 1

# The real answer derivation – non-obvious due to distractions
base_diagnostic = aggregate_risk * context_weight
if pattern_match >= 2:
    base_diagnostic -= 50
else:
    base_diagnostic += 20

# Final adjustment using bitwise and arithmetic
flag_set = extract_critical_flags(log_entries)
critical_flag_count = len([f for f in flag_set if f & 3])  # Checks CPU or MEM critical

final_diagnostic = base_diagnostic + (critical_flag_count * 15)

# Print required output
print(f"Result: {final_diagnostic}")