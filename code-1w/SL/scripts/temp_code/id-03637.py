temperature = 28
humidity = 65
is_active = 3.2
mode = 'eco'
baseline = 1.0

# Key computation with conditional expression
energy_threshold = temperature * (is_active if humidity > 60 else 1.5)

# Irrelevant follow-up for minor distraction (intervention level 5)
if mode == 'performance':
    energy_threshold *= 1.2

print(f"Result: {energy_threshold}")