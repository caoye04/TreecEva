import itertools

# Simulated sensor readings (irrelevant but plausible)
sensor_a = [0.87, 0.82, 0.91, 0.75]
sensor_b = [1.02, 0.99, 1.05, 0.94]

# Irrelevant calibration constants
calibration_x = 0.0034
offset_z = -0.012
baseline_correction = lambda x: x * 1.01 + 0.005

# Distractor function - never called
def compute_buffer_flow(rate):
    return sum([rate ** i for i in range(3)]) if rate > 0 else 0

# Another decoy - unused data structure
event_log = [
    {'type': 'startup', 'code': 101},
    {'type': 'calibrate', 'code': 205},
    {'type': 'error', 'code': 503}
]

# Core state variables
reactor_phase = 'stabilization'
modulation_factor = 7
phase_shift = 3

# Bit manipulation for signal masking (partially relevant)
signal_mask = (modulation_factor << phase_shift) & 0xFF

# Conditional expression with nested logic
is_locked = True if modulation_factor > 5 and phase_shift % 2 == 1 else False

# Intermediate calculation chain
activation_level = (signal_mask ^ 0b11010101) + (is_locked and 1 or 0)
scaling_ratio = activation_level / 64.0

# Red herring: complex-looking but unused transformation
dummy_transform = [round(baseline_correction(x), 3) for x in sensor_a]

# Real processing begins here — multiple assignments
turbine_state, reactor_state, coolant_level = 1, 0, 0
for cycle in itertools.count():
    if cycle >= 3:
        break
    # Nested conditional updates
    if cycle == 1:
        turbine_state = (turbine_state + cycle) * 2
    elif cycle == 2:
        reactor_state = turbine_state ^ (cycle | 5)

# Decoy loop — looks important but does nothing
for _ in range(2):
    temp = 0
    for j in range(5):
        temp ^= j * 2
    # Result unused

# Actual core logic: conditional expression with bitwise and arithmetic
intermediate_flux = (reactor_state << 2) ^ (reactor_state >> 1)
adjusted_flux = intermediate_flux + (intermediate_flux & 7)

# Final computation via lambda-like reasoning
compute_core_metric = lambda x: (x ** 2 + 3 * x + 1) % 1000
metric_value = compute_core_metric(adjusted_flux)

# Key statement
thermal_capacity = calculate_thermal_output(reactor_state)

# Supporting function definition (placed late to obscure relevance)
def calculate_thermal_output(state):
    base = state * 17
    # Mix modular arithmetic and bit ops
    extended = (base ^ 0x1F) % 89
    # Additional layer: conditional adjustment
    adjustment = 11 if (extended & 1) else -7
    final = (extended + adjustment) * 3
    # Inject a distraction with unused local
    snapshot = {'reading': final, 'timestamp': 1699999999}
    return final

# Print result as required
print(f"Result: {thermal_capacity}")