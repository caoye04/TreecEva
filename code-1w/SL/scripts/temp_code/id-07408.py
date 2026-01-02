def analyze_crop_performance(plots, thresholds):
    # Irrelevant metrics for distraction
    avg_moisture = sum(p['moisture'] for p in plots) / len(plots)
    total_rainfall = sum(p['rainfall'] for p in plots)
    growth_scores = []
    
    for i, plot in enumerate(plots):
        base_yield = plot['size'] * plot['fertility']
        adjustment_factor = 1.0
        
        if plot['pests']:
            adjustment_factor *= 0.8
        
        # Real logic starts here
        stress_level = 0
        if plot['moisture'] < thresholds['min_moisture']:
            stress_level += 1
        if plot['sunlight'] < thresholds['min_sunlight']:
            stress_level += 1
        
        # Distractor: unused variable
        hypothetical_yield = base_yield * (0.5 ** stress_level)
        
        # Relevant computation with lambda
        modifier = (lambda x: 0.9 if x > 0 else 1.1)(stress_level)
        adjusted_yield = base_yield * modifier
        
        growth_scores.append((i, adjusted_yield))
    
    # Use of enumerate and zip to align indices and scores
    index_map = dict(enumerate([g[0] for g in growth_scores]))
    yields = [g[1] for g in growth_scores]
    combined = list(zip(index_map.values(), yields))
    
    # Set operations to filter high-performing plots
    high_performers = {idx for idx, yld in combined if yld >= 200}
    low_performers = {idx for idx, yld in combined if yld < 150}
    mixed_performers = set(range(len(plots))) - high_performers - low_performers
    
    # Dead code path (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print("Debug:", high_performers, low_performers)
    
    def calculate_harvest_efficiency(yields, mixed_set):
        base_efficiency = sum(yields) / len(yields)
        bonus = 0.0
        
        # Nested loop with early break
        for idx, yld in enumerate(yields):
            for _ in range(2):
                if idx in mixed_set:
                    bonus += 0.05 * yld
                    break  # Early exit
        return base_efficiency + bonus
    
    final_yield = calculate_harvest_efficiency(yields, mixed_performers)
    Result: {final_yield}