from collections import defaultdict, Counter
import math

# Simulated material testing data
test_cycles = [3, 5, 7, 9, 11]
failure_modes = ['crack', 'deform', 'fracture', 'crack', 'deform', 'none', 'none']
baseline_stress = 42.5
sensitivity_factor = 0.86

# Irrelevant statistical counters (distractor)
mode_count = Counter(failure_modes)
unused_ratio = mode_count['crack'] / len(failure_modes)

# Dummy function that is never called (dead code path)
def deprecated_analysis(data):
    return sum(x ** 0.5 for x in data if x > 5)

# Secondary helper with misleading intermediate output
def assess_integrity(values):
    peak = max(values)
    avg = sum(values) / len(values)
    deviation_score = (peak - avg) * sensitivity_factor
    # Following line looks important but is unused later
    anomaly_flag = deviation_score > 15.0
    return int(avg) % 7

# Complex preprocessing with red herring operations
stress_sequence = []
for cycle in test_cycles:
    adjusted = baseline_stress * (cycle / 3)
    if cycle % 2 == 1:
        adjusted += math.log(cycle) * 1.5
    stress_sequence.append(int(adjusted))

# Introduce irrelevant transformation chain
transform_map = defaultdict(lambda: 0)
for idx, val in enumerate(stress_sequence):
    transform_map[f'phase_{idx}'] = val * 0.9 + 2.1

# Unused cumulative analysis (distractor)
cumulative_risk = 0
for i in range(len(stress_sequence) - 1):
    diff = abs(stress_sequence[i+1] - stress_sequence[i])
    cumulative_risk += diff * 0.3

# Fake model calibration (misleading computation)
calibration_data = []
for x in stress_sequence:
    calibrated = (x * 1.05) - 4.2
nonsense_offset = sum(calibration_data) if calibration_data else 99

# Real logic buried among distractions
def compute_resistance_factor(seq):
    total = 0
    for i, s in enumerate(seq):
        if i % 2 == 0:
            total += s // (i + 1)
        else:
            total -= s % 5
    return abs(total) % 13

# Multi-step efficiency derivation with plausible decoys
raw_efficiency = sum(stress_sequence) / len(stress_sequence)
filtered_efficiency = raw_efficiency * (1 + 0.01 * assess_integrity(test_cycles))
efficiency = int(filtered_efficiency) - 5

# Critical distraction: a similarly named but irrelevant variable
efficiency_backup = efficiency * 0.97  # Never used

# Main calculation chain — actual answer depends on this
resistance = compute_resistance_factor(stress_sequence)

# Simulate environmental degradation factor (partially relevant)
degradation_log = []
for temp in [23, 25, 29, 35]:
    decay = math.exp(-temp * 0.01)
    degradation_log.append(round(decay, 3))
development_factor = sum(degradation_log) / 4

# Core formula embedded in noise
def calculate_strain_yield(eff, seq):
    base_yield = 0
    multiplier = eff % 10
    
    # Nested logic with mixed operations
    for i in range(len(seq)):
        if i < resistance:
            if seq[i] % 2 == 0:
                base_yield += seq[i] // multiplier if multiplier != 0 else 0
            else:
                base_yield -= seq[i] % (multiplier + 1)
        else:
            # Dead branch due to resistance being small
            base_yield += int(math.sqrt(seq[i]))
    
    # Final adjustment using development factor (irrelevant in practice)
    final_value = base_yield + int(development_factor * 10)
    
    # Red herring: complex bit manipulation that doesn't affect result
    bit_mask = (resistance << 2) ^ 7
    masked_yield = final_value & bit_mask | 1
    
    return final_value  # masked_yield is never used

# Key execution point
final_yield = calculate_strain_yield(efficiency, stress_sequence)

# Additional distractor: printing unrelated stats
print(f"Diagnostics: {len(transform_map)} phases, risk={cumulative_risk:.2f}")
print(f"Mode count: {dict(mode_count)}")

# Output required result
print(f"Target result: {final_yield}")