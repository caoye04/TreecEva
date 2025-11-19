from functools import lru_cache

def modified_edit_distance(obs1, obs2):
    m, n = len(obs1), len(obs2)
    
    @lru_cache(maxsize=None)
    def dp(i, j):
        if i == 0:
            return j * 1.5
        if j == 0:
            return i * 1.5
        
        cost = 0 if obs1[i-1] == obs2[j-1] else 1.2
        
        deletion = dp(i-1, j) + 1.5
        insertion = dp(i, j-1) + 1.5
        substitution = dp(i-1, j-1) + cost
        
        # Ternary operator for bonus rule
        bonus = 0.3 if i > 1 and j > 1 and obs1[i-1] == obs2[j-2] and obs1[i-2] == obs2[j-1] else 0
        
        return min(deletion, insertion, substitution) - bonus
    
    return dp(m, n)

def calculate_species_similarity(observations):
    total_score = 0.0
    n = len(observations)
    
    for i in range(n):
        for j in range(i+1, n):
            score = modified_edit_distance(observations[i], observations[j])
            total_score += score if score > 0 else 0  # Logical AND operation
    
    return total_score

# Tide pool species observation sequences
species_observations = [
    "ABCDGHI",
    "ABCEHI",
    "ACDFGI",
    "BCDEHI"
]

biodiversity_score = calculate_species_similarity(species_observations)
observation_count = len(species_observations)

# Final index calculation with floating point operations and logical operations
final_biodiversity_index = biodiversity_score / observation_count if observation_count > 0 and biodiversity_score >= 0 else 0

print(f"Result: {final_biodiversity_index}")