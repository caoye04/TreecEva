from functools import reduce

def calculate_phase_efficiency(data):
    base = data['input'] * 0.9
    loss_factor = data.get('loss', 0.05)
    adjusted = base - (base * loss_factor)
    
    # Distractor: Irrelevant transformation
    temp_debug = [x ** 0.5 for x in range(1, 6)]
    temp_sum = sum(temp_debug) / len(temp_debug)
    
    if data['type'] == 'primary':
        adjustment = 1.1
    elif data['type'] == 'secondary':
        adjustment = 0.85
    else:
        adjustment = 1.0
        fallback_used = True  # Dead variable
    
    return adjusted * adjustment

def calculate_optimal_yield(phases):
    efficiencies = []
    cumulative_stats = {'total_input': 0, 'peak_efficiency': 0}
    
    for idx, phase in enumerate(phases):
        cumulative_stats['total_input'] += phase['input']
        
        # Real computation
        efficiency = calculate_phase_efficiency(phase)
        efficiencies.append(efficiency)
        
        # Tracking peak (used later)
        if efficiency > cumulative_stats['peak_efficiency']:
            cumulative_stats['peak_efficiency'] = efficiency
        
        # Distractor: complex unused mapping
        debug_map = {i: efficiency * (i+1) for i in range(3)}
        unused_derivative = reduce(lambda a, b: a + b, debug_map.values()) / 3
    
    # Real logic: weighted yield based on peak efficiency and average
    average_eff = sum(efficiencies) / len(efficiencies)
    boost_factor = 1 + (cumulative_stats['peak_efficiency'] / 100)
    
    # Final yield calculation
    final_yield = average_eff * boost_factor
    
    # Red herring computation
    projected_next = final_yield * 1.05
    safety_margin = 0.97
    
    return final_yield

def main():
    production_phases = [
        {'input': 150, 'type': 'primary', 'loss': 0.04},
        {'input': 200, 'type': 'secondary', 'loss': 0.06},
        {'input': 175, 'type': 'primary', 'loss': 0.03}
    ]
    
    # Intermediate tracking (semi-relevant)
    total_capacity = sum(p['input'] for p in production_phases)
    scaling_ratio = total_capacity / 525  # normalized reference
    
    # Key execution point
    final_yield = calculate_optimal_yield(production_phases)
    
    # Output required format
    print(f"Result: {final_yield}")

if __name__ == "__main__":
    main()