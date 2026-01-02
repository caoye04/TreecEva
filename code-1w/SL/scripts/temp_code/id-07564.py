from collections import Counter

# System diagnostics simulation with realistic variables
flow_rate = 87.5
pressure_ratio = 92.3
temperature_readings = [23, 25, 24, 26, 23, 23, 24]

counter = Counter(temperature_readings)
dominant_temp = counter.most_common(1)[0][1]  # Frequency of most common temp
event_log = temperature_readings[1:4]  # Slice: [25, 24, 26]

division_result = flow_rate / 5 + len(event_log)
checksum = sum(temperature_readings[:3]) + dominant_temp

# Key logic statement
threshold_flag = not (flow_rate > pressure_ratio) or (checksum % 2 == 0)

Result: threshold_flag