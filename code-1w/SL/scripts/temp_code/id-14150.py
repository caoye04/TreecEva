def calculate_efficiency(level):
    base = 100 if level > 50 else 50
    modifier = (lambda x: x * 0.1 if x < 30 else x * 0.2)(level)
    return base + modifier

status_code = 200
activation_level = 45
energy_threshold = None
activation_level += 5
energy_threshold = calculate_efficiency(activation_level)
print(f"Target result: {energy_threshold}")