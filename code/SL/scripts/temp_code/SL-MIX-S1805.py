from functools import reduce
from dataclasses import dataclass

def accelerator_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result % 1000
    return wrapper

@accelerator_decorator
def compute_interaction(a, b):
    return (a * 17 + b * 23) % 1000

@dataclass
class Particle:
    id: int
    energy: int

particles = [Particle(i, (i * 37) % 100) for i in range(1, 6)]
interactions = [(p1.energy, p2.energy) for p1 in particles for p2 in particles if p1.id < p2.id]

energy_accumulator = 0
for idx, (e1, e2) in enumerate(interactions):
    intermediate = compute_interaction(e1, e2) if e1 > e2 else compute_interaction(e2, e1)
    energy_accumulator = (energy_accumulator + intermediate * (idx + 1)) % 1000

resonance_energy = energy_accumulator if energy_accumulator > 500 else (energy_accumulator * 3) % 1000
print(f"Result: {resonance_energy}")