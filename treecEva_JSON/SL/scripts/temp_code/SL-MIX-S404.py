from functools import reduce
from collections import namedtuple

class PlantNode:
    def __init__(self, growth_rate, next_node=None):
        self.growth_rate = growth_rate
        self.next = next_node

def create_growth_chain(rates):
    head = None
    for rate in reversed(rates):
        head = PlantNode(rate, head)
    return head

def calculate_cumulative_growth(head):
    total = 0
    current = head
    while current:
        total += current.growth_rate
        current = current.next
    return total

GrowthData = namedtuple('GrowthData', ['species_id', 'optimal_temp', 'optimal_humidity'])

# Environmental conditions for three rare plant species
environment_map = {
    'Xerophyta': GrowthData('Xerophyta', 35, 20),
    'Hydrostachys': GrowthData('Hydrostachys', 22, 85),
    'Cryophila': GrowthData('Cryophila', 5, 60)
}

# Growth rates over 5 measurement periods
xerophyta_rates = [1.2, 1.5, 1.3, 1.7, 1.4]
hydrostachys_rates = [2.1, 2.3, 2.0, 2.5, 2.2]
cryophila_rates = [0.8, 0.9, 0.7, 1.1, 1.0]

# Create linked list structures for growth data
xerophyta_chain = create_growth_chain(xerophyta_rates)
hydrostachys_chain = create_growth_chain(hydrostachys_rates)
cryophila_chain = create_growth_chain(cryophila_rates)

# Calculate cumulative growth using functional approach
growth_totals = list(map(calculate_cumulative_growth, [xerophyta_chain, hydrostachys_chain, cryophila_chain]))

# Environmental stress factors
stress_factors = [0.85, 1.15, 0.95]

# Apply stress factors and calculate adaptive responses
adjusted_growth = [g * s for g, s in zip(growth_totals, stress_factors)]

# Determine if environmental conditions are optimal
xerophyta_optimal = environment_map['Xerophyta'].optimal_temp > 30 and environment_map['Xerophyta'].optimal_humidity < 25
hydrostachys_optimal = environment_map['Hydrostachys'].optimal_temp < 25 and environment_map['Hydrostachys'].optimal_humidity > 80
cryophila_optimal = environment_map['Cryophila'].optimal_temp < 10 and environment_map['Cryophila'].optimal_humidity > 50

# Calculate adaptive score with short-circuit evaluation
adaptive_score = 0
if xerophyta_optimal and hydrostachys_optimal and cryophila_optimal:
    adaptive_score = reduce(lambda x, y: x + y, adjusted_growth) * 1.2
elif xerophyta_optimal or hydrostachys_optimal or cryophila_optimal:
    adaptive_score = reduce(lambda x, y: x + y, adjusted_growth) * 0.9
else:
    adaptive_score = reduce(lambda x, y: x + y, adjusted_growth) * 0.7

print(f"Result: {adaptive_score}")