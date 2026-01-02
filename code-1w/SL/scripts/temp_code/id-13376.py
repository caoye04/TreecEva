def calculate_harvest_efficiency(plots, soil_quality):
    base_multiplier = 1.5
    efficiency_map = {1: 0.8, 2: 1.1, 3: 1.5, 4: 1.3, 5: 0.9}
    temp_results = []
    total_adjustment = 0.0
    cumulative_score = 0
    
    for plot_id, details in plots.items():
        size = details['size']
        crop_type = details['crop']
        irrigation = details['irrigation']
        
        # Irrelevant scoring for distraction
        if crop_type == 'wheat':
            local_score = size * 1.2
        elif crop_type == 'corn':
            local_score = size * 1.4
        else:
            local_score = size * 1.0
        
        cumulative_score += local_score
        
        # Real computation path
        soil_rank = soil_quality.get(plot_id, 1)
        efficiency_factor = efficiency_map.get(soil_rank, 1.0)
        
        yield_potential = size * base_multiplier * efficiency_factor
        
        if irrigation:
            yield_potential *= 1.25
        
        # Distractor: complex adjustment not used in final result
        adjustment_noise = (yield_potential % 7) * 0.1
        total_adjustment += adjustment_noise
        
        temp_results.append(yield_potential)
    
    # Final computation using relevant data only
    raw_total = sum(temp_results)
    plot_count = len(plots)
    average_penalty = 0.95 if plot_count > 3 else 1.0
    
    final_yield = int(raw_total * average_penalty)
    
    # Misleading intermediate print (not affecting logic)
    debug_value = cumulative_score / (raw_total + 1e-8)
    
    return final_yield

# Data setup
plots = {
    101: {'size': 20, 'crop': 'wheat', 'irrigation': True},
    102: {'size': 15, 'crop': 'corn', 'irrigation': False},
    103: {'size': 25, 'crop': 'wheat', 'irrigation': True},
    104: {'size': 10, 'crop': 'barley', 'irrigation': True}
}

soil_quality = {101: 2, 102: 3, 103: 4, 104: 1}

# Execution point
final_yield = calculate_harvest_efficiency(plots, soil_quality)
print(f"Result: {final_yield}")