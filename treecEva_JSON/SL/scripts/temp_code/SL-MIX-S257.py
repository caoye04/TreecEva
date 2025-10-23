import hashlib
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Set

def hash_particle_id(particle_id: str) -> int:
    return int(hashlib.md5(particle_id.encode()).hexdigest()[:8], 16) % 1000

@dataclass(frozen=True)
class ParticleInteraction:
    particle_a: str
    particle_b: str
    interaction_energy: float
    
    def __hash__(self):
        return hash((self.particle_a, self.particle_b))

# Particle tracking system
particle_registry = {
    'H2O_molecule_001': ['O_001', 'H_002', 'H_003'],
    'CO2_complex_002': ['C_004', 'O_005', 'O_006'],
    'NH3_structure_003': ['N_007', 'H_008', 'H_009', 'H_010']
}

interaction_map = defaultdict(set)
total_interactions = 0
unique_interactions = set()

# Process particle groups
for molecule_id, particles in particle_registry.items():
    group_hash = hash_particle_id(molecule_id)
    
    # Create interactions within molecule
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            interaction = ParticleInteraction(
                particle_a=particles[i],
                particle_b=particles[j],
                interaction_energy=(i+j) * 0.5
            )
            unique_interactions.add(interaction)
            interaction_map[group_hash].add(interaction)
    
    # Cross-molecule interactions
    for other_molecule_id, other_particles in particle_registry.items():
        if other_molecule_id != molecule_id:
            other_group_hash = hash_particle_id(other_molecule_id)
            key = tuple(sorted([group_hash, other_group_hash]))
            
            # Only process each pair once
            if key not in interaction_map:
                for p1 in particles:
                    for p2 in other_particles:
                        if p1 != p2:  # Prevent self-interaction
                            interaction = ParticleInteraction(
                                particle_a=p1,
                                particle_b=p2,
                                interaction_energy=1.0
                            )
                            unique_interactions.add(interaction)
                            interaction_map[key].add(interaction)

# Calculate total weighted interactions
for interaction_set in interaction_map.values():
    for interaction in interaction_set:
        total_interactions += int(interaction.interaction_energy * 10)

print(f"Result: {total_interactions}")