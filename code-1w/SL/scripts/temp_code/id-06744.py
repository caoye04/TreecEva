from collections import defaultdict

# Simulate time-series sensor readings for system load analysis
time_slots = ['morning', 'afternoon', 'evening', 'night']
sensor_data = [
    [180, 210, 195],
    [230, 245, 220],
    [265, 270, 280],
    [200, 190, 205]
]

# Aggregate max readings per time slot using list comprehension
max_per_slot = [max(readings) for readings in sensor_data]

# Map time slots to peak values using dictionary comprehension
capacity_map = {slot: value for slot, value in zip(time_slots, max_per_slot)}

# Compute rolling average of peaks with lambda function
rolling_avg = lambda data: sum(data[-3:]) / 3 if len(data) >= 3 else sum(data) / len(data)
average_peak = rolling_avg(max_per_slot)

# System configuration
baseline_offset = 15
threshold = 250
system_load = capacity_map['evening']

# Fallback logic based on recent patterns
fallback_capacity = int(average_peak + baseline_offset)
peak_capacity = capacity_map['evening']

# Critical decision point
final_analysis = system_load > threshold and peak_capacity or fallback_capacity

Result: peak_capacity