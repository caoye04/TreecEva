from itertools import combinations

# Simulated system metrics from a distributed service
cpu_loads = [0.78, 0.82, 0.65, 0.91, 0.74]
memory_usage = [0.63, 0.71, 0.59, 0.88, 0.67]
disk_iops = [120, 135, 110, 150, 130]
network_latency_ms = [23, 18, 25, 20, 27]

# Irrelevant historical data (distractor)
historical_cpu_peaks = [0.95, 0.93, 0.97, 0.94, 0.96]
seasonal_factors = [1.05, 0.98, 1.02, 1.10, 0.99]

# Misleading intermediate aggregation (dead path)
temp_aggregate = 0
for i in range(len(cpu_loads)):
    temp_aggregate += cpu_loads[i] * memory_usage[i] * 100

# Real-time health indicators (some used, some not)
health_flags = {"cpu": True, "mem": True, "disk": False, "network": True}
status_codes = [200, 200, 503, 200, 404]

# Distractor: unused helper function
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Distractor: unused transformation
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Key metric preprocessing
normalized_cpu = [min(1.0, load / 0.85) for load in cpu_loads]
normalized_mem = [min(1.0, usage / 0.70) for usage in memory_usage]

# Weighted scoring components
metric_components = {
    "response_time_weighted": sum(1 / lat for lat in network_latency_ms[:3]) * 10,
    "stability_score": len([x for x in status_codes if x == 200]),
    "load_balance_ratio": len(list(combinations(cpu_loads[:4], 2))) / 10.0
}

# Unused slicing operation (distractor)
cpu_window = cpu_loads[1:4:1]
mem_snapshot = memory_usage[::-1][:3]

# Relevant aggregated metrics
metrics = [
    sum(normalized_cpu) / len(normalized_cpu),  # avg_cpu_normalized
    sum(normalized_mem) / len(normalized_mem),  # avg_mem_normalized
    disk_iops[2] / 100.0,                        # center_node_iops_scaled
    metric_components["stability_score"] / 5.0  # uptime_ratio
]

# Weight vector (aligned with metrics)
weights = [0.3, 0.3, 0.2, 0.2]

# Distractor: string manipulation unrelated to logic
diag_label = "SYS_PERF_"
service_tag = "svc-a"
diag_code = ''.join([diag_label.lower(), service_tag.upper()])
version_info = diag_code.split('_')[1] + ".1"

# Core evaluation logic
weighted_sum = 0.0
for i in range(len(metrics)):
    weighted_sum += metrics[i] * weights[i]

# Secondary adjustment based on health flags
adjustment_factor = 1.0
if health_flags["cpu"] and health_flags["network"]:
    adjustment_factor *= 1.1
if not health_flags["disk"]:
    adjustment_factor *= 0.9

# Final performance score computation
final_score = int(weighted_sum * adjustment_factor * 100)

# Additional distractor: dictionary operations not affecting final result
summary_report = {}
summary_report['metrics_count'] = len(metrics)
summary_report['weight_total'] = sum(weights)
summary_report['version'] = version_info
summary_report['flags'] = tuple(health_flags.keys())
summary_report['slice_hash'] = hash(tuple(cpu_window + mem_snapshot))

# Output target result
print(f"Result: {final_score}")