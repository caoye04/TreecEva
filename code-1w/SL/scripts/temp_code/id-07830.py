def analyze_soil(terrain):
    # Irrelevant soil analysis with decoy computations
    nutrients = {k: v * 0.3 for k, v in terrain.items()}
    ph_levels = [round((val % 7) + 5, 2) for val in nutrients.values()]
    return sum(ph_levels) / len(ph_levels)


def simulate_rainfall(days):
    # Misleading weather simulation (dead code path)
    total_rain = 0
    for d in range(days):
        if d % 5 == 0:
            total_rain += d * 0.7
    return total_rain


def track_pest_migration(zone_map):
    # Distractor function: computes pest zones but unused in final logic
    infested = []
    for region, data in zone_map.items():
        risk = sum(data.get('edges', [])) * data.get('temp', 0)
        if risk > 50:
            infested.append(region)
    return infested


def calculate_harvest(regions, pests_present):
    # Core logic buried among distractions
    base_yield = 0
    bonuses = []
    penalties = {}

    for name, attrs in regions.items():
        # Relevant calculation: yield based on size and fertility
        contribution = attrs['size'] * attrs['fertility']

        # Conditional bonus logic (actual impact)
        if attrs['fertility'] > 0.7:
            bonuses.append(contribution * 0.1)

        # Penalty only applies if pests are present in specific region
        if pests_present.get(name, False):
            penalties[name] = contribution * 0.25

        base_yield += contribution

    # Real computation path: apply penalties only when pests present
    net_loss = sum(penalties.values())
    adjusted_yield = base_yield - net_loss

    # Final adjustment using list comprehension (required feature)
    growth_factors = [1.05 if b > 50 else 1.0 for b in bonuses]
    boosted_yield = adjusted_yield * (sum(growth_factors) / len(growth_factors)) if growth_factors else adjusted_yield

    # Determine final result via conditional expression (required feature)
    final_yield = boosted_yield if adjusted_yield > 1000 else boosted_yield * 0.92

    return final_yield

# Main execution block
if __name__ == '__main__':
    # Complex input structure with red herring fields
    regions = {
        'alpha': {'size': 120, 'fertility': 0.85, 'elevation': 150, 'edges': [3, 7, 2], 'temp': 22},
        'beta': {'size': 95, 'fertility': 0.65, 'elevation': 200, 'edges': [5, 1], 'temp': 25},
        'gamma': {'size': 140, 'fertility': 0.90, 'elevation': 110, 'edges': [8], 'temp': 20},
        'delta': {'size': 80, 'fertility': 0.55, 'elevation': 180, 'edges': [2, 4, 6], 'temp': 27}
    }

    # Pest presence map — only two regions actually matter
    pests_present = {'alpha': True, 'gamma': True}  # beta and delta unaffected

    # Irrelevant pre-processing steps
    avg_soil = analyze_soil({k: v['elevation'] for k, v in regions.items()})
    projected_rain = simulate_rainfall(30)

    # Critical execution point
    final_yield = calculate_harvest(regions, pests_present)

    # Track decoy pest migration (unused result)
    active_infestations = track_pest_migration(regions)

    # Output the required result
    print(f"Result: {final_yield}")