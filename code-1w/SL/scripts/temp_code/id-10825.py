temperature = 47
humidity = 63
mode = 'eco'

# Initial diagnostic check (irrelevant to final result)
if mode == 'performance':
    adjustment = 10
else:
    adjustment = 2

# Core computation
base_level = 15
adjusted_temp = temperature - adjustment
energy_threshold = adjusted_temp // 2 + (humidity > 60) * 5

# Additional status log (distractor)
status_code = 200 if energy_threshold < 30 else 500

Result: energy_threshold