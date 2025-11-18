import math
import random

class Bacterium:
    def __init__(self, generation, parent_survival_time=0):
        self.generation = generation
        self.survival_time = random.uniform(1.0, 10.0)
        self.lambda_param = 0.1
        self.children = []
    
    def survives(self):
        probability = math.exp(-self.lambda_param * self.survival_time)
        return random.random() < probability
    
    def reproduce(self):
        if self.survives():
            for _ in range(3):
                child = Bacterium(self.generation + 1, self.survival_time)
                self.children.append(child)
        return self.children

def calculate_biomass(node):
    biomass = node.survival_time * math.exp(node.generation)
    for child in node.children:
        biomass += calculate_biomass(child)
    return biomass

def simulate_population(initial_bacterium, max_generation):
    stack = [initial_bacterium]
    while stack:
        current = stack.pop()
        if current.generation < max_generation:
            offspring = current.reproduce()
            stack.extend(offspring)
    return calculate_biomass(initial_bacterium)

random.seed(42)
initial_bacterium = Bacterium(generation=0)
total_biomass = simulate_population(initial_bacterium, 3)
print(f"Result: {total_biomass}")