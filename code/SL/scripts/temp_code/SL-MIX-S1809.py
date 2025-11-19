from collections import defaultdict
import math

class SimulationLogger:
    def __enter__(self):
        self.log = []
        return self
    
    def record(self, event):
        self.log.append(event)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def breeding_season(population, season_factor):
    if population <= 1:
        return population
    adjusted_population = int(population * season_factor)
    return breeding_season(adjusted_population // 2, season_factor) + breeding_season(adjusted_population // 2, season_factor)

@count_calls
def resolve_conflict(species_a, species_b, territory_matrix):
    if species_a >= len(territory_matrix) or species_b >= len(territory_matrix[0]):
        return 0
    if territory_matrix[species_a][species_b] == 1:
        return 1
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = species_a + dx, species_b + dy
            if 0 <= nx < len(territory_matrix) and 0 <= ny < len(territory_matrix[0]):
                if resolve_conflict(nx, ny, territory_matrix):
                    return 1
    return 0

state_machine = {
    'SPRING': 'BREEDING',
    'BREEDING': 'CONFLICT',
    'CONFLICT': 'STABILIZE',
    'STABILIZE': 'SPRING'
}

territory_map = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

initial_populations = [12, 18, 9]
seasonal_factors = [1.2, 1.5, 0.8]
conflict_threshold = 2

total_breeding_cycles = 0
conflict_resolutions = 0
ecosystem_stability_index = 0

with SimulationLogger() as logger:
    current_state = 'SPRING'
    for season in range(3):
        next_state = state_machine[current_state]
        logger.record(f"Transitioning from {current_state} to {next_state}")
        
        if next_state == 'BREEDING':
            for i in range(len(initial_populations)):
                new_pop = breeding_season(initial_populations[i], seasonal_factors[i])
                total_breeding_cycles += new_pop
                initial_populations[i] = new_pop
        
        elif next_state == 'CONFLICT':
            for i in range(len(territory_map)):
                for j in range(len(territory_map[i])):
                    if resolve_conflict(i, j, territory_map):
                        conflict_resolutions += 1
        
        elif next_state == 'STABILIZE':
            stability_sum = sum(initial_populations)
            ecosystem_stability_index = stability_sum - (conflict_resolutions * conflict_threshold) + total_breeding_cycles
        
        current_state = next_state

print(f"Result: {ecosystem_stability_index}")