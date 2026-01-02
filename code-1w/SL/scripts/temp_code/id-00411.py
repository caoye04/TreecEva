def analyze_node_stability(readings):
    stability_score = 0
    for r in readings:
        if r % 7 == 0:
            stability_score += 3
        elif r > 50:
            stability_score -= 1
        else:
            stability_score += r // 10
    return max(stability_score, 0)


def compute_bandwidth_efficiency(packets, errors):
    if packets == 0:
        return 0.0
    efficiency = (packets - errors) / packets
    penalty = 0
    for e in errors:
        penalty += e * 0.1  # Simulated jitter penalty
    return efficiency - penalty

# System telemetry data
node_readings = [14, 23, 56, 91, 44, 7]
packet_counts = [100, 150, 200, 120]
error_counts = [5, 8, 12, 3]
diagnostic_flags = {"overheat": True, "pressure_low": False, "flow_optimal": True}

# Irrelevant health metrics (distractor)
cpu_temps = [67, 72, 65, 78, 70]
memory_usage = [80, 85, 76, 90]

# Auxiliary mapping table (partially used)
node_severity_map = {
    1: 'critical',
    2: 'elevated',
    3: 'normal',
    4: 'optimal',
    5: 'unknown'
}

# Simulated node statuses
node_status_codes = [3, 3, 4, 2, 3, 1]

# Real-time operational nodes (subset)
operational_nodes = [1, 3, 4, 5]

# Fault log with diagnostic codes (dictionary used)
fault_log = {
    1: [9, 2],
    3: [],
    5: [4, 4, 7]
}

# Misleading intermediate calculation (dead path)
system_baseline = sum(cpu_temps) / len(cpu_temps)
if system_baseline > 70:
    baseline_adjusted = True
    adjustment_factor = 1.1
else:
    baseline_adjusted = False
    adjustment_factor = 1.0

# Unused helper function (distractor)
def normalize_signal_strength(signal):
    return max(0, min(100, signal + 10))

# Core evaluation logic
stability_index = analyze_node_stability(node_readings)
efficiency_metric = compute_bandwidth_efficiency(sum(packet_counts), sum(error_counts))

# State tracking with dictionary operations
health_weights = {
    'stability': 0.4,
    'efficiency': 0.35,
    'fault_count': 0.25
}

total_faults = 0
for node_id, faults in fault_log.items():
    if node_id in operational_nodes:
        total_faults += len(faults)

# Secondary irrelevant count
irrelevant_event_count = 0
for code in node_status_codes:
    if code == 2 or code == 1:
        irrelevant_event_count += 1

# Main health computation
weighted_health = (
    health_weights['stability'] * stability_index +
    health_weights['efficiency'] * efficiency_metric * 10 +
    health_weights['fault_count'] * (5 - min(total_faults, 5))  # Cap at 5
)

# Final diagnostic level
final_diagnostic = int(round(weighted_health))

# Output result
print(f"Result: {final_diagnostic}")