def calculate_efficiency(tasks):
    base_power = 12.5
    overhead = 2
    efficiency_ratio = 0.8

    # Irrelevant diagnostic variable (minimal distraction)
    debug_mode = True

    # Core logic: compute effective operations using list comprehension and lambda
    valid_tasks = [t for t in tasks if t > 0]
    processed_load = list(map(lambda x: x ** 0.5 + base_power, valid_tasks))

    # Apply bitwise mask to simulate hardware constraint
    total_load = sum(processed_load)
    masked_load = int(total_load) & 0xFF  # Simulate 8-bit truncation

    # Conditional adjustment based on threshold logic
    if masked_load > 100:
        masked_load = masked_load ^ 0x5A  # XOR flip certain bits

    energy_threshold = (masked_load * efficiency_ratio) - overhead
    return energy_threshold

# Input data representing task intensities
task_loads = [16, 9, 25, 4]

# Execute calculation
energy_threshold = calculate_efficiency(task_loads)

print(f"Result: {energy_threshold}")