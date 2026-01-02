from itertools import combinations

def analyze_series(data):
    paired_diffs = {}
    for a, b in combinations(data, 2):
        diff = abs(a - b)
        paired_diffs[(a, b)] = diff
    return paired_diffs

def calculate_total(deviations):
    transform = lambda x: x ** 0.5 if x > 4 else x / 2
    total = 0
    for key in sorted(deviations.keys()):
        if key[0] % 2 == 0:
            total += transform(deviations[key])
    return round(total, 3)

# Main data
sensor_readings = [4, 7, 10, 14]
deviation_map = analyze_series(sensor_readings)
noise_floor = sum(sensor_readings) / len(sensor_readings)  # Irrelevant distractor
baseline_flag = noise_floor > 8  # Another minor distractor

final_score = calculate_total(deviation_map)
print(f"Result: {final_score}")