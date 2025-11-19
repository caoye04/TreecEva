def log_usage(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_usage
def calculate_energy(power, hours):
    return power * hours

appliances_status = {
    'refrigerator': (150, 24, True),
    'lamp': (30, 5, True),
    'oven': (2000, 1, False),
    'tv': (80, 4, True),
    'microwave': (1200, 0.5, True)
}

total_energy = 0
for appliance, (power, hours, active) in appliances_status.items():
    if active and power > 50:
        total_energy += calculate_energy(power, hours)

print(f"Result: {total_energy}")