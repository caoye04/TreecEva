from collections import defaultdict
from functools import reduce
from contextlib import contextmanager

@contextmanager
def data_stream(simulated_data):
    try:
        yield iter(simulated_data)
    finally:
        pass

def compute_biodiversity_index(sightings):
    if not sightings:
        return 0
    unique_species = len(set(sightings))
    total_sightings = len(sightings)
    return unique_species * 100 // total_sightings if total_sightings else 0

zone_reports = [
    {'zone_id': 'A', 'species': ['wolf', 'bear', 'deer', 'deer']},
    {'zone_id': 'B', 'species': ['rabbit', 'fox', 'fox', 'squirrel', 'squirrel', 'squirrel']},
    {'zone_id': 'C', 'species': ['eagle', 'hawk', 'owl']},
    {'zone_id': 'D', 'species': ['salmon', 'trout', 'bass', 'bass', 'bass', 'bass']},
    {'zone_id': 'E', 'species': ['wolf', 'wolf', 'wolf', 'wolf', 'wolf']}
]

critical_zone_count = 0
biodiversity_threshold = 25

with data_stream(zone_reports) as stream:
    zone_data_map = {zone['zone_id']: zone['species'] for zone in stream}
    
    # Compute biodiversity index for each zone
    biodiversity_scores = {
        zone_id: compute_biodiversity_index(species_list)
        for zone_id, species_list in zone_data_map.items()
    }
    
    # Apply conservation logic using short-circuit and logical operations
    for zone_id, score in biodiversity_scores.items():
        species_list = zone_data_map[zone_id]
        dominant_species_ratio = species_list.count(species_list[0]) == len(species_list)
        
        # A zone is critical if either:
        # 1. Biodiversity is low AND there's a single dominant species, OR
        # 2. There are fewer than 3 unique species regardless of other factors
        if (score < biodiversity_threshold and dominant_species_ratio) or (len(set(species_list)) < 3):
            critical_zone_count += 1
        elif score >= 50:  # Early exit for healthy zones
            continue

# Final adjustment based on overall reserve health
if critical_zone_count > len(zone_reports) // 2:
    critical_zone_count = len(zone_reports) // 2

print(f"Result: {critical_zone_count}")