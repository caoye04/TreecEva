import itertools

def calculate_performance(base, data):
    filtered = [x for x in data if x > base * 0.75]
    smoothed = [round((a + b) / 2, 2) for a, b in itertools.pairwise(filtered)]
    return sum(smoothed) if smoothed else 0

# Baseline sensor threshold
target_floor = 23.5
baseline = 30
offset = 5.5  # Irrelevant variable (minimal distraction)

readings = [32, 20, 28, 35, 27, 18]

# Key computation step
calibration_mode = False
if calibration_mode:
    final_score = -1
else:
    final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")