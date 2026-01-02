temperature = 28
humidity = 65
mode = 'auto'

# Environmental control logic
is_active = mode == 'auto'
target_humidity = 50 if is_active else 80

# Key statement
energy_threshold = temperature > 25 and humidity < 70

# Additional non-essential but realistic operation
adjustment_needed = target_humidity - humidity if not energy_threshold else 0

print(f"Result: {energy_threshold}")