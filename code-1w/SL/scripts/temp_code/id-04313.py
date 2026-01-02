from collections import Counter, defaultdict

# Simulate a network flow diagnostic system with multiple sources and sinks
data_packets = [
    ('source_A', 'sink_X'), ('source_B', 'sink_Y'), ('source_A', 'sink_Z'),
    ('source_A', 'sink_X'), ('source_C', 'sink_Y'), ('source_B', 'sink_X'),
    ('source_A', 'sink_Y'), ('source_C', 'sink_Z')
]

inflow_counter = Counter()
outflow_tracker = defaultdict(int)
packet_latency_log = []
redundant_checksum = 0

# Process each packet for routing analysis
for src, sink in data_packets:
    inflow_counter[src] += 1
    outflow_tracker[sink] += 1
    
    # Irrelevant latency simulation (distraction)
    if src == 'source_A':
        packet_latency_log.append(15)
    elif sink == 'sink_Y':
        packet_latency_log.append(25)
    else:
        packet_latency_log.append(10)

    # Misleading checksum accumulation (dead computation)
    redundant_checksum += hash(src[:2]) % 7

# Auxiliary diagnostic: peak traffic detection (semi-relevant)
critical_nodes = set()
for node, count in inflow_counter.items():
    if count > 2:
        critical_nodes.add(node)

for node, count in outflow_tracker.items():
    if count >= 2:
        critical_nodes.add(f'out_{node}')

# State validation step (distraction)
system_health = len(critical_nodes) < 5 and redundant_checksum > 0

# Key computational branch affecting final result
baseline_offset = 0
if inflow_counter['source_A'] > 3:
    baseline_offset += 2
else:
    baseline_offset -= 1

# Secondary adjustment based on unused path
phantom_route_detected = False
for src, _ in data_packets:
    if src == 'source_D':
        phantom_route_detected = True

if phantom_route_detected:
    baseline_offset += 5  # Never executed – dead logic path

# Core calculation with distractor variables
raw_inflow = sum(inflow_counter.values())
raw_outflow = sum(outflow_tracker.values())
total_delta = raw_inflow - raw_outflow  # Always zero by construction (misleading)

# Critical assignment point
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)
net_flow += baseline_offset  # Final adjustment

# Output must follow required format
print(f"Result: {net_flow}")