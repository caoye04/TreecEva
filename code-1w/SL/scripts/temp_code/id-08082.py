from itertools import combinations

def evaluate_performance(pair):
    a, b = pair
    return (a * b) / (a + b) if (a + b) != 0 else 0

def calculate_system_efficiency(machines):
    pairs = list(combinations(machines, 2))
    efficiencies = map(evaluate_performance, pairs)
    total_efficiency = sum(efficiencies)
    return total_efficiency

# Irrelevant auxiliary variable (minor distraction)
machine_names = ['Alpha', 'Beta', 'Gamma', 'Delta']

machines = [4, 6, 8]
total_efficiency = calculate_system_efficiency(machines)
print(f"Result: {total_efficiency}")