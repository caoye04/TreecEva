from collections import defaultdict
import math

# Irrelevant helper function (dead code path)
def unused_energy_calculator(x):
    return sum(i ** 2 for i in x if i % 3 == 0)

# Misleading intermediate computation
temp_log = [math.sin(i * 0.1) for i in range(100)]
smoothed_log = [abs(val) * 1.5 for val in temp_log]

# Core simulation parameters (some are decoys)
def initialize_reactor():
    config = defaultdict(int)
    config['core_temperature'] = 5500
    config['pressure_level'] = 230
    config['neutron_flux'] = 987
    config['coolant_rate'] = 41
    return config

# Distractor: complex but unused physics model
def quantum_tunnelling_factor(energy, barrier):
    if energy <= 0:
        return 0.0
    return math.exp(-2 * barrier / (energy + 1))

# Real processing logic buried within noise
def process_phase_shift(stages):
    shift_values = []
    for idx, stage in enumerate(stages):
        if idx % 2 == 0:
            shift_values.append((stage * 1.7) + 3.5)
        else:
            shift_values.append(stage * 0.8)
    return shift_values

# Heavily obfuscated but relevant transformation
def transform_metrics(data_list):
    processed = []
    for item in data_list:
        transformed = int((item ** 1.1) // 1.3)
        if transformed > 100:
            transformed = transformed // 2
        processed.append(transformed)
    # Red herring: this filtering does nothing due to data range
    filtered = [x for x in processed if x % 7 != 0]
    return filtered

# Decoy function that looks important but isn't called
def assess_stability_index(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings)
    return variance < 1e5

# Actual core calculation function
def calculate_thermal_output(phases):
    base_score = 0
    multiplier = 1.618  # Golden ratio distraction?

    # Nested logic with mixed operations
    for i, p in enumerate(phases):
        if i % 3 == 0:
            base_score += int(p * 1.3)
        elif i % 3 == 1 and p > 40:
            base_score += int(math.sqrt(p) * 2.5)
        else:
            base_score += p // 4

    # Bit manipulation decoy (looks critical but not impactful)
    final_int = int(base_score)
    masked = final_int ^ 0xFF
    shifted = (masked << 2) >> 1

    # Key real operation hidden among distractions
    adjusted = abs(shifted - 512)  # Compensate for bit shifts

    # List comprehension with filtering (actually used)
    samples = [adjusted + i for i in range(5) if (adjusted + i) % 2 == 0]
    thermal_result = sum(samples) / len(samples)

    # Early return trap (never triggered due to data)
    if thermal_result < 0:
        return 0.0

    return thermal_result

# Irrelevant sensor array
def generate_synthetic_sensors(n):
    return [((i * 17) % 251) for i in range(n) if i % 5 != 0]

# Unused matrix builder (distractor)
sensor_matrix = [[i*j for j in range(8)] for i in range(8)]

# Main execution flow
reactor_config = initialize_reactor()
raw_stages = [64, 72, 38, 85, 44, 29]

# Apply multiple transformations (some irrelevant)
modified_stages = process_phase_shift(raw_stages)
refined_stages = transform_metrics(modified_stages)

# Critical statement — target of query
thermal_capacity = calculate_thermal_output(refined_stages)

# Print result as required
print(f"Target result: {thermal_capacity}")