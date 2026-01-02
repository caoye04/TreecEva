from collections import defaultdict

# Simulate sensor readings with default behavior
default_sensor_value = lambda: 2
sensor_data = defaultdict(default_sensor_value)

for i in range(5):
    sensor_data[i] = (i + 1) ** 2

# Irrelevant auxiliary variable (minor distraction)
aux_scale = 3.7

# Process sequence using conditional logic and arithmetic
def process_sequence(data):
    total = 0
    for key in data:
        if data[key] > 5:
            total += data[key] * 0.5 if key % 2 else data[key] * 0.8
    return int(total)

result = process_sequence(sensor_data)
print(f"Result: {result}")