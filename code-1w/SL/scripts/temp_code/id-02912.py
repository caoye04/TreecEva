from collections import defaultdict

# Simulate water flow measurements over time
readings = [120, 135, 98, 142, 110]
threshold = 115
count_log = defaultdict(int)

inflow = 0
outflow = 0

for reading in readings:
    count_log[reading // 10] += 1
    if reading > threshold:
        inflow += reading * 0.9
    else:
        outflow += reading * 1.1

# Key statement
net_flow = inflow - outflow if inflow > threshold else outflow - inflow

# Irrelevant auxiliary calculation (minor distraction)
temp_correction = sum(count_log.values()) * 0.5

print(f"Result: {net_flow}")