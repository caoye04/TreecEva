from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 150, 130, 160, 145, 138, 142, 158, 139, 147]
node_loads = [0.65, 0.82, 0.43, 0.91, 0.73, 0.55, 0.67, 0.88, 0.49, 0.77]
packet_loss = [0.001, 0.003, 0.002, 0.012, 0.005, 0.001, 0.004, 0.015, 0.002, 0.006]

def calculate_efficiency(durations):
    avg = sum(durations) / len(durations)
    variance = sum((x - avg) ** 2 for x in durations) / len(durations)
    return 100 * (1 - (variance / (avg ** 2 + 1)))

def assess_stability(loss_rates):
    base_score = 100
    for rate in loss_rates:
        if rate > 0.01:
            base_score -= 15
        elif rate > 0.005:
            base_score -= 5
        else:
            base_score -= 2
    return max(base_score, 0)

def compute_load_balance(load_vals):
    sorted_loads = sorted(load_vals)
    median = sorted_loads[len(sorted_loads) // 2]
    balanced_nodes = sum(1 for load in load_vals if abs(load - median) < 0.1)
    return (balanced_nodes / len(load_vals)) * 100

# Irrelevant helper function (decoy)
def network_diagnostic_trace():
    history = defaultdict(list)
    for i in range(8):
        for j in range(i+1, min(i+5, 10)):
            history[f'node_{i}'].append(f'trace_{j}')
    return dict(history)

def analyze_redundancy_patterns(data):
    # Dead code path - never used
    patterns = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            patterns.append(val * 2)
        elif val > 100:
            patterns.append(val // 2)
    return patterns

# Distractor variables
temp_analysis = [x * 1.05 for x in task_durations if x > 140]
redundant_calc = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
diag_report = network_diagnostic_trace()

# Real metrics used later
metrics = {
    'efficiency': calculate_efficiency(task_durations),
    'stability': assess_stability(packet_loss),
    'balance': compute_load_balance(node_loads),
    'throughput': 89.4  # Simulated constant metric
}

# Weight configuration for scoring (critical)
weights = defaultdict(float)
weights['efficiency'] = 0.3
weights['stability'] = 0.25
weights['balance'] = 0.25
weights['throughput'] = 0.2

# Unused weight entries (red herring)
weights['latency_jitter'] = 0.05
weights['memory_headroom'] = 0.1

# Another decoy function using list comprehension and zip (irrelevant)
def generate_synthetic_benchmarks():
    samples = [i * 10 + 7 for i in range(1, 6)]
    labels = ['A', 'B', 'C', 'D', 'E']
    synth_data = {}
    for label, val in zip(labels, samples):
        synth_data[label] = [val + j for j in range(3)]
    return synth_data

synth_metrics = generate_synthetic_benchmarks()

# Core evaluation logic
contributions = []
for key in ['efficiency', 'stability', 'balance', 'throughput']:
    weighted_contribution = metrics[key] * weights[key]
    contributions.append(weighted_contribution)

# Final aggregation
total_weight = sum(weights[k] for k in ['efficiency', 'stability', 'balance', 'throughput'])
final_score = sum(contributions) / total_weight

# Distractor: complex but unused calculation
aggregated_diagnostics = []
for node_id, traces in diag_report.items():
    trace_counter = Counter(traces)
    aggregated_diagnostics.append(len(trace_counter))

# Secondary irrelevant transformation
transformed_diagnostics = [
    math.log(x + 1) * 10 
    for i, x in enumerate(aggregated_diagnostics) 
    if i % 2 == 0
]

# Print final result as required
Result: {final_score}