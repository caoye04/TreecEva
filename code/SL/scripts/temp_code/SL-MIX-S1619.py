from collections import Counter

region_alpha_sessions = [
    [101, 102, 103],
    [102, 104],
    [101, 103, 105],
    [102, 103, 106]
]

region_beta_sessions = [
    [103, 107],
    [101, 102, 103],
    [102, 108],
    [103, 105, 109]
]

total_sessions = len(region_alpha_sessions) + len(region_beta_sessions)
threshold = 0.75 * total_sessions

all_species = [species for session in region_alpha_sessions + region_beta_sessions for species in session]
species_counts = Counter(all_species)

qualified_species = [species for species, count in species_counts.items() if count >= threshold]

final_count = len(qualified_species)
print(f"Result: {final_count}")