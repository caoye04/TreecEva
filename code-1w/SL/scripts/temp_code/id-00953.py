import math

# Simulated system performance metrics from a distributed computing environment
def generate_metrics():
    base_load = [120, 150, 130, 160, 145]
    error_rates = [0.01, 0.03, 0.02, 0.05, 0.04]
    response_times = [230, 190, 250, 210, 220]
    throughput = [850, 900, 870, 920, 890]
    uptime = [99.9, 99.8, 99.95, 99.7, 99.85]

    # Irrelevant transformations (distractors)
    normalized_throughput = [t / max(throughput) * 100 for t in throughput]
    adjusted_uptime = [u ** 1.1 for u in uptime]
    
    # Relevant metric: efficiency score per node
    efficiency = []
    for i in range(len(base_load)):
        score = (base_load[i] * 0.3 + response_times[i] * 0.7) / (error_rates[i] + 0.01)
        efficiency.append(round(score, 2))
    
    return {
        'efficiency': efficiency,
        'error_rates': error_rates,
        'response_times': response_times,
        'throughput': throughput,
        'redundant_data': normalized_throughput,  # distractor
        'decoy_flag': True,
        'unused_counter': 0
    }

# Weighting scheme for evaluation
weights = {
    'efficiency': 0.6,
    'stability': 0.4
}

# Decoy function - looks important but unused
def calculate_robustness(metrics):
    errors = metrics['error_rates']
    return sum([1/e for e in errors if e > 0]) / len(errors)

# Another decoy: complex transformation with no impact
lambda_transform = lambda x: math.log(x + 1) * 2.5

# Real evaluation logic
# Aggregates multiple concepts: list comp, zip, enumerate, dict, early return



def evaluate_performance(metrics, weights):
    efficiency_list = metrics['efficiency']
    error_rates = metrics['error_rates']
    stability_score = 0

    # Compute stability: inverse relationship with error rate volatility
    volatility = 0
    for i in range(1, len(error_rates)):
        volatility += abs(error_rates[i] - error_rates[i-1])
    stability_score = 100 - min(volatility * 10, 100)

    # Distractor: complex-looking but unused calculation
    fake_risk_index = sum([
        math.sin(e * 100) * (i+1) 
        for i, e in enumerate(error_rates)
    ])

    # Early termination red herring (never triggered due to data)
    if metrics.get('decoy_flag', False) and sum(efficiency_list) < 500:
        return -999  # dead path

    # Real computation begins
    avg_efficiency = sum(efficiency_list) / len(efficiency_list)

    # Weighted combination
    composite = avg_efficiency * weights['efficiency'] + stability_score * weights['stability']

    # Additional distraction: tuple unpacking with irrelevant data
    metadata_summary = []
    for idx, (e, r) in enumerate(zip(efficiency_list, response_times)):
        metadata_summary.append((idx, e * 0.1, r // 10))

    # Final adjustment based on hidden rule: number of "efficient" nodes
    efficient_node_count = 0
    for i, eff in enumerate(efficiency_list):
        if eff > 300:  # threshold determined empirically
            efficient_node_count += 1

    # Bonus applied only if at least 3 efficient nodes
    if efficient_node_count >= 3:
        bonus = efficient_node_count * 2.5
        composite += bonus

    # Irrelevant bitwise manipulation (looks low-level and important)
    magic_key = 0b101010
    for val in efficiency_list:
        magic_key ^= int(val) & 0b1111

    final_value = round(composite, 2)

    # Critical assignment point
    final_score = int(final_value)  # truncate to integer

    return final_score

# Execution flow
metrics = generate_metrics()

# Dead code path: function defined but not used
def debug_dump(data):
    for k, v in data.items():
        print(f'{k}: {v}')

# Unused intermediate variable
shadow_copy = {k: v for k, v in metrics.items()}

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")