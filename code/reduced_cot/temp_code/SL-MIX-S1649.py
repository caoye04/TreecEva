from collections import defaultdict
import hashlib

def hash_particle(particle_type, index):
    return hashlib.md5(f"{particle_type}_{index}".encode()).hexdigest()

def get_valid_interactions(particle_types, max_pairs):
    valid_combinations = []
    type_counter = defaultdict(int)
    
    # Generate all possible pairs with replacement
    for i, type1 in enumerate(particle_types):
        for j, type2 in enumerate(particle_types[i:], i):
            if i != j or particle_types.count(type1) > 1:
                pair = tuple(sorted([type1, type2]))
                if type_counter[pair] < max_pairs:
                    valid_combinations.append(pair)
                    type_counter[pair] += 1
    
    # Remove duplicates while preserving order
    unique_interactions = list(dict.fromkeys(valid_combinations))
    return len(unique_interactions)

class SimulationContext:
    def __init__(self, particles):
        self.particles = particles
        self.interaction_hashes = set()
    
    def __enter__(self):
        # Precompute hashes for all particles
        for idx, particle in enumerate(self.particles):
            particle_hash = hash_particle(particle, idx)
            self.interaction_hashes.add(particle_hash)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Particle types in the simulation
particle_species = ['H', 'O', 'C', 'N', 'S']
max_interaction_pairs = 2

with SimulationContext(particle_species) as sim:
    total_unique_interactions = get_valid_interactions(particle_species, max_interaction_pairs)
    # Adjust for symmetric interactions and self-interactions
    adjusted_interactions = total_unique_interactions
    if len(particle_species) > 2:
        adjusted_interactions = total_unique_interactions - len(particle_species) + len(set(particle_species))
    
    final_interaction_count = adjusted_interactions * len(sim.interaction_hashes) // len(particle_species)

print(f"Result: {final_interaction_count}")