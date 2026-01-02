from collections import defaultdict

# Simulate sensor data processing pipeline with noise filtering
raw_readings = [105, -999, 203, 187, -999, 405, 321, 389, -999, 293]
processed_data = [x for x in raw_readings if x != -999]

# Noise counter (distractor: not used later)
noise_events = sum(1 for x in raw_readings if x == -999)

# Initialize system state variables
cycle_count = len(processed_data)
total_output = 0
system_states = defaultdict(int)

temp_buffer = []
for reading in processed_data:
    # Apply nonlinear calibration curve (real processing)
    calibrated = int(reading * 0.87)
    
    # Track state transitions (semi-relevant)
    magnitude = 'high' if calibrated > 300 else 'low'
    system_states[magnitude] += 1
    
    # Simulate accumulation with loss factor
    energy_loss = 0.05 * calibrated
    net_gain = calibrated - energy_loss
    temp_buffer.append(net_gain)

# Secondary loop to simulate post-processing integration
correction_factor = 1.02
final_values = list(map(lambda x: x * correction_factor, temp_buffer))

# Accumulate final output
for val in final_values:
    total_output += val

# Distractor variables
average_input = sum(raw_readings) / len(raw_readings)  # Includes noise
peak_value = max(processed_data)
dummy_metric = noise_events * average_input

# Key computation point
efficiency_score = total_output / cycle_count if cycle_count > 0 else 0

# Final debug print (required format)
print(f"Result: {efficiency_score}")