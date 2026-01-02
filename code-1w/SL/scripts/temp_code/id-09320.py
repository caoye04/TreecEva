def analyze_sensor_drift(readings):
    drift_compensation = 0
    for i, reading in enumerate(readings):
        if i > 0 and abs(reading - readings[i-1]) > 5:
            drift_compensation += 1.5
    return drift_compensation

readings = [10, 12, 18, 25, 26, 30, 45, 47]
compensation = analyze_sensor_drift(readings)

# Simulate temperature-corrected pressure states
temp_offsets = [3, -1, 2, 0, -2]
base_pressures = [101.3, 99.7, 102.1, 98.4, 100.8]

corrected_pressures = [
    base_pressures[i] + temp_offsets[i] + (compensation * 0.2)
    for i in range(len(base_pressures))
]

# Track state transitions with auxiliary metadata
states = ['idle', 'active', 'overload', 'active', 'idle']
state_codes = {s: idx for idx, s in enumerate(states)}
thermo_states = list(zip(corrected_pressures, states, temp_offsets))

# Misleading redundancy: unused transformation path
def transform_state(state_tuple):
    pressure, mode, offset = state_tuple
    if mode == 'overload':
        return pressure * 1.1
    elif mode == 'idle':
        return pressure * 0.95
    return pressure + 0.5

# Auxiliary diagnostic logging (no effect on main result)
diagnostic_trace = []
for idx, (p, s, o) in enumerate(thermo_states):
    if s == 'active':
        diagnostic_trace.append(f"A{idx}")
    elif p > 102:
        diagnostic_trace.append(f"O{idx}")

# Real computation path: stabilization via active-state filtering
def calculate_stabilized_pressure(state_data):
    valid_pressures = []
    for pressure, status, _ in state_data:
        if status == 'active':
            valid_pressures.append(pressure)
    if not valid_pressures:
        return state_data[0][0]  # fallback
    raw_avg = sum(valid_pressures) / len(valid_pressures)
    
    # Secondary adjustment based on offset correlation (unused but looks relevant)
    total_offset = sum(o for _, _, o in state_data)
    adjustment_factor = abs(total_offset) * 0.05  # distraction
    
    # Actual rule: floor to nearest integer if more than 2 active states
    if len(valid_pressures) > 2:
        return int(raw_avg)
    else:
        return round(raw_avg + adjustment_factor, 2)

# Critical assignment point
final_pressure = calculate_stabilized_pressure(thermo_states)
print(f"Result: {final_pressure}")