from collections import Counter, defaultdict
import math

# Simulated system telemetry data
telemetry_stream = [
    'ERROR: disk_usage HIGH',
    'INFO: cpu_temp NORMAL',
    'WARNING: memory_load ELEVATED',
    'ERROR: disk_usage HIGH',
    'INFO: network_io STABLE',
    'WARNING: memory_load ELEVATED',
    'ERROR: cpu_temp HIGH',
    'INFO: disk_usage NORMAL'
]

# Irrelevant transformation - distractor
buffer_map = defaultdict(int)
for entry in telemetry_stream:
    tokens = entry.split(': ')
    if len(tokens) > 1:
        buffer_map[tokens[0]] += 1

# Misleading diagnostic chain
raw_counts = Counter([entry.split()[-1] for entry in telemetry_stream])
status_weights = {'NORMAL': 1, 'STABLE': 1, 'ELEVATED': 3, 'HIGH': 5}
weighted_score = sum(status_weights.get(k, 0) * v for k, v in raw_counts.items())

# Decoy function - never called
def analyze_health_snapshot(data):
    return sum(len(x) for x in data) % 7

# Another red herring: complex but unused calculation
token_frequency = {}
for entry in telemetry_stream:
    for token in entry.replace(':', ' ').split():
        token_frequency[token] = token_frequency.get(token, 0) + 1

# Relevant data extraction
log_data = [line for line in telemetry_stream if 'ERROR' in line]

# System flags with bitfield encoding (only some bits matter)
system_flags = 0b1101  # Bit 0: disk, Bit 1: memory, Bit 2: cpu, Bit 3: network
active_alerts = bin(system_flags).count('1')

# Distractor: fake priority matrix
priority_matrix = [[i * j for j in range(4)] for i in range(4)]
impact_factor = 0
for row in priority_matrix:
    for val in row:
        impact_factor += val % 3

# Auxiliary irrelevant logic: string case manipulation
capitalized_logs = [log.upper().replace(' ', '_') for log in telemetry_stream]
dummy_hash = sum(ord(c) for c in ''.join(capitalized_logs)) % 19

# Core processing function
def process_metrics(errors, flags):
    error_count = len(errors)
    
    # Extract relevant bit flags (only first 3 bits are meaningful)
    disk_alert = flags & 0b0001
    mem_alert = (flags >> 1) & 0b0001
    cpu_alert = (flags >> 2) & 0b0001
    
    # Real logic: count how many error types match active alerts
    error_types = set()
    for e in errors:
        if 'disk' in e: error_types.add('disk')
        if 'memory' in e: error_types.add('memory')
        if 'cpu' in e: error_types.add('cpu')
    
    matched = 0
    if 'disk' in error_types and disk_alert: matched += 1
    if 'memory' in error_types and mem_alert: matched += 1
    if 'cpu' in error_types and cpu_alert: matched += 1
    
    # Secondary computation: severity multiplier
    severity = 0
    for err in errors:
        if 'HIGH' in err:
            severity += 2
    
    # Final diagnostic formula
    base = error_count * 100
    bonus = matched * 50
    penalty = severity * 10
    return base + bonus - penalty

# Dead code path - looks important but unused
def compute_system_stability_index(seq):
    freq = Counter(seq)
    return math.log(sum(freq.values()) + 1) * 100

# Critical execution point
final_diagnostic = process_metrics(log_data, system_flags)
print(f"Target result: {final_diagnostic}")