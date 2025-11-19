<<<<<<< HEAD:code/SL/scripts/temp_code/SL-MIX-S2025.py
def calculate_biodiversity_index(station_data):
    unique_species = frozenset()
    frequency_weights = {}
    diversity_threshold = 15
    
    for station_id, observations in station_data.items():
        station_species = {species for species in observations if len(species) > 3}
        unique_species |= station_species
        
        # Early return condition for exceptional biodiversity
        if len(station_species) > diversity_threshold:
            return len(unique_species) * 3
        
        for species in station_species:
            frequency_weights[species] = frequency_weights.get(species, 0) + observations.count(species)
    
    # Apply weighting formula using dictionary comprehension
    weighted_scores = {species: count * (2 if count > 5 else 1) for species, count in frequency_weights.items()}
    
    # Calculate final score with divide and conquer approach
    def sum_scores(scores_dict):
        if len(scores_dict) <= 1:
            return sum(scores_dict.values())
        mid = len(scores_dict) // 2
        keys = list(scores_dict.keys())
        left_sum = sum_scores({k: scores_dict[k] for k in keys[:mid]})
        right_sum = sum_scores({k: scores_dict[k] for k in keys[mid:]})
        return left_sum + right_sum
    
    base_score = sum_scores(weighted_scores)
    
    # Apply penalty for low diversity stations
    penalty = sum(1 for observations in station_data.values() if len({s for s in observations if len(s) > 3}) < 3)
    
    biodiversity_score = base_score - penalty
    return biodiversity_score

# Monitoring data from 4 stations
ecological_data = {
    'station_alpha': ['pinus', 'quercus', 'betula', 'pinus', 'abies', 'quercus', 'fagus'],
    'station_beta': ['salix', 'populus', 'alnus', 'salix', 'ulmus', 'populus', 'salix', 'salix'],
    'station_gamma': ['picea', 'larix', 'picea', 'abies', 'pinus'],
    'station_delta': ['quercus', 'fagus', 'castanea', 'quercus', 'tilia']
}

biodiversity_score = calculate_biodiversity_index(ecological_data)
print(f"Result: {biodiversity_score}")
=======
import re

def sanitize_metadata(doc_meta):
    return re.sub(r'[^a-zA-Z0-9_\- ]', '', doc_meta).strip()

def evaluate_clearance(doc_meta):
    sanitized = sanitize_metadata(doc_meta)
    is_internal = 'INTERNAL' in sanitized
    is_confidential = 'CONFIDENTIAL' in sanitized
    is_public = 'PUBLIC' in sanitized
    
    # Short-circuit evaluation with logical operations
    if is_public and not (is_internal or is_confidential):
        return 1
    elif is_internal and not is_confidential:
        return 2
    elif is_confidential or (is_internal and 'RESTRICTED' in sanitized):
        return 3
    else:
        return 0

documents_metadata = [
    'PUBLIC DOCUMENT',
    'INTERNAL USE ONLY - CONFIDENTIAL',
    'CONFIDENTIAL - RESTRICTED ACCESS',
    'PUBLIC RELEASE - INTERNAL REVIEW',
    'RESTRICTED CONFIDENTIAL DOCUMENT'
]

# List comprehension with generator expression
processed_levels = [evaluate_clearance(meta) for meta in documents_metadata if len(meta) > 10]

# Pattern matching for final classification
access_level = 0
match sum(processed_levels):
    case n if n > 10:
        access_level = 5
    case n if n > 7:
        access_level = 4
    case n if n > 4:
        access_level = 3
    case n if n > 1:
        access_level = 2
    case _:
        access_level = 1

print(f'Result: {access_level}')
>>>>>>> 8c5c932813e654ac18a90b0baa3958c2af7a429b:treecEva_JSON/SL/scripts/temp_code/SL-MIX-S2025.py
