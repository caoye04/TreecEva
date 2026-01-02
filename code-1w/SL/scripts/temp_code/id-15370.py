def analyze_soil_composition(data):
    # Irrelevant helper function – dead code path
    return sum(x ** 0.5 for x in data if x > 5)


def normalize_readings(readings):
    # Distractor function: looks important but unused
    return [round(r / max(readings), 3) for r in readings]


def compute_root_depth(profile):
    # Another decoy function with misleading calculations
    depth = 0
    for p in profile:
        if p > 20:
            depth += p // 4
    return depth + 11  # red herring result


def calculate_harvest_efficiency(metrics, cycles):
    cumulative_gain = 0
    efficiency_log = []
    
    # Simulate multi-phase crop growth cycle
    for i, (zone, values) in enumerate(zip(['north', 'south', 'east', 'west'], metrics)):
        base_yield = 0
        adjustment_factor = 1.0
        
        # Process each growth stage
        for stage in cycles:
            stage_total = 0
            for j, val in enumerate(values):
                # Bit manipulation distractor
                masked_val = val ^ 7 & 3
                if stage == 'germination':
                    stage_total += val * 0.3
                elif stage == 'growth':
                    stage_total += val * (1 + (j % 3) * 0.1)
                elif stage == 'maturation':
                    # Conditional expression used idiomatically
                    bonus = 2.5 if (val > 40 and i + j) % 2 == 0 else 0.0
                    stage_total += val * 0.8 + bonus
            
            # Accumulate per-stage yield
            base_yield += stage_total
        
        # Apply zone-specific modifier (only some are relevant)
        modifiers = {'north': 1.1, 'south': 0.95, 'east': 1.05, 'west': 1.0}
        adjusted_yield = base_yield * modifiers.get(zone, 1.0)
        efficiency_log.append(adjusted_yield)
    
    # Final aggregation with filtering
    filtered_yields = [y for y in efficiency_log if y > 150]  # exclude low yields
    total_efficiency = sum(filtered_yields)
    
    # Decoy computation: looks like normalization but unused
    if len(filtered_yields) > 0:
        average_decoy = total_efficiency / len(filtered_yields)
        normalized = [round((y - average_decoy) / average_decoy, 4) for y in filtered_yields]
        _ = sum(normalized)  # unused result
    
    # Key answer computation
    final_yield = int(total_efficiency / 2)  # actual deterministic answer
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Real input data
    area_metrics = [
        [34, 45, 52, 38],  # north zone
        [40, 38, 41, 39],  # south zone
        [47, 50, 45, 49],  # east zone
        [42, 44, 43, 46]   # west zone
    ]
    
    growth_cycles = ['germination', 'growth', 'maturation']
    
    # Irrelevant preprocessing steps
    processed_data = [x for row in area_metrics for x in row if x % 2 == 0]
    squared_evens = [n ** 2 for n in processed_data]  # dead-end calculation
    _ = sum(squared_evens) / len(squared_evens) if squared_evens else 0  # unused stat
    
    # Soil analysis – calls irrelevant function
    soil_profile = [12, 25, 30, 18, 22]
    _ = compute_root_depth(soil_profile)
    
    # Critical statement
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    
    # Output result as required
    print(f"Target result: {final_yield}")