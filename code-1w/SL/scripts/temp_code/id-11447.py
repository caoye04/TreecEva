sensor_readings = [23.5, 45.0, 47.3, 44.1, 26.8, 46.9, 48.2]

# Track high-temperature events above 45.0
temperature_status = []
high_count = 0
trigger_warning = False

for temp in sensor_readings:
    if temp > 45.0:
        temperature_status.append('HIGH')
        high_count += 1
        if high_count >= 3:
            trigger_warning = True
    else:
        temperature_status.append('NORMAL')

# Analyze pattern using string method to detect sustained spikes
status_str = ''.join(temperature_status)
long_spike_detected = 'HIGHHIGHHIGH' in status_str.lower()

# Final alert logic based on count and pattern
threshold_alert = trigger_warning and (high_count > 2)

Result: threshold_alert