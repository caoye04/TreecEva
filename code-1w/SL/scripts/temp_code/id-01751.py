def calculate_efficiency(filter_func):
    return lambda data: sum([v for v in data if filter_func(v)])

# System performance metrics (in arbitrary efficiency units)
metrics = [12.5, 8.3, 15.7, 4.2, 18.9, 6.1, 20.0, 9.8]
baseline = 10.0
critical_level = baseline * 1.2

# Irrelevant distraction variable
temp_log = [x * 2 for x in metrics if x < 9]

# Key computation chain
filtered_sum = 0
for val in metrics:
    if val > critical_level:
        filtered_sum += val

energy_threshold = calculate_efficiency(lambda x: x > critical_level)(metrics)

# Additional unrelated operation (minor interference)
status_flags = [True if x > 15 else False for x in metrics]

print(f"Result: {energy_threshold}")