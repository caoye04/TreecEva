from collections import defaultdict

# Simulate sensor data over time using defaultdict
temperature_log = defaultdict(int)
readings = [78, 82, 85, 87, 86, 90]
for temp in readings:
    temperature_log[temp] += 1

# Determine severity level using lambda and conditional expression
assess_risk = lambda t: 'high' if t > 85 else 'moderate'

current_temperature = 87
risk_level = assess_risk(current_temperature)

# Linear search for first high-risk occurrence
historical = [75, 79, 81, 84, 87, 88]
first_critical_index = None
for i in range(len(historical)):
    if historical[i] > 85:
        first_critical_index = i
        break

# Determine alert status based on current risk and history
alert_flag = True if risk_level == 'high' and first_critical_index is not None else False

temperature_status = lambda t: 1 if t >= 85 and alert_flag else 0

# Key execution point
threshold_alert = temperature_status(87)

print(f"Result: {threshold_alert}")