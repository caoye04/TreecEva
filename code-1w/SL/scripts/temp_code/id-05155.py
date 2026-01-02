from itertools import cycle

# System parameters for a distributed sensor network
current_load = 47
base_capacity = 120
peak_threshold = 95
maintenance_mode = False
sensor_nodes = [3, 5, 2, 8, 7]

def calculate_stress_factor(nodes):
    total = sum(n ** 2 for n in nodes)
    return total // len(nodes)

def assess_health_status(load, threshold):
    return 'critical' if load > threshold else 'stable'

def generate_modifiers(factor):
    mod_sequence = []
    for i in range(6):
        if i % 2 == 0:
            mod_sequence.append((i * factor) % 13)
        else:
            mod_sequence.append(-(i + factor) % 7)
    return mod_sequence

def integrate_diagnostics(mods, base):
    adjusted = base
    temp_tracker = []
    for m in mods:
        if m > 0:
            adjusted += m * 0.7
        else:
            adjusted -= abs(m) * 0.3
        temp_tracker.append(round(adjusted, 2))
    # Misleading: temp_tracker is logged but not used later
    avg_temp = sum(temp_tracker) / len(temp_tracker) if temp_tracker else 0
    return int(adjusted)

def apply_safety_margin(value, status):
    if status == 'critical':
        return max(10, value - 15)
    else:
        return min(200, value + 10)

# Irrelevant pre-computations (distraction)
redundant_calc_1 = (current_load * 2 + 5) // 3
redundant_calc_2 = sum([x % 3 for x in sensor_nodes])

stress_level = calculate_stress_factor(sensor_nodes)
health_status = assess_health_status(current_load, peak_threshold)

# Generate modification sequence based on stress
modifiers = generate_modifiers(stress_level)

# Apply integration with diagnostic logging (semi-relevant)
interim_capacity = integrate_diagnostics(modifiers, base_capacity)

# Simulate dynamic adjustment under safety protocols
if health_status == 'stable':
    interim_capacity = apply_safety_margin(interim_capacity, health_status)

# Red herring: spurious loop over itertools.cycle with no side effects
temp_sum = 0
count = 0
for val in cycle([2, 4, 6]):
    temp_sum += val
    count += 1
    if count >= 9:
        break

# Final adjustment using conditional expression
modifier = 5 if stress_level > 40 else 3
base = interim_capacity if maintenance_mode else interim_capacity + 8

# Key statement
final_capacity = adjust_capacity(base, modifier) if 'adjust_capacity' in globals() else base + modifier

# Define function after use (legal in Python due to execution order)
def adjust_capacity(b, m):
    phase_offset = 4
    return b + m + phase_offset

# Misleading dead code path
if False:
    final_capacity *= 0.9

# Tracking variable that looks important but isn't part of answer
effective_yield = final_capacity * 0.987

print(f"Result: {final_capacity}")