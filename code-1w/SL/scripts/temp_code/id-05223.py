def normalize(data, scale):
    filtered = [x for x in data if x > 0]
    processed = list(map(lambda x: x ** 0.5, filtered))
    total = sum(processed)
    return round(total / scale, 3)

# Sensor readings with some invalid (non-positive) values
readings = [16, -5, 25, 0, 36, 49]
factor = 4
offset = 10  # Irrelevant variable (minimal distraction)

energy_threshold = normalize(readings, factor)

print(f"Result: {energy_threshold}")