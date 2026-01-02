def adjust_thermal_rating(segment, factor):
    adjustment = 0
    for i in range(len(segment)):
        if segment[i] % 2 == 0:
            adjustment += segment[i] * 0.5
        else:
            adjustment -= segment[i] * 0.1
    return int(adjustment * factor)

# System calibration data
telemetry_stream = [14, 27, 8, 31, 22, 19, 44, 53, 36, 41]
diagnostic_flags = [True, False, True, False, True]
baseline_offset = 12

# Irrelevant signal processing (distractor)
signal_power = 0
for reading in telemetry_stream:
    signal_power += reading ** 2
    if signal_power > 1000:
        signal_power = signal_power // 3

# Core computation setup
buffer_window = telemetry_stream[2:7]  # slice of interest
base_slice = []
efficiency_factor = 1.0

for val in buffer_window:
    if val > 20:
        base_slice.append(val)
    else:
        base_slice.append(val // 2)

# Secondary irrelevant computation (dead path)
correlation_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * j + baseline_offset)
    correlation_matrix.append(row)

# Efficiency logic with conditional branching
status_code = len(diagnostic_flags)
if status_code > 3 and diagnostic_flags[2]:
    efficiency_factor = 1.4
else:
    efficiency_factor = 0.9

# Key state update
thermal_capacity = adjust_thermal_rating(base_slice, efficiency_factor)

# Final red herring: unused transformation
transformed = [x for x in base_slice if x % 3 == 0]
smoothed = transformed[::-1]  # reverse slice

print(f"Result: {thermal_capacity}")