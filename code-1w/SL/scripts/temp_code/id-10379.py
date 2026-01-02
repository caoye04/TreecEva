def calculate_system_efficiency(units):
    total_efficiency = 0
    base_performance = 1.5
    for idx, (perf, load) in enumerate(zip(units['performance'], units['workload'])):
        efficiency = (perf * base_performance) / (load + 1)
        if efficiency > 2.0:
            total_efficiency += efficiency * 0.9
        else:
            total_efficiency += efficiency * 1.1
    return total_efficiency

# System configuration data
turbine_specs = {
    'performance': [3.2, 2.8, 4.1, 3.6],
    'workload': [3, 2, 5, 4]
}

# Irrelevant auxiliary variable (minimal distraction)
max_capacity = sum(turbine_specs['performance'])

total_efficiency = calculate_system_efficiency(turbine_specs)
print(f'Result: {total_efficiency}')