def calculate_efficiency(data):
    filtered = [x for x in data if x > 0]
    squared = list(map(lambda y: y ** 2, filtered))
    avg = sum(squared) / len(squared) if squared else 0
    return int(avg ** 0.5)

# Sensor readings with some invalid (non-positive) values
temperature_readings = [3, -1, 4, 1, -2, 5, 9]

# Irrelevant auxiliary variable (minor distraction)
baseline_correction = 0.5

energy_output = calculate_efficiency(temperature_readings)
print(f"Result: {energy_output}")