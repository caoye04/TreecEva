def analyze_system_load(base_load, peak_hours):
    # Simulate complex load distribution across hours
    load_curve = [base_load * (1.5 if h in peak_hours else 0.8) for h in range(24)]
    avg_load = sum(load_curve) / len(load_curve)
    peak_load = max(load_curve)
    normalized_peak = (peak_load - avg_load) / avg_load
    
    # Distractor: energy cost calculation (not used later)
    hourly_costs = [(load * 0.12 * 1.15) for load in load_curve]  # including tax
    total_energy_cost = round(sum(hourly_costs), 2)
    cost_efficiency_ratio = (avg_load / total_energy_cost) if total_energy_cost else 0

    # Irrelevant security check simulation
    security_flags = set()
    if any(load > 90 for load in load_curve):
        security_flags.add('HIGH_LOAD')
    if base_load < 10:
        security_flags.add('LOW_BASELINE')

    # Return only performance metrics
    return {
        'average': avg_load,
        'normalized_peak': normalized_peak,
        'security_issues': len(security_flags)
    }


def evaluate_performance(weights, results_dict):
    # Weighted scoring using lambda for dynamic contribution
    compute_contribution = lambda w, v: round(w * v, 3)
    score_components = [
        compute_contribution(weights['stability'], results_dict['normalized_peak']),
        compute_contribution(weights['efficiency'], results_dict['average'])
    ]
    
    # Distractor: unused component based on security (present but not included in final logic)
    security_penalty = 0
    if results_dict['security_issues'] > 0:
        temp_penalty = results_dict['security_issues'] * 5.0
        security_penalty = min(temp_penalty, 15)  # capped penalty
    
    # Another distractor: historical comparison with dead code path
    historical_benchmark = [1.2, 0.8, 1.5, 0.9, 1.1]
    deviation_from_history = abs(results_dict['normalized_peak'] - historical_benchmark[0])
    adaptation_factor = 1.0
    if deviation_from_history > 1.0:
        adaptation_factor = 0.9  # unused in final computation

    # Final score computed from relevant components only
    raw_score = sum(score_components)
    scaled_score = raw_score * 100
    final_score = int(round(scaled_score))

    # Debugging leftovers (irrelevant prints commented out)
    # print(f'Score components: {score_components}')
    # print(f'Raw score: {raw_score}, Scaled: {scaled_score}')

    return final_score

# Main execution context
metric_weights = {
    'stability': 0.6,   # weight for normalized peak stability
    'efficiency': 0.04 # weight for average load efficiency (smaller impact)
}

raw_results = analyze_system_load(base_load=40, peak_hours={8, 12, 18, 19})

# Critical statement
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Result: {final_score}")