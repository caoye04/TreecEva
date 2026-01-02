from itertools import compress

# Sensor readings over time (simulated)
pressure_readings = [98, 100, 102, 115, 103]
temperature_readings = [22, 23, 24, 26, 30]

def analyze_sensor_burst(readings, threshold):
    return sum(1 for x in readings if x > threshold)

# Analyze abnormal bursts
pressure_bursts = analyze_sensor_burst(pressure_readings, 110)
temperature_bursts = analyze_sensor_burst(temperature_readings, 28)

# Determine individual anomalies
pressure_spike = pressure_bursts > 0
temperature_anomaly = temperature_bursts >= 2

# System trigger condition based on initialization sequence
system_ready = True
initialization_cycles = 3
trigger_condition = system_ready and (initialization_cycles >= 2)

# Final safety threshold alert logic
treshold_alert = trigger_condition and (pressure_spike or temperature_anomaly)

Result: threshold_alert