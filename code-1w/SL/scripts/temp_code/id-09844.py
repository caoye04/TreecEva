from collections import defaultdict

# Simulate battery capacity degradation over cycles
cycle_data = [3, 1, 4, 1, 5, 9, 2, 6]
initial_capacity = 100
degradation_rate = defaultdict(float)

for cycle in cycle_data:
    if cycle % 2 == 0:
        degradation_rate[cycle] += 0.75
    else:
        degradation_rate[cycle] += 0.25

total_degradation = 0
for cycle, rate in degradation_rate.items():
    total_degradation += rate * initial_capacity * 0.01

remaining_capacities = []
for i in range(5):
    remaining_capacity = initial_capacity - (total_degradation * (i + 1) / 5)
    remaining_capacities.append(round(remaining_capacity, 2))

final_capacity = max(remaining_capacities)
print(f"Result: {final_capacity}")