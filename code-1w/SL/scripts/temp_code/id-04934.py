from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.78, 'errors': 3, 'temp': 67, 'uptime': 1200},
    {'node': 'B', 'load': 0.45, 'errors': 1, 'temp': 54, 'uptime': 1800},
    {'node': 'C', 'load': 0.92, 'errors': 8, 'temp': 83, 'uptime': 900},
    {'node': 'A', 'load': 0.61, 'errors': 2, 'temp': 65, 'uptime': 1201},
    {'node': 'D', 'load': 0.33, 'errors': 0, 'temp': 47, 'uptime': 2000},
    {'node': 'B', 'load': 0.53, 'errors': 1, 'temp': 56, 'uptime': 1801},
    {'node': 'C', 'load': 0.88, 'errors': 6, 'temp': 80, 'uptime': 901},
    {'node': 'E', 'load': 0.21, 'errors': 0, 'temp': 44, 'uptime': 2100}
]

# Irrelevant helper (decoy)
def analyze_bandwidth(data):
    total = 0
    for d in data:
        if 'bandwidth' in d:
            total += d['bandwidth']
    return total

# Unused function (dead code path)
def compute_redundancy_score(nodes):
    return len(nodes) * 0.75

# Misleading intermediate calculation
temp_fluctuations = []
for i in range(1, len(telemetry_stream)):
    prev_temp = telemetry_stream[i-1]['temp']
    curr_temp = telemetry_stream[i]['temp']
    temp_fluctuations.append(abs(curr_temp - prev_temp))

average_fluctuation = sum(temp_fluctuations) / len(temp_fluctuations) if temp_fluctuations else 0

# Core aggregation logic
node_data = defaultdict(list)
for entry in telemetry_stream:
    node_data[entry['node']].append(entry)

# Distractor: unused aggregation
error_prone_nodes = [node for node, data in node_data.items() if sum(d['errors'] for d in data) > 5]

# Another red herring: uptime ranking
sorted_by_uptime = sorted(telemetry_stream, key=lambda x: x['uptime'], reverse=True)
median_uptime = sorted_by_uptime[len(sorted_by_uptime)//2]['uptime']

# Character counting distraction (suggested paradigm)
node_names = ''.join(node_data.keys())
char_frequency = Counter(node_names)
dominant_char_count = max(char_frequency.values())  # Not used later

# Real processing begins here
aggregated_metrics = {}
for node, records in node_data.items():
    loads = [r['load'] for r in records]
    avg_load = sum(loads) / len(loads)
    max_error_rate = max(r['errors'] for r in records)
    high_temp_events = sum(1 for r in records if r['temp'] > 75)
    
    # Composite health score (not yet final)
    stability_score = (1 - avg_load) * 100 - (max_error_rate * 10) + (high_temp_events * -15)
    aggregated_metrics[node] = {
        'score': stability_score,
        'critical_events': high_temp_events + max_error_rate
    }

# System-wide summary
system_health = {
    'total_nodes': len(node_data),
    'overloaded_nodes': sum(1 for m in aggregated_metrics.values() if m['score'] < 20),
    'total_critical': sum(m['critical_events'] for m in aggregated_metrics.values())
}

# Decoy list comprehension with no side effects
_ = [math.log(n['load'] + 1e-5) for n in telemetry_stream if n['temp'] > 70]

# Simulated log snapshot (irrelevant fields included)
log_snapshot = {
    'timestamp': '2023-12-05T10:30:00Z',
    'level': 'WARNING',
    'message': 'High load detected on node C',
    'raw_telemetry_count': len(telemetry_stream),
    'duplicate_nodes': len(telemetry_stream) - len(set(e['node'] for e in telemetry_stream)),
    'extra_flag': False
}

# Main processing function
def process_metrics(log, health):
    # Extract and ignore irrelevant log content
    if 'extra_flag' in log and not log['extra_flag']:
        pass  # deliberate noop
    
    base = health['total_nodes'] * 100
    penalty = health['overloaded_nodes'] * 25
    crisis_factor = health['total_critical'] * 8
    
    # Bit manipulation red herring
    masked_penalty = penalty & 0xFF
    
    # Real computation
    raw_diagnostic = base - penalty + crisis_factor
    
    # Additional obfuscation via trigonometric decoy
    angle = math.pi / 6
    trig_adjustment = int(10 * math.sin(angle))  # evaluates to 5, but misleading
    
    # Final result (this is the answer)
    final_diagnostic = raw_diagnostic + trig_adjustment
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_snapshot, system_health)
print(f"Target result: {final_diagnostic}")