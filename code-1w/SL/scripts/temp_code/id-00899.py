def calculate_engine_cycles(phase_map):
    base_cycle = 17
    total_cycles = 0
    for key in phase_map:
        if key.startswith('ignition'):
            duration = phase_map[key]
            cycles = (base_cycle * duration) % 13
            total_cycles += cycles
    return total_cycles

# Engine phase data (ms)
phases = {
    'ignition_a': 5,
    'cooling_b': 8,  # irrelevant phase
    'ignition_c': 3,
    'startup_d': 2,  # irrelevant phase
    'ignition_e': 7
}

# Calculation entry point
total_cycles = calculate_engine_cycles(phases)

# Output result
print(f"Result: {total_cycles}")