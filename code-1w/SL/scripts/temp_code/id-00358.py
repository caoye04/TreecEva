import itertools

# Simulate agricultural yield optimization with noise and distractors
def analyze_soil_ph(levels):
    # Irrelevant helper function analyzing pH (not used in final result)
    adjusted = [round(7.0 + 0.5 * ((i % 3) - 1), 2) for i in range(len(levels))]
    return dict(zip(levels, adjusted))


def generate_growth_pattern(base_cycle):
    # Creates a cyclic permutation of growth phases (distractor)
    return list(itertools.chain.from_iterable(
        itertools.repeat(base_cycle, 3)
    ))[:12]

# Main field parameters
temperature_zones = [22, 25, 27, 24]
humidity_buffer = [60, 65, 70, 68, 72]  # Unused in calculation

# Field layout: (x, y) coordinates of plots
field_layout = [(0,0), (0,1), (1,0), (1,1), (2,0)]
growth_cycles = 4

# Simulated sensor drift values (red herring)
sensor_drift_compensation = {
    'temp': sum([t * 0.03 for t in temperature_zones]),
    'humidity': max(humidity_buffer) - min(humidity_buffer)
}

# Generate growth sequence (used but partially irrelevant)
growth_sequence = generate_growth_pattern(['germinate', 'grow', 'flower'])

# Phantom state tracking (dead code path)
state_log = []
for i, phase in enumerate(growth_sequence):
    if phase == 'germinate':
        state_log.append(f"Cycle {i}: Activation")
    elif phase == 'grow' and i % 2 == 0:
        state_log.append(f"Cycle {i}: Expansion")
    else:
        continue  # Misleading control flow

# Core yield calculation
def calculate_harvest_efficiency(layout, cycles):
    base_efficiency = 0.85
    plot_bonus = 0.0
    
    # Real logic begins here
    for x, y in layout:
        if x > y:
            plot_bonus += 0.05
        elif x == y and x > 0:
            plot_bonus += 0.03
    
    # Environmental multipliers (only temperature matters)
    temp_multiplier = sum(temperature_zones) / (len(temperature_zones) * 25.0)
    
    # Distractor: unused humidity effect
    humidity_factor = 1.0
    if len(humidity_buffer) > 4:
        avg_hum = sum(humidity_buffer) / len(humidity_buffer)
        humidity_factor = 1.0 + (avg_hum - 65) * 0.005
    
    # Bitwise operation to encode cycle efficiency (real use)
    cycle_flag = (cycles & 3)  # 4 & 3 = 0
    cycle_adjustment = [0.95, 1.05, 1.0, 0.9][cycle_flag] if cycle_flag < 4 else 1.0
    
    # Redundant unpacking example (distraction)
    a, b, c, d, e = layout
    _, _y = a  # unpacking but only one used
    
    # Key intermediate computation
    raw_yield = len(layout) * 100 * base_efficiency
    raw_yield *= (1 + plot_bonus)
    raw_yield *= temp_multiplier
    raw_yield *= cycle_adjustment
    
    # Final adjustment based on pattern symmetry (real condition)
    flat_coords = [z for pair in layout for z in pair]
    unique_count = len(set(flat_coords))
    if unique_count % 2 == 0:
        raw_yield *= 1.05
    
    return int(round(raw_yield))

# Execution point of interest
final_yield = calculate_harvest_efficiency(field_layout, growth_cycles)

# Print result as required
print(f"Result: {final_yield}")