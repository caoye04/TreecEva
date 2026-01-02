import math

# Irrelevant helper function (dead code path)
def calculate_harmonic_mean(values):
    if not values:
        return 0
    return len(values) / sum(1/v for v in values if v > 0)

# Misleading data transformation (distractor)
electrical_phases = [1.2, 0.8, 1.5]
phase_weights = [0.3, 0.4, 0.3]
weighted_phase_sum = sum(p * w for p, w in zip(electrical_phases, phase_weights))

# Simulated sensor calibration (irrelevant but plausible)
sensor_offsets = {f'sensor_{i}': (i ** 2) % 7 for i in range(1, 6)}
active_sensors = [k for k in sensor_offsets.keys() if '3' not in k]

def generate_baseline_profile(duration: int):
    # Complex-looking but unused logic
    profile = []
    for t in range(duration):
        if t % 5 == 0:
            profile.append(math.sin(t / 2) * math.cos(t / 3))
        elif t % 3 == 0:
            profile.extend([0.1] * (t % 4))
    return profile[:duration] if len(profile) > duration else profile + [0]*(duration - len(profile))

# Unused recursive structure (decoy)
def compute_stability_factor(n):
    if n <= 1:
        return 1.0
    return 0.9 * compute_stability_factor(n-1) + 0.1 * compute_stability_factor(n-2)

# Real computation begins here — hidden among distractions
transient_load = [i * 1.5 for i in range(10)]
baseline_metrics = {
    'peak': max(transient_load),
    'decay_rate': 0.85,
    'history': [8.0, 7.2, 6.1, 5.8],
    'threshold': 12.0
}

# Core logic buried in abstraction
extra_factors = [math.log(x + 2) for x in range(5)]
mask_filter = [i for i in range(len(extra_factors)) if extra_factors[i] > 1.0]
filtered_correction = sum(extra_factors[i] for i in mask_filter) if mask_filter else 0.0

# Key function with mixed concepts: conditionals, accumulation, bit ops, and list comp
def analyze_thermal_response(load, metrics):
    # Level 1: Preprocess load using conditional expression and bit manipulation
    adjusted_load = [
        (val << 1) if val < metrics['threshold'] else (val >> 1)
        for val in load
    ]
    
    # Level 2: Accumulate energy with conditional branching and short-circuit logic
    accumulated_energy = 0.0
    for i, val in enumerate(adjusted_load):
        if i % 2 == 0 and (metrics.get('decay_rate') or 1) > 0.5:
            adjustment = metrics['decay_rate'] ** i
            accumulated_energy += val * adjustment
        else:
            # Unused branch that looks important
            backup_metric = metrics['history'][i % len(metrics['history'])] if metrics['history'] else 0
            accumulated_energy += val // (i + 1) if i != 0 else val
    
    # Level 3: Apply correction based on composite logical condition
    safety_margin = 1.0
    if metrics['peak'] > 10 and len(metrics['history']) >= 3:
        # Complex conditional expression (Python idiom)
        safety_margin = 1.2 if metrics['decay_rate'] > 0.8 else (1.5 if metrics['peak'] > 14 else 1.1)
    
    # Level 4: Final integration with distractor variables
    dummy_offset = sum(1 << (i % 3) for i in range(7))  # Irrelevant bit shifting
    raw_capacity = accumulated_energy * safety_margin
    
    # Actual answer derivation — depends only on relevant chain
    return int(raw_capacity) ^ dummy_offset  # Bitwise mix, but deterministic

# Execution point of interest
thermal_capacity = analyze_thermal_response(transient_load, baseline_metrics)

# Print required output
print(f"Result: {thermal_capacity}")