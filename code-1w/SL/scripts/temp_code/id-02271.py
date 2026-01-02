from collections import defaultdict

# Simulate agricultural yield prediction based on plot conditions and soil data
def main():
    plots = [
        {'id': 'A1', 'size': 10, 'crop': 'wheat', 'irrigated': True},
        {'id': 'A2', 'size': 15, 'crop': 'corn', 'irrigated': False},
        {'id': 'A3', 'size': 12, 'crop': 'wheat', 'irrigated': True},
        {'id': 'A4', 'size': 8, 'crop': 'barley', 'irrigated': True},
        {'id': 'A5', 'size': 20, 'crop': 'corn', 'irrigated': True}
    ]

    soil_quality = {
        'A1': 0.8, 'A2': 0.5, 'A3': 0.75, 'A4': 0.6, 'A5': 0.9
    }

    # Irrelevant preprocessing: normalize plot IDs (not used in final calculation)
    normalized_ids = [p['id'].replace('A', 'PLOT_') for p in plots]
    _ = [id.lower() for id in normalized_ids]  # Dead computation

    # Track crop counts (semi-relevant, but not directly used in final formula)
    crop_counter = defaultdict(int)
    for plot in plots:
        crop_counter[plot['crop']] += plot['size']

    # Auxiliary metric: average soil quality per crop (distractor)
    avg_soil_per_crop = defaultdict(float)
    crop_count = defaultdict(int)
    for plot in plots:
        crop = plot['crop']
        plot_id = plot['id']
        avg_soil_per_crop[crop] += soil_quality[plot_id]
        crop_count[crop] += 1
    
    for crop in avg_soil_per_crop:
        if crop_count[crop] > 0:
            avg_soil_per_crop[crop] /= crop_count[crop]

    # Misleading efficiency score based on irrigation only
    irrigated_plots = [p for p in plots if p['irrigated']]
    non_irrigated_plots = [p for p in plots if not p['irrigated']]
    fake_efficiency = len(irrigated_plots) * 0.3 - len(non_irrigated_plots) * 0.1

    # Real calculation begins: yield depends on size, soil, and crop type multiplier
    def calculate_base_yield(plot, soil_score):
        base_multiplier = 1.0
        if plot['crop'] == 'wheat':
            base_multiplier = 2.5
        elif plot['crop'] == 'corn':
            base_multiplier = 3.0
        elif plot['crop'] == 'barley':
            base_multiplier = 1.8
        
        # Yield = size * soil_quality * crop_multiplier
        return plot['size'] * soil_score * base_multiplier

    # Intermediate aggregation by crop (semi-relevant)
    yield_by_crop = defaultdict(float)
    total_potential_size = 0
    weighted_yield_sum = 0.0

    for i, plot in enumerate(plots):
        plot_id = plot['id']
        soil_score = soil_quality[plot_id]
        raw_yield = calculate_base_yield(plot, soil_score)
        yield_by_crop[plot['crop']] += raw_yield
        
        # Accumulate for overall efficiency
        total_potential_size += plot['size']
        weighted_yield_sum += raw_yield

        # Red herring: adjust for index parity (never used)
        if i % 2 == 0:
            _ = raw_yield * 0.95  # Distractor
        else:
            _ = raw_yield * 1.05  # Distractor

    # Calculate final harvest efficiency as weighted average yield per unit area
    if total_potential_size > 0:
        preliminary_efficiency = weighted_yield_sum / total_potential_size
    else:
        preliminary_efficiency = 0

    # Apply bonus for high soil quality consistency (measured via variance distractor)
    qualities = list(soil_quality.values())
    mean_q = sum(qualities) / len(qualities)
    variance = sum((x - mean_q) ** 2 for x in qualities) / len(qualities)  # Computed but unused

    # Final adjustment: +0.25 if all irrigated plots have above-average soil
    irrigated_qualities = [soil_quality[p['id']] for p in irrigated_plots]
    if irrigated_qualities and all(q > 0.65 for q in irrigated_qualities):
        final_yield = preliminary_efficiency + 0.25
    else:
        final_yield = preliminary_efficiency

    # Print result as required
    print(f"Result: {final_yield}")
    return final_yield

# Execute main function
def calculate_harvest_efficiency(plots, soil_map):
    # Wrapper to simulate external call
    return main()

# Global invocation
result = main()
