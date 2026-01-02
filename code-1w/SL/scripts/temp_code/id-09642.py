def calculate_performance(base, delta, factor):
    adjusted = base + delta * factor
    if adjusted > 100:
        adjusted = 100
    elif adjusted < 0:
        adjusted = 0
    return round(adjusted, 2)

# Simulate sensor data processing pipeline
timestamps = ['T001', 'T002', 'T003']
baseline = 87.5
deviation = -12
correction_factor = 0.75

# Irrelevant string operation (minor distraction)
data_tag = 'SENSORv2'.lower().replace('v2', '_calibrated')

# Key computation
final_score = calculate_performance(baseline, deviation, correction_factor)

print(f'Result: {final_score}')