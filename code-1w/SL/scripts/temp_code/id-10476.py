import math

# Simulated system metrics for a distributed computing task
def collect_metrics(node_count, duration):
    base_load = node_count * 1.8
    fluctuation = abs(math.sin(duration)) * 0.5
    temp_buffer = (base_load + fluctuation) * 1.2  # Irrelevant intermediate
    peak_load = base_load + 2.1
    efficiency_ratio = (base_load / peak_load) if peak_load else 0
    return {
        'load': base_load,
        'peak': peak_load,
        'efficiency': efficiency_ratio,
        'duration': duration,
        'nodes': node_count,
        'dummy_flag': True,
        'unused_array': [i**2 for i in range(5)]  # Dead data structure
    }

# Secondary analysis - mostly irrelevant
def analyze_redundancy(data):
    if len(data.get('unused_array', [])) > 3:
        checksum = sum(x % 3 for x in data['unused_array'])
        return checksum * 0.1
    return 0

# Decoy function that looks important but isn't used in critical path
def calculate_thermal_decay(temp, time):
    decay = temp / (time + 1)
    adjustment = math.log(decay + 1) if decay > 0 else 0
    return adjustment  # Never called

# Real processing begins here
def normalize_metric(value, min_val, max_val):
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)

# Another distraction: hardware simulation
class HardwareSimulator:
    def __init__(self, cores):
        self.cores = cores
        self.buffer_state = [0] * cores
        self.sim_time = 0

    def update(self, step):
        self.sim_time += step
        for i in range(self.cores):
            self.buffer_state[i] = (self.buffer_state[i] + step) % 7
        return sum(self.buffer_state)

# Unused utility
def sort_by_priority(items):
    return sorted(items, key=lambda x: x[1], reverse=True)

# Core evaluation logic
metrics_log = collect_metrics(node_count=7, duration=13)

# Add fake side-channel data
side_data = {
    'timestamp': 1678892345,
    'voltage': 3.3,
    'noise_floor': 0.045
}

# Distractor computation chain
redundant_score = analyze_redundancy(metrics_log)
simulator = HardwareSimulator(cores=4)
for i in range(3):
    simulator.update(i + 1)  # Updates internal state but result ignored

# Begin actual relevant logic
raw_efficiency = metrics_log['efficiency']
normalized_efficiency = normalize_metric(raw_efficiency, 0.4, 0.95)

# Multiple assignment red herring
alpha, beta, gamma = 1.1, 2.2, 3.3
beta = alpha * 1.5  # Overwritten immediately
beta = normalized_efficiency * 4.0

# Dictionary manipulation - relevant part
metrics_log['adjusted'] = normalized_efficiency * 100
metrics_log['flags'] = {}
if metrics_log['load'] > 10:
    metrics_log['flags']['high_load'] = True
if metrics_log['duration'] > 5:
    metrics_log['flags']['long_duration'] = True

# Critical weight calculation with bitwise distraction
shifted_nodes = metrics_log['nodes'] << 1  # 7 << 1 = 14
masked_value = shifted_nodes & 13  # 14 & 13 = 12 (binary: 1110 & 1101 = 1100)
weight_factor = masked_value / 10.0  # 1.2

# Real performance formula begins here
base_performance = metrics_log['adjusted'] * weight_factor

# Conditional adjustment using boolean logic and short-circuiting
has_flags = 'high_load' in metrics_log['flags'] and metrics_log['flags']['high_load']
bonus_applied = False
if has_flags or (metrics_log['duration'] < 20 and not bonus_applied):
    base_performance *= 1.15  # Apply bonus

# Final aggregation with decoy list accumulation
debug_trace = []
for i in range(2):
    debug_trace.append(f'Step {i}: Active')  # Irrelevant logging

# Key statement - answer depends on this execution
def evaluate_performance(log):
    score = base_performance  # Inherits from outer scope
    if log['nodes'] >= 5:
        score += 17.5
    return int(score)  # Final integer conversion

final_score = evaluate_performance(metrics_log)
print(f"Target result: {final_score}")