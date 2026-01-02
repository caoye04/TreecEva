from collections import defaultdict, Counter
import math

# Simulated system log analysis with heavy distractions
def analyze_system_load(log_data):
    temp_cache = []
    debug_trace = [0] * len(log_data)
    stats_map = defaultdict(int)
    anomaly_flags = set()

    for entry in log_data:
        parts = entry.split('|')
        timestamp = int(parts[0])
        cpu = int(parts[1])
        mem = int(parts[2])
        disk = int(parts[3])
        net_in = int(parts[4])
        net_out = int(parts[5])

        load_score = (cpu * 1.1) + (mem * 0.8) + (disk * 0.6)
        perf_ratio = (net_in + net_out) / (load_score + 1)

        # Irrelevant network symmetry check (dead logic path)
        if net_in > 2 * net_out:
            debug_trace.append(1)
        elif net_out > 2 * net_in:
            debug_trace.append(-1)

        # Real metric accumulation
        stats_map['total_load'] += load_score
        stats_map['peak_cpu'] = max(stats_map['peak_cpu'], cpu)
        stats_map['acc_mem'] += mem

        # Distractor: Anomaly detection that isn't used later
        if cpu > 90 and mem > 85:
            anomaly_flags.add(timestamp)
            stats_map['critical_count'] += 1

        # More red herrings
        if disk > 75:
            temp_cache.append(disk * 0.15)

    # Unused transformation (distractor)
    normalized_cache = [round(x, 2) for x in temp_cache if x > 5]
    decay_factor = sum(normalized_cache) / (len(normalized_cache) + 1e-5)

    return stats_map

# Decoy function – looks important but unused
def compute_health_vector(data_stream):
    vec = [0] * 5
    for item in data_stream:
        if item % 7 == 0:
            vec[0] += 1
        elif item % 5 == 0:
            vec[1] += item
    return vec

# Core processing with subtle dependencies
def evaluate_stability_index(entries):
    raw_scores = []
    temporal_weights = []

    for e in entries:
        fields = e.split('|')
        t, cpu, mem, disk, _, _ = map(int, fields)

        # Weight based on time (older = less weight)
        weight = 0.95 ** (2023 - (t % 100))

        # Real signal buried in noise
        base_metric = (cpu * 2) + mem - (disk // 3)
        adjusted = base_metric * weight

        raw_scores.append(adjusted)
        temporal_weights.append(weight)

        # Distractor: temperature simulation (unused)
        thermal_proxy = (cpu ** 1.1) / (mem + 1)
        if thermal_proxy > 80:
            continue  # fake optimization

    # Correct aggregation despite noise
    total_weighted = sum(raw_scores)
    total_weight = sum(temporal_weights)
    return total_weighted / total_weight if total_weight > 0 else 0

# Another decoy - complex but irrelevant
complex_transform = lambda x: math.sin(x / 10) * math.cos(x / 15)

# Main orchestration with critical distraction layers
def process_metrics(logs, threshold):
    # Step 1: Extract primary diagnostics
    diagnostics = analyze_system_load(logs)

    # Step 2: Compute stability index (key value)
    stability = evaluate_stability_index(logs)

    # Step 3: Generate fake correlation matrix (distraction)
    n = len(logs)
    fake_corr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(i - j)
            fake_corr[i][j] = math.tanh(diff / (stability + 1))

    # Step 4: Count severity levels (some relevant)
    severe_count = 0
    moderate_count = 0
    for line in logs:
        vals = list(map(int, line.split('|')[1:4]))  # cpu, mem, disk
        avg_util = sum(vals) / 3
        if avg_util >= threshold:
            severe_count += 1
        elif avg_util >= threshold - 15:
            moderate_count += 1

    # Step 5: Build summary (mixing real and fake)
    summary_stats = {
        'stability': stability,
        'severe': severe_count,
        'moderate': moderate_count,
        'baseline': diagnostics['total_load'] // (len(logs) + 1),
        'legacy_flag': False
    }

    # Step 6: Apply hidden correction factor (crucial step)
    correction = 1.0
    if diagnostics['peak_cpu'] > 85:
        correction *= 0.9
    if diagnostics['critical_count'] > 2:
        correction *= 0.85

    # Step 7: Final computation chain
    raw_final = summary_stats['stability'] \
                 + (summary_stats['severe'] * 2.5) \
                 - (summary_stats['moderate'] * 0.7)

    intermediate = raw_final * correction

    # Step 8: Final adjustment using list comprehension (python idiom)
    history_buffer = [intermediate * (0.9 ** i) for i in range(5)]
    filtered = [x for x in history_buffer if x > 10]
    final_adjustment = sum(filtered) / len(filtered) if filtered else intermediate

    # Critical assignment point
    final_diagnostic = int(round(final_adjustment * 1.03))

    # Dead code - misleading print that looks important
    if final_diagnostic < 0:
        print("CRITICAL SYSTEM FAILURE")
    else:
        temp_report = [final_diagnostic, "OK"]
        # This would print status but doesn't affect result

    return final_diagnostic

# Generate deterministic input
base_timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
cpu_loads = [88, 92, 85, 94, 87, 90, 86]
memory_use = [78, 88, 82, 90, 76, 84, 80]
disk_io = [65, 72, 68, 74, 69, 70, 67]
network_in = [1200, 1100, 1300, 1150, 1250, 1180, 1220]
network_out = [1100, 1150, 1050, 1200, 1100, 1170, 1190]

log_entries = []
for i in range(len(base_timestamps)):
    entry = f"{base_timestamps[i]}|{cpu_loads[i]}|{memory_use[i]}|{disk_io[i]}|{network_in[i]}|{network_out[i]}"
    log_entries.append(entry)

system_threshold = 80

# Execute main logic
diagnostics = analyze_system_load(log_entries)
stability_index = evaluate_stability_index(log_entries)
final_diagnostic = process_metrics(log_entries, system_threshold)

print(f"Result: {final_diagnostic}")