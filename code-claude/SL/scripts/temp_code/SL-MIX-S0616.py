# Calculate total energy from particle interactions in physics simulation

def calculate_particle_momentum(velocity, mass):
    # Simple momentum calculation
    return velocity * mass

# Initialize parameters
base_velocities = [3, 5, 2, 8, 4]
base_masses = [1.5, 2.0, 1.0, 0.5, 3.0]

# Interaction factors (distractors)
field_strength = 2.5
temperature_factor = 0.75

# Adjust velocities based on temperature (distractor)
adjusted_velocities = [v * temperature_factor if i % 2 == 0 else v 
                      for i, v in enumerate(base_velocities)]

# Calculate momentum for each particle
momentum_values = [calculate_particle_momentum(v, m) 
                  for v, m in zip(base_velocities, base_masses)]

# Calculate potential energy values
potential_energy = lambda mass, height: mass * 9.8 * height
heights = [1.0, 1.5, 0.5, 2.0, 1.0]
potential_energies = [potential_energy(m, h) for m, h in zip(base_masses, heights)]

# Calculate kinetic energy
kinetic_energy = lambda mass, velocity: 0.5 * mass * velocity**2

# Power level calculation (what we actually need)
power_levels = []
for i in range(len(base_velocities)):
    mass = base_masses[i]
    velocity = base_velocities[i]
    
    # Distractor calculations
    momentum = momentum_values[i]
    pot_energy = potential_energies[i]
    
    # What actually matters for the answer
    power = kinetic_energy(mass, velocity)
    power_levels.append(power)

# Calculate energy interactions (distractor)
interaction_matrix = [[i*j for j in range(3)] for i in range(5)]
field_modifier = sum([row[1] for row in interaction_matrix])

# This is the key statement
total_energy = sum(power_levels)

# Final result with irrelevant modification (distractor)
display_value = total_energy * field_strength if field_strength > 3 else total_energy

print(f"Result: {total_energy}")