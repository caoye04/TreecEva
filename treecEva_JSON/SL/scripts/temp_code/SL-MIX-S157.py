from dataclasses import dataclass
from functools import wraps

def modular_transform(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result % 17
    return wrapper

@dataclass
class ParticleState:
    id: int
    spin: int
    entangled: bool = False

@modular_transform
def calculate_entanglement(particles):
    total = 0
    for particle in particles:
        if particle.entangled:
            total += particle.spin * 3
        else:
            total -= particle.spin * 2
    return total

particles = [
    ParticleState(1, 5, True),
    ParticleState(2, 3, False),
    ParticleState(3, 7, True),
    ParticleState(4, 2, True),
    ParticleState(5, 4, False)
]

entanglement_index = calculate_entanglement(particles)

for i in range(len(particles)):
    if particles[i].spin > 4:
        particles[i].entangled = not particles[i].entangled
        if particles[i].entangled:
            entanglement_index += particles[i].spin
            break
    else:
        entanglement_index -= particles[i].spin

entanglement_index = (entanglement_index * 3) % 19
print(f"Result: {entanglement_index}")