from collections import Counter

# System monitoring variables
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
pressure_level = sum(temperature_readings) / len(temperature_readings)
flow_rate = temperature_readings[-1] * 1.75
status_counter = Counter({'active': 5, 'standby': 2})
status_check = status_counter['active'] > status_counter['standby']

# Key computational statement
threshold_flag = not (flow_rate > pressure_level and status_check)

# Irrelevant auxiliary variable (minimal distraction)
avg_temp = pressure_level  # duplicate for no critical purpose

print(f"Result: {threshold_flag}")