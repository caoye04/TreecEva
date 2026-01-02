from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed service
def get_raw_metrics():
    return {
        'latency_ms': [120, 85, 93, 110, 98, 105, 113],
        'error_rate': [0.002, 0.003, 0.001, 0.004, 0.002, 0.001, 0.003],
        'throughput_rps': [2400, 2650, 2580, 2390, 2700, 2620, 2500],
        'cpu_util': [78, 82, 75, 88, 80, 77, 85]
    }

# Irrelevant auxiliary function — dead code path
def analyze_user_behavior(logs):
    user_freq = defaultdict(int)
    for log in logs:
        parts = log.split(' ')
        if len(parts) > 2:
            user_freq[parts[1]] += 1
    return dict(user_freq)

# Misleading transformation: looks important but unused
def normalize_values(data_list):
    max_val = max(data_list)
    return [x / max_val for x in data_list]

# Decoy scoring function with plausible logic
def legacy_scoring(metrics):
    score = 0
    score += sum(metrics['latency_ms']) // 10
    score -= int(sum(metrics['error_rate']) * 1000)
    score += max(metrics['throughput_rps']) // 100
    return score * 2  # Red herring result

# Auxiliary computation — distractor
intermediate_stats = {}
raw_data = get_raw_metrics()
for key, values in raw_data.items():
    intermediate_stats[key + '_avg'] = sum(values) / len(values)
    intermediate_stats[key + '_peak'] = max(values)

# Fake aggregation using string manipulation (distractor)
dummy_report = ''
for k, v in intermediate_stats.items():
    if 'avg' in k:
        dummy_report += f"{k.upper()}: {v:.2f}; "
dummy_report = dummy_report.strip().rstrip(';')
dummy_report = dummy_report.replace('_', ' ').title()

# Real processing begins here
filtered_latency = [x for x in raw_data['latency_ms'] if x < 120]  # exclude outlier
smoothed_errors = [x for x in raw_data['error_rate'] if x <= 0.003]  # filter spikes

# Build performance vector
efficiency_vector = [
    sum(filtered_latency) / len(filtered_latency),
    sum(smoothed_errors) / len(smoothed_errors),
    sum(raw_data['throughput_rps']) / len(raw_data['throughput_rps']),
    sum(raw_data['cpu_util']) / len(raw_data['cpu_util'])
]

# Weight profile — some distraction via unused entries
weights = defaultdict(float)
weights['latency'] = 0.4
weights['errors'] = 0.3
weights['throughput'] = 0.2
weights['cpu'] = 0.1
# Unused weights below — misleading
weights['memory'] = 0.05
weights['disk_io'] = 0.02

# Another decoy structure
system_flags = {
    'overloaded': any(cpu > 85 for cpu in raw_data['cpu_util']),
    'stable_errors': all(er < 0.005 for er in raw_data['error_rate']),
    'high_load': sum(raw_data['throughput_rps']) > 18000
}

# Bit manipulation red herring
status_code = 0
for flag in system_flags.values():
    status_code = (status_code << 1) | int(flag)
status_diagnostic = bin(status_code ^ 0b111)  # Looks diagnostic, unused

# Core evaluation logic
weighted_parts = []
weighted_parts.append(efficiency_vector[0] * weights['latency'] * -1)  # latency inversely affects score
weighted_parts.append(efficiency_vector[1] * weights['errors'] * -1000)
weighted_parts.append((efficiency_vector[2] / 100) * weights['throughput'])
weighted_parts.append((100 - efficiency_vector[3]) * weights['cpu'] * 0.5)  # headroom bonus

# Final calculation
base_component = sum(weighted_parts)
scale_factor = 10.0

# Additional noise: string-based condition that always passes
trigger_flag = 'ACTIVATE'[:3].lower() == 'act'
if trigger_flag:
    scale_factor *= 1.5

# Critical statement
final_score = base_component * scale_factor

# Output must be printed exactly like this
print(f"Result: {final_score}")