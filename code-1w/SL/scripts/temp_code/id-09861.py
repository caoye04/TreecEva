from itertools import cycle, islice
import math

# Irrelevant sensor simulation data (distractor)
def generate_noise(length):
    return [math.sin(i * 0.1) + 0.5 for i in range(length)]

sensor_buffer = generate_noise(50)
baseline_offset = sum(sensor_buffer[:10]) / 10
adjusted_readings = [x - baseline_offset for x in sensor_buffer]
spurious_peak = max(adjusted_readings)

# Core reactor state parameters
reactor_phase = 'stabilized'
core_temperature = 3278
neutron_flux = 98437
modulation_index = 0.87

# Efficiency tracking with historical logs
efficiency_log = [0.85, 0.87, 0.86, 0.88, 0.89, 0.87, 0.85, 0.90, 0.91, 0.89]

# Ancillary systems (mostly irrelevant)
coolant_levels = {'primary': 94.3, 'secondary': 88.7, 'backup': 100.0}
if coolant_levels['primary'] > 90:
    safety_margin = 1.2
else:
    safety_margin = 0.8

# Simulated control rod positions (red herring)
control_rods = list(islice(cycle([12, 15, 18, 20]), 8))
rod_insertion_avg = sum(control_rods) / len(control_rods)

# Power modulation history (unused path)
power_cycles = []
for i in range(5):
    cycle_entry = {
        'phase': f'cycle_{i}',
        'load': round(85 + (i % 3) * 2.5, 1),
        'duration': 120 + i * 15
    }
    power_cycles.append(cycle_entry)

# Reactor state vector (key input)
reactor_state = {
    'temp': core_temperature,
    'flux': neutron_flux,
    'phase': reactor_phase,
    'index': modulation_index
}

# Decoy function that is never called
def evaluate_stability_metric(state):
    raw_score = state['temp'] / 1000
    penalty = 0.1 if state['flux'] > 90000 else 0
    return raw_score - penalty

# Auxiliary transformation (looks important but isn't used in final calc)
def normalize_flux_reading(flux_value):
    normalized = flux_value / 100000.0
    scaled = math.log(normalized * 10 + 1)
    return round(scaled, 3)

# Actual thermal calculation logic
def calculate_thermal_output(state, log_history):
    base_temp = state['temp']
    current_index = state['index']
    
    # Historical efficiency processing (real computation)
    recent_efficiency = sum(log_history[-4:]) / 4  # moving average
    efficiency_factor = 1 + (recent_efficiency - 0.85) * 2
    
    # Flux impact via bit manipulation (non-obvious but relevant)
    flux_word = int(state['flux'])
    shifted_flux = (flux_word >> 6) & 0x3FF  # Extract bits 6-15
    flux_contribution = shifted_flux / 100.0
    
    # Spurious dependency on string state (misleading)
    phase_code = ''.join([chr(ord(c) + 1) for c in state['phase']])  # 'stabilized' → 'tubjmj{fe'
    magic_offset = sum([ord(c) % 10 for c in phase_code])  # = 38
    
    # Real formula mixed with distractions
    intermediate = (base_temp * 0.01) + (flux_contribution * 10)
    intermediate *= efficiency_factor
    intermediate += modulation_index * 5  # reuse of global
    
    # Final adjustment using integer division and rounding
    final_value = int(intermediate // 1)  # truncate fractional part
    final_value = round(final_value + magic_offset)  # add string-derived offset
    
    # Dead code branch (never taken due to phase)
    if state['phase'] == 'overclocked':
        final_value *= 2
    
    return final_value

# Execute main logic
thermal_capacity = 0
thermal_capacity = calculate_thermal_output(reactor_state, efficiency_log)

# Output result as required
print(f"Result: {thermal_capacity}")