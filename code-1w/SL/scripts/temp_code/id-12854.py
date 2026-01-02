def analyze_workload(workload):
    peak_hours = [i for i, load in enumerate(workload) if load > 80]
    off_peak_reduction = sum(1 for load in workload if load < 30)
    return peak_hours, off_peak_reduction


def track_efficiency(metrics):
    status_flags = []
    efficiency_scores = []n    for val in metrics:
        if val > 90:
            status_flags.append('OPTIMAL')
            efficiency_scores.append(val * 0.95)
        elif val > 60:
            status_flags.append('STABLE')
            efficiency_scores.append(val * 0.85)
        else:
            status_flags.append('LOW')
            efficiency_scores.append(val * 0.70)
    return efficiency_scores, status_flags


def calculate_baseline(capacity, usage_pattern):
    base_util = sum(usage_pattern) / len(usage_pattern)
    fluctuation_index = max(usage_pattern) - min(usage_pattern)
    adjusted_capacity = capacity * (base_util / 100) * (0.9 + fluctuation_index / 200)
    return adjusted_capacity


def optimize_allocation(resources, logs):
    temp_adjustments = []
    for log in logs:
        if isinstance(log, float):
            temp_adjustments.append(int(log) % 7)
    
    cumulative_shift = 0
    for adj in temp_adjustments:
        cumulative_shift += adj * 1.5
    
    net_resource = 0
    for r in resources:
        if r.get('active'):
            net_resource += r['allocation'] * (r['priority'] / 10)
    
    # Misleading intermediate computation
    phantom_load = sum(i * 2 for i in range(len(temp_adjustments))) if len(temp_adjustments) > 3 else 0
    dummy_sync = phantom_load * 0.1  # Dead code path — not used later

    final_bandwidth = int(net_resource - (cumulative_shift % 25))
    return final_bandwidth

# Main execution
workload_data = [75, 82, 88, 91, 74, 68, 85, 93]
metric_stream = [88, 76, 91, 64, 79, 95]
resource_pool = [
    {'name': 'server_a', 'allocation': 120, 'priority': 8, 'active': True},
    {'name': 'server_b', 'allocation': 80, 'priority': 5, 'active': True},
    {'name': 'backup_c', 'allocation': 60, 'priority': 3, 'active': False},
    {'name': 'cache_d', 'allocation': 100, 'priority': 7, 'active': True}
]

# Trigger analysis steps
peak_periods, idle_drop = analyze_workload(workload_data)
efficiency_values, health_status = track_efficiency(metric_stream)
baseline_cap = calculate_baseline(500, workload_data)

# Generate efficiency log with mixed types (floats and ints)
efficiency_log = [round(v, 1) for v in efficiency_values]
efficiency_log.append(88)      # Add integer

# Key execution point
final_bandwidth = optimize_allocation(resource_pool, efficiency_log)

print(f"Result: {final_bandwidth}")