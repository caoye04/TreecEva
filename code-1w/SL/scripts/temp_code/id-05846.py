import math

def analyze_packet_loss(rate):
    if rate < 0.05:
        return 'stable'
    elif rate < 0.15:
        return 'fluctuating'
    else:
        return 'critical'

# Simulated network telemetry
timestamps = [1623456780, 1623456790, 1623456800, 1623456810]
signal_strength = [-45, -52, -61, -73]
packet_loss_rates = [0.03, 0.08, 0.12, 0.18]
data_throughput = [987, 854, 721, 432]  # Mbps

# Irrelevant signal processing (distractor)
decayed_signals = []
for i, strength in enumerate(signal_strength):
    decay_factor = math.exp(-i * 0.1)
    adjusted = strength * decay_factor
    decayed_signals.append(round(adjusted, 2))

# Health state mapping (core logic disguised)
health_map = {'stable': 1, 'fluctuating': 0, 'critical': -2}
state_weights = {'A': 3, 'B': 1, 'C': -1}

# Misleading diagnostic chain (red herring)
baseline_diagnostic = 0
for rate in packet_loss_rates:
    category = analyze_packet_loss(rate)
    baseline_diagnostic += health_map.get(category, 0)

# Dummy data structure with unused transformations
snapshot_buffer = {}
for ts in timestamps:
    snapshot_buffer[ts] = {
        'checksum': (ts % 1000) ^ 42,
        'flag': False,
        'buffer': []
    }

# Core system health assessment (actual path)
system_health = 0
network_state_log = []

for i in range(len(timestamps)):
    state_key = chr(65 + (i % 3))  # A, B, C cycling
    loss_state = analyze_packet_loss(packet_loss_rates[i])
    
    # Real accumulation logic buried in noise
    if loss_state == 'critical':
        system_health -= 3
    elif i % 2 == 0:
        system_health += 1
    
    entry = {
        'time': timestamps[i],
        'state': loss_state,
        'weight': state_weights[state_key],
        'throughput_bin': data_throughput[i] // 100
    }
    network_state_log.append(entry)

# Decoy statistical summary (dead path)
mean_throughput = sum(data_throughput) / len(data_throughput)
median_index = len(data_throughput) // 2
median_throughput = sorted(data_throughput)[median_index]
mode_approx = max(set(data_throughput), key=data_throughput.count)

# Character counting distraction (irrelevant)
log_string = "system.network.diagnostic.v2"
char_count = sum(1 for c in log_string if c == '.')

# Unused recursive function (decoy)
def calculate_depth(level):
    if level <= 1:
        return 1
    return level + calculate_depth(level - 2)

recursive_trace = [calculate_depth(i) for i in range(1, 5)]

# Primary metric aggregation (key computation)
def aggregate_metrics(log_entries, base_score):
    total = base_score * 2
    critical_count = 0
    recent_throughput = 0
    
    for entry in log_entries:
        total += entry['weight']
        if entry['state'] == 'critical':
            critical_count += 1
        if entry['throughput_bin'] > 5:
            recent_throughput += entry['throughput_bin']
    
    # Compound adjustment
    total += (recent_throughput * 2) - (critical_count * 5)
    return total

# Secondary offset calculation (subtle but relevant)
corrective_offset = 0
for entry in network_state_log:
    if entry['state'] == 'fluctuating' and entry['time'] > 1623456795:
        corrective_offset += 2
    elif entry['state'] == 'stable':
        corrective_offset += 1

corrective_offset = max(corrective_offset, 0)

# Final synthesis (target execution point)
final_diagnostic = aggregate_metrics(network_state_log, system_health) + corrective_offset

# Additional red herring: unused dictionary transformation
summary_report = {}
for entry in network_state_log:
    hour = entry['time'] // 3600
    if hour not in summary_report:
        summary_report[hour] = {'count': 0, 'states': []}
    summary_report[hour]['count'] += 1
    summary_report[hour]['states'].append(entry['state'])

# Spurious bit manipulation (distractor)
bit_flags = 0
for i in range(3):
    bit_flags |= (1 << i)
    bit_flags ^= (i + 1)

# Output the target result
print(f"Result: {final_diagnostic}")