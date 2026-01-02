def calculate_optimal_yield(data):
    # Preprocessing: filter valid species using lambda and string methods
    valid_species = list(filter(lambda x: x['name'].upper().startswith('A') and 'habitat' in x, data))
    
    # Irrelevant computation: calculate average lifespan (not used in final result)
    avg_lifespan = sum([s['lifespan'] for s in data if 'lifespan' in s]) / len([s for s in data if 'lifespan' in s]) if data else 0
    
    # Distractor: complex but unused set operation
    all_traits = set()
    for species in data:
        if 'traits' in species:
            all_traits.update(species['traits'])
    unique_trait_letters = {c for trait in all_traits for c in trait}.intersection(set('abcdef'))

    # Core logic: compute yield based on abundance and growth rate
    base_yields = []
    for species in valid_species:
        if species['abundance'] > 50:
            adjusted_growth = species.get('growth_rate', 1.0) * 0.8
        else:
            adjusted_growth = species.get('growth_rate', 1.0) * 1.2
        
        # Secondary filtering: only consider species with sufficient resilience
        resilience_score = 0
        if 'resilience' in species:
            resilience_parts = species['resilience'].split('/')
            if len(resilience_parts) == 2:
                resilience_score = int(resilience_parts[0]) / int(resilience_parts[1])
        
        if resilience_score >= 0.5:
            base_yields.append(species['abundance'] * adjusted_growth)
    
    # Tertiary distractor: unused dictionary aggregation
    habitat_summary = {}
    for species in data:
        loc = species.get('habitat', 'unknown').lower()
        if loc not in habitat_summary:
            habitat_summary[loc] = {'count': 0, 'total_abundance': 0}
        habitat_summary[loc]['count'] += 1
        habitat_summary[loc]['total_abundance'] += species.get('abundance', 0)
    
    # Final calculation
    if not base_yields:
        return 0.0
    
    raw_yield = sum(base_yields)
    efficiency_factor = 0.9 if len(valid_species) > 2 else 0.7
    penalty = len([y for y in base_yields if y < 30]) * 2.5  # small yield penalty
    final_yield = (raw_yield * efficiency_factor) - penalty
    
    return max(final_yield, 0)  # ensure non-negative

# Simulated ecosystem dataset
ecosystem_data = [
    {'name': 'Apexa vulgata', 'abundance': 65, 'growth_rate': 1.5, 'habitat': 'Forest', 'resilience': '3/4'},
    {'name': 'Aquilonis borealis', 'abundance': 40, 'growth_rate': 2.0, 'habitat': 'Tundra', 'resilience': '5/6'},
    {'name': 'Arelia marina', 'abundance': 80, 'growth_rate': 1.2, 'habitat': 'Coastal', 'resilience': '2/5'},
    {'name': 'Boreothrix zena', 'abundance': 70, 'growth_rate': 1.8, 'habitat': 'Forest', 'resilience': '4/5'},
    {'name': 'Apsera villosa', 'abundance': 55, 'growth_rate': 1.6, 'habitat': 'Grassland', 'resilience': '3/3'}
]

# Execution point of interest
final_yield = calculate_optimal_yield(ecosystem_data)
print(f"Result: {final_yield}")