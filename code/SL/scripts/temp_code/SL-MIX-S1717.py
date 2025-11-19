from functools import reduce
from collections import namedtuple

# Define region data structure
RegionData = namedtuple('RegionData', ['region_id', 'species_count', 'endemic_species'])

# Sample biodiversity data
ecosystem_regions = [
    RegionData('Amazon_Basin', 450, 120),
    RegionData('Congo_Basin', 380, 95),
    RegionData('Madagascar', 290, 180),
    RegionData('Australia_East', 320, 110),
    RegionData('Galapagos', 180, 90)
]

# Calculate regional diversity metrics
regional_metrics = {}
for region in ecosystem_regions:
    if region.species_count > 300:
        diversity_ratio = region.endemic_species / region.species_count
        normalized_score = round(diversity_ratio * 1000)
        regional_metrics[region.region_id] = normalized_score
    else:
        # Early return for insufficient data
        continue

# Compute intersection of high-diversity regions
high_diversity_regions = frozenset(region_id for region_id, score in regional_metrics.items() if score > 250)
target_regions = frozenset(['Amazon_Basin', 'Congo_Basin', 'Madagascar'])
overlap_regions = high_diversity_regions & target_regions

# Apply divide and conquer approach to calculate final index
if len(overlap_regions) >= 2:
    overlap_scores = [regional_metrics[r] for r in overlap_regions]
    max_score = max(overlap_scores)
    min_score = min(overlap_scores)
    # Comparison-based adjustment
    if max_score - min_score > 100:
        adjusted_scores = [score * 0.85 if score == max_score else score for score in overlap_scores]
    else:
        adjusted_scores = overlap_scores
    
    # Final aggregation using functional approach
    aggregate_sum = reduce(lambda x, y: x + y, adjusted_scores, 0)
    normalized_index = int(aggregate_sum / len(adjusted_scores))
else:
    normalized_index = 0

print(f"Result: {normalized_index}")