from itertools import combinations

# Simulate system performance metrics under varying load conditions
def generate_metrics(base_load, stress_factor):
    loads = [base_load * (1.1 ** i) for i in range(5)]
    temperatures = [l * 0.8 + 25 for l in loads]
    response_times = [max(0.1, (l / 10) ** 1.5) for l in loads]
    error_rates = [min(0.05, (t - 70) * 0.001) for t in temperatures]

    # Distractor computation: irrelevant thermal modeling
    heat_capacity = 4200
    energy_input = sum([heat_capacity * (t - 25) for t in temperatures])

    return {
        'loads': loads,
        'response_times': response_times,
        'error_rates': error_rates,
        'meta': {'total_energy': energy_input, 'peak_temp': max(temperatures)}
    }

def analyze_response_patterns(rt_list):
    # Analyze burst patterns in response times using sliding window
    bursts = 0
    for i in range(len(rt_list) - 2):
        if rt_list[i] < rt_list[i+1] > rt_list[i+2]:
            bursts += 1

    # Distractor: combinatorial analysis of non-critical pairs
    critical_pairs = list(combinations([i for i, rt in enumerate(rt_list) if rt > 1.0], 2))
    pair_count = len(critical_pairs)

    return bursts, pair_count

def calculate_stability(errors):
    stability = 100.0
    for e in errors:
        if e > 0.02:
            stability -= 5.0
        elif e > 0.01:
            stability -= 2.0
    # Clamp to reasonable bounds
    return max(0, stability)

def evaluate_performance(metrics, baseline):
    r_times = metrics['response_times']
    e_rates = metrics['error_rates']
    
    # Compute primary indicators
    avg_response = sum(r_times) / len(r_times)
    peak_load_ratio = metrics['loads'][-1] / baseline
    
    # Use helper functions
    burst_count, _ = analyze_response_patterns(r_times)
    stability_score = calculate_stability(e_rates)
    
    # Intermediate distractor calculation: unused efficiency metric
    efficiency = (1 / avg_response) * stability_score if avg_response > 0 else 0
    
    # Weighted scoring model
    time_penalty = max(0, (avg_response - 0.5) * 10)
    load_penalty = max(0, (peak_load_ratio - 1.5) * 8)
    burst_penalty = burst_count * 3
    
    base_score = 100
    final_score = base_score - time_penalty - load_penalty - burst_penalty - (100 - stability_score)
    
    # Execution point of interest
    final_score = int(round(final_score))
    
    # Dead code branch - never executed but adds cognitive load
    if False:
        fallback = sum(metrics['loads']) // len(metrics['loads'])
        final_score = max(final_score, fallback)

    return final_score

# Main execution
baseline_load = 80
metrics_data = generate_metrics(baseline_load, stress_factor=1.4)
final_score = evaluate_performance(metrics_data, baseline_load)
print(f"Target result: {final_score}")