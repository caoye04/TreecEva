from itertools import cycle

# Simulate sensor readings over time with noise
def simulate_sensor_data(base, duration):
    return [base + (i % 7) - 3 for i in range(duration)]

# Main parameters
base_flow = 42
adjustment_cap = 15
efficiency_factor = 0.87
pulse_sequence = [1, 0, -1, 0]

data_log = simulate_sensor_data(base_flow, 12)
adjusted_readings = []
out_of_range_count = 0
running_offset = 0

counter_cycle = cycle([2, -1, 3])
for i, reading in enumerate(data_log):
    offset = next(counter_cycle)
    temp_adjusted = reading + offset
    
    if temp_adjusted > base_flow + adjustment_cap:
        out_of_range_count += 1
        temp_adjusted = base_flow + adjustment_cap
    elif temp_adjusted < base_flow - adjustment_cap:
        out_of_range_count += 1
        temp_adjusted = base_flow - adjustment_cap
    
    # Apply pulse modulation every 4th step
    if i % 4 == 0:
        temp_adjusted += pulse_sequence[i % 4]
    
    # Track running offset for diagnostics (not used in final result)
    running_offset += abs(temp_adjusted - base_flow)
    adjusted_readings.append(temp_adjusted)

# Secondary processing: find stable window
stable_window_size = 0
for start in range(len(adjusted_readings) - 4):
    window = adjusted_readings[start:start+5]
    if all(abs(x - base_flow) <= 5 for x in window):
        stable_window_size = len(window)
        break

# Compute final flow metric
aggregate_flow = sum(adjusted_readings[::3])  # Every third sample
baseline_projection = base_flow * len(adjusted_readings)
device_age_compensation = 1.0 - (0.02 * stable_window_size)  # Minor correction
adjusted_flow = aggregate_flow * device_age_compensation

# Key statement
final_flux = adjusted_flow * efficiency_factor

# Diagnostic outputs (distractors)
total_variance = sum((x - base_flow)**2 for x in adjusted_readings)
diagnostic_code = f'DVC-{out_of_range_count}{stable_window_size}'
metadata_checksum = sum(map(ord, diagnostic_code)) % 100

print(f"Result: {final_flux}")