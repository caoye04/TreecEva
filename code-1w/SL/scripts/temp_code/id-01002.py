def calculate_efficiency(input_energy, losses):
    base_efficiency = 0.85
    adjustment = 0.03 if input_energy > 1000 else -0.02
    efficiency = base_efficiency + adjustment
    
    # Irrelevant computation - distractor
    hypothetical_gain = input_energy * 0.015
    temp_buffer = [hypothetical_gain * i for i in range(3)]
    
    final_efficiency = efficiency * (1 - losses)
    return int(input_energy * final_efficiency)

# System parameters
energy_input = 1200
loss_factor = 0.12

# Secondary metrics (not used in final result)
diagnostic_mode = True
sensor_readings = [987, 1012, 995]
avg_reading = sum(sensor_readings) / len(sensor_readings)
status_flag = 'OK' if avg_reading > 990 else 'CALIBRATE'

# Core calculation with conditional expression
thermal_output = calculate_efficiency(energy_input, loss_factor)

# Dead code path - misleading control flow
if diagnostic_mode and False:
    correction_cycle = True
    recalibrate_system = lambda x: x * 1.05
    energy_input = recalibrate_system(energy_input)

# Logging irrelevant state
system_log = f"Processed {energy_input} units with flag {status_flag}"
buffer_size = len(system_log) % 7

print(f"Result: {thermal_output}")