def analyze_soil_quality(plots):
    quality_scores = []
    for plot in plots:
        base_score = plot['nutrients'] * 0.4 + plot['moisture'] * 0.6
        adjustment = 0
        if plot['ph'] < 5.5 or plot['ph'] > 7.5:
            adjustment = -10
        elif 6.0 <= plot['ph'] <= 7.0:
            adjustment = 5
        adjusted_score = base_score + adjustment
        quality_scores.append(adjusted_score)
    return quality_scores


def filter_viable_plots(plots):
    viable = []
    temp_invalid_count = 0
    for i, plot in enumerate(plots):
        if plot['area'] <= 0:
            temp_invalid_count += 1
            continue
        sunlight_ok = plot['sunlight_hours'] >= 6
        space_ok = plot['area'] >= 10
        if sunlight_ok and space_ok:
            viable.append(plot)
    # Irrelevant sorting (distractor)
    sorted(viable, key=lambda x: x['area'])
    return viable


def optimize_harvest(filtered_plots):
    yields = []
    buffer_zone = 2  # Unused distraction
    total_aux_energy = 0

    for plot in filtered_plots:
        # Primary yield calculation
        raw_yield = plot['area'] * 0.8
        
        # Conditional boost based on soil quality score (computed earlier)
        if 'score' in plot and plot['score'] > 60:
            raw_yield *= 1.25
        
        # Simulate diminishing returns with large areas
        if plot['area'] > 50:
            raw_yield *= 0.9
        
        yields.append(raw_yield)
    
    # Secondary processing with list comprehension (relevant)
    boosted_yields = [y * 1.1 for y in yields if y < 40]
    
    # Merging original and boosted where applicable
    final_individual_yields = []
    for y in yields:
        if y < 40:
            final_individual_yields.append(y * 1.1)
        else:
            final_individual_yields.append(y)
    
    # Aggregate result
    aggregate = sum(final_individual_yields)
    
    # Fake optimization step (distractor)
    convergence_reached = True
    iteration_limit = 100
    for _ in range(iteration_limit):
        if aggregate > 1000:
            convergence_reached = False
            break
    
    # Final scaling based on number of plots
    scaling_factor = len(filtered_plots) / max(len(final_individual_yields), 1)
    return int(aggregate * scaling_factor)


# Main execution
if __name__ == '__main__':
    # Input data: agricultural plots
    field_data = [
        {'area': 30, 'nutrients': 70, 'moisture': 60, 'ph': 6.5, 'sunlight_hours': 8},
        {'area': 60, 'nutrients': 50, 'moisture': 40, 'ph': 4.0, 'sunlight_hours': 7},
        {'area': 25, 'nutrients': 80, 'moisture': 75, 'ph': 6.8, 'sunlight_hours': 5},  # Low sunlight
        {'area': 45, 'nutrients': 65, 'moisture': 70, 'ph': 6.2, 'sunlight_hours': 9},
        {'area': 15, 'nutrients': 90, 'moisture': 80, 'ph': 5.0, 'sunlight_hours': 10}
    ]

    # Step 1: Filter viable plots based on area and sunlight
    processed_plots = filter_viable_plots(field_data)

    # Step 2: Analyze soil quality (score used later)
    scores = analyze_soil_quality(processed_plots)
    for i, score in enumerate(scores):
        processed_plots[i]['score'] = score

    # Step 3: Optimize harvest yield calculation
    auxiliary_sum = sum(p['nutrients'] for p in processed_plots)  # Distractor
    normalization_constant = 100  # Unused variable
    metadata_log = {'run_id': 'AGRI_2024', 'status': 'completed'}  # Dead code

    final_yield = optimize_harvest(processed_plots)
    print(f"Result: {final_yield}")