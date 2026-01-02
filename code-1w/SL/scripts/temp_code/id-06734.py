def calculate_stability(data):
    filtered = [x for x in data if x > 25]
    adjusted = [x ^ 3 for x in filtered]
    return sum(adjusted) // len(adjusted)

readings = [20, 27, 30, 24, 33, 28]
temperature_flags = {i: temp > 26 for i, temp in enumerate(readings)}
humidity_levels = [45, 50, 52, 48, 60, 55]

# Key computation step
pressure_index = calculate_stability(readings)
print(f"Target result: {pressure_index}")