import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([x ** 2 for x in data if x > 5])

# Misleading intermediate calculation with decoy variables
decoherence_rate = 0.87
temporal_offset = 42
normalization_bias = [i * 0.1 for i in range(10)]

# Core system parameters (some relevant, some not)
grid_state = [3, 7, 1, 9, 4]
efficiency_factor = 0.68
scaling_exponent = 2.5

# Distractor: complex but unused transformation
transformed_signals = [
    int((x ** scaling_exponent) % 7) + (1 if x % 2 == 0 else 0)
    for x in grid_state
    if x != max(grid_state)
]

# Red herring: looks important but unused in final calculation
aggregate_diagnostic = 0
for i, val in enumerate(transformed_signals):
    aggregate_diagnostic += val * (i + 1)

# Decoy function that is defined but never called
def compute_entanglement(x, y):
    return (x + y) ** 0.5 if y != 0 else 0

# Real logic: calculate thermal response based on filtered and transformed inputs
filter_threshold = 2
efficient_nodes = [x for x in grid_state if x > filter_threshold]

# Conditional expression used to adjust factor based on parity of sum
efficiency_factor = efficiency_factor if sum(efficient_nodes) % 2 == 0 else efficiency_factor * 1.1

# Key intermediate computation with distractors around it
signal_power = sum([math.sin(x) * efficiency_factor for x in efficient_nodes])
baseline_reference = math.log(abs(signal_power) + 1)

# Multiple assignments that look significant but only one matters
dummy_a, dummy_b, thermal_base = 117, 89, signal_power * baseline_reference
dummy_c, _, _ = (42, 55, 66)

# Critical function with embedded distractions
def calculate_thermal_response(state, factor):
    # Nested list comprehension with filtering
    processed = [x * factor for x in state if x in efficient_nodes]
    
    # Bit manipulation that appears crucial but is actually irrelevant
    bit_analysis = 0
    for p in processed:
        bit_analysis ^= int(p) & 0xFF
    
    # Real computation buried among distractions
    raw_sum = sum(processed)
    adjustment = math.cos(len(processed))
    entropy_component = -sum([p * math.log(p + 1e-5) for p in processed])
    
    # Final result combines multiple concepts but only a subset is meaningful
    result = raw_sum * adjustment + entropy_component * 0.1  # entropy has minor role
    
    # Dead code branch (never executes due to fixed condition)
    if len(state) < 0:
        result *= 0.5
        
    return result

# Execution point where key variable is assigned
thermal_capacity = calculate_thermal_response(grid_state, efficiency_factor)

# Print result as required
print(f"Result: {thermal_capacity}")