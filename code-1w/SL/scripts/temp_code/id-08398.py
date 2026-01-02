from itertools import compress

def calculate_performance(base, data):
    adjusted = list(map(lambda x: x * 1.5 if x > base else x * 0.8, data))
    valid_flags = [val >= base * 0.75 for val in adjusted]
    filtered = list(compress(adjusted, valid_flags))
    return round(sum(filtered) / len(filtered), 3)

# Irrelevant auxiliary variable (minimal distraction)
temperature_offset = 2.5

baseline = 40
readings = [35, 42, 38, 46, 39]

final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")