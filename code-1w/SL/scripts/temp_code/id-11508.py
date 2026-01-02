import math

# Simulate a multi-phase system with feedback adjustments
def run_phase_simulation(phases, base_intensity=1.3):
    history = []
    noise_accumulator = 0.0
    temp_cache = {}

    for p in range(1, phases + 1):
        # Irrelevant noise modeling (distractor)
        noise_level = (p ** 2) % 7 / 100.0
        noise_accumulator += noise_level

        # Core computation begins
        raw_signal = base_intensity * p * math.log(p + 1)
        
        # Misleading transformation (semi-relevant but not used directly)
        smoothed = raw_signal * (1 - noise_level)
        if p not in temp_cache:
            temp_cache[p] = smoothed * 0.95

        # Real signal path
        threshold = 2.5 if p > 2 else 1.8
        activated = raw_signal > threshold
        
        # Use list comprehension to simulate parallel state tracking (relevant)
        state_flags = [activated and (i % p == 0) for i in range(1, 6)]
        flag_sum = sum(state_flags)

        # Weight adjustment using modular arithmetic (core concept)
        weight_seed = (p * 17) % 13
        adjustment = (weight_seed + flag_sum) % 5

        # Store meaningful data in dictionary (relevant)
        history.append({
            'phase': p,
            'signal': raw_signal,
            'adjustment': adjustment,
            'noise': noise_level
        })

    return history

# Main execution
num_phases = 5
time_series_data = run_phase_simulation(num_phases)

# Begin result derivation
final_phase_data = time_series_data[-1]
signal_value = final_phase_data['signal']
raw_adjustment = final_phase_data['adjustment']

# Dead code path - irrelevant calculation (interference)
if signal_value < 10:
    dummy_calc = (signal_value ** 2) / 3.14
    buffer = [dummy_calc * i for i in range(3)]  # Unused

# Construct weights using dictionary operations (relevant)
base_weights = {1: 1.1, 2: 1.3, 3: 1.5, 4: 1.7, 5: 1.9}
final_weights = {k: v + 0.1 * (v % k) for k, v in base_weights.items()}

# Correction logic with red herring variables
saturation_level = 8.5
overshoot_risk = signal_value > saturation_level  # True but unused

# Critical statement contains key answer
phase = num_phases
correction_factor = 0.85
offset = raw_adjustment * 2.5

# This is the target line
equilibrium_score = final_weights[phase] * correction_factor + offset

# Print result as required
print(f"Result: {equilibrium_score}")