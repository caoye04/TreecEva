import itertools

def analyze_system_status(temperature, pressure, vibration):
    if temperature > 85 and pressure > 90:
        return 'OVERHEAT'
    elif vibration > 75 and pressure < 60:
        return 'INSTABILITY_RISK'
    else:
        return 'STABLE'

# Irrelevant diagnostic function (dead code path)
def legacy_diagnostic(seq):
    cumulative = 0
    for i in seq:
        cumulative += i ** 2
    return cumulative // len(seq) if seq else 0

# Unused but misleading intermediate computation
turbine_sequence = [3, 6, 9, 12, 15]
rolling_avg = sum(turbine_sequence) / len(turbine_sequence)
decoherence_index = rolling_avg * 1.75 - 4.2  # Looks important, never used

# Core calculation with distractors
safety_codes = ['A7', 'B9', 'C3']
active_code = 'B9'

if active_code in safety_codes:
    base_threshold = 23.7
else:
    base_threshold = 45.1

# Red herring: complex-looking but irrelevant bit manipulation
bitmask = 0b10101010
inverted_mask = ~bitmask & 0xFF
shifted_val = (inverted_mask << 2) ^ 0b11001100
redundant_flag = shifted_val % 7 == 0

# Real inputs disguised among noise
thermal_load = 145.6
friction_loss = 18.3
ambient_compensation = 0.87

# Distractor: unused sensor fusion logic
sensor_readings = [142.1, 146.3, 144.8, 147.0]
synchronized = list(itertools.accumulate(sensor_readings, lambda x, y: (x + y) * 0.5))
smoothing_factor = synchronized[-1] / len(synchronized)

# Conditional branch with early exit red herring
if thermal_load > 150:
    final_rating = -1
    print("System halted")
elif friction_loss > 20:
    final_rating = -2
else:
    # This is the actual execution path
    adjusted_load = thermal_load * ambient_compensation
    normalized_loss = friction_loss * 1.15

    def calculate_efficiency(load, loss, margin=1.0):
        base_effort = load - loss
        stress_factor = base_effort * 0.01
        if stress_factor > 1.5:
            stress_adjustment = 1.5
        else:
            stress_adjustment = stress_factor
        
        # Multiple steps with plausible distractions
        candidate_scores = []
        for i in range(1, 4):
            score = (base_effort - stress_adjustment * i) / (loss + i)
            candidate_scores.append(score)
        
        # Use of itertools in non-essential but realistic transformation
        expanded = list(itertools.chain.from_iterable([(x, x*0.9) for x in candidate_scores]))
        filtered = [x for x in expanded if x > 50]
        
        # Final relevant assignment
        efficiency_score = int(sum(filtered) / len(filtered)) if filtered else 0
        return efficiency_score

    # Key statement
    efficiency_score = calculate_efficiency(thermal_load, friction_loss, safety_margin=base_threshold)

# Irrelevant telemetry logging
telemetry_stream = [(1, 'T1'), (2, 'T2'), (3, 'T3')]
transmission_log = [f'{code}:{id}' for id, code in telemetry_stream]

# Print required result
print(f"Result: {efficiency_score}")