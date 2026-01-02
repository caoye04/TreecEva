from collections import Counter, defaultdict

# Simulate data ingestion from multiple sensors across zones
data_packets = [
    ('sensor_1', 'zone_blue', 'source_A', 15),
    ('sensor_2', 'zone_red', 'source_B', 8),
    ('sensor_3', 'zone_blue', 'source_A', 12),
    ('sensor_4', 'zone_green', 'source_C', 20),
    ('sensor_5', 'zone_red', 'source_A', 7)
]

errors_log = []
temp_aggregates = []
redundant_sum = 0

# Initialize counters for flow tracking
inflow_counter = Counter()
outflow_tracker = defaultdict(int)
zone_metrics = defaultdict(lambda: defaultdict(int))

# Process incoming data and simulate some irrelevant bookkeeping
for packet in data_packets:
    node, zone, source, volume = packet
    
    # Relevant: track inflow by source
    inflow_counter[source] += volume
    
    # Irrelevant: accumulate redundant sum (not used later)
    redundant_sum += volume * 0.1
    
    # Semi-relevant: update zone-level stats (partially used)
    zone_metrics[zone]['total_in'] += volume
    zone_metrics[zone]['updates_count'] += 1

# Simulate outflows (some mapped, some not)
outflow_records = [
    ('sink_X', 'zone_blue', 10),
    ('sink_Y', 'zone_red', 5),
    ('sink_Z', 'zone_green', 18)
]

for sink, zone, amount in outflow_records:
    outflow_tracker[sink] += amount
    # Update zone metrics with outflow (adds distraction)
    if zone_metrics[zone]['total_in'] > 0:
        zone_metrics[zone]['total_out'] += amount

# Compute efficiency ratios (distractor computation)
efficiency_report = {}
for zone in zone_metrics:
    total_in = zone_metrics[zone]['total_in']
    total_out = zone_metrics[zone]['total_out']
    efficiency_report[zone] = total_out / total_in if total_in > 0 else 0

# Critical assignment point — this determines the answer
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Dead code path (never executed) — adds mild interference
if False:
    net_flow *= 2
    errors_log.append('critical_mismatch')

# Print final result as required
print(f"Result: {net_flow}")