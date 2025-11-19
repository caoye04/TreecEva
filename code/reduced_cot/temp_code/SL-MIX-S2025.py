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