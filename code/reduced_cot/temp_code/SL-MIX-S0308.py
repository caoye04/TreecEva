import math

class EnergyTracker:
    def __init__(self):
        self.total_energy_loss = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def record_loss(self, loss):
        self.total_energy_loss += loss

def correction_factor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 1.25 if result > 0 else result * 0.9
    return wrapper

@correction_factor
def calculate_base_score(particles_count, decay_constant):
    base = particles_count * math.log(decay_constant)
    adjusted = base - (particles_count // 3)
    return adjusted

initial_particles = 120
constant = 7
correction_applied = False
final_score = 0

with EnergyTracker() as tracker:
    base_score = calculate_base_score(initial_particles, constant)
    tracker.record_loss(initial_particles * 0.05)
    corrected_base = base_score - tracker.total_energy_loss
    if corrected_base > 50:
        final_score = int(corrected_base * 1.1)
    else:
        final_score = int(corrected_base * 0.95)

print(f'Result: {final_score}')