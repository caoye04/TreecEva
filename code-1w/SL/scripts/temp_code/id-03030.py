import math

# Simulate a thermal equilibrium system with noise filtering and state tracking
def calculate_equilibrium():
    initial_heat = 42.5
    ambient_loss = 8.3
    cycle_count = 6
    damping_factor = 0.92
    sensor_noise = [0.1, -0.05, 0.2, 0.0, -0.15]

    # Irrelevant signal processing (distractor)
    filtered_noise = list(map(lambda x: round(x ** 2, 3), sensor_noise))
    avg_noise = sum(filtered_noise) / len(filtered_noise) if filtered_noise else 0

    # Core state initialization
    core_temperature = initial_heat - ambient_loss
    transient_buffer = []

    # Simulate thermal cycles with damping
    for i in range(1, cycle_count + 1):
        fluctuation = (core_temperature * 0.05) * ((-1) ** i)
        core_temperature += fluctuation

        # Nested logic for phase detection (some branches irrelevant)
        if i % 2 == 0:
            if core_temperature > 35.0:
                adjustment = (i % 3 + 1) * 0.75
                core_temperature -= adjustment
                if i == 4:
                    transient_buffer.append(core_temperature)
            else:
                transient_buffer.append(core_temperature * 0.95)
        else:
            core_temperature *= damping_factor

    # Secondary derived values (mix of relevant and red herring)
    temperature_regulator = abs(transient_buffer[-1] - transient_buffer[0]) if transient_buffer else 0
    stability_index = sum([t ** 0.5 for t in transient_buffer]) // len(transient_buffer) if transient_buffer else 0

    # Redundant combinatorics (distractor)
    pair_combinations = 0
    for a in range(len(transient_buffer)):
        for b in range(a + 1, len(transient_buffer)):
            if transient_buffer[a] != transient_buffer[b]:
                pair_combinations += 1

    # Key computational chain
    base_energy = core_temperature * 2.1
    balance_factor = (base_energy % 17) + (cycle_count // 2)
    
    # Critical statement
    final_adjustment = balance_factor * temperature_regulator

    # Auxiliary metrics (irrelevant to answer)
    efficiency_ratio = (base_energy / (final_adjustment + 1e-8)) * 100
    diagnostic_log = f'Regulator={temperature_regulator}, Pairs={pair_combinations}'

    # Output target result
    equilibrium_score = int(final_adjustment + 0.5)  # rounded to nearest integer
    print(f"Result: {equilibrium_score}")

    return equilibrium_score

# Execute and capture result
calculate_equilibrium()