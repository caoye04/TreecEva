import itertools

def analyze_soil_composition(elements):
    # Irrelevant helper function with distracting computation
    weighted_sum = 0
    for elem in elements:
        if elem % 3 == 0:
            weighted_sum += elem * 1.5
        elif elem % 5 == 0:
            weighted_sum += elem * 0.8
    return weighted_sum

def calculate_harvest_efficiency(metrics, cycles):
    base_efficiency = 0
    adjustment_factor = 0.95
    
    # Real logic starts here — multiple steps with nesting and comprehension
    for metric in metrics:
        temp_score = 0
        
        # Key computational block
        if metric['type'] == 'fertile':
            values = [v for v in metric['readings'] if v > 50]  # List comprehension
            if len(values) > 0:
                avg_val = sum(values) / len(values)
                temp_score = avg_val * 1.2
        elif metric['type'] == 'barren':
            capped_max = min(max(metric['readings']), 75)
            temp_score = capped_max * 0.4
        
        base_efficiency += temp_score
    
    # Apply cycle-based decay (relevant)
    for i in range(len(cycles)):
        base_efficiency *= (0.9 + 0.05 * cycles[i]['rainfall'])
    
    # Distractor: unused transformation
    normalized = [round(x['ph'], 2) for x in metrics if 'ph' in x]
    ph_aggregate = sum(normalized) / len(normalized) if normalized else 7.0
    
    # Final calculation (answer depends only on real path)
    final = base_efficiency * adjustment_factor
    
    # Dead code: never used
    outlier_check = list(itertools.combinations([m['readings'][0] for m in metrics], 2))
    
    return int(final)

# Main execution block
soil_elements = [12, 18, 25, 30, 45, 60]
dummy_analysis = analyze_soil_composition(soil_elements)

area_metrics = [
    {
        'type': 'fertile',
        'readings': [65, 70, 80, 55],
        'ph': 6.8
    },
    {
        'type': 'barren',
        'readings': [30, 40, 90, 20],
        'ph': 5.2
    },
    {
        'type': 'fertile',
        'readings': [75, 85, 95],
        'ph': 7.1
    }
]

growth_cycles = [
    {'season': 'spring', 'rainfall': 1},
    {'season': 'summer', 'rainfall': 0},
    {'season': 'autumn', 'rainfall': 2}
]

intermediate_total = sum(m['readings'][0] for m in area_metrics)  # Distractor variable
buffer_zone_ratio = intermediate_total / 100  # Unused but looks important

final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Print result as required
print(f"Result: {final_yield}")