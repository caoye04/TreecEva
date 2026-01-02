def analyze_crop_patterns(plots):
    # Irrelevant preprocessing: normalize plot IDs (distractor)
    normalized_ids = [p['id'] % 17 for p in plots]
    avg_id = sum(normalized_ids) / len(normalized_ids)

    # Extract soil quality and rainfall, filter viable plots
    viable_plots = []
    for plot in plots:
        if plot['soil_quality'] > 3 and plot['rainfall'] >= 20:
            viability_score = (plot['soil_quality'] * 0.6) + (plot['rainfall'] * 0.01)
            viable_plots.append({**plot, 'score': viability_score})

    # Sort by score descending
    viable_plots.sort(key=lambda x: x['score'], reverse=True)

    # Group into clusters based on proximity (simulated by id ranges)
    clusters = [[], [], []]
    for vp in viable_plots:
        cluster_idx = (vp['id'] // 10) % 3
        clusters[cluster_idx].append(vp)

    # Compute cluster-level metrics with list comprehensions and set ops
    cluster_scores = []
    all_ids_seen = set()
    redundant_tracker = set()
    for i, cl in enumerate(clusters):
        if not cl:
            continue
        
        # Mean score per cluster
        scores = [c['score'] for c in cl]
        mean_score = sum(scores) / len(scores)
        
        # Use set operations to detect overlap in neighboring regions (semi-relevant)
        plot_id_set = {c['id'] for c in cl}
        intersection_with_previous = plot_id_set & all_ids_seen
        all_ids_seen.update(plot_id_set)
        
        # Simulate interference via unused computation
        fake_entropy = 0
        for sid in plot_id_set:
            fake_entropy ^= (sid * 31)  # Bitwise distraction
        redundant_tracker.add(fake_entropy)
        
        # Weighted contribution: more plots = higher weight
        stability_bias = len(cl) * 0.1
        adjusted_score = mean_score + stability_bias
        cluster_scores.append(adjusted_score)
    
    return cluster_scores


def calculate_harvest_efficiency(cluster_scores):
    # Augment scores with min/max normalization (redundant step)
    if not cluster_scores:
        return 0
    
    max_score = max(cluster_scores)
    min_score = min(cluster_scores)
    
    # Normalize to 0-1 range (not actually needed)
    normalized = [(s - min_score) / (max_score - min_score + 1e-8) for s in cluster_scores]
    
    # Real logic: efficiency = average score + bonus for uniformity
    raw_average = sum(cluster_scores) / len(cluster_scores)
    variance_penalty = sum((s - raw_average) ** 2 for s in cluster_scores) / len(cluster_scores)
    uniformity_bonus = 1.0 / (1.0 + variance_penalty)  # Higher if scores are close
    
    # Final formula
    final_yield = int(raw_average * 100 + uniformity_bonus * 10)
    
    # Dead code path - never executed but looks important
    if len(cluster_scores) > 5:
        extra_adjustment = 0
        for cs in cluster_scores:
            extra_adjustment += cs % 7
        final_yield -= int(extra_adjustment)
    
    return final_yield

# Main execution
plots_data = [
    {'id': 25, 'soil_quality': 5, 'rainfall': 22},
    {'id': 32, 'soil_quality': 2, 'rainfall': 18},  # filtered out
    {'id': 36, 'soil_quality': 4, 'rainfall': 25},
    {'id': 41, 'soil_quality': 6, 'rainfall': 19},  # filtered out
    {'id': 44, 'soil_quality': 5, 'rainfall': 30},
    {'id': 53, 'soil_quality': 3, 'rainfall': 20},
    {'id': 58, 'soil_quality': 4, 'rainfall': 24},
    {'id': 62, 'soil_quality': 2, 'rainfall': 35},  # filtered out
    {'id': 67, 'soil_quality': 5, 'rainfall': 28}
]

intermediate_result = analyze_crop_patterns(plots_data)
final_yield = calculate_harvest_efficiency(intermediate_result)
print(f"Target result: {final_yield}")