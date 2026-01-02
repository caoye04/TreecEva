import math

# Simulated system benchmark data
def generate_test_data():
    return {
        'operations': [i for i in range(1, 101) if i % 3 == 0],
        'timings': [round(math.sin(i / 10), 4) for i in range(100)],
        'flags': [i & 1 for i in range(100)],
        'metadata': {'version': '2.1', 'mode': 'stress'}
    }

def analyze_flags(flags):
    # Irrelevant analysis (distractor)
    count_even = sum(1 for f in flags if f == 0)
    count_odd = sum(1 for f in flags if f == 1)
    ratio = count_even / (count_odd + 1e-5)
    return round(ratio, 3)

def compute_efficiency(op_list, time_list):
    # Real computation path
    total_ops = sum(op_list)
    avg_time = sum(time_list) / len(time_list)
    efficiency = total_ops / (abs(avg_time) + 1)
    return int(efficiency)

def apply_correction(value, version_str):
    # Version-based adjustment (semi-relevant)
    version_number = float(version_str)
    if version_number >= 2.0:
        return value * 1.1
    else:
        return value * 0.9

# Misleading auxiliary function (dead code path)
def deprecated_metric(data):
    if 'legacy' in data['metadata']:
        return sum(data['timings']) * 0.5
    return 0

# Another red herring: unused transformation
transform = lambda x: [i ** 0.5 for i in x if i > 0]

# Main processing pipeline
benchmark_data = generate_test_data()

# Extract components
ops = benchmark_data['operations']
times = benchmark_data['timings']
flag_analysis = analyze_flags(benchmark_data['flags'])  # Used only for logging

# Core calculation chain
raw_performance = compute_efficiency(ops, times)

# Apply conditional scaling based on metadata
version_tag = benchmark_data['metadata']['version']
adjusted_perf = apply_correction(raw_performance, version_tag)

# Additional filtering step (relevant)
filtered_ops = list(filter(lambda x: x > 10, ops))
op_sum = sum(filtered_ops)
modifier = len(filtered_ops) % 7  # contributes to final result

# Final computation with distractor variables
baseline = raw_performance
scaling_factor = 1.25  # looks important but isn't used directly
dummy_calc = [math.log(abs(t) + 1) for t in times[:10]]  # dead-end computation

# Critical statement
final_score = adjusted_perf + modifier - len(dummy_calc)

print(f"Result: {final_score}")