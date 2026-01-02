from itertools import combinations

# Simulate quantum energy state transitions in a lattice structure
def generate_coherent_states(n):
    states = []
    for i in range(1, n+1):
        phase = (i ** 2 + 3*i) % 8
        amplitude = abs((i * (i - 1)) // 2 - 10)
        states.append((amplitude, phase))
    return states

# Misleading auxiliary function - not used in final computation
def compute_inertial_dampening(x):
    temp = 0
    for i in range(x):
        temp += (i * i) % 7
    return temp

# Core calculation function
calculate_thermal_output = lambda states: sum(
    amp * (ph % 3) for amp, ph in states if amp > 0 and (amp + ph) % 2 == 0
)

# Initialize system parameters
lattice_size = 7
redundant_buffer = [i * 2 + 1 for i in range(lattice_size)]  # Unused data

# Generate physical states
energy_states = generate_coherent_states(lattice_size)

# Irrelevant pre-processing step (simulates signal filtering)
filtered_signals = []
for s in energy_states:
    filtered = (s[0] + 1e-5) / (s[1] + 1) if s[1] != 0 else s[0]
    normalized = round(filtered, 3)
    if normalized > 2.0:
        filtered_signals.append(normalized)

# Secondary unused computation path
temporary_moment = 0
for pair in combinations([s[0] for s in energy_states], 2):
    diff = abs(pair[0] - pair[1])
    temporary_moment += diff * diff

# Key physics-based computation
thermal_capacity = calculate_thermal_output(energy_states)

# Print result as required
print(f"Result: {thermal_capacity}")