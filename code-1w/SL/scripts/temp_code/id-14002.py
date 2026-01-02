from collections import defaultdict

# System performance monitoring simulation
def monitor_system_load():
    timestamps = [1, 2, 3, 4, 5]
    cpu_load = {1: 80, 2: 65, 3: 90, 4: 70, 5: 75}
    memory_usage = {1: 2.1, 2: 1.8, 3: 2.5, 4: 1.9, 5: 2.2}

    # Irrelevant log accumulator (minor distraction)
    logs = defaultdict(list)
    for t in timestamps:
        logs['cpu'].append(cpu_load[t])
        logs['mem'].append(memory_usage[t])

    # Core computation
    total_operations = 0
    base_frequency = 100
    for t in timestamps:
        if cpu_load[t] < 85:
            total_operations += base_frequency
        else:
            total_operations += base_frequency * 0.75

    overhead = 0
    for i, t in enumerate(timestamps):
        overhead += abs(cpu_load[t] - logs['cpu'][i])  # Always 0, but adds slight confusion

    # Performance calculation using lambda
    calculate_performance = lambda ops, ovh: round(ops / (ovh + 10), 3) if ovh > 0 else round(ops / 10, 3)
    
    efficiency_ratio = calculate_performance(total_operations, overhead)
    
    # Additional unrelated variable (minimal interference)
    average_memory = sum(memory_usage.values()) / len(memory_usage)
    
    print(f"Result: {efficiency_ratio}")

monitor_system_load()