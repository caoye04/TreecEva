def analyze_throughput(raw_metrics):
    total_units = 0
    invalid_count = 0
    for entry in raw_metrics:
        if 'status' in entry and entry['status'] == 'failed':
            invalid_count += 1
            continue
        if 'units_processed' in entry:
            total_units += entry['units_processed']
    return total_units

raw_metrics_list = [
    {'units_processed': 120, 'status': 'success', 'timestamp': '2023-05-01'},
    {'units_processed': 95, 'status': 'success', 'timestamp': '2023-05-02'},
    {'units_processed': 0, 'status': 'failed', 'timestamp': '2023-05-03'},
    {'units_processed': 130, 'status': 'success', 'timestamp': '2023-05-04'}
]

overhead_logs = {
    'system_a': {'cycles': 450, 'idle': 90},
    'system_b': {'cycles': 600, 'idle': 150},
    'system_c': {'cycles': 300, 'idle': 60}
}

process_data = analyze_throughput(raw_metrics_list)

baseline_reference = 250
redundant_calc_1 = (baseline_reference * 1.2) - 70
redundant_calc_2 = sum(overhead_logs[sys]['idle'] for sys in overhead_logs)
dummy_filter = [x for x in range(5) if x % 2 == 0]

intermediate_total = 0
for system, metrics in overhead_logs.items():
    active_cycles = metrics['cycles'] - metrics['idle']
    intermediate_total += active_cycles

scaling_factor = 1.0
if process_data > 200:
    scaling_factor = 1.1
elif process_data < 100:
    scaling_factor = 0.9

adjusted_output = process_data * scaling_factor
auxiliary_sum = sum([len(raw_metrics_list), len(overhead_logs), 1])

# Misleading branch that doesn't affect final result
def debug_analyze(data):
    return sum(1 for x in data if x.get('status') == 'success')

debug_count = debug_analyze(raw_metrics_list)

# Core calculation disguised among distractions
def calculate_efficiency(output, overhead):
    total_active = sum(ov['cycles'] - ov['idle'] for ov in overhead.values())
    if total_active == 0:
        return 0.0
    efficiency = output / total_active
    return round(efficiency * 100, 4)

efficiency_ratio = calculate_efficiency(process_data, overhead_logs)

Result: {efficiency_ratio}