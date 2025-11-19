import itertools

def calculate_biodiversity_index(habitat_data):
    species_sets = [frozenset(location) for location in habitat_data]
    intersection_weights = {}
    
    # Generate all pairwise combinations of habitats
    for h1, h2 in itertools.combinations(range(len(species_sets)), 2):
        intersection = species_sets[h1] & species_sets[h2]
        if intersection:
            weight = len(intersection) * (h1 + h2 + 2)
            intersection_weights[(h1, h2)] = weight
    
    # Apply dynamic programming to accumulate weighted intersections
    dp = [0] * (len(species_sets) + 1)
    for i in range(1, len(species_sets) + 1):
        dp[i] = dp[i-1] + sum(w for (h1, h2), w in intersection_weights.items() if h2 == i-1)
    
    # Calculate final biodiversity score with conditional adjustments
    base_score = dp[-1]
    unique_species_bonus = len(set().union(*species_sets)) * 3
    
    overlap_penalty = 0
    for (h1, h2), weight in intersection_weights.items():
        if weight > 10:
            overlap_penalty += weight // 2
    
    biodiversity_score = base_score + unique_species_bonus - overlap_penalty
    return biodiversity_score

# Research data: species identifiers in different habitat locations
research_sites = [
    ['SP001', 'SP002', 'SP003', 'SP004'],
    ['SP003', 'SP004', 'SP005', 'SP006'],
    ['SP005', 'SP006', 'SP007', 'SP008'],
    ['SP001', 'SP005', 'SP009', 'SP010']
]

biodiversity_score = calculate_biodiversity_index(research_sites)
print(f"Result: {biodiversity_score}")