import math

# Simulated quantum register diagnostics (irrelevant initial setup)
def initialize_calibration():
    base_offset = 0.739
    harmonics = [round(math.sin(i * base_offset), 3) for i in range(12)]
    return {f'q{i}': harmonics[i] for i in range(10)}

calibration_map = initialize_calibration()

# Misleading decoy function - looks important but unused
def deprecated_analysis(registers):
    temp_score = 0
    for k, v in registers.items():
        if 'q5' in k:
            temp_score += v ** 2
    return int(temp_score * 100)

# Ancillary system monitoring (distractor data)
current_temps = {'core_1': 67, 'core_2': 65, 'io': 58}
temp_baseline = sum(current_temps.values()) / len(current_temps)
thermal_adjustment = temp_baseline > 60

# Quantum register state simulator (core logic buried among noise)
def simulate_register_decay(depth):
    result = []
    for i in range(depth):
        val = (i + 1) ** 2.5
        if i % 3 == 0:
            val = abs(math.cos(val)) * 10
        result.append(round(val, 3))
    return result

# Real preprocessing step (subtly used later)
def preprocess_readings(raw):
    filtered = [x for x in raw if isinstance(x, (int, float)) and x > 1.0]
    return [x * 0.85 for x in filtered]

# System health mapper - red herring with plausible naming
def compute_health_index(registers):
    total = 0
    weights = {'q0': 1.0, 'q1': 0.8, 'q2': 0.6}
    for k, v in registers.items():
        if k in weights:
            total += abs(v) * weights[k]
    return round(total, 4)

# Main analysis pipeline
quantum_registers = {
    'q0': 3.14159,
    'q1': 2.71828,
    'q2': 1.41421,
    'q3': 1.61803,
    'q4': 0.57721
}

# Irrelevant transformation chain
dummy_chain = [{'step': i, 'value': math.log(i + 2)} for i in range(5)]
chain_sum = sum(d['value'] for d in dummy_chain)

# Hidden dependency: uses simulate_register_decay output as weight proxy
decay_profile = simulate_register_decay(5)
weight_factor = sum(preprocess_readings(decay_profile)) / 10

# Decoy assignment - looks like final result but isn't
diagnostic_score = compute_health_index(quantum_registers)

# Critical intermediate computation (non-obvious path)
adjusted_values = []
for idx, (k, v) in enumerate(quantum_registers.items()):
    adjustment = math.sin(idx + 1) * weight_factor
    adjusted_values.append(v + adjustment)

# Data structure transformation - distractor
register_list = list(quantum_registers.keys())
index_lookup = {k: i for i, k in enumerate(register_list)}

# Core aggregation logic
aggregation_key = 0
for i, val in enumerate(adjusted_values):
    if i % 2 == 0:
        aggregation_key += val * (i + 1)
    else:
        aggregation_key -= val * 0.5

# Final diagnostic computation (answer depends on this)
def analyze_system_state(registers):
    base_sum = sum(registers.values())
    penalty = len([v for v in registers.values() if v < 2.0]) * 0.75
    # The real answer comes from aggregation_key in outer scope
    # This function just returns a transformed version of it
    return int((aggregation_key - base_sum) - penalty) + 100

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers)

print(f"Result: {final_diagnostic}")