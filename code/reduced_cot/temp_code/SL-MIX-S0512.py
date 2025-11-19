from collections import deque
from math import factorial as fact

def combinatorial_selection(n, k):
    if k > n or k < 0:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

class ForestSimulation:
    def __init__(self, initial_pairs):
        self.mature_pairs = initial_pairs
        self.offspring_queue = deque([0] * 3)
        self.genetic_scores = []
    
    def next_generation(self):
        # Fibonacci-like reproduction with environmental factor
        new_offspring = self.mature_pairs + self.offspring_queue[0]
        survival_rate = 0.7 if new_offspring > 10 else 0.9
        
        # Update queue and mature pairs
        self.offspring_queue.append(new_offspring)
        matured = self.offspring_queue.popleft()
        self.mature_pairs += matured
        
        # Genetic diversity calculation using combinatorics
        genetic_options = combinatorial_selection(self.mature_pairs, 2)
        diversity_score = genetic_options * survival_rate
        self.genetic_scores.append(diversity_score)
        
        return diversity_score

# Initialize simulation
ecosystem = ForestSimulation(3)
simulation_cycles = 5
survival_index = 0

# Run simulation
for cycle in range(simulation_cycles):
    score = ecosystem.next_generation()
    survival_index = survival_index + score if cycle % 2 == 0 else survival_index

# Apply final adjustment based on total genetic health
final_genetic_pool = sum(ecosystem.genetic_scores)
total_mature_pairs = ecosystem.mature_pairs
survival_index = int(survival_index * 0.5) if final_genetic_pool > total_mature_pairs * 10 else int(survival_index * 0.8)

print(f"Target result: {survival_index}")