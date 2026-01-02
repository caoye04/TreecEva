from collections import defaultdict, Counter

# Simulated telemetry data from distributed sensors
telemetry_streams = [
    [12, 15, 14, 13, 45, 16, 12, 18],
    [9, 11, 10, 44, 10, 12, 11, 9],
    [13, 13, 14, 15, 16, 55, 18, 17],
    [10, 9, 8, 43, 11, 10, 12, 13]
]

# Irrelevant baseline configuration (distractor)
system_baseline = {
    'version': '2.1.9',
    'nodes': 7,
    'latency_cap_ms': 120,
    'redundancy_level': 3
}

# Decoy function that looks important but is unused
def compute_health_score(nodes, weights):
    return sum(n * w for n, w in zip(nodes, weights)) % 100

# Misleading intermediate processing (dead code path)
shadow_buffer = []
for stream in telemetry_streams:
    temp_shadow = []
    for val in stream:
        if val > 40:
            temp_shadow.append(val * 0.1)
        else:
            temp_shadow.append(val * 1.1)
    shadow_buffer.append(temp_shadow)

# Actual relevant data transformation
filtered_alerts = []
for idx, stream in enumerate(telemetry_streams):
    for pos, reading in enumerate(stream):
        if reading > 42:  # Threshold for anomaly
            # Composite key using enumerate and meaningful context
            filtered_alerts.append((idx, pos, reading))

# Distractor: Unused statistical summary
counter_summary = Counter()
for _, _, val in filtered_alerts:
    bucket = val // 10
    counter_summary[bucket] += 1

# Real logic begins: aggregate by node index
node_anomalies = defaultdict(list)
for node_idx, position, value in filtered_alerts:
    node_anomalies[node_idx].append(value)

# Compute diagnostic fingerprint using modular arithmetic and bit ops
fingerprint_seed = 0
for node_id, anomalies in node_anomalies.items():
    base_metric = sum(anomalies) // len(anomalies)
    # Bit manipulation with shift and XOR to obscure logic
    shifted = (base_metric << 2) ^ 0b1010
    fingerprint_seed += shifted % 17

# Secondary decoy calculation (looks like security hash)
security_hash = 0
for k, v in system_baseline.items():
    if isinstance(v, int):
        security_hash ^= (v * 31) + len(k)

# Control flow with red herring condition
override_mode = False
if fingerprint_seed > 10:
    # This block appears significant but doesn't affect final result
    adjustment_factor = 0
    for i in range(3):
        adjustment_factor += (fingerprint_seed >> i) & 1
    override_mode = adjustment_factor >= 2  # Always true, but irrelevant

# Critical computation hidden among distractions
def process_metrics(alert_list, threshold):
    total_excess = 0
    for _, _, val in alert_list:
        if val > threshold:
            # Integer division and rounding behavior matters here
            contribution = (val // 3) * 2
            total_excess += contribution
    # Non-linear scaling on final sum
    return int((total_excess ** 0.5) * 3)

# Another decoy: unused data structure transformation
zipped_view = list(zip(*telemetry_streams))
row_averages = [sum(row)/len(row) for row in zipped_view]

# Key statement embedded in setup
system_threshold = 42
log_data = filtered_alerts
final_diagnostic = process_metrics(log_data, system_threshold)

# Final print statement required
print(f"Result: {final_diagnostic}")