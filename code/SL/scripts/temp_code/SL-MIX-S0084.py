import math
from collections import namedtuple
from itertools import product

def calculate_adaptation_factor(stress_level, time_hours):
    return math.log(max(1, stress_level)) * math.exp(-0.1 * time_hours)

def apply_environmental_factors(base_growth, factors):
    multiplier = 1.0
    for factor in factors:
        if factor == 'heat':
            multiplier *= 0.8
        elif factor == 'cold':
            multiplier *= 0.9
        elif factor == 'radiation':
            multiplier *= 0.6
        else:  # nutrient_rich
            multiplier *= 1.3
    return base_growth * multiplier

GrowthCondition = namedtuple('GrowthCondition', ['temperature', 'radiation', 'nutrients'])

initial_population = 1000
simulation_days = 5
daily_measurements = []

conditions = [
    GrowthCondition(37, 0.2, 'normal'),
    GrowthCondition(42, 0.1, 'rich'),
    GrowthCondition(30, 0.4, 'normal'),
    GrowthCondition(39, 0.3, 'rich'),
    GrowthCondition(35, 0.0, 'normal')
]

for day in range(simulation_days):
    daily_growth_rate = 1.15
    stress_combination = []
    
    if conditions[day].temperature > 40:
        stress_combination.append('heat')
    elif conditions[day].temperature < 32:
        stress_combination.append('cold')
        
    if conditions[day].radiation > 0.25:
        stress_combination.append('radiation')
        
    if conditions[day].nutrients == 'rich':
        stress_combination.append('nutrient_rich')
    
    adjusted_growth = apply_environmental_factors(daily_growth_rate, stress_combination)
    adaptation = calculate_adaptation_factor(sum([0.1 if s=='heat' else 0.15 if s=='cold' else 0.2 if s=='radiation' else -0.1 for s in stress_combination]), day*24)
    
    if day == 0:
        colony_count = initial_population
    else:
        colony_count = daily_measurements[-1]
        
    new_colonies = int(colony_count * adjusted_growth * (1 + adaptation))
    daily_measurements.append(new_colonies)

final_colony_count = daily_measurements[-1]
print(f"Result: {final_colony_count}")