from dataclasses import dataclass
from typing import Set, FrozenSet
import base64

def encode_id(particle_id: int) -> str:
    return base64.b64encode(str(particle_id).encode()).decode()

def decode_id(encoded_str: str) -> int:
    return int(base64.b64decode(encoded_str.encode()).decode())

@dataclass(frozen=True)
class ParticleInteraction:
    primary_id: int
    secondary_ids: FrozenSet[int]
    
    def get_interaction_potential(self) -> int:
        return sum(self.secondary_ids) * (self.primary_id if self.primary_id > 0 else 1)

# Initial particle identifiers
initial_particles = [12, -5, 8, 0, 15]
encoded_particles = [encode_id(pid) for pid in initial_particles]

def process_particles(encoded_list):
    decoded_set = {decode_id(e) for e in encoded_list}
    positive_particles = {p for p in decoded_set if p > 0}
    negative_particles = {abs(p) for p in decoded_set if p < 0}
    neutral_particle = 1 if 0 in decoded_set else 0
    
    # Ternary operator for conditional assignment
    effective_neutral = neutral_particle if neutral_particle != 0 else len(positive_particles)
    
    # Create interaction object
    interaction_obj = ParticleInteraction(
        primary_id=max(positive_particles) if positive_particles else 0,
        secondary_ids=frozenset(negative_particles.union({effective_neutral}))
    )
    
    return interaction_obj.get_interaction_potential()

# String transformations on particle data
transformed_data = []
for ep in encoded_particles:
    # Apply multiple string operations
    modified = ep.replace('=', '').lower()[::-1]  # Remove =, lowercase, reverse
    restored = modified[::-1].upper() + '=='  # Reverse back, uppercase, add padding
    transformed_data.append(restored)

# Process the transformed data
aggregated_score = process_particles(transformed_data)
print(f"Result: {aggregated_score}")