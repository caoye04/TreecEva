import re
from collections import namedtuple
from contextlib import contextmanager

def calculate_velocity(dx, dy, dt):
    return (dx**2 + dy**2)**0.5 / dt if dt > 0 else 0

@contextmanager
def sensor_data_context(data_string):
    try:
        yield data_string.strip().split('\n')
    finally:
        pass

SensorReading = namedtuple('SensorReading', ['timestamp', 'x_pos', 'y_pos', 'sound_level'])

raw_sensor_data = """
T12:34:56 X:120 Y:80 S:75
T12:35:10 X:125 Y:82 S:78
T12:35:25 X:132 Y:85 S:82
T12:35:40 X:140 Y:87 S:79
"""

pod_movement_metrics = []
pod_activity_index = 0

with sensor_data_context(raw_sensor_data) as readings:
    parsed_readings = []
    for line in readings:
        if match := re.match(r'T(\d+):(\d+):(\d+)\s+X:(\d+)\s+Y:(\d+)\s+S:(\d+)', line):
            hour, minute, second, x, y, sound = match.groups()
            timestamp = int(hour)*3600 + int(minute)*60 + int(second)
            parsed_readings.append(SensorReading(timestamp, int(x), int(y), int(sound)))
    
    velocity_calculations = [
        calculate_velocity(
            parsed_readings[i].x_pos - parsed_readings[i-1].x_pos,
            parsed_readings[i].y_pos - parsed_readings[i-1].y_pos,
            parsed_readings[i].timestamp - parsed_readings[i-1].timestamp
        )
        for i in range(1, len(parsed_readings))
    ]
    
    avg_velocity = sum(velocity_calculations) / len(velocity_calculations) if velocity_calculations else 0
    
    sound_variance = sum((r.sound_level - 78.5)**2 for r in parsed_readings) / len(parsed_readings)
    
    activity_function = lambda v, s: round(v * (1 + s/100), 2)
    pod_activity_index = activity_function(avg_velocity, sound_variance)

print(f"Result: {pod_activity_index}")