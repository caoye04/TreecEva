from collections import defaultdict, Counter
import math

def compute_zone_diversity(species_data, zone_weights):
    zone_species = defaultdict(set)
    for record in species_data:
        zone, species = record['zone'], record['species']
        if record['confidence'] > 0.7:
            zone_species[zone].add(species)
    
    diversity_scores = {}
    for zone, species_set in zone_species.items():
        unique_count = len(species_set)
        if unique_count > 0:
            # Calculate weighted diversity index
            weight = zone_weights.get(zone, 1.0)
            raw_score = unique_count * math.log(unique_count + 1)
            diversity_scores[zone] = raw_score * weight
    return diversity_scores

# Biodiversity dataset
ecological_records = [
    {'zone': 'A', 'species': 'SP-001', 'confidence': 0.85},
    {'zone': 'A', 'species': 'SP-002', 'confidence': 0.92},
    {'zone': 'A', 'species': 'SP-001', 'confidence': 0.65},  # Low confidence, filtered out
    {'zone': 'A', 'species': 'SP-003', 'confidence': 0.78},
    {'zone': 'B', 'species': 'SP-004', 'confidence': 0.88},
    {'zone': 'B', 'species': 'SP-005', 'confidence': 0.72},
    {'zone': 'B', 'species': 'SP-004', 'confidence': 0.91},
    {'zone': 'C', 'species': 'SP-006', 'confidence': 0.83},
    {'zone': 'C', 'species': 'SP-007', 'confidence': 0.68},  # Low confidence, filtered out
]

zone_weighting_factors = {'A': 1.2, 'B': 0.9, 'C': 1.5}

# Compute initial diversity scores
zone_diversity_map = compute_zone_diversity(ecological_records, zone_weighting_factors)

# Apply additional ecological corrections
adjusted_scores = {}
for zone, score in zone_diversity_map.items():
    # Apply correction based on zone characteristics
    if zone == 'A':
        adjusted_scores[zone] = score * 1.1
    elif zone == 'B':
        adjusted_scores[zone] = score * 0.95
    else:  # Zone C
        adjusted_scores[zone] = score * 1.05

# Calculate final ecosystem health score
final_eco_score = sum(adjusted_scores.values())

# Apply normalization factor
normalization_factor = len(adjusted_scores) / (len(adjusted_scores) + 1)
final_eco_score *= normalization_factor

print(f"Result: {round(final_eco_score, 2)}")