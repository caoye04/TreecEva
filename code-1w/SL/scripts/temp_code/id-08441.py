import itertools

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 95, 134, 78, 108, 118, 99]
node_loads = [0.67, 0.82, 0.54, 0.91, 0.73, 0.61, 0.87]
fault_counts = [2, 0, 1, 3, 0, 1, 2]
packet_loss_rates = [0.002, 0.005, 0.001, 0.012, 0.003, 0.001, 0.004]
energy_consumption = [450, 395, 510, 320, 415, 460, 380]

# Irrelevant transformation - distractor (bit manipulation on unrelated data)
def scramble_value(x):
    return ((x << 3) ^ 0xCAFEBABE) & 0xFFFFFFFF

distorted_energy = [scramble_value(int(e)) for e in energy_consumption]

# Misleading aggregation - never used later
total_distorted = sum(distorted_energy) // len(distorted_energy)

# Another red herring: unused function simulating network latency adjustment
def adjust_for_latency(values, factor=1.05):
    return [v * factor for v in values]

# Decoy data structure with plausible naming
historical_benchmark = {
    'peak_throughput': 987.65,
    'avg_response_time': 45.2,
    'degraded_nodes': 3,
    'calibration_offset': 0.073
}

# Fake normalization function that looks important but is not used
def legacy_normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val + 1e-8) for x in data]

# Real processing begins here — subtle due to surrounding noise
processed_durations = [d / 60.0 for d in task_durations]  # convert to minutes
inverse_faults = [1 / (f + 1) for f in fault_counts]  # higher is better
load_efficiency = [1 - load for load in node_loads]

# Composite metric using list comprehension with filtering
valid_nodes = [
    (dur, inv_f, eff, loss) 
    for dur, inv_f, eff, loss in zip(
        processed_durations, inverse_faults, load_efficiency, packet_loss_rates
    )
    if inv_f > 0.5  # only nodes with less than 1 fault
]

# Extract components back for further use
filtered_durations, filtered_fault_scores, filtered_efficiency, filtered_loss = zip(*valid_nodes)

# Secondary distraction: attempt to compute something with packet loss but unused
loss_penalty = sum([int(1000 * rate) for rate in filtered_loss if rate > 0.003])
system_health_warning = loss_penalty > 10

# Real weight vector (well-hidden among distractions)
weights = [0.4, 0.3, 0.2, 0.1]  # duration, fault resilience, efficiency, loss tolerance

# Core evaluation function buried after decoys
def evaluate_performance(metrics_list, w):
    # metrics_list shape: (duration, fault_score, efficiency, loss)
    composite_scores = []
    for m in metrics_list:
        score = 0
        for i in range(len(w)):
            if i == 0:
                # shorter duration → higher score
                score += (1 / m[i]) * w[i] * 10
            elif i == 3:
                # lower loss → higher score
                score += (1 / (m[i] + 0.001)) * w[i] * 0.1
            else:
                score += m[i] * w[i]
        composite_scores.append(score)
    
    # Final aggregation: geometric mean with offset
    product = 1
    for s in composite_scores:
        product *= (s + 1)
    geometric_mean = product ** (1 / len(composite_scores))
    
    # Apply bonus if no node exceeded 2% packet loss
    strict_loss_compliance = all(rate <= 0.02 for rate in packet_loss_rates)
    bonus = 15 if strict_loss_compliance else 0
    
    return int(geometric_mean + bonus)

# Key execution point
metrics = list(zip(filtered_durations, filtered_fault_scores, filtered_efficiency, filtered_loss))
final_score = evaluate_performance(metrics, weights)

# Irrelevant post-processing (dead code path)
optimized_schedule = list(itertools.permutations(task_durations[:3]))
planned_maintenance_window = sum(
    1 for l in node_loads if l > 0.8
) * 15  # in minutes, unused

# Critical output
print(f"Result: {final_score}")